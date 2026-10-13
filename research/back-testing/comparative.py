"""AIDCF-VAL-001 v1.1 comparative validation (protocol section 10A).

Validation and paired metrics for the comparison between AIDCF and conventional
review methods. Imported by backtest_check.py; standard library only and
deterministic (seeded) output.

Files (beside backtest_check.py unless overridden):
  baselines.csv                    frozen comparator specification (section 10A.2)
  comparative-sheet.csv            FACTOR, BASELINE, AIDCF_EOD and GAP_DISPOSITION rows
  run-log/comparative-locks.csv    SHA-256 locks and seeds

The AIDCF side of every pair is read from coding-sheet.csv (v1.0 semantics,
unchanged). Baseline coders work in comparative-sheet.csv, so the two sides can
be locked separately (section 10A.4).
"""

import csv
import hashlib
import math
import random
import re
from collections import Counter, defaultdict

METHODS = ["BL-TIER", "BL-CX", "BL-ENG", "BL-OT", "BL-ISMS", "BL-TDD"]
BASELINE_COLUMNS = [
    "baseline_id", "name", "references", "edition_profile", "scope", "deliverable", "evidence",
    "constraints", "exclusions", "applicability", "pilot_status", "version", "approval_status",
    "approved_on", "reviewer_id",
]
SHEET_COLUMNS = [
    "incident_id", "record_type", "coder_id", "coding_round", "independent_of_author",
    "prior_familiarity", "factor_id", "factor_origin", "factor_source", "knowability",
    "coding_phase", "eod_sampled", "baseline_id", "detection_judgement", "baseline_criteria",
    "exclusion_id", "applicability_rule", "eng_discipline", "eng_technique", "eod",
    "eod_assumptions", "eod_confidence", "gap_disposition", "disposition_citation", "notes",
]
LOCK_COLUMNS = ["artefact", "value", "locked_on", "locked_by", "notes"]

RECORD_TYPES = {"FACTOR", "BASELINE", "AIDCF_EOD", "GAP_DISPOSITION"}
PILOT_STATUS = {"ACTIVE", "NOT_EVALUATED"}
APPROVAL = {"DRAFT", "APPROVED"}
ORIGINS = {"AIDCF", "BASELINE", "BOTH", "ADJUDICATOR"}
KNOWABLE = {"STATED_KNOWN", "DISCOVERABLE"}
KNOWABILITY = {"STATED_KNOWN", "DISCOVERABLE", "NOT_KNOWABLE", "NOT_STATED"}
AIDCF_JUDGEMENTS = ["DETECTED", "PARTIALLY_DETECTED", "NOT_DETECTED", "NOT_ADDRESSED",
                    "INSUFFICIENT_INFORMATION"]
BASELINE_JUDGEMENTS = AIDCF_JUDGEMENTS + ["OUT_OF_SCOPE", "NOT_APPLICABLE"]
CITED = {"DETECTED", "PARTIALLY_DETECTED", "NOT_DETECTED"}
EOD_VALUES = {"LIKELY", "POSSIBLE", "UNLIKELY", "INDETERMINATE"}
EOD_CONFIDENCE = {"LOW", "MEDIUM", "HIGH"}
ENG_DISCIPLINES = {"POWER", "COOLING", "OTHER"}
DISPOSITIONS = {"ACTIONABLE_GAP", "OUTSIDE_DECLARED_BOUNDARY", "BELOW_INTENDED_GRANULARITY",
                "DELEGATED_TO_STANDARD", "DISPUTED"}
ACTIONABLE_GAP_TYPES = {"G1_NO_CONTROL", "G2_NO_CRITERION", "G3_EVIDENCE_PROFILE"}
DETECTION_RANK = {"DETECTED": 3, "PARTIALLY_DETECTED": 2, "NOT_DETECTED": 1}

PRIMARY_THRESHOLD = 0.5
SENSITIVITY_THRESHOLDS = [0.25, 0.5, 0.75, 1.0]
EOD_FRACTION = 0.3
BOOTSTRAP_RESAMPLES = 10000
MIN_INCIDENTS_FOR_INTERVAL = 10
MIN_INCIDENTS_FOR_STRATUM = 5
DIFFERENTIAL_FLAG = 0.10

