#!/usr/bin/env python3
"""Build the AIDCF mini-pilot Starter Profile and Evidence Request List.

Writes two files from the AIDCF-007A registry (registries/controls/*.csv,
registries/gates/critical-gates.csv):

  pilots/pilot-framework/starter-profile.csv
  pilots/pilot-authorisation/evidence-request-list.csv
  pilots/pilot-results/control-claim-log-template.csv

Selection rule (documented in AIDCF-PIL-001 section 7):

  In-scope mapped gates G = CG-01, CG-02, CG-03, CG-05, CG-06, CG-07, CG-10.
  (CG-11 and CG-12 are meta-gates evaluated across the whole profile; they
  carry no per-control mapping and select no controls.)

  R1  every control holding a CRITICAL mapping to a gate in G, so that each
      in-scope gate can be evaluated by the AIDCF-010 roll-up rule (a gate
      cannot PASS while any CRITICAL control is NOT_ASSESSED);
  R2  every AI-layer control (domain CMP, STO or NET) not selected by R1 that
      holds a SUPPORTING mapping to CG-01, or SUPPORTING mappings to two or
      more gates in G.

Mandatory claim types at the pilot target level T = AL3 follow AIDCF-010
Part IV: L = min(T, r), where r is the registry requiredAssuranceLevel;
L = AL2 gives DESIGN, L = AL3 gives DESIGN;IMPLEMENTATION.

Evidence Request List rule (documented in AIDCF-PIL-003):

  For each selected control and each mandatory claim type c at AL3:
    - if c equals the profile claimType p, one MANDATORY row per registry
      mandatoryItem, carrying the profile's classes, floors, coverage,
      independence, alternatives and unknownEffect unchanged;
    - if c is shallower than p, one MANDATORY row stating the AIDCF-008 s29
      minimum pattern for c (registry profile fields that apply to c are
      carried; sufficiency target S3 per AIDCF-008 s25 and the AIDCF-010
      Part VIII effective floor).
  For each selected control whose p is deeper than AL3, one AVAILABILITY_ONLY
  row per registry mandatoryItem, used to measure evidence availability and
  to plan an AL4/AL5 follow-on. Such items are not assessed for p at AL3.
  For each criterion of each in-scope gate (registries/gates/
  critical-gate-criteria.csv), one GATE_CRITERION row. Criteria whose test
  method names TEST, SCENARIO_EXERCISE or REPERFORMANCE are marked
  MANDATORY_EXISTING_RECORDS_ONLY (the pilot reviews existing records and
  performs no test); CG-11 and CG-12 criteria are ASSESSMENT_RECORD rows
  satisfied from the assessment team's own records.

Usage:
    python3 pilots/pilot-framework/tools/build_starter_profile.py           # write files
    python3 pilots/pilot-framework/tools/build_starter_profile.py --check   # exit 1 if any file would change

Standard library only. Deterministic. Output UTF-8, LF line endings, minimal
RFC 4180 quoting. Multi-valued cells use ";" (gates, claim types) or the
registry's own "; " separator (evidence classes, operating states).
"""

import csv
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = ROOT / "registries"
OUT_PROFILE = ROOT / "pilots" / "pilot-framework" / "starter-profile.csv"
OUT_ERL = ROOT / "pilots" / "pilot-authorisation" / "evidence-request-list.csv"
OUT_LOG = ROOT / "pilots" / "pilot-results" / "control-claim-log-template.csv"

TARGET_AL = "AL3"
IN_SCOPE_GATES = ["CG-01", "CG-02", "CG-03", "CG-05", "CG-06", "CG-07", "CG-10"]
META_GATES = ["CG-11", "CG-12"]
AI_LAYER = ("CMP", "STO", "NET")
CLAIM_ORDER = ["DESIGN", "IMPLEMENTATION", "OPERATION", "EFFECTIVENESS", "RESILIENCE"]
AL_ORDER = ["AL0", "AL1", "AL2", "AL3", "AL4", "AL5", "AL6"]
MANDATORY_BY_L = {
    "AL2": ["DESIGN"],
    "AL3": ["DESIGN", "IMPLEMENTATION"],
}

