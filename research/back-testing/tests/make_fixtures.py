#!/usr/bin/env python3
"""Build the fictional fixtures for the v1.1 comparative tests (section 10A).

Every row is FICTIONAL. The fixtures exercise every judgement class, both
readings, NOT_APPLICABLE, OUT_OF_SCOPE, INSUFFICIENT_INFORMATION on each side,
baseline-only (AIDCF loss) cases with gap dispositions, the incident-exclusion
rule, origins, and the seeded EOD sample. Run from any directory; it rewrites
tests/fixtures/ deterministically.
"""

import csv
import hashlib
import io
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIX = HERE / "fixtures"
sys.path.insert(0, str(HERE.parent))
import backtest_check as bc  # noqa: E402
import comparative as cp  # noqa: E402

TEMPLATE = dict(zip(bc.SHEET_COLUMNS, next(csv.reader(
    (HERE.parent / "coding-sheet.csv").read_text(encoding="utf-8").splitlines()[1:2]))))

CATEGORY = {1: "COOLING", 2: "POWER", 3: "COOLING", 4: "POWER", 5: "CONTROL_PLANE_OT", 6: "COOLING",
            7: "POWER", 8: "CONTROL_PLANE_OT", 9: "COOLING", 10: "POWER", 11: "COOLING", 12: "POWER"}

# (incident, factor, origin, knowability, phase, AIDCF judgement, {method: judgement})
D, P, ND, NA_, II, OOS, NAP = ("DETECTED", "PARTIALLY_DETECTED", "NOT_DETECTED", "NOT_ADDRESSED",
                               "INSUFFICIENT_INFORMATION", "OUT_OF_SCOPE", "NOT_APPLICABLE")