FACTOR_RE = re.compile(r"^CF-\d{2}$")
CODER_RE = re.compile(r"^C\d{2}$")
DECL_RE = re.compile(r"^((?:EXC|APP)-\d{2}):\s*(.+)$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def split(value):
    return [v.strip() for v in (value or "").split(";") if v.strip()]


def read_csv(path):
    raw = path.read_bytes()
    if b"\r" in raw:
        raise ValueError("%s: CR characters found; files must use LF line endings" % path)
    rows = list(csv.reader(raw.decode("utf-8").splitlines()))
    if not rows:
        raise ValueError("%s: empty file (a header row is required)" % path)
    return rows[0], [dict(zip(rows[0], r)) for r in rows[1:]], rows[1:]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ------------------------------------------------------------ judgement mapping (section 10A.5.1)

def side_value(judgement, reading, side):
    """Map one judgement to 'S' (surfaced), 'M' (miss), 'X' (indeterminate) or 'NA'.

    reading is 'strict' or 'inclusive'; side is 'AIDCF' or 'BASELINE'.
    """
    allowed = AIDCF_JUDGEMENTS if side == "AIDCF" else BASELINE_JUDGEMENTS
    if judgement not in allowed:
        raise ValueError("%s is not a valid %s judgement" % (judgement, side))
    if judgement == "DETECTED":
        return "S"
    if judgement == "PARTIALLY_DETECTED":
        return "S" if reading == "inclusive" else "M"
    if judgement in {"NOT_DETECTED", "NOT_ADDRESSED", "OUT_OF_SCOPE"}:
        return "M"
    if judgement == "INSUFFICIENT_INFORMATION":
        return "X"
    return "NA"  # NOT_APPLICABLE


def miss_subtype(judgement, reading):
    if judgement == "PARTIALLY_DETECTED" and reading == "strict":
        return "PARTIAL"
    return {"NOT_DETECTED": "ADDRESSED_NOT_DETECTED", "NOT_ADDRESSED": "NOT_ADDRESSED",
            "OUT_OF_SCOPE": "DECLARED_EXCLUSION"}.get(judgement)


def combine_union(judgements, reading):
    """BL-ANY rule (section 10A.5.2). judgements: {method: judgement} for the evaluated methods."""
    values = [side_value(j, reading, "BASELINE") for j in judgements.values()]
    applicable = [v for v in values if v != "NA"]
    if not applicable:
        return "NA"
    if "S" in applicable:
        return "S"
    if all(v == "M" for v in applicable):
        return "M"
    return "X"


def pair_class(aidcf_value, baseline_value):
    """Return a, b, c, d or an exclusion reason, from side values S/M/X/NA."""
    if baseline_value == "NA":
        return "EXCLUDED_NOT_APPLICABLE"
    if aidcf_value == "X":
        return "EXCLUDED_INDETERMINATE_AIDCF"
    if baseline_value == "X":
        return "EXCLUDED_INDETERMINATE_BASELINE"
    return {("S", "S"): "a", ("S", "M"): "b", ("M", "S"): "c", ("M", "M"): "d"}[(aidcf_value, baseline_value)]


def union_label(active):
    if sorted(active) == sorted(METHODS):
        return "BL-ANY"
    return "BL-ANY-%d" % len(active)


def union_note(active):
    label = union_label(active)
    if label == "BL-ANY":
        return "BL-ANY is the combined-method coverage benchmark of all six methods, not one conventional assessment."
    return ("%s is the combined-method coverage benchmark of %s only. The six-method BL-ANY has not been "
            "evaluated; %s were not evaluated in this run." %
            (label, ", ".join(sorted(active)), ", ".join(m for m in METHODS if m not in active)))


# ------------------------------------------------------------ loading

def parse_declarations(text):
    out = {}
    for item in split(text):
        m = DECL_RE.match(item)
        if not m:
            raise ValueError(item)
        out[m.group(1)] = m.group(2)
    return out


def load_baselines(path, chk):
    header, rows, raw = read_csv(path)
    if header != BASELINE_COLUMNS:
        chk.err(path.name, "header does not match the baselines.csv specification")
        return {}
    spec = {}
    for i, r in enumerate(rows, start=2):
        w = "%s:%d" % (path.name, i)
        if len(raw[i - 2]) != len(header):
            chk.err(w, "field count mismatch")
            continue
        bid = r["baseline_id"]
        if bid not in METHODS and bid != "AIDCF":
            chk.err(w, "baseline_id must be one of %s or AIDCF" % ", ".join(METHODS))
            continue
        if bid in spec:
            chk.err(w, "duplicate baseline_id %s" % bid)
        if r["pilot_status"] not in PILOT_STATUS:
            chk.err(w, "pilot_status must be ACTIVE or NOT_EVALUATED")
        if bid == "AIDCF" and r["pilot_status"] != "ACTIVE":
            chk.err(w, "the AIDCF constraints row is always ACTIVE")
        if r["approval_status"] not in APPROVAL:
            chk.err(w, "approval_status must be DRAFT or APPROVED")
        if r["approval_status"] == "APPROVED" and not (re.match(r"^\d{4}-\d{2}-\d{2}$", r["approved_on"])
                                                       and CODER_RE.match(r["reviewer_id"])):
            chk.err(w, "APPROVED rows need approved_on (YYYY-MM-DD) and a practitioner reviewer_id C01..C99")
        for col in ("name", "references", "edition_profile", "scope", "constraints", "version"):
            if not r[col].strip():
                chk.err(w, "%s is required" % col)
        try:
            exc = parse_declarations(r["exclusions"])
            app = parse_declarations(r["applicability"])
        except ValueError as e:
            chk.err(w, "exclusions and applicability are '; '-separated 'EXC-NN: text' / 'APP-NN: text' items (%s)" % e)
            exc, app = {}, {}
        if any(not k.startswith("EXC-") for k in exc) or any(not k.startswith("APP-") for k in app):
            chk.err(w, "exclusions use EXC-NN and applicability uses APP-NN")
        spec[bid] = dict(r, exc=exc, app=app)
    for m in METHODS + ["AIDCF"]:
        if m not in spec:
            chk.err(path.name, "missing row for %s" % m)
    return spec


def load_locks(path, chk):
    header, rows, raw = read_csv(path)
    if header != LOCK_COLUMNS:
        chk.err(path.name, "header does not match the comparative-locks.csv specification")
        return {}
    locks = {}
    for i, r in enumerate(rows, start=2):
        w = "%s:%d" % (path.name, i)
        a = r["artefact"]
        if a in {"BASELINES", "EOD_FRAME"} or a.startswith("FILE:"):
            if not SHA_RE.match(r["value"]):
                chk.err(w, "%s value must be a SHA-256 hex digest" % a)
        elif a in {"EOD_SEED", "BOOTSTRAP_SEED"}:
            if not r["value"].isdigit():
                chk.err(w, "%s value must be a non-negative integer" % a)
        else:
            chk.err(w, "unknown artefact %r (BASELINES, EOD_FRAME, EOD_SEED, BOOTSTRAP_SEED or FILE:<path>)" % a)
        if a in locks and not a.startswith("FILE:"):
            chk.err(w, "%s is locked once; a changed lock is a protocol deviation" % a)
        locks[a] = r["value"]
    return locks


# ------------------------------------------------------------ AIDCF side from coding-sheet.csv

def aidcf_factor_judgements(coding_rows):
    """Factor-level AIDCF judgement from RECONCILED CONTROL rows (v1.0 section 10 'best' rule)."""
    by_factor = defaultdict(list)
    meta = {}
    for r in coding_rows:
        if r["coding_round"] == "RECONCILED" and r["record_type"] == "CONTROL" and FACTOR_RE.match(r["factor_id"]):
            k = (r["incident_id"], r["factor_id"])
            by_factor[k].append(r["detection_judgement"])
            meta[k] = r
    best = {}
    for k, js in by_factor.items():
        if meta[k]["knowability"] == "NOT_KNOWABLE":
            continue
        ranked = [j for j in js if j in DETECTION_RANK]
        if ranked:
            best[k] = max(ranked, key=lambda j: DETECTION_RANK[j])
        elif "NOT_ADDRESSED" in js:
            best[k] = "NOT_ADDRESSED"
        else:
            best[k] = "INSUFFICIENT_INFORMATION"
    return best, meta


# ------------------------------------------------------------ EOD sample (section 10A.3.2)

def eod_frame(factor_rows):
    return sorted((r["incident_id"], r["factor_id"]) for r in factor_rows
                  if r["knowability"] in KNOWABLE and r["coding_phase"] == "PRE_REVEAL")


def frame_digest(frame):
    return hashlib.sha256("\n".join("%s %s" % f for f in frame).encode("utf-8")).hexdigest()


def draw_eod_sample(frame, category_of, seed, fraction=EOD_FRACTION):
    """At least one factor per incident, then fill each failure-category stratum to ceil(fraction * n)."""
    rng = random.Random(int(seed))
    chosen = set()
    by_incident = defaultdict(list)
    for inc, fid in frame:
        by_incident[inc].append((inc, fid))
    for inc in sorted(by_incident):
        chosen.add(rng.choice(by_incident[inc]))
    strata = defaultdict(list)
    for f in frame:
        strata[category_of(f[0])].append(f)
    for s in sorted(strata):
        members = strata[s]
        target = math.ceil(fraction * len(members))
        rest = [f for f in members if f not in chosen]
        rng.shuffle(rest)
        have = sum(1 for f in members if f in chosen)
        for f in rest:
            if have >= target:
                break
            chosen.add(f)
            have += 1
    return sorted(chosen)


# ------------------------------------------------------------ validation

def check_comparative(sheet_path, baselines_path, locks_path, coding_rows, category_of, chk):
    """Validate the comparative files. Returns (rows, spec, locks)."""
    spec = load_baselines(baselines_path, chk)
    locks = load_locks(locks_path, chk)
    header, rows, raw = read_csv(sheet_path)
    if header != SHEET_COLUMNS:
        chk.err(sheet_path.name, "header does not match the comparative-sheet dictionary column order")
        return [], spec, locks
    active = {m for m in METHODS if spec.get(m, {}).get("pilot_status") == "ACTIVE"}
    consolidated = {(r["incident_id"], r["factor_id"]): r for r in coding_rows
                    if r["record_type"] == "CONTROL" and FACTOR_RE.match(r["factor_id"])}
    factors, seen = {}, Counter()
    for i, r in enumerate(raw, start=2):
        if len(r) != len(header):
            chk.err("%s:%d" % (sheet_path.name, i), "expected %d fields, found %d" % (len(header), len(r)))
    for i, r in enumerate(rows, start=2):
        w = "%s:%d" % (sheet_path.name, i)
        rt = r["record_type"]
        if rt not in RECORD_TYPES:
            chk.err(w, "record_type must be FACTOR, BASELINE, AIDCF_EOD or GAP_DISPOSITION")
            continue
        if r["incident_id"].startswith("INC-EXAMPLE-") and "FICTIONAL" not in r["notes"].upper():
            chk.err(w, "example rows must be marked FICTIONAL in notes")
        if not FACTOR_RE.match(r["factor_id"]):
            chk.err(w, "factor_id must be a consolidated CF-NN")
        if r["coding_round"] not in {"A", "B", "RECONCILED"}:
            chk.err(w, "coding_round must be A, B or RECONCILED")
        if not CODER_RE.match(r["coder_id"]):
            chk.err(w, "coder_id must be C01..C99")
        if r["independent_of_author"] not in {"Y", "N"}:
            chk.err(w, "independent_of_author must be Y or N")
        if rt in {"BASELINE", "AIDCF_EOD"} and r["prior_familiarity"] not in {"NONE", "GENERAL", "DETAILED"}:
            chk.err(w, "prior_familiarity must be NONE, GENERAL or DETAILED")
        if rt == "FACTOR":
            k = (r["incident_id"], r["factor_id"])
            if r["coding_round"] != "RECONCILED":
                chk.err(w, "FACTOR rows are the adjudicator's consolidated list (coding_round RECONCILED)")
            if k in factors:
                chk.err(w, "duplicate FACTOR row for %s %s" % k)
            factors[k] = r
            if r["factor_origin"] not in ORIGINS:
                chk.err(w, "factor_origin must be AIDCF, BASELINE, BOTH or ADJUDICATOR")
            if not r["factor_source"].strip():
                chk.err(w, "factor_source (coder IDs and dossier passages) is required")
            if r["knowability"] not in KNOWABILITY:
                chk.err(w, "knowability invalid")
            if r["coding_phase"] not in {"PRE_REVEAL", "POST_REVEAL"}:
                chk.err(w, "coding_phase must be PRE_REVEAL or POST_REVEAL")
            if r["eod_sampled"] not in {"Y", "N"}:
                chk.err(w, "eod_sampled must be Y or N")
            for col in ("baseline_id", "detection_judgement", "eod", "gap_disposition"):
                if r[col]:
                    chk.err(w, "%s must be empty on FACTOR rows" % col)
            c = consolidated.get(k)
            if c and (c["knowability"] != r["knowability"] or c["coding_phase"] != r["coding_phase"]):
                chk.err(w, "knowability and coding_phase must match the consolidated factor in coding-sheet.csv")
    # every consolidated AIDCF factor of an incident in the comparison is in the factor list
    compared = {r["incident_id"] for r in rows}
    for (inc, fid) in sorted(consolidated):
        if inc in compared and (inc, fid) not in factors:
            chk.err(sheet_path.name, "%s %s is consolidated in coding-sheet.csv but missing from the FACTOR list" % (inc, fid))
    sampled = {k for k, r in factors.items() if r["eod_sampled"] == "Y"}

    for i, r in enumerate(rows, start=2):
        w = "%s:%d" % (sheet_path.name, i)
        rt = r["record_type"]
        k = (r["incident_id"], r["factor_id"])
        if rt in {"BASELINE", "AIDCF_EOD", "GAP_DISPOSITION"} and k not in factors:
            chk.err(w, "%s %s is not in the consolidated FACTOR list" % k)
        if rt == "BASELINE":
            bid = r["baseline_id"]
            seen[(r["incident_id"], r["factor_id"], bid, r["coding_round"], r["coder_id"])] += 1
            if bid not in METHODS:
                chk.err(w, "baseline_id must be one of %s" % ", ".join(METHODS))
                continue
            if bid not in active:
                chk.err(w, "%s is NOT_EVALUATED in this run; it cannot be judged (and is never NOT_APPLICABLE by default)" % bid)
            if r["independent_of_author"] != "Y":
                chk.err(w, "baseline coders must be independent of the framework author")
            j = r["detection_judgement"]
            if j not in BASELINE_JUDGEMENTS:
                chk.err(w, "detection_judgement must be one of %s" % ", ".join(BASELINE_JUDGEMENTS))
                continue
            decl = spec.get(bid, {})
            if j in CITED and not r["baseline_criteria"].strip():
                chk.err(w, "%s requires baseline_criteria (clause or procedure step relied on)" % j)
            if j == "NOT_ADDRESSED" and (r["baseline_criteria"] or not r["notes"].strip()):
                chk.err(w, "NOT_ADDRESSED leaves baseline_criteria empty and states in notes what was searched")
            if j == "OUT_OF_SCOPE":
                if r["exclusion_id"] not in decl.get("exc", {}):
                    chk.err(w, "OUT_OF_SCOPE must cite an EXC-NN declared for %s in baselines.csv" % bid)
            elif r["exclusion_id"]:
                chk.err(w, "exclusion_id is used only with OUT_OF_SCOPE")
            if j == "NOT_APPLICABLE":
                if r["applicability_rule"] not in decl.get("app", {}):
                    chk.err(w, "NOT_APPLICABLE must cite an APP-NN declared for %s in baselines.csv" % bid)
            elif r["applicability_rule"]:
                chk.err(w, "applicability_rule is used only with NOT_APPLICABLE")
            if bid == "BL-ENG":
                if r["eng_discipline"] not in ENG_DISCIPLINES or not r["eng_technique"].strip():
                    chk.err(w, "BL-ENG rows record eng_discipline (POWER, COOLING, OTHER) and eng_technique")
            elif r["eng_discipline"] or r["eng_technique"]:
                chk.err(w, "eng_discipline and eng_technique are used only on BL-ENG rows")
            check_eod(w, r, k in sampled, chk)
        elif rt == "AIDCF_EOD":
            if r["baseline_id"] or r["detection_judgement"]:
                chk.err(w, "AIDCF_EOD rows carry only the AIDCF side's estimated operational detectability")
            if k not in sampled:
                chk.err(w, "AIDCF_EOD rows exist only for factors in the EOD sample")
            check_eod(w, r, True, chk)
        elif rt == "GAP_DISPOSITION":
            if r["coding_round"] != "RECONCILED" or r["baseline_id"] not in METHODS:
                chk.err(w, "GAP_DISPOSITION rows are RECONCILED and name the method of the class-c pair")
            d = r["gap_disposition"]
            if d not in DISPOSITIONS:
                chk.err(w, "gap_disposition must be one of %s" % ", ".join(sorted(DISPOSITIONS)))
            elif d == "DISPUTED":
                if not r["notes"].strip():
                    chk.err(w, "DISPUTED records both positions in notes")
            elif not r["disposition_citation"].strip():
                chk.err(w, "%s requires disposition_citation" % d)
            elif d == "ACTIONABLE_GAP" and not any(g in r["disposition_citation"] for g in ACTIONABLE_GAP_TYPES):
                chk.err(w, "ACTIONABLE_GAP cites the G1, G2 or G3 gap record")
    for key, n in seen.items():
        if n > 1:
            chk.err(sheet_path.name, "duplicate BASELINE row for %s" % " ".join(key))

    # EOD sample must be exactly the seeded draw from the locked frame
    if sampled:
        frame = eod_frame(factors.values())
        if locks.get("EOD_FRAME") != frame_digest(frame):
            chk.err(sheet_path.name, "eod_sampled is set but the EOD frame digest does not match the EOD_FRAME lock")
        elif "EOD_SEED" not in locks:
            chk.err(sheet_path.name, "eod_sampled is set but EOD_SEED is not locked")
        elif set(draw_eod_sample(frame, category_of, locks["EOD_SEED"])) != sampled:
            chk.err(sheet_path.name, "eod_sampled does not match the seeded draw from the locked frame")
    return rows, spec, locks


def check_eod(w, r, sampled, chk):
    v = r["eod"]
    if not sampled:
        if v or r["eod_assumptions"] or r["eod_confidence"]:
            chk.err(w, "EOD is coded only for factors in the EOD sample")
        return
    if not v:
        return  # sampled factor not yet estimated; completeness is enforced by --comparative
    if v not in EOD_VALUES:
        chk.err(w, "eod must be LIKELY, POSSIBLE, UNLIKELY or INDETERMINATE")
    elif v != "INDETERMINATE" and (not r["eod_assumptions"].strip() or r["eod_confidence"] not in EOD_CONFIDENCE):
        chk.err(w, "%s requires eod_assumptions and eod_confidence (LOW, MEDIUM, HIGH)" % v)
    elif v == "INDETERMINATE" and not r["eod_assumptions"].strip():
        chk.err(w, "INDETERMINATE states in eod_assumptions why no credible estimate is possible")


# ------------------------------------------------------------ analysis

def build_pairs(rows, spec, coding_rows):
    """Return the comparison data set: factors, AIDCF judgements and baseline judgements per method."""
    active = sorted(m for m in METHODS if spec.get(m, {}).get("pilot_status") == "ACTIVE")
    best, meta = aidcf_factor_judgements(coding_rows)
    factor_rows = {(r["incident_id"], r["factor_id"]): r for r in rows if r["record_type"] == "FACTOR"}
    base = defaultdict(dict)
    for r in rows:
        if r["record_type"] == "BASELINE" and r["coding_round"] == "RECONCILED":
            base[(r["incident_id"], r["factor_id"])][r["baseline_id"]] = r["detection_judgement"]
    disp = {(r["incident_id"], r["factor_id"], r["baseline_id"]): r for r in rows
            if r["record_type"] == "GAP_DISPOSITION"}
    return {"active": active, "best": best, "meta": meta, "factors": factor_rows, "base": base, "disp": disp}


def comparable(data):
    """Factors that enter the comparison: in the FACTOR list, knowable and identified before the reveal."""
    return sorted(k for k, r in data["factors"].items()
                  if r["knowability"] in KNOWABLE and r["coding_phase"] == "PRE_REVEAL")


def judgement_for(data, k, method):
    if method == "UNION":
        return {m: data["base"].get(k, {}).get(m) for m in data["active"]}
    return data["base"].get(k, {}).get(method)


def classify(data, k, method, reading):
    """Class of factor k for a method or 'UNION'. Returns (class, aidcf_value, baseline_value)."""
    a_j = data["best"].get(k)
    if a_j is None:
        return "MISSING_AIDCF", None, None
    a_v = side_value(a_j, reading, "AIDCF")
    if method == "UNION":
        js = judgement_for(data, k, "UNION")
        if any(v is None for v in js.values()):
            return "MISSING_BASELINE", a_v, None
        b_v = combine_union(js, reading)
    else:
        b_j = judgement_for(data, k, method)
        if b_j is None:
            return "MISSING_BASELINE", a_v, None
        b_v = side_value(b_j, reading, "BASELINE")
    return pair_class(a_v, b_v), a_v, b_v


def subset(data, keys, origin):
    if origin == "ALL":
        return keys
    want = {"AIDCF": {"AIDCF", "BOTH"}, "BASELINE": {"BASELINE", "BOTH"}}[origin]
    return [k for k in keys if data["factors"][k]["factor_origin"] in want]


def table(data, keys, method, reading):
    counts = Counter()
    subtypes = defaultdict(Counter)
    for k in keys:
        cls, _, _ = classify(data, k, method, reading)
        counts[cls] += 1
        if cls in {"b", "c", "d"}:
            a_j = data["best"][k]
            st_a = miss_subtype(a_j, reading)
            if method != "UNION":
                st_b = miss_subtype(judgement_for(data, k, method), reading)
            else:
                st_b = "UNION_MISS"
            if cls in {"c", "d"} and st_a:
                subtypes[cls]["AIDCF " + st_a] += 1
            if cls in {"b", "d"} and st_b:
                subtypes[cls]["baseline " + st_b] += 1
    return counts, subtypes


def net(counts):
    n = sum(counts.get(c, 0) for c in "abcd")
    return (None, 0) if n == 0 else ((counts.get("b", 0) - counts.get("c", 0)) / n, n)


def bootstrap(data, keys, method, reading, seed):
    by_inc = defaultdict(list)
    for k in keys:
        cls, _, _ = classify(data, k, method, reading)
        if cls in {"a", "b", "c", "d"}:
            by_inc[k[0]].append(cls)
    incidents = sorted(by_inc)
    if len(incidents) < MIN_INCIDENTS_FOR_INTERVAL:
        return None, len(incidents)
    rng = random.Random(int(seed))
    stats = []
    for _ in range(BOOTSTRAP_RESAMPLES):
        c = Counter()
        for _ in incidents:
            c.update(by_inc[rng.choice(incidents)])
        v, _ = net(c)
        stats.append(v)
    stats.sort()
    lo = stats[int(0.025 * BOOTSTRAP_RESAMPLES)]
    hi = stats[int(0.975 * BOOTSTRAP_RESAMPLES) - 1]
    return (lo, hi), len(incidents)


def indeterminacy(data, keys, method):
    """Share of comparable, applicable factors that are INSUFFICIENT_INFORMATION on each side."""
    n = xa = xb = 0
    for k in keys:
        cls, a_v, b_v = classify(data, k, method, "strict")
        if cls == "EXCLUDED_NOT_APPLICABLE" or cls.startswith("MISSING"):
            continue
        n += 1
        xa += a_v == "X"
        xb += b_v == "X"
    if n == 0:
        return None
    return xa / n, xb / n, n


def incident_level(data, keys, method, reading, threshold):
    """Incident classes on the common factor set (section 10A.5.4)."""
    by_inc = defaultdict(list)
    for k in keys:
        by_inc[k[0]].append(k)
    counts, excluded = Counter(), Counter()
    for inc in sorted(by_inc):
        classes = [classify(data, k, method, reading)[0] for k in by_inc[inc]]
        applicable = [c for c in classes if c != "EXCLUDED_NOT_APPLICABLE" and not c.startswith("MISSING")]
        indeterminate = [c for c in applicable if c.startswith("EXCLUDED_INDETERMINATE")]
        eligible = [c for c in applicable if c in {"a", "b", "c", "d"}]
        if not eligible:
            excluded["no eligible pair"] += 1
            continue
        if len(indeterminate) / len(applicable) > threshold:
            excluded["over %.0f%% indeterminate" % (threshold * 100)] += 1
            continue
        a_s = any(c in {"a", "b"} for c in eligible)
        b_s = any(c in {"a", "c"} for c in eligible)
        counts[{(True, True): "a", (True, False): "b", (False, True): "c", (False, False): "d"}[(a_s, b_s)]] += 1
    return counts, excluded


def fmt_table(counts):
    n = sum(counts[c] for c in "abcd")
    ex = {k: v for k, v in sorted(counts.items()) if k not in set("abcd")}
    return ("a shared %d | b AIDCF-only %d | c baseline-only %d | d neither %d | N %d | excluded %s" %
            (counts["a"], counts["b"], counts["c"], counts["d"], n, ex if ex else "{}"))


def comparative_report(rows, spec, locks, coding_rows, category_of, threshold=PRIMARY_THRESHOLD):
    """Full comparative report. Raises ValueError if the run is not in a reportable state."""
    data = build_pairs(rows, spec, coding_rows)
    active = data["active"]
    problems = []
    for m in active + ["AIDCF"]:
        if spec[m]["approval_status"] != "APPROVED":
            problems.append("%s is not APPROVED in baselines.csv" % m)
    if "BASELINES" not in locks:
        problems.append("baselines.csv is not locked (BASELINES in comparative-locks.csv)")
    keys = comparable(data)
    for k in keys:
        if k not in data["best"]:
            problems.append("%s %s has no RECONCILED AIDCF judgement" % k)
        for m in active:
            if judgement_for(data, k, m) is None:
                problems.append("%s %s has no RECONCILED %s judgement" % (k[0], k[1], m))
    for reading in ("strict", "inclusive"):
        for k in keys:
            for m in active:
                cls, _, _ = classify(data, k, m, reading)
                if cls == "c" and (k[0], k[1], m) not in data["disp"]:
                    problems.append("%s %s %s is baseline-only (%s) without a GAP_DISPOSITION row" % (k[0], k[1], m, reading))
    for (inc, fid, m) in sorted(data["disp"]):
        if not any(classify(data, (inc, fid), m, rd)[0] == "c" for rd in ("strict", "inclusive")):
            problems.append("GAP_DISPOSITION %s %s %s is not on a baseline-only pair" % (inc, fid, m))
    if problems:
        raise ValueError("\n".join(sorted(set(problems))))

    seed = locks.get("BOOTSTRAP_SEED")
    label = union_label(active)
    methods = active + ["UNION"]
    name = lambda m: label if m == "UNION" else m
    out = [
        "AIDCF-VAL-001 v1.1 comparative results (section 10A). EXPLORATORY.",
        "A paper-based retrospective comparison of written criteria. It does not show higher incident prevention,",
        "better predictive validity, lower operational risk, better cost-effectiveness, or better detection by real",
        "engineering teams.",
        union_note(active),
        "Methods evaluated: %s. Not evaluated: %s." % (", ".join(active) or "none",
                                                       ", ".join(m for m in METHODS if m not in active) or "none"),
        "baselines.csv locked digest: %s" % locks["BASELINES"],
    ]
    origins = Counter(data["factors"][k]["factor_origin"] for k in keys)
    out.append("Comparable factors (knowable, PRE_REVEAL, in the consolidated list): %d; by origin %s" %
               (len(keys), dict(sorted(origins.items()))))
    out.append("Factors in the list but not comparable: %d" % (len(data["factors"]) - len(keys)))
    reviewers = defaultdict(set)
    for r in rows:
        if r["record_type"] == "BASELINE" and r["coding_round"] in {"A", "B"} and r["independent_of_author"] == "Y":
            reviewers[r["baseline_id"]].add(r["coder_id"])
    for m in active:
        n_rev = len(reviewers[m])
        out.append("Independent reviewers for %s: %d%s" % (m, n_rev, "" if n_rev >= 2 else
                                                            " (below the target of 2: results for this method are exploratory)"))

    for origin in ("ALL", "AIDCF", "BASELINE"):
        ks = subset(data, keys, origin)
        out.append("")
        out.append("== Factor level, factors of origin %s (%d) ==" % (
            {"ALL": "ALL", "AIDCF": "AIDCF or BOTH", "BASELINE": "BASELINE or BOTH"}[origin], len(ks)))
        for m in methods:
            for reading in ("strict", "inclusive"):
                counts, subtypes = table(data, ks, m, reading)
                v, n = net(counts)
                line = "%-9s %-9s %s" % (name(m), reading, fmt_table(counts))
                if v is None:
                    line += " | no eligible pairs: no metric"
                else:
                    line += " | net incremental %+.3f" % v
                    if origin == "ALL":
                        if seed is None:
                            line += " (no interval: BOOTSTRAP_SEED not locked)"
                        else:
                            ci, n_inc = bootstrap(data, ks, m, reading, seed)
                            line += (" (no interval: %d eligible incidents < %d)" % (n_inc, MIN_INCIDENTS_FOR_INTERVAL)
                                     if ci is None else " (95%% incident-cluster bootstrap %+.3f to %+.3f)" % ci)
                out.append(line)
                for cls in "bcd":
                    if subtypes[cls]:
                        out.append("            %s miss subtypes: %s" % (cls, dict(sorted(subtypes[cls].items()))))
        if origin == "ALL":
            out.append("Differential indeterminacy (INSUFFICIENT_INFORMATION share, comparable applicable factors):")
            for m in methods:
                ind = indeterminacy(data, ks, m)
                if ind is None:
                    out.append("  %-9s no applicable factors" % name(m))
                    continue
                xa, xb, n = ind
                flag = " FLAG: differs by more than %.0f points" % (DIFFERENTIAL_FLAG * 100) if abs(xa - xb) > DIFFERENTIAL_FLAG else ""
                out.append("  %-9s AIDCF %.2f, baseline %.2f, n %d%s" % (name(m), xa, xb, n, flag))

    out.append("")
    out.append("== Incident level (common factor set; primary threshold %.0f%%) ==" % (threshold * 100))
    for m in methods:
        for reading in ("strict", "inclusive"):
            counts, excluded = incident_level(data, keys, m, reading, threshold)
            out.append("%-9s %-9s %s | incidents excluded %s" % (name(m), reading, fmt_table(counts),
                                                                 dict(sorted(excluded.items())) or "{}"))
    out.append("Sensitivity to the incident-exclusion threshold (strict):")
    for m in methods:
        parts = []
        for t in SENSITIVITY_THRESHOLDS:
            counts, _ = incident_level(data, keys, m, "strict", t)
            v, n = net(counts)
            parts.append("%s: N %d net %s" % ("none" if t >= 1 else "%.0f%%" % (t * 100), n, "n/a" if v is None else "%+.3f" % v))
        out.append("  %-9s %s" % (name(m), "; ".join(parts)))
    strata = defaultdict(set)
    for k in keys:
        strata[category_of(k[0])].add(k[0])
    small = sorted(s for s, incs in strata.items() if len(incs) < MIN_INCIDENTS_FOR_STRATUM)
    if small:
        out.append("Strata with fewer than %d incidents (descriptive only): %s" % (MIN_INCIDENTS_FOR_STRATUM, ", ".join(small)))

    out.append("")
    out.append("== Baseline-only results (comparative disadvantages for AIDCF) ==")
    listed = 0
    for k in keys:
        for m in active:
            classes = [rd for rd in ("strict", "inclusive") if classify(data, k, m, rd)[0] == "c"]
            if classes:
                d = data["disp"][(k[0], k[1], m)]
                out.append("  %s %s %s (%s): AIDCF %s, %s %s; disposition %s %s" % (
                    k[0], k[1], m, "/".join(classes), data["best"][k], m, judgement_for(data, k, m),
                    d["gap_disposition"], d["disposition_citation"] or "(see notes)"))
                listed += 1
    if not listed:
        out.append("  none")
    disp_counts = Counter(r["gap_disposition"] for r in data["disp"].values())
    out.append("Gap dispositions: %s" % (dict(sorted(disp_counts.items())) or "{}"))

    out.append("")
    out.append("== Estimated operational detectability (expert estimate, not observed performance) ==")
    eod_a = {(r["incident_id"], r["factor_id"]): r["eod"] for r in rows
             if r["record_type"] == "AIDCF_EOD" and r["coding_round"] == "RECONCILED"}
    sampled = [k for k in keys if data["factors"][k]["eod_sampled"] == "Y"]
    out.append("Sampled factors: %d of %d comparable" % (len(sampled), len(keys)))
    for m in active:
        eod_b = {(r["incident_id"], r["factor_id"]): r["eod"] for r in rows
                 if r["record_type"] == "BASELINE" and r["coding_round"] == "RECONCILED" and r["baseline_id"] == m}
        applicable = [k for k in sampled if judgement_for(data, k, m) != "NOT_APPLICABLE"]
        cross = Counter((eod_a.get(k) or "MISSING", eod_b.get(k) or "MISSING") for k in applicable)
        out.append("  %-9s (AIDCF, %s) counts: %s" % (m, m, dict(sorted(cross.items())) or "{}"))
    return out
