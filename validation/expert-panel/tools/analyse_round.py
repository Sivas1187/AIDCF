#!/usr/bin/env python3
"""Analyse one Delphi round of the AIDCF expert panel (AIDCF-VAL-002).

Standard library only. Reads one or more filled response CSVs in the layout of
round-1-response-template.csv (one file per panellist, or several panellists
per file distinguished by panelistCode), and computes for every item and
rating dimension:

  N        number of valid ratings (1-4); blank, NA and UNSURE are excluded
  A        number of ratings of 3 or 4
  I-CVI    A / N
  Pc       probability of chance agreement = C(N, A) * 0.5**N
  k*       modified kappa = (I-CVI - Pc) / (1 - Pc)
  median, Q1, Q3, IQR (inclusive quartiles)

and, per rating dimension and item type, S-CVI/Ave (mean I-CVI) and
S-CVI/UA (share of items with I-CVI = 1.00).

Thresholds (AIDCF-VAL-002 section 8):
  I-CVI   1.00 when N <= 5; 0.78 when N >= 6 (I-CVI compared after rounding
          to two decimals, so 7 of 9 = 0.78 meets the threshold)
  k*      > 0.74 excellent; 0.60-0.74 good; 0.40-0.59 fair; < 0.40 poor
  IQR     <= 1 on the 4-point scale for consensus
  S-CVI/Ave >= 0.90

Usage:
  python3 analyse_round.py responses/*.csv --out item-results.csv \
      [--scale-out scale-results.csv] [--comments-out comments.csv] [--min-n 6]
  python3 analyse_round.py --self-test
"""
import argparse
import csv
import io
import math
import os
import tempfile
import statistics
import sys
from collections import defaultdict
from pathlib import Path

CONTROL_DIMS = ["relevance", "clarity", "testability", "claimTypeCorrect", "gateRoleAppropriate"]
GATE_DIMS = ["gateNecessity", "criteriaAdequacy", "failCeilingAppropriate", "unknownCeilingAppropriate"]
DIMS = {"CONTROL": CONTROL_DIMS, "GATE": GATE_DIMS}
EXCLUDED = {"", "NA", "UNSURE"}
KAPPA_EXCELLENT, KAPPA_GOOD, KAPPA_FAIR = 0.74, 0.60, 0.40
ICVI_LARGE_PANEL = 0.78
SCVI_AVE_MIN = 0.90
IQR_MAX = 1.0

FIXTURE = Path(__file__).resolve().parent / "test-fixtures" / "SYNTHETIC_round-1-responses.csv"


def icvi_threshold(n):
    return 1.0 if n <= 5 else ICVI_LARGE_PANEL


def kappa_band(k):
    if k is None:
        return ""
    if k > KAPPA_EXCELLENT:
        return "EXCELLENT"
    if k >= KAPPA_GOOD:
        return "GOOD"
    if k >= KAPPA_FAIR:
        return "FAIR"
    return "POOR"


def quartiles(vals):
    if len(vals) == 1:
        return vals[0], vals[0]
    q = statistics.quantiles(vals, n=4, method="inclusive")
    return q[0], q[2]


def item_stats(ratings):
    n = len(ratings)
    if n == 0:
        return None
    a = sum(1 for r in ratings if r >= 3)
    icvi = a / n
    pc = math.comb(n, a) * 0.5 ** n
    kappa = (icvi - pc) / (1 - pc) if pc < 1 else None
    q1, q3 = quartiles(sorted(ratings))
    return {"N": n, "A": a, "ICVI": icvi, "Pc": pc, "kappa": kappa,
            "median": statistics.median(ratings), "Q1": q1, "Q3": q3, "IQR": q3 - q1}


def classify(s, min_n):
    flags = []
    if s["N"] < min_n:
        flags.append("LOW_N")
    icvi_ok = round(s["ICVI"], 2) >= icvi_threshold(s["N"])
    if not icvi_ok:
        flags.append("ICVI_BELOW_THRESHOLD")
    if s["kappa"] is None or s["kappa"] <= KAPPA_EXCELLENT:
        flags.append("KAPPA_NOT_EXCELLENT")
    if s["IQR"] > IQR_MAX:
        flags.append("IQR_ABOVE_1")
    if s["IQR"] <= IQR_MAX and icvi_ok and "KAPPA_NOT_EXCELLENT" not in flags:
        consensus = "CONSENSUS_ACCEPT"
    elif s["IQR"] <= IQR_MAX and s["ICVI"] < 0.5:
        consensus = "CONSENSUS_REJECT"
    else:
        consensus = "NO_CONSENSUS"
    return flags, consensus


