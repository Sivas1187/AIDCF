#!/usr/bin/env python3
"""AIDCF-VAL-001 incident back-testing kit: validator, agreement and metrics.

Standard library only; deterministic output.

Usage (from any directory):
  python3 research/back-testing/backtest_check.py --check        validate files
  python3 research/back-testing/backtest_check.py --agreement    coder agreement (rounds A vs B)
  python3 research/back-testing/backtest_check.py --metrics      coverage metrics (RECONCILED rows)
  python3 research/back-testing/backtest_check.py --list-families
Options:
  --sheet PATH      coding sheet (default: coding-sheet.csv beside this script)
  --register PATH   incident register (default: incident-register.csv beside this script)
  --include-examples  include INC-EXAMPLE-* rows in --agreement and --metrics

--check exits 1 if any error is found. Codes are validated against AIDCF-004 v1.1
(scenario families, library scenarios, failure modes, generic modes, cause families),
registries/controls/controls.csv, the AIDCF-007A control catalogue (assessment-criterion
numbers), registries/gates/critical-gates.csv, critical-gate-criteria.csv and the
canonical vocabularies in registries/vocabularies/.
"""

import argparse
import csv
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
THREAT_MODEL = ROOT / "foundations/threat-model/AIDCF-004_Threat_Hazard_and_Failure_Model_v1.1.md"
CONTROL_MD_DIR = ROOT / "standards/aidcf-007a/registry/controls"
REG = ROOT / "registries"

SHEET_COLUMNS = [
    "incident_id", "record_type", "coder_id", "coding_round", "independent_of_author",
    "prior_familiarity", "coding_phase", "source_urls", "source_types", "access_date",
    "incident_date", "operator_type", "failure_category", "timeline_before_cause",
    "factor_id", "factor_role", "causal_factor", "knowability", "cause_family",
    "scenario_family", "library_scenario", "failure_modes", "generic_modes",
    "control_id", "control_criteria", "projected_control_result", "detection_judgement",
    "gate_id", "gate_criteria", "gate_judgement", "gap_type", "gap_description",
    "confidence", "notes",
]
REGISTER_COLUMNS = [
    "incident_id", "neutral_descriptor", "operator_name_as_published", "operator_type",
    "incident_date", "failure_category", "tags", "primary_source_url", "primary_source_type",
    "other_source_urls", "access_date", "archive_refs", "found_via", "detail_level",
    "eligibility_status", "exclusion_code", "screened_by", "exclusion_checked_by",
    "stratum_draw_rank", "coder_a", "coder_b", "adjudicator", "coding_status", "notes",
]

RECORD_TYPES = {"CONTROL", "GATE"}
ROUNDS = {"A", "B", "RECONCILED"}
YN = {"Y", "N"}
FAMILIARITY = {"NONE", "GENERAL", "DETAILED"}
PHASES = {"PRE_REVEAL", "POST_REVEAL"}
SOURCE_TYPES = {"PRIMARY", "REGULATOR", "SECONDARY_PRESS"}
OPERATOR_TYPES = {"HYPERSCALE_CLOUD", "COLOCATION", "ENTERPRISE", "AI_HPC_FACILITY",
                  "TELECOM_NETWORK", "MANAGED_SERVICE", "PUBLIC_SECTOR", "OTHER"}
CATEGORIES = ["POWER", "COOLING", "NETWORK_FABRIC", "STORAGE", "CONTROL_PLANE_OT",
              "CHANGE_HUMAN", "EXTERNAL_DEPENDENCY"]
TAGS = {"HEAT_EVENT", "LIQUID_COOLING", "AI_HPC", "FIRE", "WATER_INGRESS", "BATTERY",
        "MULTI_SITE", "REGULATOR_REPORT"}
FACTOR_ROLES = {"INITIATING", "PREDISPOSING", "ESCALATION", "RECOVERY"}
KNOWABILITY = {"STATED_KNOWN", "DISCOVERABLE", "NOT_KNOWABLE", "NOT_STATED"}
DETECTION = ["DETECTED", "PARTIALLY_DETECTED", "NOT_DETECTED", "NOT_ADDRESSED",
             "INSUFFICIENT_INFORMATION"]
