#!/usr/bin/env python3
"""Build the AIDCF expert-panel control and gate sample (AIDCF-VAL-002).

Deterministic, standard library only. Reads the canonical registries and
writes, into validation/expert-panel/:

  control-sample.csv            48 sampled controls with selection reasons
  gate-sample.csv               all 15 Critical Gates with criteria counts
  round-1-response-template.csv one row per control item and gate item
  round-1-item-booklet.md       the text panellists rate (from the registries)

Usage:
  python3 build_sample.py           write the outputs
  python3 build_sample.py --check   regenerate in memory; exit 1 if any output
                                    on disk differs or a sampling rule fails

Selection rules (documented in AIDCF-VAL-002 section 6):

  Ordering key. No pseudo-random generator is used. Every control is ranked by
  SHA-256 of "<SEED>:<controlId>" (lowest hex digest first). The order is
  therefore identical on every platform and Python version, and changing SEED
  is the only way to draw a different sample.

  R1 Gate floor. For each gate in GATE_FLOOR_GATES, in gate order, add
     CRITICAL-mapped controls (by rank) until the sample holds at least
     GATE_FLOOR CRITICAL controls for that gate. A control CRITICAL for
     several gates counts towards each.
  R2 Claim-type floor. For each claim type (canonical order), add controls of
     that type until CLAIM_FLOOR are held. Candidates from domains holding
     fewer than DOMAIN_CAP sampled controls are preferred, then rank.
  R3 Domain floor. For each domain (registry order), add controls until
     DOMAIN_FLOOR are held, preferring a claim type the domain does not yet
     have in the sample, then rank. R2 and R3 deliberately do not prefer
     CRITICAL controls, so that SUPPORTING-only and unmapped controls are
     represented and their gate role can be challenged.
  R4 Critical-weighted fill. Until SAMPLE_SIZE is reached, add from domains
     below DOMAIN_CAP, preferring the domain with fewest sampled controls,
     then a CRITICAL mapping, then rank. Over-weighting of CRITICAL controls
     comes from R1 and R4; --check fails unless the CRITICAL-holding share of
     the sample exceeds the population share.
"""
import argparse
import csv
import hashlib
import io
import sys
from collections import Counter, defaultdict
from pathlib import Path

SEED = "AIDCF-VAL-002-2026-10-11"
SAMPLE_SIZE = 48
GATE_FLOOR = 2
GATE_FLOOR_GATES = [f"CG-{n:02d}" for n in list(range(1, 11)) + [13, 14, 15]]
CLAIM_FLOOR = 4
DOMAIN_FLOOR = 3
DOMAIN_CAP = 4
CLAIM_ORDER = ["DESIGN", "IMPLEMENTATION", "OPERATION", "EFFECTIVENESS", "RESILIENCE"]

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
REPO = KIT.parent.parent
REG = REPO / "registries"

CONTROL_DIMS = ["relevance", "clarity", "testability", "claimTypeCorrect", "gateRoleAppropriate"]
GATE_DIMS = ["gateNecessity", "criteriaAdequacy", "failCeilingAppropriate", "unknownCeilingAppropriate"]
TEMPLATE_HEADER = (["panelistCode", "round", "itemType", "itemId", "itemTitle"]
                   + CONTROL_DIMS + GATE_DIMS
                   + ["proposedClaimType", "proposedGateRole", "comment"])


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def rank_key(cid):
    return hashlib.sha256(f"{SEED}:{cid}".encode("utf-8")).hexdigest()


def load():
    controls = read_csv(REG / "controls" / "controls.csv")
    mappings = read_csv(REG / "controls" / "gate-mappings.csv")
    gates = read_csv(REG / "gates" / "critical-gates.csv")
    criteria = read_csv(REG / "gates" / "critical-gate-criteria.csv")
    domains = [r["domainId"] for r in read_csv(REG / "domains" / "domains.csv")]
    claim_vocab = [r["code"] for r in read_csv(REG / "vocabularies" / "claim-types.csv")]
    if sorted(claim_vocab) != sorted(CLAIM_ORDER):
        raise SystemExit(f"claim-type vocabulary changed: {claim_vocab}")
    crit, supp = defaultdict(list), defaultdict(list)
    gate_ids = {g["gateId"] for g in gates}
    for m in mappings:
        if m["gateId"] not in gate_ids:
            raise SystemExit(f"gate-mappings.csv: unknown gate {m['gateId']}")
        (crit if m["role"] == "CRITICAL" else supp)[m["controlId"]].append(m["gateId"])
    return controls, crit, supp, gates, criteria, domains


