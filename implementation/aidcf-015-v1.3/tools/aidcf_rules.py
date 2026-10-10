"""AIDCF-016 canonical rules for the AIDCF-015 v1.3 reference package.

Shared by tools/build_dataset.py (which records declared results and asserts they agree with
these functions) and tools/run_all.py (which recomputes everything independently from the
dataset and the copied registries and reports every disagreement).

Rule identifiers: BR-001..BR-015 are the AIDCF-014 v1.1 section 18 business rules; MDM-R01..MDM-R20
are the AIDCF-016 canonical rules; TR-01..TR-18 are the AIDCF-014 section 11 traceability rules.
"""
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG.parents[1] / "schemas" / "tools"))
import aidcf_model as M  # noqa: E402

RANK = M.DECISION_RANK
CRANK = M.CLAIM_RANK
CLS_RANK = M.CLASSIFICATION_RANK
REL_PROPS = {r[1]: r for r in M.REL}
INVERSE_PROPS = set(M.INVERSES)
RELEASE_ID = "AIDCF-REL-2026.10.1"
SCORE_METHOD = "AIDCF-016 MDM score 1.3"


# ------------------------------------------------------------------ loading
def read_csv(p):
    with Path(p).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_registry(pkg=PKG):
    r = pkg / "registries"
    reg = {
        "controls": {x["controlId"]: x for x in read_csv(r / "controls/controls.csv")},
        "controls_json": {x["controlId"]: x for x in json.loads((r / "controls/controls.json").read_text(encoding="utf-8"))["controls"]},
        "families": {x["familyId"]: x for x in read_csv(r / "families/control-families.csv")},
        "domains": {x["domainId"]: x for x in read_csv(r / "domains/domains.csv")},
        "gates": {x["gateId"]: x for x in read_csv(r / "gates/critical-gates.csv")},
        "criteria": read_csv(r / "gates/critical-gate-criteria.csv"),
        "mappings": read_csv(r / "controls/gate-mappings.csv"),
        "profiles": {x["controlId"]: x for x in read_csv(r / "controls/evidence-profiles.csv")},
    }
    reg["roles"] = defaultdict(dict)  # gate -> {control: role}
    for m in reg["mappings"]:
        reg["roles"][m["gateId"]][m["controlId"]] = m["role"]
    return reg


def load_records(paths):
    recs = []
    for p in paths:
        d = json.loads(Path(p).read_text(encoding="utf-8"))
        items = d["@graph"] if isinstance(d, dict) and "@graph" in d else (d if isinstance(d, list) else [d])
        for it in items:
            recs.append(it)
    return recs


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


class Index:
    def __init__(self, recs):
        self.recs = {}
        self.dupes = []
        for r in recs:
            if r.get("id") in self.recs:
                self.dupes.append(r.get("id"))
            self.recs[r.get("id")] = r
        self.out = defaultdict(list)   # (s, prop) -> [o]
        self.inn = defaultdict(list)   # (o, prop) -> [s]
        self.edges = []                # (s, prop, o)
        for r in self.recs.values():
            for k, v in r.items():
                if k in REL_PROPS:
                    for o in as_list(v):
                        self.out[(r["id"], k)].append(o)
                        self.inn[(o, k)].append(r["id"])
                        self.edges.append((r["id"], k, o))

    def get(self, i):
        return self.recs.get(i, {})

    def type(self, i):
        return self.recs.get(i, {}).get("type")

    def is_a(self, i, c):
        t = self.type(i)
        return t is not None and c in M.superclasses(t)

    def of(self, c):
        return [r for r in self.recs.values() if r.get("type") and c in M.superclasses(r["type"])]

    def o(self, s, p):
        return self.out.get((s, p), [])

    def i(self, o, p):
        return self.inn.get((o, p), [])


# ------------------------------------------------------------------ gate roll-up (SPEC 6.2 + AIDCF-016 9.2)
def suff(code):
    return int(code[1:]) if code and code[0] == "S" else -1


def open_unknown(u):
    return u.get("unknownStatus") != "RESOLVED"


def gate_attached_unknowns(ix, gr_id):
    us = set(ix.o(gr_id, "hasUnknown")) | {s for s in ix.i(gr_id, "constrains") if ix.type(s) == "UnknownRecord"}
    return [ix.get(u) for u in sorted(us) if ix.type(u) == "UnknownRecord"]


def control_results(ix):
    """controlId -> (result, CA id) for controls with a Control Assessment in the dataset."""
    out = {}
    for c in ix.of("Control"):
        cas = ix.o(c["id"], "assessedBy")
        if cas:
            ca = ix.get(cas[0])
            out[c["controlCode"]] = (ca.get("result"), cas[0])
    return out


def rollup(gate_code, reg, results, criteria_outcomes, unknowns, evidence_suff, supporting_evals=None, applicability="IN_SCOPE",
           na_ok=False):
    """Return (state, rationale) for one gate.

    results: controlId -> result for assessed controls. Registry CRITICAL controls without a result are NOT_ASSESSED.
    criteria_outcomes: criterionId -> MET | NOT_MET | UNKNOWN | NOT_EVALUATED.
    unknowns: UNKNOWN Records attached to the gate (HAS_UNKNOWN or CONSTRAINS).
    """
    if applicability == "APPROVED_NA":
        return ("APPROVED_NA", "Approved boundary rationale.") if na_ok else ("UNKNOWN", "APPROVED_NA claimed without rationale and approval.")
    roles = reg["roles"].get(gate_code, {})
    crit = sorted(c for c, r in roles.items() if r == "CRITICAL")
    crit_res = {c: results.get(c, "NOT_ASSESSED") for c in crit}
    bad = [c for c, r in crit_res.items() if r in ("PARTIAL", "NONCONFORMING")]
    not_met = [k for k, v in criteria_outcomes.items() if v == "NOT_MET"]
    if bad or not_met:
        return "FAIL", "FAIL: CRITICAL control(s) %s; criteria not met: %s." % (
            ", ".join("%s %s" % (c, crit_res[c]) for c in bad) or "none", ", ".join(not_met) or "none")
    us45 = [u["id"] for u in unknowns if u.get("unknownSeverity") in ("US4", "US5") and open_unknown(u)]
    assessed_crit = [c for c, r in crit_res.items() if r != "NOT_ASSESSED"]
    evaluated_criteria = [k for k, v in criteria_outcomes.items() if v != "NOT_EVALUATED"]
    if not assessed_crit and not evaluated_criteria and not us45:
        return "NOT_ASSESSED", "No CRITICAL control of this gate (%d in the registry) was assessed and no gate criterion was evaluated." % len(crit)
    reasons = []
    unk = [c for c, r in crit_res.items() if r in ("UNKNOWN", "NOT_ASSESSED")]
    if unk:
        reasons.append("%d of %d CRITICAL controls UNKNOWN or NOT_ASSESSED" % (len(unk), len(crit)))
    pend = [k for k, v in criteria_outcomes.items() if v in ("UNKNOWN", "NOT_EVALUATED")]
    if pend:
        reasons.append("criteria not demonstrated met: %s" % ", ".join(sorted(pend)))
    floor = reg["gates"][gate_code]["evidenceFloor"]
    if suff(evidence_suff) < suff(floor):
        reasons.append("gate evidence %s below floor %s" % (evidence_suff, floor))
    if us45:
        reasons.append("US4/US5 UNKNOWN attached: %s" % ", ".join(us45))
    if not crit and gate_code not in ("CG-11", "CG-12"):
        reasons.append("no CRITICAL control mapped")
    for e in supporting_evals or []:
        if e.get("controlResult") == "NONCONFORMING" and not e.get("gateLevelEvaluation"):
            reasons.append("SUPPORTING control %s NONCONFORMING without gate-level evaluation" % e["controlRef"].rsplit("/", 1)[-1])
    if reasons:
        return "UNKNOWN", "UNKNOWN: " + "; ".join(reasons) + "."
    return "PASS", "PASS: all CRITICAL controls CONFORMING, criteria met, evidence at or above floor."