DETECTION_RANK = {"DETECTED": 3, "PARTIALLY_DETECTED": 2, "NOT_DETECTED": 1}
GATE_JUDGEMENTS = {"PASS", "FAIL", "UNKNOWN", "APPROVED_NA", "INSUFFICIENT_INFORMATION"}
GAP_TYPES = {"NONE", "G1_NO_CONTROL", "G2_NO_CRITERION", "G3_EVIDENCE_PROFILE",
             "G4_GATE_MAPPING", "G5_GATE_CRITERION", "G6_THREAT_MODEL"}
ELIGIBILITY = {"CANDIDATE", "ELIGIBLE", "EXCLUDED", "SELECTED", "RESERVE", "WITHDRAWN"}
EXCLUSION_CODES = {"EX-01", "EX-02", "EX-03", "EX-04", "EX-05", "EX-06", "EX-07", "EX-08"}
DETAIL_LEVELS = {"HIGH", "MEDIUM", "LOW"}
CODING_STATUS = {"NOT_STARTED", "DOSSIER_READY", "PASS1_LOCKED", "FACTORS_CONSOLIDATED",
                 "PASS2_LOCKED", "RECONCILED", "QA_COMPLETE"}

INC_RE = re.compile(r"^INC-(\d{3}|EXAMPLE-\d{2})$")
LOCAL_FACTOR_RE = re.compile(r"^CF-[AB]\d{2}$")
FACTOR_RE = re.compile(r"^CF-\d{2}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CODER_RE = re.compile(r"^C\d{2}$")


def split(value):
    return [v.strip() for v in value.split(";") if v.strip()]


def read_csv(path):
    raw = path.read_bytes()
    if b"\r" in raw:
        raise ValueError("%s: CR characters found; files must use LF line endings" % path)
    text = raw.decode("utf-8")
    reader = csv.reader(text.splitlines())
    rows = list(reader)
    return rows[0], [dict(zip(rows[0], r)) for r in rows[1:]], rows[1:]


# ---------------------------------------------------------------- reference data

def load_threat_model():
    text = THREAT_MODEL.read_text(encoding="utf-8").splitlines()
    families, library, fm, modes, causes = set(), set(), {}, set(), set()
    part = None
    domain = None
    for line in text:
        if line.startswith("# Part "):
            part = line.split(" - ")[0].replace("# Part ", "").strip()
            continue
        if part == "XIII":
            m = re.match(r"^## \d+\. ([A-Z]{3}) ", line)
            if m:
                domain = m.group(1)
                continue
            if domain and line.startswith("| ") and not line.startswith("| **") and not line.startswith("|--"):
                name = line.split("|")[1].strip().split(" †")[0].strip()
                if name:
                    families.add("%s:%s" % (domain, name))
        if part == "VI" and line.startswith("| ") and not line.startswith("| **"):
            name = line.split("|")[1].strip()
            if name and not name.startswith("-"):
                causes.add(name)
        if part == "VII":
            m = re.match(r"^\| (M\d\d) \|", line)
            if m:
                modes.add(m.group(1))
        m = re.match(r"^## (X\d\d) ", line)
        if m:
            library.add(m.group(1))
        m = re.match(r"^\| (FM-[A-Z]{3}-\d{3}) \| (RF-[A-Z]{3}-\d{2}) \| (M\d\d) ", line)
        if m:
            fm[m.group(1)] = m.group(3)
    return families, library, fm, modes, causes


def load_controls():
    with open(REG / "controls/controls.csv", encoding="utf-8", newline="") as fh:
        controls = {r["controlId"]: r for r in csv.DictReader(fh)}
    criteria_count = {}
    for path in sorted(CONTROL_MD_DIR.glob("AIDCF-007A_Controls_*_v1.1.md")):
        current, in_criteria = None, False
        for line in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^### (MCF-[A-Z]{3}-\d{3})\s*$", line)
            if m:
                current, in_criteria = m.group(1), False
                criteria_count[current] = 0
                continue
            if current is None:
                continue
            if line.startswith("**Assessment criteria**"):
                in_criteria = True
                continue
            if in_criteria and line.startswith("**"):
                in_criteria = False
            if in_criteria and re.match(r"^\d+\. ", line):
                criteria_count[current] += 1
    with open(REG / "controls/gate-mappings.csv", encoding="utf-8", newline="") as fh:
        mappings = defaultdict(dict)
        for r in csv.DictReader(fh):
            mappings[r["controlId"]][r["gateId"]] = r["role"]
    return controls, criteria_count, mappings


def load_gates():
    with open(REG / "gates/critical-gates.csv", encoding="utf-8", newline="") as fh:
        gates = {r["gateId"] for r in csv.DictReader(fh)}
    with open(REG / "gates/critical-gate-criteria.csv", encoding="utf-8", newline="") as fh:
        criteria = {r["criterionId"]: r["gateId"] for r in csv.DictReader(fh)}
    return gates, criteria


def load_vocab(name, kind=None):
    with open(REG / "vocabularies" / name, encoding="utf-8", newline="") as fh:
        return {r["code"] for r in csv.DictReader(fh) if kind is None or r.get("kind") == kind}


# ---------------------------------------------------------------- validation

class Checker:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def err(self, where, msg):
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where, msg):
        self.warnings.append("%s: %s" % (where, msg))