FACTORS = [
    (1, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": NAP}),   # W1
    (1, 2, "BOTH", "DISCOVERABLE", "PRE_REVEAL", P, {"BL-ENG": NA_, "BL-CX": D, "BL-OT": NAP}),      # W2
    (2, 1, "AIDCF", "STATED_KNOWN", "PRE_REVEAL", ND, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": P}),    # W3
    (2, 2, "BASELINE", "DISCOVERABLE", "PRE_REVEAL", NA_, {"BL-ENG": OOS, "BL-CX": NA_, "BL-OT": NAP}),  # W4
    (3, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": D, "BL-CX": II, "BL-OT": NAP}),     # W5 (CX)
    (3, 2, "AIDCF", "NOT_STATED", "PRE_REVEAL", II, {"BL-ENG": D, "BL-CX": D, "BL-OT": NAP}),       # not comparable
    (4, 1, "BOTH", "DISCOVERABLE", "PRE_REVEAL", II, {"BL-ENG": D, "BL-CX": NA_, "BL-OT": NAP}),     # W6
    (4, 2, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": ND, "BL-CX": II, "BL-OT": NAP}),    # W7 (union X)
    (5, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NAP, "BL-CX": NAP, "BL-OT": NAP}),  # W8
    (5, 2, "BASELINE", "DISCOVERABLE", "PRE_REVEAL", ND, {"BL-ENG": NAP, "BL-CX": NAP, "BL-OT": D}),
    (6, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", P, {"BL-ENG": NA_, "BL-CX": P, "BL-OT": NAP}),     # W9
    # W10: 4 knowable factors, 3 indeterminate on the BL-OT side
    (7, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": D, "BL-CX": NA_, "BL-OT": II}),
    (7, 2, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": II}),
    (7, 3, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", ND, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": II}),
    (7, 4, "BOTH", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": NA_}),
    (8, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NAP, "BL-CX": NA_, "BL-OT": D}),
    (8, 2, "BASELINE", "STATED_KNOWN", "PRE_REVEAL", NA_, {"BL-ENG": NAP, "BL-CX": NA_, "BL-OT": D}),
    (9, 1, "AIDCF", "DISCOVERABLE", "POST_REVEAL", D, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": NAP}),  # not comparable
    (9, 2, "ADJUDICATOR", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": D, "BL-CX": D, "BL-OT": NAP}),
    (10, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NA_, "BL-CX": NA_, "BL-OT": NAP}),
    (10, 2, "BASELINE", "DISCOVERABLE", "PRE_REVEAL", NA_, {"BL-ENG": D, "BL-CX": NA_, "BL-OT": NAP}),
    (11, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", P, {"BL-ENG": P, "BL-CX": NA_, "BL-OT": NAP}),
    (12, 1, "AIDCF", "DISCOVERABLE", "PRE_REVEAL", D, {"BL-ENG": NA_, "BL-CX": OOS, "BL-OT": NAP}),
    (12, 2, "AIDCF", "NOT_KNOWABLE", "PRE_REVEAL", None, {}),  # not comparable
]
EOD_SEED, BOOT_SEED = "20261013", "4242"


def inc(n):
    return "INC-EXAMPLE-%02d" % n


def aidcf_row(n, f, know, phase, j):
    r = dict(TEMPLATE)
    r.update(incident_id=inc(n), coding_round="RECONCILED", coder_id="C05", factor_id="CF-%02d" % f,
             knowability=know, coding_phase=phase, failure_category=CATEGORY[n],
             causal_factor="FICTIONAL factor %d of %s" % (f, inc(n)), gap_type="NONE", gap_description="",
             notes="FICTIONAL comparative fixture - not a real incident.")
    if j is None:
        r.update(control_id="MCF-DEP-006", control_criteria="", projected_control_result="", detection_judgement="")
    elif j == "NOT_ADDRESSED":
        r.update(control_id="NONE", control_criteria="", projected_control_result="", detection_judgement=j,
                 gap_type="G1_NO_CONTROL", gap_description="FICTIONAL gap")
    elif j == "INSUFFICIENT_INFORMATION":
        r.update(control_id="NONE", control_criteria="", projected_control_result="", detection_judgement=j)
    else:
        r.update(control_id="MCF-DEP-006", control_criteria="1", detection_judgement=j,
                 projected_control_result={"DETECTED": "NONCONFORMING", "PARTIALLY_DETECTED": "PARTIAL",
                                           "NOT_DETECTED": "CONFORMING"}[j])
    return r


def comp_row(**kw):
    r = {c: "" for c in cp.SHEET_COLUMNS}
    r.update(coder_id="C09", coding_round="RECONCILED", independent_of_author="Y", prior_familiarity="NONE",
             notes="FICTIONAL comparative fixture.")
    r.update(kw)
    return r


def baseline_row(n, f, m, j, sampled, round_="RECONCILED", coder="C09"):
    r = comp_row(incident_id=inc(n), record_type="BASELINE", factor_id="CF-%02d" % f, baseline_id=m,
                 detection_judgement=j, coding_round=round_, coder_id=coder)
    if j in cp.CITED:
        r["baseline_criteria"] = "FICTIONAL clause 4.2"
    if j == "NOT_ADDRESSED":
        r["notes"] = "FICTIONAL: whole frozen scope searched; no criterion covers it."
    if j == "OUT_OF_SCOPE":
        r["exclusion_id"] = "EXC-01"
    if j == "NOT_APPLICABLE":
        r["applicability_rule"] = "APP-01"
    if m == "BL-ENG":
        r.update(eng_discipline="COOLING" if CATEGORY[n] == "COOLING" else "POWER", eng_technique="FMEA")
    if sampled:
        v = ["POSSIBLE", "LIKELY", "UNLIKELY", "INDETERMINATE"][(n + f + len(m)) % 4]
        if v == "INDETERMINATE":
            r.update(eod=v, eod_assumptions="FICTIONAL: the dossier does not say how the review would be scoped")
        else:
            r.update(eod=v, eod_assumptions="FICTIONAL: two-day review, sampled settings", eod_confidence="LOW")
    return r


def write(path, cols, rows):
    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    path.write_text(out.getvalue(), encoding="utf-8")


def main():
    FIX.mkdir(exist_ok=True)
    coding = [aidcf_row(n, f, k, ph, j) for n, f, _, k, ph, j, _ in FACTORS]
    write(FIX / "coding-sheet.csv", bc.SHEET_COLUMNS, coding)

    base = list(csv.DictReader((HERE.parent / "baselines.csv").read_text(encoding="utf-8").splitlines()))
    for r in base:
        r.update(approval_status="APPROVED", approved_on="2026-10-13", reviewer_id="C30",
                 edition_profile="FICTIONAL fixture edition", version="1.0")
    write(FIX / "baselines.csv", cp.BASELINE_COLUMNS, base)

    factor_rows = [comp_row(incident_id=inc(n), record_type="FACTOR", factor_id="CF-%02d" % f, factor_origin=o,
                            factor_source="C05 pass 1; FICTIONAL dossier para %d" % f, knowability=k,
                            coding_phase=ph, eod_sampled="N")
                   for n, f, o, k, ph, _, _ in FACTORS]
    frame = cp.eod_frame(factor_rows)
    sample = set(cp.draw_eod_sample(frame, lambda i: CATEGORY[int(i[-2:])], EOD_SEED))
    for r in factor_rows:
        if (r["incident_id"], r["factor_id"]) in sample:
            r["eod_sampled"] = "Y"
    rows = list(factor_rows)
    for n, f, _, _, _, _, js in FACTORS:
        s = (inc(n), "CF-%02d" % f) in sample
        for m, j in js.items():
            rows.append(baseline_row(n, f, m, j, s))
        if s:
            rows.append(comp_row(incident_id=inc(n), record_type="AIDCF_EOD", factor_id="CF-%02d" % f,
                                 eod=["LIKELY", "POSSIBLE", "UNLIKELY"][n % 3],
                                 eod_assumptions="FICTIONAL: AIDCF-009 plan, three-day assessment", eod_confidence="MEDIUM"))
    # two independent BL-ENG reviewers (rounds A and B) on every BL-ENG factor of incidents 1 to 6, for the
    # reviewer count and round agreement; B differs from the reconciled judgement on two factors
    flip = {"DETECTED": "PARTIALLY_DETECTED", "PARTIALLY_DETECTED": "DETECTED", "NOT_ADDRESSED": "NOT_DETECTED",
            "NOT_DETECTED": "NOT_ADDRESSED", "NOT_APPLICABLE": "NOT_ADDRESSED", "OUT_OF_SCOPE": "NOT_ADDRESSED",
            "INSUFFICIENT_INFORMATION": "NOT_ADDRESSED"}
    differ = 0
    for n, f, _, _, _, _, js in FACTORS:
        if n <= 6 and "BL-ENG" in js:
            s = (inc(n), "CF-%02d" % f) in sample
            j = js["BL-ENG"]
            rows.append(baseline_row(n, f, "BL-ENG", j, s, "A", "C21"))
            b = flip[j] if differ < 2 and j != "NOT_APPLICABLE" else j
            differ += b != j
            rows.append(baseline_row(n, f, "BL-ENG", b, s, "B", "C22"))
    # gap dispositions for every baseline-only pair under either reading
    import backtest_check  # noqa: F401
    data = cp.build_pairs(rows, {r["baseline_id"]: dict(r) for r in base}, coding)
    disp = ["OUTSIDE_DECLARED_BOUNDARY", "ACTIONABLE_GAP", "DELEGATED_TO_STANDARD", "DISPUTED", "BELOW_INTENDED_GRANULARITY"]
    i = 0
    for k in cp.comparable(data):
        for m in data["active"]:
            if any(cp.classify(data, k, m, rd)[0] == "c" for rd in ("strict", "inclusive")):
                d = disp[i % len(disp)]
                i += 1
                cite = {"ACTIONABLE_GAP": "G2_NO_CRITERION FICTIONAL", "DISPUTED": ""}.get(d, "FICTIONAL AIDCF clause 3.1")
                rows.append(comp_row(incident_id=k[0], record_type="GAP_DISPOSITION", factor_id=k[1], baseline_id=m,
                                     coder_id="C40", gap_disposition=d, disposition_citation=cite,
                                     notes="FICTIONAL. Adjudicator and coder positions recorded." if d == "DISPUTED" else "FICTIONAL."))
    write(FIX / "comparative-sheet.csv", cp.SHEET_COLUMNS, rows)

    # a locked snapshot of one coder's judgement file (section 10A.4), then the reconciled files
    (FIX / "locked").mkdir(exist_ok=True)
    write(FIX / "locked" / "C21-BL-ENG-round-A.csv", cp.SHEET_COLUMNS, [r for r in rows if r["coder_id"] == "C21"])
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    file_locks = [dict(artefact="FILE:tests/fixtures/%s" % name, value=sha(FIX / name), locked_on="2026-10-13",
                       locked_by="C40", notes="FICTIONAL")
                  for name in ("locked/C21-BL-ENG-round-A.csv", "coding-sheet.csv", "comparative-sheet.csv")]
    digest = hashlib.sha256((FIX / "baselines.csv").read_bytes()).hexdigest()
    locks = [
        dict(artefact="BASELINES", value=digest, locked_on="2026-10-13", locked_by="C40", notes="FICTIONAL"),
        dict(artefact="EOD_FRAME", value=cp.frame_digest(frame), locked_on="2026-10-13", locked_by="C40", notes="FICTIONAL"),
        dict(artefact="EOD_SEED", value=EOD_SEED, locked_on="2026-10-13", locked_by="C40", notes="FICTIONAL"),
        dict(artefact="BOOTSTRAP_SEED", value=BOOT_SEED, locked_on="2026-10-13", locked_by="C40", notes="FICTIONAL"),
    ] + file_locks
    write(FIX / "comparative-locks.csv", cp.LOCK_COLUMNS, locks)
    (FIX / "incident-register.csv").write_text(",".join(bc.REGISTER_COLUMNS) + "\n", encoding="utf-8")
    print("fixtures written: %d coding rows, %d comparative rows, %d sampled factors" % (len(coding), len(rows), len(sample)))


if __name__ == "__main__":
    main()