def decision_ceiling(gate_states, gate_ceilings, unknowns):
    """gate_states: gate -> state; gate_ceilings: gate -> (failCeiling, unknownCeiling); unknowns: open UNKNOWN Records in scope.
    Returns (ceilingCode, drivers). Ranks follow AIDCF-010 (NOT_ASSURED below INCONCLUSIVE); ranks are unique, so there is no tie-break."""
    cands = [("REASONABLY_ASSURED", "no constraint")]
    for g, s in sorted(gate_states.items()):
        fc, uc = gate_ceilings[g]
        if s == "FAIL":
            cands.append((fc, "%s FAIL (failCeiling %s)" % (g, fc)))
        elif s in ("UNKNOWN", "NOT_ASSESSED"):
            cands.append((uc, "%s %s (unknownCeiling %s)" % (g, s, uc)))
    for u in unknowns:
        sev = u.get("unknownSeverity")
        code = {"US5": "INCONCLUSIVE", "US4": "LIMITED", "US3": "CONDITIONALLY_ASSURED"}.get(sev)
        if code:
            cands.append((code, "%s %s (%s)" % (u["id"].rsplit(":", 1)[-1], sev, code)))
    low = min(RANK[c] for c, _ in cands)
    code = next(c for c, _ in cands if RANK[c] == low)
    drivers = [d for c, d in cands if RANK[c] == low]
    return code, drivers


def gate_ceilings_from(ix):
    out = {}
    for g in ix.of("CriticalGate"):
        out[g["gateCode"]] = (g["failCeiling"], g["unknownCeiling"])
    return out


# ------------------------------------------------------------------ score (SPEC 5.12)
def band_for(mean):
    if mean is None:
        return "WITHHELD"
    return "B5" if mean >= 90 else "B4" if mean >= 75 else "B3" if mean >= 50 else "B2" if mean >= 25 else "B1"


def compute_score(reg, results, open_unknowns):
    """results: controlId -> result for assessed controls (others NOT_ASSESSED)."""
    inputs = []
    for cid in sorted(reg["controls"]):
        res = results.get(cid, "NOT_ASSESSED")
        inputs.append([cid, res, M.SCORE_VALUE.get(res)])
    us45 = any(u.get("unknownSeverity") in ("US4", "US5") for u in open_unknowns)

    def agg(rows):
        n = len(rows)
        na = sum(r[1] == "NOT_APPLICABLE" for r in rows)
        scored = [r[2] for r in rows if r[2] is not None]
        cov = round(100.0 * len(scored) / (n - na), 4) if n - na else 0.0
        mean = round(sum(scored) / len(scored), 4) if scored else None
        withheld = cov < 80 or us45
        reason = []
        if cov < 80:
            reason.append("coverage %.4f%% below 80%%" % cov)
        if us45:
            reason.append("US4/US5 UNKNOWN open in scope")
        return dict(inScopeCount=n, notApplicableCount=na, scoredCount=len(scored),
                    unknownCount=sum(r[1] == "UNKNOWN" for r in rows), notAssessedCount=sum(r[1] == "NOT_ASSESSED" for r in rows),
                    assessedCount=sum(r[1] != "NOT_ASSESSED" for r in rows), coveragePercent=cov, meanScore=mean,
                    band="WITHHELD" if withheld else band_for(mean), reason="; ".join(reason))
    total = agg(inputs)
    doms = []
    for d in M.DOMAINS:
        a = agg([r for r in inputs if r[0].split("-")[1] == d])
        e = {"domainCode": d, "inScopeCount": a["inScopeCount"], "scoredCount": a["scoredCount"],
             "coveragePercent": a["coveragePercent"], "band": a["band"]}
        if a["meanScore"] is not None:
            e["meanScore"] = a["meanScore"]
        if a["band"] == "WITHHELD":
            e["bandWithheldReason"] = a["reason"]
        doms.append(e)
    payload = {"method": SCORE_METHOD, "weighting": "UNWEIGHTED", "inputs": inputs}
    h = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    return dict(inputs=inputs, total=total, domains=doms, hash=h)


# ------------------------------------------------------------------ change impact (AIDCF-014 section 22, step 3-4)
CONTEXT_CLASSES = {"ArchitectureSnapshot", "CapabilityInstance", "Assessment", "AssuranceProgram"}
REASSESS_CLASSES = ["Control", "ControlAssessment", "GateResult", "AssuranceDecision", "ServiceOutcome"]


def impact(ix, subject):
    """Records affected by a change to `subject`: dependents through DEPENDS_ON, IMPLEMENTED_BY, COMPOSED_OF,
    PROTECTED_BY, SHARES_FAULT_DOMAIN_WITH, REQUIRES_FUNCTION, RECOVERS_THROUGH and EVIDENCED_BY, fault domains
    containing an affected member, then Control Assessments whose subject or evidence is affected, the Controls
    they assess, Controls governing affected Safeguards, Gate Results fed by affected assessments and decisions
    referencing affected gates. Context containers (snapshot, capability, assessment, programme) are not expanded."""
    aff = {subject}
    changed = True
    while changed:
        changed = False
        for s, p, o in ix.edges:
            if s in aff and p == "sharesFaultDomainWith" and o not in aff and ix.type(o) not in CONTEXT_CLASSES:
                aff.add(o); changed = True
            if o in aff and s not in aff and ix.type(s) not in CONTEXT_CLASSES and p in (
                    "dependsOn", "implementedBy", "composedOf", "protectedBy", "sharesFaultDomainWith", "requiresFunction",
                    "recoversThrough", "evidencedBy"):
                aff.add(s); changed = True
        for fd in ix.of("FaultDomain"):
            if fd["id"] not in aff and set(as_list(fd.get("faultDomainMembers"))) & aff:
                aff.add(fd["id"]); changed = True
    arch = set(aff)
    for ca in ix.of("ControlAssessment"):
        if ca.get("subjectRef") in arch or set(ix.o(ca["id"], "evidencedBy")) & arch:
            aff.add(ca["id"])
            aff.update(ix.i(ca["id"], "assessedBy"))
            aff.update(g for g in ix.o(ca["id"], "evaluatesGate"))
    for sg in ix.of("Safeguard"):
        if sg["id"] in arch:
            aff.update(ix.o(sg["id"], "governedBy"))
    for d in ix.of("AssuranceDecision"):
        if set(as_list(d.get("gateResultRefs"))) & aff:
            aff.add(d["id"])
    aff.discard(subject)
    return sorted(a for a in aff if a in ix.recs)