def check_sheet(path, chk, ref):
    families, library, fm, modes, causes, controls, crit_count, mappings, gates, gcrit, \
        control_results, confidence = ref
    header, rows, raw = read_csv(path)
    if header != SHEET_COLUMNS:
        chk.err(path.name, "header does not match the data dictionary column order")
        return []
    for i, r in enumerate(raw, start=2):
        if len(r) != len(header):
            chk.err("%s:%d" % (path.name, i), "expected %d fields, found %d" % (len(header), len(r)))
    factor_seen = {}
    for i, r in enumerate(rows, start=2):
        w = "%s:%d" % (path.name, i)
        g = r.get
        if not INC_RE.match(g("incident_id", "")):
            chk.err(w, "incident_id must be INC-NNN or INC-EXAMPLE-NN")
        example = g("incident_id", "").startswith("INC-EXAMPLE-")
        if example and "FICTIONAL" not in g("notes", "").upper():
            chk.err(w, "example rows must be marked FICTIONAL in notes")
        rt = g("record_type")
        if rt not in RECORD_TYPES:
            chk.err(w, "record_type must be CONTROL or GATE")
        if not CODER_RE.match(g("coder_id", "")) and g("coding_round") != "RECONCILED":
            chk.err(w, "coder_id must be a pseudonymous code C01..C99")
        if g("coding_round") not in ROUNDS:
            chk.err(w, "coding_round must be A, B or RECONCILED")
        if g("independent_of_author") not in YN:
            chk.err(w, "independent_of_author must be Y or N")
        if g("prior_familiarity") not in FAMILIARITY:
            chk.err(w, "prior_familiarity invalid")
        if g("coding_phase") not in PHASES:
            chk.err(w, "coding_phase must be PRE_REVEAL or POST_REVEAL")
        urls, stypes = split(g("source_urls", "")), split(g("source_types", ""))
        if not urls or len(urls) != len(stypes):
            chk.err(w, "source_urls and source_types must be non-empty and the same length")
        if any(not u.startswith("https://") and not u.startswith("http://") for u in urls):
            chk.err(w, "source_urls must be absolute URLs")
        if any(s not in SOURCE_TYPES for s in stypes):
            chk.err(w, "source_types invalid")
        if stypes and not ({"PRIMARY", "REGULATOR"} & set(stypes)):
            chk.err(w, "at least one PRIMARY or REGULATOR source is required")
        for col in ("access_date", "incident_date"):
            if not DATE_RE.match(g(col, "")):
                chk.err(w, "%s must be YYYY-MM-DD" % col)
        if g("operator_type") not in OPERATOR_TYPES:
            chk.err(w, "operator_type invalid")
        if g("failure_category") not in CATEGORIES:
            chk.err(w, "failure_category invalid")
        if not g("timeline_before_cause", "").strip():
            chk.err(w, "timeline_before_cause is required")
        if g("confidence") not in confidence:
            chk.err(w, "confidence must be a canonical level code CONF-0..CONF-4")
        gap = g("gap_type")
        if gap not in GAP_TYPES:
            chk.err(w, "gap_type invalid")
        elif (gap == "NONE") != (not g("gap_description", "").strip()):
            chk.err(w, "gap_description required if and only if gap_type is not NONE")

        if rt == "CONTROL":
            fid = g("factor_id", "")
            local = bool(LOCAL_FACTOR_RE.match(fid))
            if not (FACTOR_RE.match(fid) or local):
                chk.err(w, "factor_id must be CF-NN (consolidated) or CF-ANN/CF-BNN (coding pass 1)")
            if g("factor_role") not in FACTOR_ROLES:
                chk.err(w, "factor_role invalid")
            if not g("causal_factor", "").strip():
                chk.err(w, "causal_factor is required")
            kn = g("knowability")
            if kn not in KNOWABILITY:
                chk.err(w, "knowability invalid")
            if g("cause_family") not in causes:
                chk.err(w, "cause_family %r not in AIDCF-004 Part VI" % g("cause_family"))
            for sf in split(g("scenario_family", "")):
                if sf not in families:
                    chk.err(w, "scenario_family %r not in AIDCF-004 Part XIII" % sf)
            if not split(g("scenario_family", "")):
                chk.err(w, "scenario_family is required (use the closest family; record G6 if none fits)")
            lib = g("library_scenario", "")
            for x in split(lib):
                if x != "NONE" and x not in library:
                    chk.err(w, "library_scenario %r not in AIDCF-004 Part XIV" % x)
            fms = split(g("failure_modes", ""))
            gms = split(g("generic_modes", ""))
            for f in fms:
                if f != "NONE" and f not in fm:
                    chk.err(w, "failure mode %r not in AIDCF-004 Appendix A" % f)
            for m in gms:
                if m not in modes:
                    chk.err(w, "generic mode %r not in AIDCF-004 Part VII" % m)
            for f in fms:
                if f in fm and fm[f] not in gms:
                    chk.err(w, "generic_modes must include %s (mode of %s)" % (fm[f], f))
            if not gms:
                chk.err(w, "generic_modes is required (M00 if unresolved)")
            key = (g("incident_id"), g("coding_round"), g("coder_id"), fid)
            sig = tuple(g(c) for c in ("factor_role", "causal_factor", "knowability", "cause_family",
                                        "scenario_family", "library_scenario", "failure_modes",
                                        "generic_modes", "coding_phase"))
            if key in factor_seen and factor_seen[key] != sig:
                chk.err(w, "factor fields differ from an earlier row for the same factor_id")
            factor_seen.setdefault(key, sig)
            for col in ("gate_id", "gate_criteria", "gate_judgement"):
                if g(col):
                    chk.err(w, "%s must be empty on CONTROL rows" % col)
            cid, crit = g("control_id", ""), g("control_criteria", "")
            pcr, det = g("projected_control_result", ""), g("detection_judgement", "")
            if local and not cid:
                if crit or pcr or det:
                    chk.err(w, "pass 1 factor rows leave control fields empty")
                continue
            if cid != "NONE" and cid not in controls:
                chk.err(w, "control_id %r not in registries/controls/controls.csv" % cid)
            if cid in controls:
                n = crit_count.get(cid, 0)
                for c in split(crit):
                    if not c.isdigit() or not 1 <= int(c) <= n:
                        chk.err(w, "control_criteria %r not an assessment-criterion number of %s (1..%d)" % (c, cid, n))
            if kn == "NOT_KNOWABLE":
                if det:
                    chk.err(w, "detection_judgement must be empty when knowability is NOT_KNOWABLE")
                continue
            if det not in DETECTION:
                chk.err(w, "detection_judgement invalid")
                continue
            if kn == "NOT_STATED" and det != "INSUFFICIENT_INFORMATION":
                chk.err(w, "knowability NOT_STATED requires INSUFFICIENT_INFORMATION")
            if det == "NOT_ADDRESSED":
                if cid != "NONE" or crit or pcr:
                    chk.err(w, "NOT_ADDRESSED requires control_id NONE and empty criteria/result")
                if gap not in {"G1_NO_CONTROL", "G6_THREAT_MODEL"}:
                    chk.err(w, "NOT_ADDRESSED requires gap_type G1_NO_CONTROL or G6_THREAT_MODEL")
                continue
            if cid == "NONE" and det != "INSUFFICIENT_INFORMATION":
                chk.err(w, "control_id NONE is only valid with NOT_ADDRESSED or INSUFFICIENT_INFORMATION")
            if det == "INSUFFICIENT_INFORMATION":
                continue
            if pcr not in control_results or pcr in {"NOT_APPLICABLE", "NOT_ASSESSED"}:
                chk.err(w, "projected_control_result must be CONFORMING, PARTIAL, NONCONFORMING or UNKNOWN")
            if not split(crit):
                chk.err(w, "control_criteria required for %s" % det)
            if det == "DETECTED" and pcr == "CONFORMING":
                chk.err(w, "DETECTED is inconsistent with a projected CONFORMING result")
            if det == "NOT_DETECTED" and pcr != "CONFORMING":
                chk.err(w, "NOT_DETECTED requires a projected CONFORMING result")
            if det == "NOT_DETECTED" and gap == "NONE":
                chk.warn(w, "NOT_DETECTED without a gap_type: confirm no criterion or evidence-profile gap")
        elif rt == "GATE":
            for col in ("control_id", "control_criteria", "projected_control_result", "detection_judgement",
                        "causal_factor", "factor_role", "knowability"):
                if g(col):
                    chk.err(w, "%s must be empty on GATE rows" % col)
            for fid in split(g("factor_id", "")):
                if not FACTOR_RE.match(fid):
                    chk.err(w, "GATE rows reference consolidated factor IDs CF-NN")
            if not split(g("factor_id", "")):
                chk.err(w, "GATE rows list the factor IDs that engage the gate")
            gid = g("gate_id", "")
            if gid not in gates:
                chk.err(w, "gate_id %r not in registries/gates/critical-gates.csv" % gid)
            for c in split(g("gate_criteria", "")):
                if gcrit.get(c) != gid:
                    chk.err(w, "gate criterion %r does not exist for %s" % (c, gid))
            gj = g("gate_judgement")
            if gj not in GATE_JUDGEMENTS:
                chk.err(w, "gate_judgement invalid")
            if gj in {"FAIL", "PASS"} and not split(g("gate_criteria", "")):
                chk.err(w, "gate_criteria required for a %s judgement" % gj)
    return rows