def select(controls, crit, domains):
    by_id = {c["controlId"]: c for c in controls}
    ranked = sorted(by_id, key=rank_key)
    chosen, reasons = [], defaultdict(list)
    dom_count, claim_count = Counter(), Counter()

    def add(cid, reason):
        if cid not in reasons:
            chosen.append(cid)
            dom_count[by_id[cid]["domainId"]] += 1
            claim_count[by_id[cid]["claimType"]] += 1
        reasons[cid].append(reason)

    # R1 gate floor
    for g in GATE_FLOOR_GATES:
        have = sum(1 for c in chosen if g in crit[c])
        for cid in ranked:
            if have >= GATE_FLOOR:
                break
            if g in crit[cid] and cid not in reasons:
                add(cid, f"R1_GATE_FLOOR:{g}")
                have += 1
    # R2 claim-type floor
    for ct in CLAIM_ORDER:
        while claim_count[ct] < CLAIM_FLOOR:
            cands = [c for c in ranked if c not in reasons and by_id[c]["claimType"] == ct]
            if not cands:
                break
            cands.sort(key=lambda c: (dom_count[by_id[c]["domainId"]] >= DOMAIN_CAP, rank_key(c)))
            add(cands[0], f"R2_CLAIM_TYPE_FLOOR:{ct}")
    # R3 domain floor
    for d in domains:
        while dom_count[d] < DOMAIN_FLOOR:
            present = {by_id[c]["claimType"] for c in chosen if by_id[c]["domainId"] == d}
            cands = [c for c in ranked if c not in reasons and by_id[c]["domainId"] == d]
            if not cands:
                break
            cands.sort(key=lambda c: (by_id[c]["claimType"] in present, rank_key(c)))
            add(cands[0], f"R3_DOMAIN_FLOOR:{d}")
    # R4 critical-weighted fill
    while len(chosen) < SAMPLE_SIZE:
        cands = [c for c in ranked if c not in reasons
                 and dom_count[by_id[c]["domainId"]] < DOMAIN_CAP]
        if not cands:
            break
        cands.sort(key=lambda c: (dom_count[by_id[c]["domainId"]], not crit[c], rank_key(c)))
        add(cands[0], "R4_CRITICAL_WEIGHTED_FILL")
    order = {d: i for i, d in enumerate(domains)}
    chosen.sort(key=lambda c: (order[by_id[c]["domainId"]], c))
    return chosen, reasons


def verify(controls, crit, domains, chosen):
    by_id = {c["controlId"]: c for c in controls}
    errors = []
    if len(chosen) != SAMPLE_SIZE:
        errors.append(f"sample size {len(chosen)} != {SAMPLE_SIZE}")
    if set(domains) - {by_id[c]["domainId"] for c in chosen}:
        errors.append("not all domains covered")
    if set(CLAIM_ORDER) - {by_id[c]["claimType"] for c in chosen}:
        errors.append("not all claim types covered")
    for g in GATE_FLOOR_GATES:
        avail = sum(1 for c in by_id if g in crit[c])
        got = sum(1 for c in chosen if g in crit[c])
        if got < min(GATE_FLOOR, avail):
            errors.append(f"{g}: {got} CRITICAL controls sampled, need {min(GATE_FLOOR, avail)}")
    pop_share = sum(1 for c in by_id if crit[c]) / len(by_id)
    smp_share = sum(1 for c in chosen if crit[c]) / max(len(chosen), 1)
    if smp_share <= pop_share:
        errors.append(f"CRITICAL not over-weighted: sample {smp_share:.2f} <= population {pop_share:.2f}")
    # controls.csv and gate-mappings.csv must agree
    for c in controls:
        listed = sorted(x for x in c["criticalGates"].split(";") if x)
        if listed != sorted(crit[c["controlId"]]):
            errors.append(f"{c['controlId']}: controls.csv criticalGates {listed} != gate-mappings {sorted(crit[c['controlId']])}")
    return errors, pop_share, smp_share