# ------------------------------------------------------------------ business rules
def V(out, rule, subj, msg, level="FAIL"):
    out.append({"ruleId": rule, "subject": subj, "message": msg, "outcome": level})


def business_rules(ix, reg):
    out = []
    results = control_results(ix)
    grs = {g["gateCode"]: g for g in ix.of("GateResult")}
    open_us = [u for u in ix.of("UnknownRecord") if open_unknown(u)]
    ceilings = gate_ceilings_from(ix)
    decisions = ix.of("AssuranceDecision")
    dc_of = {d["id"]: d for d in ix.of("DistributionControl")}

    # BR-001
    for ca in ix.of("ControlAssessment"):
        n = len(ix.i(ca["id"], "assessedBy"))
        if n != 1:
            V(out, "BR-001", ca["id"], "Control Assessment is assessed-of %d controls (exactly one required)" % n)
        for f in ("claimType", "subjectRef", "applicabilityBasis"):
            if not ca.get(f):
                V(out, "BR-001", ca["id"], "missing %s" % f)
    # BR-002
    for ca in ix.of("ControlAssessment"):
        if ca.get("result") == "NOT_APPLICABLE":
            if not ca.get("naRationale") or not ix.o(ca["id"], "reviewedBy"):
                V(out, "BR-002", ca["id"], "NOT_APPLICABLE without rationale and reviewing ReviewRecord")
            if ix.o(ca["id"], "hasUnknown"):
                V(out, "BR-002", ca["id"], "NOT_APPLICABLE recorded where an UNKNOWN is attached (missing evidence yields UNKNOWN)")
    for g in grs.values():
        if g.get("gateState") == "APPROVED_NA" and (not g.get("naRationale") or not ix.o(g["id"], "reviewedBy")):
            V(out, "BR-002", g["id"], "APPROVED_NA without boundary rationale and review")
    # BR-003
    for ca in ix.of("ControlAssessment"):
        for c in ix.i(ca["id"], "assessedBy"):
            ct = ix.get(c).get("claimType")
            if CRANK.get(ca.get("claimType"), 0) < CRANK.get(ct, 0):
                V(out, "BR-003", ca["id"], "assessed claim type %s below control claim type %s" % (ca.get("claimType"), ct))
    # BR-004
    for code, g in grs.items():
        if g.get("gateState") == "PASS":
            floor = reg["gates"][code]["evidenceFloor"]
            if suff(g.get("evidenceSufficiency")) < suff(floor) or not ix.o(g["id"], "evidencedBy"):
                V(out, "BR-004", g["id"], "PASS without evidence at or above floor %s" % floor)
            for c, r in reg["roles"].get(code, {}).items():
                if r == "CRITICAL" and results.get(c, ("NOT_ASSESSED",))[0] != "CONFORMING":
                    V(out, "BR-004", g["id"], "PASS while CRITICAL control %s is %s" % (c, results.get(c, ("NOT_ASSESSED",))[0]))
    # BR-005 and MDM-R03
    for d in decisions:
        st = d.get("decisionState")
        refs = [ix.get(x) for x in as_list(d.get("gateResultRefs"))]
        if st == "REASONABLY_ASSURED":
            bad = [x.get("gateCode") for x in refs if x.get("gateState") in ("FAIL", "UNKNOWN")]
            us = [u["id"] for u in open_us if u.get("unknownSeverity") in ("US4", "US5")]
            if bad or us:
                V(out, "BR-005", d["id"], "REASONABLY_ASSURED with gates %s or open US4/US5 %s" % (bad, us))
        if st in ("REASONABLY_ASSURED", "CONDITIONALLY_ASSURED"):
            bad = [x.get("gateCode") for x in refs if x.get("gateState") not in ("PASS", "APPROVED_NA")]
            us = [u["id"] for u in open_us if u.get("unknownSeverity") in ("US4", "US5") or (st == "REASONABLY_ASSURED" and u.get("unknownSeverity") == "US3")]
            if bad:
                V(out, "MDM-R03", d["id"], "positive decision %s while gates are not PASS/APPROVED_NA: %s" % (st, ", ".join(sorted(bad))))
            if us:
                V(out, "MDM-R03", d["id"], "positive decision %s while UNKNOWN blocks it: %s" % (st, ", ".join(us)))
        if len(refs) != 15 or sorted(x.get("gateCode") for x in refs) != sorted(reg["gates"]):
            V(out, "MDM-R03", d["id"], "decision does not reference exactly one Gate Result per gate CG-01..CG-15")
    # BR-006
    for s in ix.of("ScoreSnapshot"):
        cov = (s.get("coverage") or {}).get("coveragePercent", 0)
        us45 = any(u.get("unknownSeverity") in ("US4", "US5") for u in open_us)
        if (cov < 80 or us45) and s.get("band") != "WITHHELD":
            V(out, "BR-006", s["id"], "band %s reported although coverage %.4f%% or US4/US5 requires WITHHELD" % (s.get("band"), cov))
        if s.get("band") == "WITHHELD" and not s.get("bandWithheldReason"):
            V(out, "BR-006", s["id"], "band withheld without reason")
    # BR-007 and TR-16 rank
    for x in ix.of("AssuranceStatement") + ix.of("AssuranceReport"):
        d = ix.get(x.get("decisionRef"))
        if not d:
            V(out, "BR-007", x["id"], "referenced decision not found")
            continue
        a, b = x.get("decisionState"), d.get("decisionState")
        if RANK.get(a, 0) > RANK.get(b, 0):
            V(out, "BR-007", x["id"], "states %s but the decision is %s" % (a, b))
        if x.get("effectiveTo") and d.get("effectiveTo") and x["effectiveTo"] > d["effectiveTo"]:
            V(out, "BR-007", x["id"], "validity extends beyond the decision validity")
    # BR-008
    for f in ix.of("Finding") + ix.of("UnknownRecord"):
        closed = f.get("findingStatus") == "CLOSED" or f.get("unknownStatus") == "RESOLVED"
        if closed:
            cl = ix.o(f["id"], "closedBy")
            if not cl:
                V(out, "BR-008", f["id"], "closed without CLOSED_BY closure evidence, reassessment or review")
            owners = {f.get("owner")} | {ix.get(a).get("owner") for a in ix.o(f["id"], "requiresAction")}
            for c in cl:
                if ix.type(c) == "ReviewRecord" and ix.get(c).get("reviewer") in owners:
                    V(out, "BR-008", f["id"], "closure reviewed by the owner or action owner")
    # BR-009
    for s, p, o in ix.edges:
        if p == "supersedes":
            if o not in ix.recs:
                V(out, "BR-009", s, "superseded record %s not retained" % o)
            elif ix.get(o).get("status") != "SUPERSEDED":
                V(out, "BR-009", o, "superseded record status is %s, not SUPERSEDED" % ix.get(o).get("status"))
    # BR-010
    for h in ix.of("IntegrationHandoff"):
        if h.get("conclusionsFederated") is not False:
            V(out, "BR-010", h["id"], "handoff federates conclusions (ownership not preserved)")
        if not ix.o(h["id"], "reviewedBy"):
            V(out, "BR-010", h["id"], "handoff not reviewed")
        for src in ix.i(h["id"], "integrationHandoff"):
            if not str(ix.get(src).get("semanticOwner", "")).startswith("AIDCF-"):
                V(out, "BR-010", src, "handed-off record not owned by an AIDCF artifact")
    # BR-011
    for d in decisions:
        if d.get("decisionLifecycle") in ("APPROVED", "ACTIVE"):
            inputs = as_list(d.get("gateResultRefs")) + as_list(d.get("unknownRefs")) + as_list(d.get("scoreRef"))
            for g in as_list(d.get("gateResultRefs")):
                inputs += ix.i(g, "evaluatesGate")
            for i in inputs:
                r = ix.get(i)
                if r.get("reviewState") == "CANDIDATE" or r.get("status") == "CANDIDATE" or \
                        (r.get("provenance") or {}).get("method") in ("AUTOMATED_DISCOVERY", "INFERENCE"):
                    V(out, "BR-011", d["id"], "approved decision uses candidate or inferred input %s" % i)
    for e in ix.of("Event"):
        if e.get("humanDisposition") == "PENDING":
            if e.get("reviewState") != "CANDIDATE":
                V(out, "BR-011", e["id"], "event awaiting disposition is not CANDIDATE")
            for r in ix.of("RelationshipRecord"):
                if (r.get("sourceRef") == e["id"] or r.get("targetRef") == e["id"]) and r.get("reviewState") != "CANDIDATE":
                    V(out, "BR-011", r["id"], "edge created by a pending event is not CANDIDATE")
            for s in ix.i(e["id"], "invalidatedBy") + ix.o(e["id"], "triggersReassessment"):
                if ix.get(s).get("status") in ("SUSPENDED", "WITHDRAWN") or ix.get(s).get("decisionLifecycle") in ("SUSPENDED", "WITHDRAWN"):
                    V(out, "BR-011", s, "record changed by a pending event without disposition (TDS-REQ-062)")
    # BR-012
    for r in ix.recs.values():
        c = r.get("classification")
        if CLS_RANK.get(c, 0) > CLS_RANK["INTERNAL"]:
            dc = dc_of.get(r.get("distributionControlRef"))
            if not dc:
                V(out, "BR-012", r["id"], "%s record without DistributionControl" % c)
            elif CLS_RANK.get(dc.get("maxClassification"), 0) < CLS_RANK[c]:
                V(out, "BR-012", r["id"], "DistributionControl does not authorise %s" % c)
    # BR-013
    for e in ix.of("Event"):
        if e.get("materiality") == "MATERIAL":
            got = sorted(as_list(e.get("affectedAssertions")))
            exp = impact(ix, e.get("subjectRef"))
            if got != exp:
                V(out, "BR-013", e["id"], "affectedAssertions differ from the section 22 impact analysis (%d recorded, %d computed; missing %s)"
                  % (len(got), len(exp), [x.rsplit(":", 1)[-1] for x in sorted(set(exp) - set(got))][:5]))
    # BR-014
    for ca in ix.of("ControlAssessment"):
        if ca.get("result") == "CONFORMING":
            for f in ix.o(ca["id"], "hasFinding"):
                ff = ix.get(f)
                if ff.get("findingStatus") != "CLOSED" and ff.get("findingClass") in ("WEAKNESS", "SIGNIFICANT_WEAKNESS", "CRITICAL_FINDING"):
                    V(out, "BR-014", ca["id"], "CONFORMING result with open %s %s (risk acceptance cannot change a result)" % (ff.get("findingClass"), f))
    # BR-015 (flag)
    for ev in ix.of("EvidenceObject"):
        cts = {ix.get(t).get("claimType") for t in ix.o(ev["id"], "supports") if ix.type(t) == "ControlAssessment"}
        if len(cts) > 1:
            V(out, "BR-015", ev["id"], "evidence reused across claim types %s; fresh SUPPORTS review required" % sorted(cts), "WARNING")

    # MDM-R01 gate roll-up recomputation; MDM-R02 inputs
    for code in sorted(reg["gates"]):
        g = grs.get(code)
        if not g:
            V(out, "MDM-R01", code, "no Gate Result for %s" % code)
            continue
        crit_out = {c["criterionId"]: c["criterionOutcome"] for c in as_list(g.get("criteriaResults"))}
        sup = [e for e in as_list(g.get("controlEvaluations")) if e.get("gateRole") == "SUPPORTING"]
        state, why = rollup(code, reg, {k: v[0] for k, v in results.items()}, crit_out, gate_attached_unknowns(ix, g["id"]),
                            g.get("evidenceSufficiency"), sup, g.get("gateApplicability"),
                            bool(g.get("naRationale")) and bool(ix.o(g["id"], "reviewedBy")))
        if state != g.get("gateState"):
            V(out, "MDM-R01", g["id"], "%s recorded %s; SPEC 6.2 roll-up gives %s (%s)" % (code, g.get("gateState"), state, why))
        gate_iri = ix.o(g["id"], "evaluatesGate")
        if len(gate_iri) != 1 or ix.get(gate_iri[0]).get("gateCode") != code:
            V(out, "MDM-R01", g["id"], "gate result does not evaluate exactly the Critical Gate %s" % code)
        ids = {x["criterionId"] for x in reg["criteria"] if x["gateId"] == code}
        if set(crit_out) != ids:
            V(out, "MDM-R02", g["id"], "criteriaResults do not list exactly the registry criteria of %s" % code)
        ev = {e["controlRef"].rsplit("/", 1)[-1]: e for e in as_list(g.get("controlEvaluations"))}
        for c, role in reg["roles"].get(code, {}).items():
            res = results.get(c, ("NOT_ASSESSED", None))
            if role == "CRITICAL" or res[0] != "NOT_ASSESSED":
                e = ev.get(c)
                if not e:
                    V(out, "MDM-R02", g["id"], "registry %s control %s missing from controlEvaluations" % (role, c))
                    continue
                if e.get("gateRole") != role:
                    V(out, "MDM-R02", g["id"], "%s role %s differs from registry role %s" % (c, e.get("gateRole"), role))
                if e.get("controlResult") != res[0]:
                    V(out, "MDM-R02", g["id"], "%s evaluated as %s but Control Assessment result is %s" % (c, e.get("controlResult"), res[0]))
                if res[1] and (e.get("controlAssessmentRef") != res[1] or g["id"] not in ix.o(res[1], "evaluatesGate")):
                    V(out, "MDM-R02", g["id"], "%s input not linked by EVALUATES_GATE from its Control Assessment" % c)
        for c in ev:
            if c not in reg["roles"].get(code, {}):
                V(out, "MDM-R02", g["id"], "%s evaluated but not mapped to %s in the registry" % (c, code))
    # MDM-R04, R05, R06
    states = {c: g.get("gateState") for c, g in grs.items()}
    in_scope_us = [u for u in open_us]
    ceil, drivers = decision_ceiling(states, ceilings, in_scope_us)
    for d in decisions:
        st = d.get("decisionState")
        for u in ix.of("UnknownRecord"):
            if not open_unknown(u):
                continue
            sev = u.get("unknownSeverity")
            if sev == "US5" and RANK.get(st, 0) > RANK["INCONCLUSIVE"]:
                V(out, "MDM-R04", d["id"], "open US5 %s caps the decision at INCONCLUSIVE; decision is %s" % (u["id"], st))
            if sev == "US4" and RANK.get(st, 0) > RANK["LIMITED"]:
                V(out, "MDM-R04", d["id"], "open US4 %s caps the decision at LIMITED; decision is %s" % (u["id"], st))
            if sev == "US3" and RANK.get(st, 0) > RANK["CONDITIONALLY_ASSURED"]:
                V(out, "MDM-R04", d["id"], "open US3 %s caps the decision at CONDITIONALLY_ASSURED; decision is %s" % (u["id"], st))
            if sev == "US3" and st == "CONDITIONALLY_ASSURED" and not any(u["id"] in as_list(c.get("relatedRefs")) for c in as_list(d.get("conditions"))):
                V(out, "MDM-R04", d["id"], "CONDITIONALLY_ASSURED without a condition for US3 %s" % u["id"])
            if sev in ("US3", "US4", "US5") and u["id"] not in as_list(d.get("unknownRefs")):
                V(out, "MDM-R04", d["id"], "open %s %s not referenced by the decision" % (sev, u["id"]))
        for code, s in states.items():
            fc, uc = ceilings[code]
            cap = fc if s == "FAIL" else uc if s in ("UNKNOWN", "NOT_ASSESSED") else None
            if cap and RANK.get(st, 0) > RANK[cap]:
                V(out, "MDM-R05", d["id"], "decision %s exceeds %s %s ceiling %s" % (st, code, s, cap))
        for rec in ix.i(d["id"], "recommends"):
            r = ix.get(rec)
            if r.get("decisionCeiling") != ceil:
                V(out, "MDM-R06", rec, "decisionCeiling %s differs from computed ceiling %s (%s)" % (r.get("decisionCeiling"), ceil, "; ".join(drivers)))
            if RANK.get(r.get("recommendedState"), 0) > RANK[ceil]:
                V(out, "MDM-R06", rec, "recommended state exceeds the ceiling")
            if RANK.get(st, 0) > RANK.get(r.get("decisionCeiling"), 0):
                V(out, "MDM-R06", d["id"], "decision exceeds the recommendation ceiling")
    # MDM-R07 CONFORMING evidence floor and classes
    for c in ix.of("Control"):
        for caid in ix.o(c["id"], "assessedBy"):
            ca = ix.get(caid)
            if ca.get("result") != "CONFORMING":
                continue
            ers = [ix.get(e) for e in ix.o(c["id"], "hasEvidenceRequirement") if ix.get(e).get("claimType") == c.get("claimType")]
            if not ers:
                V(out, "MDM-R07", caid, "no Evidence Requirement for the control claim type")
                continue
            er = ers[0]
            if suff(ca.get("evidenceSufficiency")) < suff(er.get("sufficiencyFloor")):
                V(out, "MDM-R07", caid, "CONFORMING with evidence %s below floor %s" % (ca.get("evidenceSufficiency"), er.get("sufficiencyFloor")))
            classes = {ix.get(e).get("evidenceClass") for e in ix.o(caid, "evidencedBy")}
            miss = set(as_list(er.get("requiredClasses"))) - classes
            if miss:
                V(out, "MDM-R07", caid, "CONFORMING without required evidence classes %s" % sorted(miss))
    # MDM-R08 assurance level
    for c in ix.of("Control"):
        if M.CLAIM_MIN_AL.get(c.get("claimType")) != c.get("requiredAssuranceLevel"):
            V(out, "MDM-R08", c["id"], "requiredAssuranceLevel %s inconsistent with claim type %s" % (c.get("requiredAssuranceLevel"), c.get("claimType")))
    # MDM-R09 US4/US5 gate effect
    for u in ix.of("UnknownRecord"):
        if open_unknown(u) and u.get("unknownSeverity") == "US4":
            tg = [ix.get(g) for g in ix.o(u["id"], "constrains") if ix.type(g) == "GateResult"]
            if not any(g.get("gateState") in ("UNKNOWN", "FAIL") for g in tg):
                V(out, "MDM-R09", u["id"], "open US4 does not constrain a Gate Result that is UNKNOWN or FAIL")
    # MDM-R10 relationship records
    rr_keys = defaultdict(list)
    for r in ix.of("RelationshipRecord"):
        code = r.get("relationshipType")
        prop = M.REL_BY_CODE.get(code, (None, None))[1]
        rr_keys[(r.get("sourceRef"), prop, r.get("targetRef"))].append(r)
        if (r.get("sourceRef"), prop, r.get("targetRef")) not in set(ix.edges):
            V(out, "MDM-R10", r["id"], "relationship record without asserted edge")
        extra = M.REL_BY_CODE.get(code, [None] * 8)[7] or {}
        for q in extra.get("qualifiers", []):
            if r.get(q) in (None, []):
                V(out, "MDM-R10", r["id"], "%s without qualifier %s" % (code, q))
        if extra.get("conditions") and not r.get("operatingStates"):
            V(out, "MDM-R10", r["id"], "%s without conditions (operating states)" % code)
        if code == "DEPENDS_ON":
            dep = ix.get(r.get("dependencyRef"))
            if dep.get("sourceRef") != r.get("sourceRef") or dep.get("targetRef") != r.get("targetRef"):
                V(out, "MDM-R10", r["id"], "dependencyRef does not describe this edge")
        if code == "SHARES_FAULT_DOMAIN_WITH":
            fd = ix.get(r.get("faultDomainRef"))
            if not {r.get("sourceRef"), r.get("targetRef")} <= set(as_list(fd.get("faultDomainMembers"))):
                V(out, "MDM-R10", r["id"], "faultDomainRef does not contain both endpoints")
        if code == "EVALUATES_GATE" and ix.type(r.get("sourceRef")) == "Control":
            cid = ix.get(r["sourceRef"]).get("controlCode")
            gid = ix.get(r["targetRef"]).get("gateCode")
            if reg["roles"].get(gid, {}).get(cid) != r.get("gateRole"):
                V(out, "MDM-R10", r["id"], "gateRole %s differs from registry role %s" % (r.get("gateRole"), reg["roles"].get(gid, {}).get(cid)))
    for e in set(ix.edges):
        if e not in rr_keys:
            V(out, "MDM-R10", e[0], "edge %s -> %s has no relationship record" % (e[1], e[2]))
    for fs in ix.of("FailureScenario"):
        steps = as_list(fs.get("propagationSteps"))
        ords = []
        for st in steps:
            r = ix.get(st)
            if r.get("relationshipType") != "PROPAGATES_TO" or r.get("scenarioRef") != fs["id"]:
                V(out, "MDM-R10", fs["id"], "propagation step %s is not a PROPAGATES_TO record of this scenario" % st)
            ords.append(r.get("stepOrdinal"))
        if ords != list(range(1, len(ords) + 1)):
            V(out, "MDM-R10", fs["id"], "step ordinals are not 1..n in order")
        mine = [r["id"] for r in ix.of("RelationshipRecord") if r.get("scenarioRef") == fs["id"]]
        if sorted(mine) != sorted(steps):
            V(out, "MDM-R10", fs["id"], "propagationSteps do not list every PROPAGATES_TO record of the scenario")
    # MDM-R11 inverses not asserted
    for r in ix.recs.values():
        for k in r:
            if k in INVERSE_PROPS:
                V(out, "MDM-R11", r["id"], "inverse property %s asserted" % k)
    # MDM-R12 classification
    for r in ix.of("RelationshipRecord"):
        m = max(CLS_RANK.get(ix.get(r.get("sourceRef")).get("classification"), 0), CLS_RANK.get(ix.get(r.get("targetRef")).get("classification"), 0))
        if CLS_RANK.get(r.get("classification"), 0) < m:
            V(out, "MDM-R12", r["id"], "edge classified below an endpoint")
    for r in ix.recs.values():
        sensitive = r.get("type") == "Conduit" or (r.get("type") == "Finding" and str(r.get("criterionRef", "")).startswith(("MCF-SEC", "MCF-SUP")))
        if sensitive and CLS_RANK.get(r.get("classification"), 0) < CLS_RANK["CONFIDENTIAL"]:
            V(out, "MDM-R12", r["id"], "OT access path or security weakness classified below CONFIDENTIAL (TDS-REQ-066)")
    # MDM-R13 registry fidelity
    ctrls = {c["controlCode"]: c for c in ix.of("Control")}
    if len(ctrls) != 360 or len(ix.of("ControlFamily")) != 90 or len(ix.of("ControlDomain")) != 15 or len(ix.of("CriticalGate")) != 15:
        V(out, "MDM-R13", "registry", "dataset does not carry 15 domains, 90 families, 360 controls and 15 gates")
    for cid, row in reg["controls"].items():
        c = ctrls.get(cid)
        if not c:
            V(out, "MDM-R13", cid, "control missing from dataset")
            continue
        for f, col in (("claimType", "claimType"), ("requiredAssuranceLevel", "requiredAssuranceLevel"), ("controlType", "controlType"),
                       ("profileTier", "profileTier"), ("familyCode", "familyId"), ("domainCode", "domainId"), ("name", "title")):
            if c.get(f) != row[col]:
                V(out, "MDM-R13", c["id"], "%s %r differs from registry %r" % (f, c.get(f), row[col]))
        maps = {(m["gateRef"].rsplit("/", 1)[-1], m["gateRole"]) for m in as_list(c.get("gateMappings"))}
        regm = {(g, r) for g, roles in reg["roles"].items() for cc, r in roles.items() if cc == cid}
        if maps != regm:
            V(out, "MDM-R13", c["id"], "gateMappings differ from registry gate-mappings.csv")
        if {x.rsplit("/", 1)[-1] for x in ix.o(c["id"], "evaluatesGate")} != {g for g, _ in regm}:
            V(out, "MDM-R13", c["id"], "EVALUATES_GATE edges differ from registry gate mappings")
        prof = reg["profiles"][cid]
        ers = [ix.get(e) for e in ix.o(c["id"], "hasEvidenceRequirement")]
        if not any(e.get("claimType") == prof["claimType"] and e.get("sufficiencyFloor") == prof["sufficiencyFloor"]
                   and sorted(as_list(e.get("requiredClasses"))) == sorted(x.strip() for x in prof["requiredClasses"].split(";")) for e in ers):
            V(out, "MDM-R13", c["id"], "Evidence Requirement differs from registry evidence-profiles.csv")
    for g in ix.of("CriticalGate"):
        row = reg["gates"].get(g["gateCode"], {})
        if g.get("evidenceFloor") != row.get("evidenceFloor") or g.get("failCeilingText") != row.get("failCeiling") \
                or g.get("unknownCeilingText") != row.get("unknownCeiling"):
            V(out, "MDM-R13", g["id"], "Critical Gate differs from registry critical-gates.csv")
        if (g.get("failCeiling"), g.get("unknownCeiling")) != (M.derive_ceiling(row.get("failCeiling", ""))[0], M.derive_ceiling(row.get("unknownCeiling", ""))[0]):
            V(out, "MDM-R13", g["id"], "machine ceilings do not follow the AIDCF-016 section 9.4 derivation from the registry text")
    # MDM-R14 composition and supersession graphs
    for prop, rule in (("composedOf", "MDM-R14"), ("supersedes", "MDM-R14")):
        adj = defaultdict(list)
        for s, p, o in ix.edges:
            if p == prop:
                adj[s].append(o)
        if has_cycle(adj):
            V(out, rule, prop, "%s graph contains a cycle" % prop)
    for s, p, o in ix.edges:
        if p == "supersedes" and o in ix.recs and ix.type(s) != ix.type(o):
            V(out, "MDM-R14", s, "supersedes a record of a different class")
        if p == "composedOf":
            pairs = M.REL_BY_CODE["COMPOSED_OF"][7]["pairs"]
            sc = next((c for c in M.superclasses(ix.type(s) or "") if c in pairs), None)
            if sc and not any(ix.is_a(o, t) for t in pairs[sc]):
                V(out, "MDM-R14", s, "COMPOSED_OF %s -> %s not a permitted whole-part pair" % (ix.type(s), ix.type(o)))
    # MDM-R15 GOVERNED_BY pairs, MDM-R16 EVALUATES_GATE pairs
    for s, p, o in ix.edges:
        if p == "governedBy":
            pairs = M.REL_BY_CODE["GOVERNED_BY"][7]["pairs"]
            sc = next((c for c in M.superclasses(ix.type(s) or "") if c in pairs), None)
            allowed = (pairs.get(sc, []) if sc else []) + pairs["*"]
            if not any(ix.is_a(o, t) for t in allowed):
                V(out, "MDM-R15", s, "GOVERNED_BY %s -> %s not permitted" % (ix.type(s), ix.type(o)))
        if p == "evaluatesGate":
            pairs = M.REL_BY_CODE["EVALUATES_GATE"][7]["pairs"]
            if not any(ix.is_a(o, t) for t in pairs.get(ix.type(s), [])):
                V(out, "MDM-R16", s, "EVALUATES_GATE %s -> %s not permitted" % (ix.type(s), ix.type(o)))
    # MDM-R17 review types and authority
    prog = {p["id"]: p for p in ix.of("AssuranceProgram")}
    for s, p, o in ix.edges:
        if p == "approvedBy" and ix.get(o).get("reviewType") != "APPROVAL":
            V(out, "MDM-R17", s, "APPROVED_BY target %s is not an APPROVAL review" % o)
        if p == "reviewedBy" and ix.get(o).get("reviewType") != "REVIEW":
            V(out, "MDM-R17", s, "REVIEWED_BY target %s is not a REVIEW record" % o)
    for d in decisions:
        auths = {p.get("decisionAuthority") for p in prog.values()}
        if not any(ix.get(r).get("reviewer") in auths for r in ix.o(d["id"], "approvedBy")):
            V(out, "MDM-R17", d["id"], "decision not approved by the programme decision authority")
    # MDM-R18 UNKNOWN subject consistency, MDM-R19 disposition
    for u in ix.of("UnknownRecord"):
        if u["id"] not in ix.o(u.get("subjectRef"), "hasUnknown"):
            V(out, "MDM-R18", u["id"], "subjectRef does not carry HAS_UNKNOWN to this record")
        if u.get("unknownStatus") == "DISPOSITIONED" and (not u.get("disposition") or not u.get("dueDate")):
            V(out, "MDM-R19", u["id"], "DISPOSITIONED without disposition and due date")
        if u.get("unknownSeverity") in ("US4", "US5") and u.get("unknownStatus") == "OPEN":
            V(out, "MDM-R19", u["id"], "US4/US5 UNKNOWN without disposition (CG-12 GC-12-3)", "WARNING")
    # MDM-R20 release binding
    for r in ix.recs.values():
        if r.get("releaseRef") != RELEASE_ID:
            V(out, "MDM-R20", r["id"], "releaseRef %s is not the pinned release %s" % (r.get("releaseRef"), RELEASE_ID))
    return out