def load_responses(paths):
    """Return ratings[(itemType,itemId,dim)] -> list[int], titles, comments, round."""
    ratings = defaultdict(list)
    titles, comments, seen, rounds, errors = {}, [], set(), set(), []
    for path in paths:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for line, row in enumerate(reader, start=2):
                where = f"{path}:{line}"
                code = (row.get("panelistCode") or "").strip()
                itype = (row.get("itemType") or "").strip()
                iid = (row.get("itemId") or "").strip()
                if not code:
                    errors.append(f"{where}: panelistCode is empty")
                    continue
                if itype not in DIMS:
                    errors.append(f"{where}: unknown itemType {itype!r}")
                    continue
                key = (code, iid)
                if key in seen:
                    errors.append(f"{where}: duplicate response for {code} / {iid}")
                    continue
                seen.add(key)
                rounds.add((row.get("round") or "").strip())
                titles[(itype, iid)] = row.get("itemTitle", "")
                for dim in DIMS[itype]:
                    v = (row.get(dim) or "").strip().upper()
                    if v in EXCLUDED:
                        continue
                    if v not in {"1", "2", "3", "4"}:
                        errors.append(f"{where}: {dim}={v!r} is not 1-4, NA, UNSURE or blank")
                        continue
                    ratings[(itype, iid, dim)].append(int(v))
                extra = {k: (row.get(k) or "").strip() for k in ("proposedClaimType", "proposedGateRole", "comment")}
                if any(x and x != "NA" for x in extra.values()):
                    comments.append({"itemType": itype, "itemId": iid, **extra})
    if len(rounds) > 1:
        errors.append(f"responses mix rounds: {sorted(rounds)}")
    return ratings, titles, comments, rounds, errors, len({c for c, _ in seen})


def analyse(ratings, titles, min_n):
    items = []
    for (itype, iid, dim) in sorted(ratings):
        s = item_stats(ratings[(itype, iid, dim)])
        if s is None:
            continue
        flags, consensus = classify(s, min_n)
        items.append({"itemType": itype, "itemId": iid, "itemTitle": titles.get((itype, iid), ""),
                      "dimension": dim, **s, "kappaBand": kappa_band(s["kappa"]),
                      "icviThreshold": icvi_threshold(s["N"]), "consensus": consensus,
                      "flags": ";".join(flags)})
    scale = []
    groups = defaultdict(list)
    for it in items:
        groups[(it["itemType"], it["dimension"])].append(it["ICVI"])
    for (itype, dim), vals in sorted(groups.items()):
        ave = sum(vals) / len(vals)
        ua = sum(1 for v in vals if v == 1.0) / len(vals)
        scale.append({"itemType": itype, "dimension": dim, "items": len(vals),
                      "SCVI_Ave": ave, "SCVI_UA": ua,
                      "flags": "" if ave >= SCVI_AVE_MIN else "SCVI_AVE_BELOW_0.90"})
    return items, scale


def fmt(v):
    if v is None:
        return ""
    if isinstance(v, float):
        return f"{v:.3f}"
    return str(v)


def write_csv(path, rows, header):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: fmt(r.get(k)) for k in header})


ITEM_HEADER = ["itemType", "itemId", "itemTitle", "dimension", "N", "A", "ICVI", "icviThreshold",
               "Pc", "kappa", "kappaBand", "median", "Q1", "Q3", "IQR", "consensus", "flags"]
SCALE_HEADER = ["itemType", "dimension", "items", "SCVI_Ave", "SCVI_UA", "flags"]
COMMENT_HEADER = ["itemType", "itemId", "proposedClaimType", "proposedGateRole", "comment"]