def check_register(path, chk, controls_ref=None):
    header, rows, raw = read_csv(path)
    if header != REGISTER_COLUMNS:
        chk.err(path.name, "header does not match the README register specification")
        return []
    ids = Counter()
    for i, r in enumerate(rows, start=2):
        w = "%s:%d" % (path.name, i)
        if len(raw[i - 2]) != len(header):
            chk.err(w, "field count mismatch")
            continue
        ids[r["incident_id"]] += 1
        if not re.match(r"^INC-\d{3}$", r["incident_id"]):
            chk.err(w, "register holds real candidates only: incident_id INC-NNN")
        if r["operator_type"] not in OPERATOR_TYPES:
            chk.err(w, "operator_type invalid")
        if r["failure_category"] not in CATEGORIES and not (r["failure_category"] == "" and r["eligibility_status"] == "EXCLUDED"):
            chk.err(w, "failure_category invalid (blank allowed only on EXCLUDED rows)")
        if any(t not in TAGS for t in split(r["tags"])):
            chk.err(w, "tags invalid")
        if r["primary_source_type"] not in SOURCE_TYPES - {"SECONDARY_PRESS"} and r["eligibility_status"] != "EXCLUDED":
            chk.err(w, "primary_source_type must be PRIMARY or REGULATOR unless EXCLUDED")
        for col in ("incident_date", "access_date"):
            if col == "incident_date" and r[col] == "" and "DATE_UNRESOLVED" in r["notes"]:
                chk.warn(w, "incident_date unresolved (DATE_UNRESOLVED); resolve before selection")
            elif not DATE_RE.match(r[col]):
                chk.err(w, "%s must be YYYY-MM-DD (or blank with DATE_UNRESOLVED in notes)" % col)
        if r["detail_level"] not in DETAIL_LEVELS:
            chk.err(w, "detail_level invalid")
        if r["eligibility_status"] not in ELIGIBILITY:
            chk.err(w, "eligibility_status invalid")
        if (r["eligibility_status"] == "EXCLUDED") != (r["exclusion_code"] in EXCLUSION_CODES):
            chk.err(w, "exclusion_code required if and only if EXCLUDED")
        if r["coding_status"] and r["coding_status"] not in CODING_STATUS:
            chk.err(w, "coding_status invalid")
    for k, n in ids.items():
        if n > 1:
            chk.err(path.name, "duplicate incident_id %s" % k)
    return rows