def has_cycle(adj):
    seen, stack = set(), set()

    def dfs(n):
        if n in stack:
            return True
        if n in seen:
            return False
        seen.add(n); stack.add(n)
        for m in adj.get(n, []):
            if dfs(m):
                return True
        stack.discard(n)
        return False
    sys.setrecursionlimit(10000)
    return any(dfs(n) for n in list(adj))


# ------------------------------------------------------------------ traceability TR-01..TR-18
def traceability(ix, reg):
    out = []
    checks = defaultdict(int)

    def T(rule, ok, subj, msg):
        checks[rule] += 1
        if not ok:
            V(out, rule, subj, msg)
    snap_members = set()
    for s in ix.of("ArchitectureSnapshot"):
        if s.get("status") != "SUPERSEDED":
            stack = list(ix.o(s["id"], "composedOf"))
            while stack:
                n = stack.pop()
                if n not in snap_members:
                    snap_members.add(n)
                    stack.extend(ix.o(n, "composedOf"))
    for c in ix.of("CapabilityInstance"):
        T("TR-01", len(ix.o(c["id"], "hasOutcome")) >= 1, c["id"], "no HAS_OUTCOME")
    for so in ix.of("ServiceOutcome"):
        T("TR-01", len(ix.i(so["id"], "hasOutcome")) == 1, so["id"], "not exactly one incoming HAS_OUTCOME")
        T("TR-02", len(ix.o(so["id"], "requiresFunction")) >= 1, so["id"], "no REQUIRES_FUNCTION")
    impl = set()
    for rf in ix.of("RequiredFunction"):
        targets = ix.o(rf["id"], "implementedBy")
        impl.update(targets)
        T("TR-03", any(t in snap_members for t in targets), rf["id"], "no IMPLEMENTED_BY to an element of the current snapshot")
    for e in sorted(impl):
        T("TR-04", bool(ix.o(e, "dependsOn")) or bool(ix.o(e, "hasUnknown")), e, "implementing element has no DEPENDS_ON and no UNKNOWN for incomplete discovery")
    step_sources = set()
    for r in ix.of("RelationshipRecord"):
        if r.get("relationshipType") == "PROPAGATES_TO" and r.get("scenarioRef") in ix.recs:
            step_sources.add(r["sourceRef"])
    step_nodes = defaultdict(set)
    for r in ix.of("RelationshipRecord"):
        if r.get("relationshipType") == "PROPAGATES_TO":
            step_nodes[r.get("scenarioRef")].update([r["sourceRef"], r["targetRef"]])
    for d in ix.of("Dependency"):
        if d.get("strength") in ("ABSOLUTE", "MATERIAL"):
            T("TR-05", d.get("targetRef") in step_sources, d["id"], "ABSOLUTE/MATERIAL dependency provider not the source of any scenario propagation step")
    for fd in ix.of("FaultDomain"):
        T("TR-05", any(set(as_list(fd.get("faultDomainMembers"))) & nodes for nodes in step_nodes.values()), fd["id"], "fault domain not covered by a failure scenario")
    for fs in ix.of("FailureScenario"):
        if any(e.get("exceedsTolerance") for e in as_list(fs.get("outcomeEffects"))):
            sg = set(as_list(fs.get("expectedSafeguards")))
            prot = any(set(ix.o(n, "protectedBy")) & sg for n in step_nodes.get(fs["id"], set()))
            T("TR-06", bool(sg) and prot, fs["id"], "expected safeguards not linked by PROTECTED_BY to an affected element")
        for sgid in as_list(fs.get("expectedSafeguards")):
            T("TR-07", bool(ix.o(sgid, "governedBy")), sgid, "safeguard relied on in a scenario not GOVERNED_BY a control")
    for c in ix.of("Control"):
        T("TR-08", any(ix.get(e).get("claimType") == c.get("claimType") for e in ix.o(c["id"], "hasEvidenceRequirement")), c["id"],
          "no HAS_EVIDENCE_REQUIREMENT for the control claim type")
    assessed_ctrl = {c["id"] for c in ix.of("Control") if any(ix.get(a).get("result") != "NOT_ASSESSED" for a in ix.o(c["id"], "assessedBy"))}
    evaluated_gates = {ix.o(g["id"], "evaluatesGate")[0] for g in ix.of("GateResult")
                       if g.get("gateState") in ("PASS", "FAIL", "UNKNOWN") and ix.o(g["id"], "evaluatesGate")}
    for owner in sorted(assessed_ctrl | evaluated_gates):
        for er in ix.o(owner, "hasEvidenceRequirement"):
            r = ix.get(er)
            evs = [ix.get(e) for e in ix.o(er, "evidencedBy")]
            ok = any(e.get("evidenceClass") in as_list(r.get("requiredClasses")) for e in evs) or bool(ix.o(er, "hasUnknown"))
            T("TR-09", ok, er, "in-scope Evidence Requirement has no evidence of a required class and no UNKNOWN")
    for ca in ix.of("ControlAssessment"):
        T("TR-10", bool(ix.i(ca["id"], "resultsIn")) and bool(ca.get("assessmentMethods")) and bool(ca.get("assessor")) and bool(ix.o(ca["id"], "reviewedBy")),
          ca["id"], "Control Assessment lacks RESULTS_IN, methods, assessor or REVIEWED_BY")
        if ca.get("result") in ("PARTIAL", "NONCONFORMING"):
            T("TR-11", bool(ix.o(ca["id"], "hasFinding")), ca["id"], "PARTIAL/NONCONFORMING without HAS_FINDING")
        if ca.get("result") == "UNKNOWN":
            T("TR-11", bool(ix.o(ca["id"], "hasUnknown")), ca["id"], "UNKNOWN without HAS_UNKNOWN")
    results = control_results(ix)
    for g in ix.of("GateResult"):
        code = g.get("gateCode")
        ok = len(ix.o(g["id"], "evaluatesGate")) == 1
        inputs = set(ix.i(g["id"], "evaluatesGate"))
        for c, role in reg["roles"].get(code, {}).items():
            if role == "CRITICAL" and c in results:
                ok = ok and results[c][1] in inputs
                for f in ix.o(results[c][1], "hasFinding"):
                    ok = ok and f in ix.o(g["id"], "hasFinding")
                for u in ix.o(results[c][1], "hasUnknown"):
                    ok = ok and (u in ix.o(g["id"], "hasUnknown") or g["id"] in ix.o(u, "constrains"))
        if g.get("gateState") in ("PASS", "FAIL"):
            ok = ok and bool(ix.o(g["id"], "evidencedBy"))
        T("TR-12", ok, g["id"], "gate result does not link its gate, CRITICAL inputs, evidence, findings and UNKNOWNs")
    for s in ix.of("ScoreSnapshot"):
        T("TR-13", bool(s.get("profileVersion")) and bool(s.get("calculationHash")) and bool(ix.i(s["id"], "summarisedBy")), s["id"],
          "score snapshot lacks pinned inputs, profile version or SUMMARISED_BY inputs")
    for d in ix.of("DecisionRecommendation"):
        summ = set(ix.i(d["id"], "summarisedBy"))
        gr_ok = all(g["id"] in summ for g in ix.of("GateResult"))
        us = [u for u in ix.of("UnknownRecord") if u.get("unknownSeverity") in ("US3", "US4", "US5") and open_unknown(u)]
        us_ok = all(u["id"] in summ for u in us)
        decs = ix.o(d["id"], "recommends")
        con_ok = all(any(t in decs or t == d["id"] for t in ix.o(u["id"], "constrains")) for u in us)
        T("TR-14", gr_ok and us_ok and con_ok, d["id"], "recommendation does not summarise every Gate Result and US3-US5 UNKNOWN, or does not apply their CONSTRAINS edges")
    prog_auth = {p.get("decisionAuthority") for p in ix.of("AssuranceProgram")}
    for d in ix.of("AssuranceDecision"):
        ok = len(ix.i(d["id"], "recommends")) == 1 and any(ix.get(r).get("reviewType") == "APPROVAL" and ix.get(r).get("reviewer") in prog_auth
                                                           for r in ix.o(d["id"], "approvedBy")) and bool(d.get("scope")) and bool(d.get("effectiveTo"))
        T("TR-15", ok, d["id"], "decision lacks RECOMMENDS, APPROVED_BY the declared authority, scope or effectiveTo")
    for x in ix.of("AssuranceStatement") + ix.of("AssuranceReport"):
        d = ix.get(x.get("decisionRef"))
        ok = d.get("decisionLifecycle") in ("APPROVED", "ACTIVE") and RANK.get(x.get("decisionState"), 9) <= RANK.get(d.get("decisionState"), 0)
        T("TR-16", ok, x["id"], "statement or report does not trace to an APPROVED/ACTIVE decision it does not exceed")
    for e in ix.of("Event"):
        if as_list(e.get("candidateTriggers")):
            tgt = set(ix.o(e["id"], "triggersReassessment")) | {x for t in as_list(e.get("candidateTriggers")) for x in ix.o(t, "triggersReassessment")}
            inv = set(ix.i(e["id"], "invalidatedBy"))
            need = [a for a in impact(ix, e.get("subjectRef")) if ix.type(a) in REASSESS_CLASSES]
            miss = [a for a in need if a not in tgt and a not in inv]
            T("TR-17", not miss, e["id"], "impacted records without TRIGGERS_REASSESSMENT or INVALIDATED_BY: %s" % [m.rsplit(":", 1)[-1].rsplit("/", 1)[-1] for m in miss][:6])
    for r in ix.recs.values():
        if r.get("status") == "SUPERSEDED":
            T("TR-18", len(ix.i(r["id"], "supersedes")) == 1, r["id"], "SUPERSEDED record without exactly one supersededBy")
    adj = defaultdict(list)
    for s, p, o in ix.edges:
        if p == "supersedes":
            adj[s].append(o)
    T("TR-18", not has_cycle(adj), "supersedes", "supersession chain is cyclic")
    return out, dict(checks)