PROFILE_COLUMNS = [
    "controlId", "domain", "title", "claimType", "requiredAssuranceLevel",
    "mandatoryClaimTypesAtAL3", "criticalGates", "selectionReason",
]
LOG_COLUMNS = [
    "controlId", "domain", "claimType", "inScopeGateRoles",
    "mandatoryEvidenceRequests", "availabilityOnlyRequests",
    "mandatoryRequestsFulfilled", "mandatoryRequestsFulfilledByDueDate",
    "availabilityOnlyItemsExisting", "assessorHours", "technicalReviewHours",
    "hostHours", "primaryResult", "secondAssessorResult", "resultAgreement",
    "disagreementCause", "sufficiencyAchieved", "confidence", "unknownType",
    "unknownSeverity", "findingIds", "usabilityIssueIds", "defectIds", "notes",
]
ERL_COLUMNS = [
    "requestId", "controlId", "criterionId", "domain", "controlTitle", "claimTypeServed",
    "requestBasis", "al3Use", "evidenceItem", "requiredClasses",
    "optionalClasses", "qualityFloor", "sufficiencyFloor", "stateCoverage",
    "periodCoverage", "independence", "acceptableAlternatives",
    "suggestedMethods", "inScopeGateRoles", "unknownEffect",
    "defaultClassification",
]

PATTERN_TEXT = {
    "DESIGN": (
        "Approved design evidence for {title}: current, approved design basis, "
        "specification, drawing or procedure showing how the requirement is met, "
        "with the competent technical analysis relied on (AIDCF-008 s29 DESIGN pattern)"
    ),
    "IMPLEMENTATION": (
        "As-built or as-configured evidence for {title}, extracted with source, "
        "method, privilege and timestamp recorded, plus observation or walkthrough "
        "corroboration, reconciled to the approved design (AIDCF-008 s29 "
        "IMPLEMENTATION pattern)"
    ),
}
PATTERN_CLASSES = {
    "DESIGN": "E1",
    "IMPLEMENTATION": "E2; E3 or E6",
}
METHODS = {
    "DESIGN": "DOCUMENT_REVIEW; ANALYSIS; INQUIRY (corroborating only)",
    "IMPLEMENTATION": "RECONCILIATION; INSPECTION; SAMPLING; DOCUMENT_REVIEW",
    "AVAILABILITY": "DOCUMENT_REVIEW (existence, date and index only)",
}
PATTERN_SUFFICIENCY = "S3"


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def render(columns, rows):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return buf.getvalue()


def mandatory_claim_types(required_level):
    level = min(TARGET_AL, required_level, key=AL_ORDER.index)
    return MANDATORY_BY_L[level]


def load():
    controls = {r["controlId"]: r for r in read_csv(REG / "controls" / "controls.csv")}
    profiles = {r["controlId"]: r for r in read_csv(REG / "controls" / "evidence-profiles.csv")}
    mappings = read_csv(REG / "controls" / "gate-mappings.csv")
    gates = {r["gateId"]: r for r in read_csv(REG / "gates" / "critical-gates.csv")}
    criteria = read_csv(REG / "gates" / "critical-gate-criteria.csv")
    domains = [r["domainId"] for r in read_csv(REG / "domains" / "domains.csv")]
    claim_types = [r["code"] for r in read_csv(REG / "vocabularies" / "claim-types.csv")]
    return controls, profiles, mappings, gates, criteria, domains, claim_types


def validate_inputs(controls, profiles, mappings, gates, claim_types):
    errors = []
    for g in IN_SCOPE_GATES + META_GATES:
        if g not in gates:
            errors.append(f"gate {g} missing from critical-gates.csv")
    if claim_types != CLAIM_ORDER:
        errors.append(f"claim-types vocabulary differs from expected order: {claim_types}")
    for m in mappings:
        if m["controlId"] not in controls:
            errors.append(f"gate-mappings references unknown control {m['controlId']}")
        if m["gateId"] not in gates:
            errors.append(f"gate-mappings references unknown gate {m['gateId']}")
    for cid in controls:
        if cid not in profiles:
            errors.append(f"control {cid} has no evidence profile")
        elif profiles[cid]["claimType"] != controls[cid]["claimType"]:
            errors.append(f"control {cid}: profile claimType differs from control claimType")
    return errors


def select(controls, mappings, domains):
    roles = {}
    for m in mappings:
        if m["gateId"] in IN_SCOPE_GATES:
            roles.setdefault(m["controlId"], []).append((m["gateId"], m["role"]))
    selected = {}
    for cid, rl in roles.items():
        crit = sorted(g for g, r in rl if r == "CRITICAL")
        sup = sorted(g for g, r in rl if r == "SUPPORTING")
        reasons = []
        if crit:
            reasons.append("R1 CRITICAL for in-scope " + ", ".join(crit))
        elif controls[cid]["domainId"] in AI_LAYER and ("CG-01" in sup or len(sup) >= 2):
            reasons.append("R2 AI-layer SUPPORTING for in-scope " + ", ".join(sup))
        else:
            continue
        if crit and sup:
            reasons.append("also SUPPORTING for in-scope " + ", ".join(sup))
        selected[cid] = {"crit": crit, "sup": sup, "reason": "; ".join(reasons)}
    order = sorted(selected, key=lambda c: (domains.index(controls[c]["domainId"]), c))
    return order, selected