def reference():
    families, library, fm, modes, causes = load_threat_model()
    controls, crit_count, mappings = load_controls()
    gates, gcrit = load_gates()
    control_results = load_vocab("control-results.csv")
    confidence = load_vocab("confidence.csv", kind="level")
    problems = []
    if len(families) < 90:
        problems.append("parsed only %d scenario families from AIDCF-004" % len(families))
    if len(library) != 20:
        problems.append("expected 20 library scenarios, parsed %d" % len(library))
    if len(modes) != 31:
        problems.append("expected M00-M30, parsed %d" % len(modes))
    if len(controls) != 360 or len([c for c in crit_count if crit_count[c]]) != 360:
        problems.append("control registry or catalogue criteria not fully parsed")
    if len(gates) != 15:
        problems.append("expected 15 gates")
    return (families, library, fm, modes, causes, controls, crit_count, mappings, gates, gcrit,
            control_results, confidence), problems


# ---------------------------------------------------------------- statistics

def cohen_kappa(pairs):
    n = len(pairs)
    if n == 0:
        return None, None, 0
    po = sum(1 for a, b in pairs if a == b) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    if pe == 1:
        return po, None, n
    return po, (po - pe) / (1 - pe), n


def wilson(k, n, z=1.959964):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def fmt_prop(k, n):
    if n == 0:
        return "n/a (n=0)"
    lo, hi = wilson(k, n)
    return "%d/%d = %.2f (95%% Wilson %.2f-%.2f)" % (k, n, k / n, lo, hi)