def to_csv(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


def render(controls, crit, supp, gates, criteria, domains, chosen, reasons):
    by_id = {c["controlId"]: c for c in controls}
    out = {}
    out["control-sample.csv"] = to_csv(
        ["controlId", "domain", "family", "title", "claimType", "criticalGates", "supportingGates", "selectionReason"],
        [[c, by_id[c]["domainId"], by_id[c]["familyId"], by_id[c]["title"], by_id[c]["claimType"],
          ";".join(sorted(crit[c])), ";".join(sorted(supp[c])), ";".join(reasons[c])] for c in chosen])
    ccount = Counter(r["gateId"] for r in criteria)
    out["gate-sample.csv"] = to_csv(
        ["gateId", "name", "criteriaCount", "criticalControlsInRegistry", "criticalControlsInSample"],
        [[g["gateId"], g["name"], ccount[g["gateId"]],
          sum(1 for c in by_id if g["gateId"] in crit[c]),
          sum(1 for c in chosen if g["gateId"] in crit[c])] for g in gates])
    rows = []
    for c in chosen:
        rows.append(["", "1", "CONTROL", c, by_id[c]["title"]] + [""] * len(CONTROL_DIMS)
                    + ["NA"] * len(GATE_DIMS) + ["", "", ""])
    for g in gates:
        rows.append(["", "1", "GATE", g["gateId"], g["name"]] + ["NA"] * len(CONTROL_DIMS)
                    + [""] * len(GATE_DIMS) + ["NA", "NA", ""])
    out["round-1-response-template.csv"] = to_csv(TEMPLATE_HEADER, rows)
    out["round-1-item-booklet.md"] = booklet(by_id, crit, supp, gates, criteria, chosen)
    return out


def booklet(by_id, crit, supp, gates, criteria, chosen):
    L = []
    a = L.append
    a("# AIDCF Expert Panel Round 1 Item Booklet")
    a("")
    a("| Field | Value |")
    a("|---|---|")
    a("| Document ID | AIDCF-VAL-002-B |")
    a("| Title | AIDCF Expert Panel Round 1 Item Booklet |")
    a("| Version | 1.0 |")
    a("| Date | 2026-10-11 |")
    a("| Status | Draft for controlled review |")
    a("| Author | Siva Sethumadhavan |")
    a("")
    a("Revision history")
    a("")
    a("| Version | Date | Change |")
    a("|---|---|---|")
    a("| 1.0 | 2026-10-11 | First issue. |")
    a("")
    a("This booklet is generated by `tools/build_sample.py` from the canonical registries "
      "(`registries/controls/controls.csv`, `registries/controls/gate-mappings.csv`, "
      "`registries/gates/critical-gates.csv`, `registries/gates/critical-gate-criteria.csv`). "
      "Do not edit it by hand. Rate each item in `round-1-response-template.csv` using the scales in "
      "`round-1-questionnaire.md` (AIDCF-VAL-002-A). Item text is reproduced verbatim from the registries; "
      "registry status of every control is CANDIDATE.")
    a("")
    a(f"Part A holds {len(chosen)} control items. Part B holds {len(gates)} gate items.")
    a("")
    a("## Part A: Control items")
    a("")
    for i, c in enumerate(chosen, 1):
        r = by_id[c]
        a(f"### A{i:02d}. {c}: {r['title']}")
        a("")
        a(f"- Domain / family: {r['domainId']} / {r['familyId']}")
        a(f"- Claim type: {r['claimType']} (required assurance level {r['requiredAssuranceLevel']})")
        a(f"- Control type: {r['controlType']}; profile tier: {r['profileTier']}; sufficiency floor: {r['sufficiencyFloor']}")
        a(f"- CRITICAL for: {', '.join(sorted(crit[c])) or 'none'}")
        a(f"- SUPPORTING for: {', '.join(sorted(supp[c])) or 'none'}")
        a("")
        a(f"Objective: {r['objective']}")
        a("")
        a(f"Requirement: {r['requirement']}")
        a("")
    a("## Part B: Gate items")
    a("")
    for g in gates:
        a(f"### {g['gateId']}: {g['name']}")
        a("")
        a(f"- Scope: {g['scope']}")
        a(f"- Evidence floor: {g['evidenceFloor']}; required evidence classes: {g['requiredClasses'].replace(';', ', ')}")
        a(f"- FAIL ceiling: {g['failCeiling']}")
        a(f"- UNKNOWN ceiling: {g['unknownCeiling']}")
        a(f"- Approved not-applicable conditions: {g['approvedNaConditions']}")
        a("")
        a("| Criterion | Statement | Evidence | Test method |")
        a("|---|---|---|---|")
        for k in criteria:
            if k["gateId"] == g["gateId"]:
                cells = [k["criterionId"], k["criterion"], k["evidence"], k["testMethod"]]
                a("| " + " | ".join(x.replace("|", "/").replace("\n", " ") for x in cells) + " |")
        a("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verify outputs on disk are current")
    args = ap.parse_args()
    controls, crit, supp, gates, criteria, domains = load()
    chosen, reasons = select(controls, crit, domains)
    errors, pop, smp = verify(controls, crit, domains, chosen)
    outputs = render(controls, crit, supp, gates, criteria, domains, chosen, reasons)
    if args.check:
        for name, text in outputs.items():
            p = KIT / name
            if not p.exists() or p.read_text(encoding="utf-8") != text:
                errors.append(f"{name} is missing or out of date; run build_sample.py")
    else:
        for name, text in outputs.items():
            (KIT / name).write_text(text, encoding="utf-8", newline="\n")
    print(f"sample={len(chosen)} CRITICAL-holding share: sample {smp:.2f}, population {pop:.2f}")
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1
    print("check passed" if args.check else "outputs written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