def self_test():
    """Check the arithmetic against hand-computed values on the SYNTHETIC fixture."""
    ratings, titles, comments, rounds, errors, panel = load_responses([FIXTURE])
    assert not errors, errors
    assert panel == 6, panel
    items, scale = analyse(ratings, titles, min_n=6)
    get = {(i["itemId"], i["dimension"]): i for i in items}
    close = lambda x, y: abs(x - y) < 1e-9

    # 6/6 agree: I-CVI 1, Pc = 1/64, k* = 1
    r = get[("MCF-SYN-001", "relevance")]
    assert (r["N"], r["A"]) == (6, 6) and close(r["ICVI"], 1.0) and close(r["Pc"], 1 / 64)
    assert close(r["kappa"], 1.0) and r["consensus"] == "CONSENSUS_ACCEPT", r
    # 5/6 agree: I-CVI .8333, Pc = 6/64, k* = (5/6 - 6/64) / (1 - 6/64) = 0.8161
    r = get[("MCF-SYN-001", "clarity")]
    assert (r["N"], r["A"]) == (6, 5) and close(r["Pc"], 6 / 64)
    assert close(r["kappa"], (5 / 6 - 6 / 64) / (1 - 6 / 64)) and r["kappaBand"] == "EXCELLENT"
    assert r["consensus"] == "CONSENSUS_ACCEPT", r
    # 4/6 agree: I-CVI .6667, Pc = 15/64, k* = 0.5646 (FAIR), fails .78
    r = get[("MCF-SYN-001", "testability")]
    assert (r["N"], r["A"]) == (6, 4) and close(r["kappa"], (4 / 6 - 15 / 64) / (1 - 15 / 64))
    assert r["kappaBand"] == "FAIR" and "ICVI_BELOW_THRESHOLD" in r["flags"], r
    # one NA and one UNSURE are excluded: 4 valid ratings, all agree -> N <= 5 threshold 1.00 met, LOW_N
    r = get[("MCF-SYN-001", "gateRoleAppropriate")]
    assert r["N"] == 4 and close(r["ICVI"], 1.0) and r["icviThreshold"] == 1.0 and "LOW_N" in r["flags"], r
    # all ratings 1 or 2, tight spread -> consensus to reject
    r = get[("MCF-SYN-002", "relevance")]
    assert r["A"] == 0 and r["IQR"] <= 1 and r["consensus"] == "CONSENSUS_REJECT", r
    # polarised 1,1,1,4,4,4: median 2.5, IQR 3 -> no consensus
    r = get[("MCF-SYN-002", "clarity")]
    assert close(r["median"], 2.5) and close(r["IQR"], 3.0) and r["consensus"] == "NO_CONSENSUS", r
    # rounding rule: 7 of 9 agree = 0.778 -> 0.78 meets threshold; k* = 0.761 excellent
    st = item_stats([4, 4, 3, 3, 3, 3, 3, 2, 1])
    fl, cons = classify(st, 6)
    assert "ICVI_BELOW_THRESHOLD" not in fl and cons == "CONSENSUS_ACCEPT", (st, fl)
    assert close(st["kappa"], (7 / 9 - 36 / 512) / (1 - 36 / 512))
    # 6 of 8 = 0.75 fails
    fl, _ = classify(item_stats([4, 4, 3, 3, 3, 3, 2, 2]), 6)
    assert "ICVI_BELOW_THRESHOLD" in fl
    # gate item
    r = get[("CG-SYN", "gateNecessity")]
    assert close(r["ICVI"], 1.0), r
    # S-CVI/Ave for CONTROL relevance = mean(1.0, 0.0) = 0.5
    s = {(x["itemType"], x["dimension"]): x for x in scale}
    assert close(s[("CONTROL", "relevance")]["SCVI_Ave"], 0.5)
    assert close(s[("CONTROL", "relevance")]["SCVI_UA"], 0.5)
    # error handling: invalid value and duplicate are reported
    bad = io.StringIO()
    bad.write(FIXTURE.read_text(encoding="utf-8").splitlines()[0] + "\n")
    fd, name = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    tmp = Path(name)
    line = "SYN-P01,1,CONTROL,MCF-SYN-001,t,5,3,3,3,3,NA,NA,NA,NA,,,\n"
    tmp.write_text(bad.getvalue() + line + line, encoding="utf-8")
    try:
        _, _, _, _, errs, _ = load_responses([tmp])
    finally:
        tmp.unlink()
    assert any("not 1-4" in e for e in errs) and any("duplicate" in e for e in errs), errs
    print(f"self-test passed ({len(items)} item-dimension results, SYNTHETIC fixture)")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Analyse an AIDCF expert-panel Delphi round.")
    ap.add_argument("responses", nargs="*", help="filled response CSV files")
    ap.add_argument("--out", help="item-level results CSV")
    ap.add_argument("--scale-out", help="scale-level (S-CVI) results CSV")
    ap.add_argument("--comments-out", help="collated anonymised free-text CSV")
    ap.add_argument("--min-n", type=int, default=6, help="minimum valid ratings per item (default 6)")
    ap.add_argument("--self-test", action="store_true", help="run arithmetic checks on the SYNTHETIC fixture")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.responses:
        ap.error("give at least one response CSV, or --self-test")
    ratings, titles, comments, rounds, errors, panel = load_responses(args.responses)
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1
    items, scale = analyse(ratings, titles, args.min_n)
    if args.out:
        write_csv(args.out, items, ITEM_HEADER)
    if args.scale_out:
        write_csv(args.scale_out, scale, SCALE_HEADER)
    if args.comments_out:
        comments.sort(key=lambda c: (c["itemType"], c["itemId"], c["comment"]))
        write_csv(args.comments_out, comments, COMMENT_HEADER)
    flagged = [i for i in items if i["flags"]]
    print(f"round={','.join(sorted(rounds))} panellists={panel} item-dimensions={len(items)} flagged={len(flagged)}")
    for s in scale:
        print(f"  S-CVI {s['itemType']:7} {s['dimension']:26} Ave={s['SCVI_Ave']:.3f} UA={s['SCVI_UA']:.3f} {s['flags']}")
    for i in flagged:
        print(f"  FLAG {i['itemId']:14} {i['dimension']:26} I-CVI={i['ICVI']:.2f} k*={fmt(i['kappa'])} IQR={i['IQR']:.2f} {i['flags']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