def default_classification(control, claim, crit_gates):
    if control["domainId"] in ("SEC", "NET"):
        return "HIGHLY_RESTRICTED"
    if claim == "IMPLEMENTATION" and "CG-07" in crit_gates:
        return "HIGHLY_RESTRICTED"
    return "CONFIDENTIAL"


def build():
    controls, profiles, mappings, gates, criteria, domains, claim_types = load()
    errors = validate_inputs(controls, profiles, mappings, gates, claim_types)
    if errors:
        raise SystemExit("input validation failed:\n  " + "\n  ".join(errors))
    order, selected = select(controls, mappings, domains)

    profile_rows = []
    erl_rows = []
    log_rows = []
    seq = 0

    def add_request(**kw):
        nonlocal seq
        seq += 1
        row = {k: "" for k in ERL_COLUMNS}
        row["requestId"] = f"ERL-{seq:03d}"
        row.update(kw)
        erl_rows.append(row)

    for cid in order:
        c = controls[cid]
        p = profiles[cid]
        sel = selected[cid]
        mct = mandatory_claim_types(c["requiredAssuranceLevel"])
        profile_rows.append({
            "controlId": cid,
            "domain": c["domainId"],
            "title": c["title"],
            "claimType": c["claimType"],
            "requiredAssuranceLevel": c["requiredAssuranceLevel"],
            "mandatoryClaimTypesAtAL3": ";".join(mct),
            "criticalGates": c["criticalGates"],
            "selectionReason": sel["reason"],
        })
        gate_roles = ";".join(
            [f"{g}:CRITICAL" for g in sel["crit"]] + [f"{g}:SUPPORTING" for g in sel["sup"]]
        )
        items = [i.strip() for i in p["mandatoryItems"].split("; ") if i.strip()]
        common = {
            "controlId": cid,
            "domain": c["domainId"],
            "controlTitle": c["title"],
            "inScopeGateRoles": gate_roles,
        }
        for claim in mct:
            cls = default_classification(c, claim, sel["crit"])
            if claim == p["claimType"]:
                for item in items:
                    add_request(
                        **common,
                        claimTypeServed=claim,
                        requestBasis="PROFILE_MANDATORY_ITEM",
                        al3Use="MANDATORY",
                        evidenceItem=item,
                        requiredClasses=p["requiredClasses"],
                        optionalClasses=p["optionalClasses"],
                        qualityFloor=p["qualityFloor"],
                        sufficiencyFloor=p["sufficiencyFloor"],
                        stateCoverage=p["stateCoverage"],
                        periodCoverage=p["periodCoverage"],
                        independence=p["independence"],
                        acceptableAlternatives=p["acceptableAlternatives"],
                        suggestedMethods=METHODS[claim],
                        unknownEffect=p["unknownEffect"],
                        defaultClassification=cls,
                    )
            else:
                add_request(
                    **common,
                    claimTypeServed=claim,
                    requestBasis="CLAIM_TYPE_PATTERN",
                    al3Use="MANDATORY",
                    evidenceItem=PATTERN_TEXT[claim].format(title=c["title"]),
                    requiredClasses=PATTERN_CLASSES[claim],
                    optionalClasses=p["optionalClasses"],
                    qualityFloor=p["qualityFloor"],
                    sufficiencyFloor=PATTERN_SUFFICIENCY,
                    stateCoverage=p["stateCoverage"],
                    periodCoverage="Design or configuration in force at the assessment date",
                    independence="Profile requirement, where it applies to this claim type: " + p["independence"],
                    acceptableAlternatives="",
                    suggestedMethods=METHODS[claim],
                    unknownEffect=p["unknownEffect"],
                    defaultClassification=cls,
                )
        if CLAIM_ORDER.index(p["claimType"]) > CLAIM_ORDER.index(mct[-1]):
            for item in items:
                add_request(
                    **common,
                    claimTypeServed=p["claimType"],
                    requestBasis="PROFILE_ITEM_ABOVE_AL3",
                    al3Use="AVAILABILITY_ONLY",
                    evidenceItem=item,
                    requiredClasses=p["requiredClasses"],
                    optionalClasses=p["optionalClasses"],
                    qualityFloor=p["qualityFloor"],
                    sufficiencyFloor=p["sufficiencyFloor"],
                    stateCoverage=p["stateCoverage"],
                    periodCoverage=p["periodCoverage"],
                    independence=p["independence"],
                    acceptableAlternatives=p["acceptableAlternatives"],
                    suggestedMethods=METHODS["AVAILABILITY"],
                    unknownEffect="Not applied at AL3: claim type above the pilot target level; record availability only",
                    defaultClassification=default_classification(c, p["claimType"], sel["crit"]),
                )

    # Gate-criterion requests: one row per criterion of each in-scope gate.
    test_methods = ("TEST", "SCENARIO_EXERCISE", "REPERFORMANCE")
    for gid in IN_SCOPE_GATES + META_GATES:
        g = gates[gid]
        meta = gid in META_GATES
        for cr in [x for x in criteria if x["gateId"] == gid]:
            method_part = cr["testMethod"].split(":")[0]
            needs_test = any(t in method_part for t in test_methods)
            if meta:
                use = "ASSESSMENT_RECORD"
            elif needs_test:
                use = "MANDATORY_EXISTING_RECORDS_ONLY"
            else:
                use = "MANDATORY"
            add_request(
                criterionId=cr["criterionId"],
                controlTitle=g["name"],
                claimTypeServed="",
                requestBasis="GATE_CRITERION",
                al3Use=use,
                evidenceItem=cr["evidence"] + " (criterion: " + cr["criterion"] + ")",
                requiredClasses=g["requiredClasses"].replace(";", "; "),
                qualityFloor="",
                sufficiencyFloor=f"S3 effective at DESIGN/IMPLEMENTATION depth (gate floor {g['evidenceFloor']}; AIDCF-010 Part VIII)",
                periodCoverage="As stated in the criterion; evidence currency per the related control profiles",
                suggestedMethods=cr["testMethod"] + (
                    " [pilot: review of existing records only; no test is performed]" if needs_test else ""),
                inScopeGateRoles=gid,
                unknownEffect="Gate UNKNOWN ceiling: " + g["unknownCeiling"],
                defaultClassification="HIGHLY_RESTRICTED" if gid == "CG-07" else "CONFIDENTIAL",
            )

    for prow in profile_rows:
        cid = prow["controlId"]
        reqs = [r for r in erl_rows if r["controlId"] == cid and not r["criterionId"]]
        avail = sum(1 for r in reqs if r["al3Use"] == "AVAILABILITY_ONLY")
        for claim in prow["mandatoryClaimTypesAtAL3"].split(";"):
            row = {k: "" for k in LOG_COLUMNS}
            row.update({
                "controlId": cid,
                "domain": prow["domain"],
                "claimType": claim,
                "inScopeGateRoles": reqs[0]["inScopeGateRoles"],
                "mandatoryEvidenceRequests": sum(
                    1 for r in reqs if r["al3Use"] == "MANDATORY" and r["claimTypeServed"] == claim
                ),
                "availabilityOnlyRequests": avail if claim == "DESIGN" else 0,
            })
            log_rows.append(row)

    # Post-conditions: every in-scope gate's CRITICAL set is fully selected.
    sel_ids = set(order)
    for m in mappings:
        if m["gateId"] in IN_SCOPE_GATES and m["role"] == "CRITICAL" and m["controlId"] not in sel_ids:
            raise SystemExit(f"post-condition failed: {m['controlId']} CRITICAL for {m['gateId']} not selected")

    return {
        OUT_PROFILE: render(PROFILE_COLUMNS, profile_rows),
        OUT_ERL: render(ERL_COLUMNS, erl_rows),
        OUT_LOG: render(LOG_COLUMNS, log_rows),
    }, profile_rows, erl_rows


def summary(profile_rows, erl_rows):
    from collections import Counter
    dom = Counter(r["domain"] for r in profile_rows)
    claims = sum(len(r["mandatoryClaimTypesAtAL3"].split(";")) for r in profile_rows)
    basis = Counter(r["requestBasis"] for r in erl_rows)
    reasons = Counter(r["selectionReason"][:2] for r in profile_rows)
    lines = [
        f"controls selected: {len(profile_rows)} ({', '.join(f'{k} {v}' for k, v in reasons.items())})",
        "by domain: " + ", ".join(f"{k} {v}" for k, v in dom.items()),
        f"mandatory control-claim assessments at AL3: {claims}",
        f"evidence requests: {len(erl_rows)} ("
        + ", ".join(f"{k} {v}" for k, v in sorted(basis.items())) + ")",
    ]
    return "\n".join(lines)


def main(argv):
    check = "--check" in argv
    outputs, profile_rows, erl_rows = build()
    stale = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            stale.append(path)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(text)
    print(summary(profile_rows, erl_rows))
    if check:
        if stale:
            for path in stale:
                print(f"out of date: {path.relative_to(ROOT)}")
            return 1
        print("check passed: outputs are up to date")
        return 0
    for path in stale:
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