def agreement(rows, include_examples):
    rows = [r for r in rows if include_examples or not r["incident_id"].startswith("INC-EXAMPLE-")]
    det, gate = defaultdict(dict), defaultdict(dict)
    maps = defaultdict(lambda: defaultdict(set))
    fams = defaultdict(dict)
    for r in rows:
        rd = r["coding_round"]
        if rd not in {"A", "B"}:
            continue
        if r["record_type"] == "CONTROL" and FACTOR_RE.match(r["factor_id"]):
            k = (r["incident_id"], r["factor_id"], r["control_id"])
            if r["detection_judgement"]:
                det[k][rd] = r["detection_judgement"]
            maps[(r["incident_id"], r["factor_id"])][rd].add(r["control_id"])
            fams[(r["incident_id"], r["factor_id"])][rd] = r["scenario_family"]
        elif r["record_type"] == "GATE":
            gate[(r["incident_id"], r["gate_id"])][rd] = r["gate_judgement"]
    out = []
    pairs = [(v["A"], v["B"]) for k, v in sorted(det.items()) if "A" in v and "B" in v]
    po, kappa, n = cohen_kappa(pairs)
    out.append("Detection judgement (same incident, factor, control): n=%d pairs" % n)
    if n:
        out.append("  percentage agreement %.3f; Cohen's kappa %s" % (po, "undefined" if kappa is None else "%.3f" % kappa))
        out.append("  marginals A: %s" % dict(sorted(Counter(a for a, _ in pairs).items())))
        out.append("  marginals B: %s" % dict(sorted(Counter(b for _, b in pairs).items())))
    pairs = [(v["A"], v["B"]) for k, v in sorted(gate.items()) if "A" in v and "B" in v]
    po, kappa, n = cohen_kappa(pairs)
    out.append("Gate judgement (same incident, gate): n=%d pairs" % n)
    if n:
        out.append("  percentage agreement %.3f; Cohen's kappa %s" % (po, "undefined" if kappa is None else "%.3f" % kappa))
    gate_only = [k for k, v in gate.items() if len(v) == 1]
    out.append("  gates judged relevant by one coder only: %d" % len(gate_only))
    jac = []
    for k, v in sorted(maps.items()):
        if "A" in v and "B" in v:
            u = v["A"] | v["B"]
            jac.append(len(v["A"] & v["B"]) / len(u) if u else 1.0)
    out.append("Control mapping (per consolidated factor): n=%d factors; mean Jaccard %s" %
               (len(jac), "%.3f" % (sum(jac) / len(jac)) if jac else "n/a"))
    fp = [(v["A"], v["B"]) for k, v in sorted(fams.items()) if "A" in v and "B" in v]
    if fp:
        out.append("Scenario-family assignment: percentage exact agreement %.3f (n=%d)" %
                   (sum(1 for a, b in fp if a == b) / len(fp), len(fp)))
    return out


def metrics(rows, controls, include_examples):
    rows = [r for r in rows if r["coding_round"] == "RECONCILED" and
            (include_examples or not r["incident_id"].startswith("INC-EXAMPLE-"))]
    out = []
    incidents = sorted({r["incident_id"] for r in rows})
    cat = {r["incident_id"]: r["failure_category"] for r in rows}
    out.append("Incidents with RECONCILED rows: %d" % len(incidents))
    factors = defaultdict(list)
    meta = {}
    for r in rows:
        if r["record_type"] == "CONTROL" and FACTOR_RE.match(r["factor_id"]):
            k = (r["incident_id"], r["factor_id"])
            factors[k].append(r)
            meta[k] = r
    best = {}
    unknowable = 0
    for k, rs in factors.items():
        if meta[k]["knowability"] == "NOT_KNOWABLE":
            unknowable += 1
            continue
        js = [x["detection_judgement"] for x in rs]
        ranked = [j for j in js if j in DETECTION_RANK]
        if ranked:
            best[k] = max(ranked, key=lambda j: DETECTION_RANK[j])
        elif "NOT_ADDRESSED" in js:
            best[k] = "NOT_ADDRESSED"
        else:
            best[k] = "INSUFFICIENT_INFORMATION"
    judged = {k: v for k, v in best.items() if v != "INSUFFICIENT_INFORMATION"}
    out.append("Factors: %d total; %d NOT_KNOWABLE (excluded); %d INSUFFICIENT_INFORMATION (excluded); %d judged" %
               (len(factors), unknowable, len(best) - len(judged), len(judged)))
    n = len(judged)
    det = sum(1 for v in judged.values() if v == "DETECTED")
    part = sum(1 for v in judged.values() if v == "PARTIALLY_DETECTED")
    addr = sum(1 for v in judged.values() if v != "NOT_ADDRESSED")
    out.append("Addressing coverage (>=1 control addresses factor): " + fmt_prop(addr, n))
    out.append("Strict detection coverage (best = DETECTED): " + fmt_prop(det, n))
    out.append("Inclusive detection coverage (DETECTED or PARTIALLY_DETECTED): " + fmt_prop(det + part, n))

    def by(keyfn, label):
        out.append("Strict detection coverage by %s:" % label)
        groups = defaultdict(list)
        for k, v in judged.items():
            groups[keyfn(k)].append(v)
        for gk in sorted(groups):
            vs = groups[gk]
            out.append("  %-22s %s" % (gk, fmt_prop(sum(1 for v in vs if v == "DETECTED"), len(vs))))

    by(lambda k: cat[k[0]], "failure category")
    by(lambda k: split(meta[k]["scenario_family"])[0].split(":")[0], "factor domain (scenario family)")

    gate_rows = [r for r in rows if r["record_type"] == "GATE"]
    out.append("Projected gate results (relevant gates only):")
    gcount = defaultdict(Counter)
    for r in gate_rows:
        gcount[r["gate_id"]][r["gate_judgement"]] += 1
    for gid in sorted(gcount):
        out.append("  %s %s" % (gid, dict(sorted(gcount[gid].items()))))
    surfaced = 0
    for inc in incidents:
        gj = [r["gate_judgement"] for r in gate_rows if r["incident_id"] == inc]
        if any(j in {"FAIL", "UNKNOWN"} for j in gj):
            surfaced += 1
    out.append("Incidents with >=1 relevant gate projected FAIL or UNKNOWN: " + fmt_prop(surfaced, len(incidents)))
    out.append("False-reassurance cases (relevant gate projected PASS):")
    for r in sorted(gate_rows, key=lambda r: (r["incident_id"], r["gate_id"])):
        if r["gate_judgement"] == "PASS":
            out.append("  %s %s factors=%s" % (r["incident_id"], r["gate_id"], r["factor_id"]))
    out.append("Control-level false reassurance (NOT_DETECTED, projected CONFORMING):")
    for r in rows:
        if r["record_type"] == "CONTROL" and r["detection_judgement"] == "NOT_DETECTED":
            out.append("  %s %s %s" % (r["incident_id"], r["factor_id"], r["control_id"]))
    out.append("Gap list:")
    for r in sorted(rows, key=lambda r: (r["incident_id"], r["factor_id"], r["control_id"], r["gate_id"])):
        if r["gap_type"] not in {"", "NONE"}:
            out.append("  %s %s %s %s: %s" % (r["incident_id"], r["factor_id"] or "-", r["control_id"] or r["gate_id"] or "-",
                                             r["gap_type"], r["gap_description"]))
    post = sum(1 for k in judged if meta[k]["coding_phase"] == "POST_REVEAL")
    out.append("Hindsight indicator (judged factors first identified POST_REVEAL): " + fmt_prop(post, n))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate files (default)")
    mode.add_argument("--agreement", action="store_true")
    mode.add_argument("--metrics", action="store_true")
    mode.add_argument("--list-families", action="store_true")
    ap.add_argument("--sheet", type=Path, default=HERE / "coding-sheet.csv")
    ap.add_argument("--register", type=Path, default=HERE / "incident-register.csv")
    ap.add_argument("--include-examples", action="store_true")
    a = ap.parse_args(argv)
    ref, problems = reference()
    if problems:
        for p in problems:
            print("REFERENCE ERROR: " + p)
        return 1
    if a.list_families:
        for f in sorted(ref[0]):
            print(f)
        return 0
    chk = Checker()
    try:
        rows = check_sheet(a.sheet, chk, ref)
        reg = check_register(a.register, chk)
    except (ValueError, UnicodeDecodeError, OSError) as exc:
        print("ERROR: %s" % exc)
        return 1
    reg_ids = {r["incident_id"] for r in reg}
    for r in rows:
        if not r["incident_id"].startswith("INC-EXAMPLE-") and r["incident_id"] not in reg_ids:
            chk.err(a.sheet.name, "%s is not in the incident register" % r["incident_id"])
    if a.agreement or a.metrics:
        if chk.errors:
            print("Files have validation errors; run --check first.")
            return 1
        lines = agreement(rows, a.include_examples) if a.agreement else metrics(rows, ref[5], a.include_examples)
        print("\n".join(lines))
        return 0
    for e in sorted(set(chk.errors)):
        print("ERROR " + e)
    for w in sorted(set(chk.warnings)):
        print("WARNING " + w)
    print("checked %d coding rows, %d register rows: %d errors, %d warnings" %
          (len(rows), len(reg), len(set(chk.errors)), len(set(chk.warnings))))
    return 1 if chk.errors else 0


if __name__ == "__main__":
    sys.exit(main())
