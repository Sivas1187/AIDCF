#!/usr/bin/env python3
"""Build the AIDCF-014 section 17 registry catalogue (TDS-REQ-057).

Writes, into registries/catalogue/, every section 17 registry that is not already
published elsewhere in registries/, each with the common columns
    code, label, definition, semanticOwner, version, status, replacedBy
followed by its registry-specific columns, plus registry-index.csv, which lists
all section 17 registries (including those owned by other tools) and reports
whether each carries the common and registry-specific columns.

Content is derived only from authoritative repository sources:
  - schemas/tools/aidcf_model.py (classes, relationships, vocabularies, schema files)
  - registries/**/*.csv (existing registries and controlled vocabularies)
  - AIDCF-002 Part IX (artifact identifier register and legacy identifiers)
  - README.md artifact catalogue
  - AIDCF-008 (quality anchors, UNKNOWN grading), AIDCF-009 (method safety rules),
    AIDCF-010 (finding effects, decision derivation), AIDCF-012 (report classes,
    finding classification), AIDCF-013 (reference patterns), AIDCF-014 (legacy
    relationship names), AIDCF-016 (MDM 1.3 migration)
  - crosswalks/*/*-mapping.csv (AIDCF-019)

A value that no source defines is left empty. The script never edits files
outside registries/catalogue/.

Usage:
    python3 registries/tools/build_catalogue.py           # write files
    python3 registries/tools/build_catalogue.py --check   # exit 1 if any file would change

Standard library only. Output is UTF-8, LF line endings, RFC 4180 quoting,
rows sorted by code (natural order). Multi-valued cells use "|".
"""
import csv
import io
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "registries" / "catalogue"
VOC = REPO / "registries" / "vocabularies"
sys.path.insert(0, str(REPO / "schemas" / "tools"))
import aidcf_model as M  # noqa: E402

COMMON = ["code", "label", "definition", "semanticOwner", "version", "status", "replacedBy"]
# Catalogue rows are generated for the MDM release the model declares; none is approved yet,
# so every row carries record-lifecycle status CANDIDATE (AIDCF-014 section 11A.1).
VERSION = M.RELEASE
STATUS = "CANDIDATE"

DOC = {
    "002": "foundations/conceptual-model/AIDCF-002_Core_Conceptual_Model_v1.0.md",
    "008": "standards/aidcf-008-evidence-model/AIDCF-008_Evidence_Model_v1.1.md",
    "009A": "standards/aidcf-009-assessment-methodology/AIDCF-009_Part_A_Core_Practitioner_Handbook_v1.1.md",
    "010": "standards/aidcf-010-scoring-framework/AIDCF-010_Scoring_and_Decision_Framework_v1.1.md",
    "012": "standards/aidcf-012-reporting-standard/AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.1.md",
    "013": "standards/aidcf-013-reference-architecture/AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.1.md",
    "014": "standards/aidcf-014-traceability-standard/AIDCF-014_End-to-End_Traceability_and_Machine-Executable_Data_Standard_v1.1.md",
}

# AIDCF-014 section 17: registry file -> (registry-specific columns, owner, published location or None)
# None means the catalogue generates the file; otherwise it is owned by another tool and only indexed.
S17 = [
    ("artifacts.csv", ["publicId", "shortCode", "title", "path", "artifactVersion", "artifactStatus"], "AIDCF-014", None),
    ("object-types.csv", ["chainStep", "ownerArtifact", "schemaRef"], "AIDCF-014", None),
    ("relationship-types.csv", ["domain", "range", "cardinalityOut", "cardinalityIn", "inverse", "symmetric", "qualifiers"], "AIDCF-014", None),
    ("vocabularies/*.csv", ["vocabulary", "sortOrder", "legacyAliases"], "Per AIDCF-014 section 11A", "registries/vocabularies"),
    ("domains.csv", ["familyCount", "controlCount"], "AIDCF-007A", "registries/domains/domains.csv"),
    ("control-families.csv", ["domainCode", "familyNumber", "controlRange"], "AIDCF-007A", "registries/families/control-families.csv"),
    ("controls.csv", ["familyId", "claimType", "requiredAssuranceLevel", "controlType", "gateMappings", "amendmentRef"], "AIDCF-007A", "registries/controls/controls.csv"),
    ("critical-gates.csv", ["name", "scope", "evidenceFloor", "criticalControlCount"], "AIDCF-010", "registries/gates/critical-gates.csv"),
    ("evidence-classes.csv", ["classCode", "examples"], "AIDCF-008", None),
    ("evidence-quality.csv", ["dimension", "level", "criterion"], "AIDCF-008", None),
    ("assessment-methods.csv", ["methodCode", "typicalEvidenceClasses", "safetyConstraint"], "AIDCF-009", None),
    ("finding-classes.csv", ["severity", "gateEffect"], "AIDCF-009", None),
    ("unknown-types.csv", ["typeCode", "defaultSeverityTest"], "AIDCF-008", None),
    ("unknown-severity.csv", ["severityCode", "test", "decisionEffect"], "AIDCF-010", None),
    ("decision-states.csv", ["rank", "ceilingRule"], "AIDCF-010", None),
    ("report-types.csv", ["audience", "mandatorySections"], "AIDCF-012", None),
    ("architecture-patterns.csv", ["patternCode", "mandatoryViews", "typicalGates"], "AIDCF-013", None),
    ("external-mappings.csv", ["externalScheme", "externalCode", "aidcfCode", "mappingType", "crosswalkRef"], "AIDCF-019", None),
    ("deprecated-terms.csv", ["deprecatedTerm", "canonicalTerm", "directionChange", "effectiveRelease"], "AIDCF-014", None),
    ("migration-rules.csv", ["sourceVersion", "targetVersion", "rule", "condition", "fallback"], "AIDCF-014", None),
]
S17_BY_FILE = {r[0]: r for r in S17}
# Columns kept beyond section 17 because the source carries them and dropping them would lose meaning.
EXTRA = {"external-mappings.csv": ["confidence"]}


# --------------------------------------------------------------------------- helpers
def read_text(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def csv_header(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return next(csv.reader(f), [])


def clean(s):
    s = re.sub(r"\*\*|`", "", s or "")
    return re.sub(r"\s+", " ", s).strip()


def md_table_after(text, heading_regex, nth=0):
    """Rows (header and separator excluded) of the nth table between the heading and the next heading."""
    m = re.search(heading_regex, text, re.M)
    if not m:
        raise ValueError("heading not found: %s" % heading_regex)
    tables, cur = [], []
    for ln in text[m.end():].split("\n")[1:]:
        if ln.startswith("#"):
            break
        if ln.strip().startswith("|"):
            cur.append(ln)
        elif cur:
            tables.append(cur)
            cur = []
    if cur:
        tables.append(cur)
    if len(tables) <= nth:
        raise ValueError("table %d not found after %s" % (nth, heading_regex))
    return [[clean(c) for c in ln.strip().strip("|").split("|")] for ln in tables[nth][2:]]


def natkey(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def slug(s):
    return re.sub(r"[^A-Z0-9]+", "_", s.upper()).strip("_")


def multi(items):
    return "|".join(i for i in items if i)


def row(code, label="", definition="", owner="", replaced="", status=STATUS, **specific):
    r = dict(code=code, label=label, definition=definition, semanticOwner=owner, version=VERSION,
             status=status, replacedBy=replaced)
    r.update(specific)
    return r


def render(fname, rows):
    cols = COMMON + S17_BY_FILE[fname][1] + EXTRA.get(fname, [])
    codes = [r["code"] for r in rows]
    dup = sorted({c for c in codes if codes.count(c) > 1})
    if dup:
        raise ValueError("%s: duplicate codes %s" % (fname, dup))
    rows = sorted(rows, key=lambda r: natkey(r["code"]))
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n", extrasaction="raise")
    w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in cols})
    return buf.getvalue()


# --------------------------------------------------------------------------- registries
def artifacts():
    owner = S17_BY_FILE["artifacts.csv"][2]
    reg = {}
    for c in md_table_after(read_text(DOC["002"]), r"^## 40\. Artifact identifier register"):
        reg[c[0]] = dict(title=c[1], short=c[2], loc=c[3])
    readme = read_text("README.md")
    entries = []
    for c in md_table_after(readme, r"^## Artifact catalogue"):
        m = re.match(r"\[(.+?)\]\((.+?)\)", c[0])
        if not m:
            continue
        text, link = m.group(1), m.group(2)
        pid = re.match(r"(AIDCF-[A-Z0-9-]+?)(?=\s|$)", text).group(1)
        base = slug(re.sub(r"\bv\d+(\.\d+)*", "", text[len(pid):]))
        entries.append(dict(text=text, link=link, pid=pid, base=base, purpose=c[1], status=c[2]))
    counts = {}
    for e in entries:
        counts[e["pid"]] = counts.get(e["pid"], 0) + 1
    rows, missing = [], []
    for e in entries:
        p = REPO / e["link"]
        if p.is_dir():
            p = p / "README.md"
        if not p.is_file():
            # README link not (yet) present: take the highest-version file of the same stem in that folder.
            stem = re.sub(r"_v\d+(\.\d+)*", "_v*", p.name)
            cands = sorted(p.parent.glob(stem), key=lambda x: natkey(x.name))
            if not cands:
                missing.append(e["link"])
                continue
            p = cands[-1]
        rel = p.relative_to(REPO).as_posix()
        # Version from the file name, else from the containing folder (for example aidcf-015-v1.3/README.md).
        vm = re.search(r"_v(\d+(?:\.\d+)*)", p.name) or re.search(r"-v(\d+(?:\.\d+)*)$", p.parent.name)
        base = slug(re.sub(r"\bv\d+(\.\d+)*", "", e["text"][len(e["pid"]):]))
        code = e["pid"]
        if counts[e["pid"]] > 1:
            code = "%s/%s" % (e["pid"], base)
            if sum(1 for x in entries if x["pid"] == e["pid"] and x["base"] == base) > 1 and vm:
                code += "-V" + vm.group(1)
        meta = reg.get(e["pid"], {})
        rows.append(row(code, e["text"], e["purpose"], owner, publicId=e["pid"], shortCode=meta.get("short", ""),
                        title=meta.get("title", ""), path=rel, artifactVersion=vm.group(1) if vm else "",
                        artifactStatus=e["status"]))
    # AIDCF-018 domain guides: one artifact per guide file.
    for p in sorted((REPO / "standards/aidcf-018-domain-guides").glob("AIDCF-018-*_v*.md")):
        txt = p.read_text(encoding="utf-8")
        pid = re.match(r"(AIDCF-018-[A-Z]{3})", p.name).group(1)
        h1 = re.search(r"^# (.+)$", txt, re.M).group(1)
        title = clean(h1[len(pid):]) if h1.startswith(pid) else clean(h1)
        st = re.search(r"^\|\s*Status\s*\|\s*(.+?)\s*\|", txt, re.M)
        vm = re.search(r"_v(\d+(?:\.\d+)*)", p.name)
        rows.append(row(pid, "%s %s" % (pid, title), "", owner, publicId=pid, shortCode=reg.get("AIDCF-018", {}).get("short", ""),
                        title=title, path=p.relative_to(REPO).as_posix(), artifactVersion=vm.group(1) if vm else "",
                        artifactStatus=st.group(1) if st else ""))
    for r in rows:
        assert (REPO / r["path"]).is_file(), r["path"]
    return rows, missing


def object_types():
    rows = []
    sdir = REPO / "schemas" / "json-schema"
    for name, meta in M.CLASS_META.items():
        if meta["group"] not in ("canonical", "reference"):
            continue  # supporting classes are pending AIDCF-014 registration; auxiliary is structural only
        sf = M.schema_file(name)
        ref = "schemas/json-schema/" + sf if (sdir / sf).is_file() else ""
        rows.append(row(name, meta["label"], meta["definition"], meta["owner"],
                        chainStep=meta.get("chain", ""), ownerArtifact=meta["owner"], schemaRef=ref))
    return rows


def _card(t):
    return "%d..%s" % (t[0], "*" if t[1] is None else t[1])


def relationship_types():
    owner = S17_BY_FILE["relationship-types.csv"][2]
    rows = []
    for code, prop, definition, dom, rng, card, inv, extra in M.REL:
        out = _card(card["out"])
        if card.get("outBy"):
            out += " (" + "; ".join("%s %s to %s" % (k, _card(v[:2]), v[2]) for k, v in sorted(card["outBy"].items())) + ")"
        inn = _card(card["inn"])
        if card.get("inBy"):
            inn += " (" + "; ".join("%s %s from %s" % (k, _card(v[:2]), v[2]) for k, v in sorted(card["inBy"].items())) + ")"
        quals = list(extra.get("qualifiers", []))
        for src, qs in sorted(extra.get("qualifiers_for", {}).items()):
            quals += ["%s (source %s)" % (q, src) for q in qs]
        rows.append(row(code, code.replace("_", " ").capitalize(), definition, owner,
                        domain=multi(dom) if dom else "AidcfRecord", range=multi(rng) if rng else "AidcfRecord",
                        cardinalityOut=out, cardinalityIn=inn, inverse=inv or "",
                        symmetric="true" if extra.get("symmetric") else "false", qualifiers=multi(quals)))
    return rows


def evidence_classes():
    owner = S17_BY_FILE["evidence-classes.csv"][2]
    return [row(r["code"], r["name"], r["primaryClaimSupported"], owner, classCode=r["code"],
                examples=multi(x.strip() for x in r["representativeSubtypes"].split(";")))
            for r in read_csv(VOC / "evidence-classes.csv")]


def evidence_quality():
    owner = S17_BY_FILE["evidence-quality.csv"][2]
    text = read_text(DOC["008"])
    dims = {r["code"]: r["name"] for r in read_csv(VOC / "quality-dimensions.csv")}
    matrix = md_table_after(text, r"^# Appendix B - Quality rating matrix")
    order = ["P", "F", "C", "R", "T", "I"]
    compact = {}
    for cells in matrix:
        for i, d in enumerate(order):
            compact[(d, cells[0])] = cells[i + 1]
    rows = []
    for d in order:
        for cells in md_table_after(text, r"^### %s rating anchors" % d):
            lvl = cells[0][len(d):]
            rows.append(row(cells[0], "%s %s" % (dims[d], lvl), cells[1], owner, dimension=d, level=lvl,
                            criterion=compact.get((d, lvl), "")))
    return rows


def assessment_methods():
    owner = S17_BY_FILE["assessment-methods.csv"][2]
    text = read_text(DOC["009A"])
    # Safety requirements of AIDCF-009 Part A that constrain how a method is executed (B10 and B13),
    # attached to the methods named in the heading of the section that states them.
    safety_ids = ["AMH-REQ-026", "AMH-REQ-029"]
    safety = {}
    for sec in re.finditer(r"^## (B\d+) [^\n(]*\(([A-Z_, ]+)\)\n(.*?)(?=^## |^# )", text, re.M | re.S):
        for rid in safety_ids:
            m = re.search(r"\*\*%s\*\*\s*(.+)" % rid, sec.group(3))
            if m:
                for meth in [x.strip() for x in sec.group(2).split(",")]:
                    safety.setdefault(meth, []).append("%s: %s" % (rid, clean(m.group(1))))
    return [row(r["code"], r["code"].replace("_", " ").capitalize(), r["meaning"], owner, methodCode=r["code"],
                typicalEvidenceClasses="", safetyConstraint=" ".join(safety.get(r["code"], [])))
            for r in read_csv(VOC / "assessment-methods.csv")]


def finding_classes():
    owner = S17_BY_FILE["finding-classes.csv"][2]
    meaning = {c[0].lower(): c[1] for c in md_table_after(read_text(DOC["012"]), r"^## IX\.1 Finding classification")}
    effect = {c[0].lower(): c[1] for c in md_table_after(read_text(DOC["010"]), r"^# Part X - Findings and scenarios")}
    rows = []
    for code, label, _ in M.VOCABS["FindingClass"][2]:
        k = label.lower()
        dk = next(x for x in meaning if x == k or x.startswith(k))
        rows.append(row(code, label if dk == k else dk.capitalize(), meaning[dk], owner,
                        severity="", gateEffect=effect.get(k, "")))
    return rows


def unknown_types():
    owner = S17_BY_FILE["unknown-types.csv"][2]
    grading = {}
    for cells in md_table_after(read_text(DOC["008"]), r"^## 35A\. UNKNOWN severity", nth=1):
        grading[cells[0].split()[0]] = cells[1]
    return [row(r["code"], r["name"], r["definition"], owner, typeCode=r["code"],
                defaultSeverityTest=grading.get(r["code"], "")) for r in read_csv(VOC / "unknown-types.csv")]


def unknown_severity():
    owner = S17_BY_FILE["unknown-severity.csv"][2]
    return [row(r["code"], r["name"], r["test"], owner, severityCode=r["code"], test=r["test"],
                decisionEffect=r["decisionEffect"]) for r in read_csv(VOC / "unknown-severity.csv")]


def decision_states():
    owner = S17_BY_FILE["decision-states.csv"][2]
    text = read_text(DOC["010"])
    order = [x.strip() for x in re.search(r"^ORDER = \[(.+?)\]", text, re.M).group(1).split(",")]
    rules = {s: [] for s in order}
    for cells in md_table_after(text, r"^## Derivation order"):
        step = cells[0]
        for clause in re.split(r"; |\. (?=[A-Z<])", cells[2]):
            for s in re.findall(r"≤ ([A-Z_]+)", clause):
                if s in rules:
                    rules[s].append("Step %s: %s" % (step, clause.strip().rstrip(".")))
    gates = read_csv(REPO / "registries/gates/critical-gates.csv")
    for s in order:
        parts = []
        for kind, col in (("FAIL", "failCeiling"), ("UNKNOWN", "unknownCeiling")):
            ids = [g["gateId"] for g in gates if M.derive_ceiling(g[col])[0] == s]
            if ids:
                parts.append("%s ceiling of %s" % (kind, ", ".join(ids)))
        if parts:
            rules[s].insert(0, "Step 1 Gates: %s (registries/gates/critical-gates.csv, derived per AIDCF-016 section 9.4)" % "; ".join(parts))
    rows = []
    for r in read_csv(VOC / "decision-states.csv"):
        rr = rules.get(r["code"], [])
        if r["code"] == order[-1] and not rr:
            rr = ["No ceiling: starting state of the AIDCF-010 Part XII derivation"]
        rows.append(row(r["code"], r["code"].replace("_", " ").capitalize(), r["meaning"], owner,
                        rank=str(order.index(r["code"]) + 1), ceilingRule=" | ".join(rr)))
    return rows


def report_types():
    owner = S17_BY_FILE["report-types.csv"][2]
    text = read_text(DOC["012"])
    rows = []
    for cells in md_table_after(text, r"^# Part III — Report classes"):
        code, title, audience = cells[0], cells[1], cells[2]
        secs = md_table_after(text, r"^## %s %s$" % (re.escape(code), re.escape(title)))
        rows.append(row(code, title, "", owner, audience=audience, mandatorySections=multi(s[1] for s in secs)))
    return rows


def architecture_patterns():
    owner = S17_BY_FILE["architecture-patterns.csv"][2]
    rows = []
    for cells in md_table_after(read_text(DOC["013"]), r"^# Reference patterns"):
        rows.append(row(slug(cells[0]), cells[0], cells[1], owner, patternCode="",
                        mandatoryViews=multi(x.strip() for x in cells[2].split(",")),
                        typicalGates=multi(x.strip() for x in cells[3].split(","))))
    return rows


def external_mappings():
    owner = S17_BY_FILE["external-mappings.csv"][2]
    rows = []
    for p in sorted((REPO / "crosswalks").glob("*/*-mapping.csv")):
        scheme = p.parent.name
        for r in read_csv(p):
            rows.append(row("%s:%s" % (scheme, r["aidcfFamilyId"]), r["externalTitle"], r["notes"], owner,
                            externalScheme=scheme, externalCode=r["externalRef"], aidcfCode=r["aidcfFamilyId"],
                            mappingType=r["relationship"], crosswalkRef=p.relative_to(REPO).as_posix(),
                            confidence=r["confidence"]))
    return rows


def deprecated_terms():
    owner = S17_BY_FILE["deprecated-terms.csv"][2]
    rows = []

    def add(scheme, term, canon, direction="", note=""):
        rows.append(row("%s:%s" % (scheme, term), term, note, owner, replaced=canon,
                        status="SUPERSEDED" if canon else "RETIRED",
                        deprecatedTerm=term, canonicalTerm=canon, directionChange=direction, effectiveRelease=""))

    for r in read_csv(VOC / "control-result-aliases.csv"):
        add("controlResult", r["legacyCode"], r["canonicalCode"], note=r["condition"])
    for r in read_csv(VOC / "decision-aliases.csv"):
        # Every legacy code here was used as a decision state; field says where it now maps.
        note = "; ".join(x for x in ("maps to %s" % r["field"] if r["field"] != "none" else "", r["note"]) if x)
        add("decisionState", r["legacyCode"], r["canonicalCode"], note=note)
    rel_csv = {r["legacyType"]: r for r in read_csv(VOC / "relationship-aliases.csv")}
    for cells in md_table_after(read_text(DOC["014"]), r"^## 9\.1 Legacy relationship aliases"):
        # AIDCF-014 section 9.1 (owner of this registry) gives the direction change for all nine names.
        legacy, canon, direction = cells[0], cells[1], cells[2]
        add("relationshipType", legacy, canon, direction, note=rel_csv.get(legacy, {}).get("note", ""))
    for r in read_csv(VOC / "assurance-levels.csv"):
        if r["legacyAlias"]:
            add("assuranceLevel", r["legacyAlias"], r["code"])
    for r in read_csv(VOC / "evidence-quality-bands.csv"):
        if r["legacyEvidenceGrade"]:
            add("evidenceGrade", r["legacyEvidenceGrade"], r["code"])
    for r in read_csv(VOC / "evidence-system-conformance-levels.csv"):
        if r["legacyCode"]:
            add("evidenceSystemConformance", r["legacyCode"], r["code"])
    for r in read_csv(VOC / "lifecycle-stages.csv"):
        for legacy in filter(None, (x.strip() for x in r["legacyStages"].split("|"))):
            add("lifecycleStage", legacy, r["code"])
    for cells in md_table_after(read_text(DOC["002"]), r"^## 41\. Legacy identifiers"):
        for legacy in (x.strip() for x in cells[0].split(";")):
            if re.fullmatch(r"AIDCF-[A-Z]+-\d{3}", legacy):
                add("artifactId", legacy, cells[1])
    return rows


def migration_rules():
    owner = S17_BY_FILE["migration-rules.csv"][2]
    fb = "No defined mapping: the value becomes UNKNOWN with a migration reason (TDS-REQ-075)"
    alias = "The original value is kept in provenance.legacyValue and a MigrationRecord is produced (TDS-REQ-044)"
    spec = [
        ("MR-ALIAS-CONTROL-RESULT", "Legacy control results",
         "Replace each legacy control-result code with the canonicalCode of its row in registries/vocabularies/control-result-aliases.csv. " + alias,
         "Apply the condition column of the matching alias row", "", VERSION),
        ("MR-ALIAS-DECISION", "Legacy decision codes",
         "Replace each legacy decision code using registries/vocabularies/decision-aliases.csv; the field column states whether it maps to decisionState or decisionLifecycle. " + alias,
         "A legacy NOT ASSESSED decision maps to no decision state: no decision is issued", "", VERSION),
        ("MR-ALIAS-RELATIONSHIP", "Legacy relationship names",
         "Replace each legacy relationship name with its canonical type (AIDCF-014 section 9.1; registries/vocabularies/relationship-aliases.csv), reversing source and target where the direction rule says so (TDS-REQ-040). " + alias,
         "Direction change as stated for the alias", "", VERSION),
        ("MR-ALIAS-ASSURANCE-LEVEL", "Legacy assurance levels",
         "Map legacy A2 to A5 one-to-one to AL2 to AL5 (registries/vocabularies/assurance-levels.csv legacyAlias). " + alias,
         "", "", VERSION),
        ("MR-ALIAS-EVIDENCE-GRADE", "Legacy evidence grades",
         "Map the AIDCF-005/AIDCF-006 evidence grade E0 to E5 to quality band Q0 to Q5 (AIDCF-008 section 19; registries/vocabularies/evidence-quality-bands.csv). " + alias,
         "Only where the legacy code denotes an evidence grade; E1 to E7 evidence classes are unchanged (CCM-REQ-031)", "", VERSION),
        ("MR-ALIAS-EVIDENCE-CONFORMANCE", "Legacy evidence-system conformance levels",
         "Map evidence-system conformance E0 to E5 (former AIDCF-008 section 4) to EC0 to EC5 (registries/vocabularies/evidence-system-conformance-levels.csv). " + alias,
         "Only where the legacy code denotes an evidence-system conformance level (CCM-REQ-031)", "", VERSION),
        ("MR-ALIAS-LIFECYCLE-STAGE", "Legacy lifecycle stages",
         "Map AIDCF-003 lifecycle stages to the canonical stage named in registries/vocabularies/lifecycle-stages.csv legacyStages. " + alias,
         "", "", VERSION),
        ("MR-ALIAS-ARTIFACT-ID", "Legacy artifact identifiers",
         "Replace legacy artifact identifiers with the public ID given in AIDCF-002 section 41.",
         "\"AIDCF-016\" is rewritten to AIDCF-VR-001 only where it denotes the Full-Stack Validation Report (AIDCF-002 section 41)", "", ""),
        ("MR-MDM13-IDENTIFIER", "AIDCF-015 v1.2 synthetic identifiers",
         "Synthetic records move to the urn:aidcf:syn: namespace; the predecessor identifier is kept only as the target of MIGRATED_FROM with the MigrationRecord as migrationRef (AIDCF-016 section 14, MDM-REQ-008, MDM-REQ-053).",
         "", "AIDCF-015 v1.2", "MDM 1.3"),
        ("MR-MDM13-EVIDENCE-CLASS", "AIDCF-015 v1.2 evidence-class words",
         "Evidence-class words (CONFIGURATION, OPERATIONAL, VALIDATION, DOCUMENTARY) become E-codes, with the original kept in provenance.legacyValue (AIDCF-016 section 14).",
         "", "AIDCF-015 v1.2", "MDM 1.3"),
        ("MR-MDM13-RESULT-REINTERPRETATION", "Recomputed results",
         "Every Gate Result is recomputed under the canonical roll-up (AIDCF-016 section 9.2) with registry roles; each change is a RESULT_REINTERPRETATION mapping that states the rule applied, and the previous value is not overwritten in the previous release (MDM-REQ-053).",
         "A result whose evidence is below the profile floor becomes UNKNOWN", "AIDCF-015 v1.2", "MDM 1.3"),
        ("MR-MDM-DEPRECATION", "Deprecation instead of deletion",
         "A new schema set does not delete a class, property or code used by the previous set; it deprecates it (owl:deprecated true with a pointer to its replacement) and publishes a MigrationRecord with fromId, toId, changeType and rationale (MDM-REQ-052; TDS-REQ-054).",
         "", "", ""),
    ]
    return [row(code, label, "", owner, rule=rule, condition=cond, fallback=fb, sourceVersion=src, targetVersion=tgt)
            for code, label, rule, cond, src, tgt in spec]


BUILDERS = {
    "object-types.csv": object_types,
    "relationship-types.csv": relationship_types,
    "evidence-classes.csv": evidence_classes,
    "evidence-quality.csv": evidence_quality,
    "assessment-methods.csv": assessment_methods,
    "finding-classes.csv": finding_classes,
    "unknown-types.csv": unknown_types,
    "unknown-severity.csv": unknown_severity,
    "decision-states.csv": decision_states,
    "report-types.csv": report_types,
    "architecture-patterns.csv": architecture_patterns,
    "external-mappings.csv": external_mappings,
    "deprecated-terms.csv": deprecated_terms,
    "migration-rules.csv": migration_rules,
}

SOURCES = {
    "artifacts.csv": "README.md (artifact catalogue); AIDCF-002 section 40; standards/aidcf-018-domain-guides/",
    "object-types.csv": "schemas/tools/aidcf_model.py (CLASSES, REFERENCE_CLASSES, schema_file); AIDCF-014 section 7",
    "relationship-types.csv": "schemas/tools/aidcf_model.py (REL); AIDCF-014 section 9",
    "vocabularies/*.csv": "AIDCF-002 Part VI",
    "domains.csv": "AIDCF-007A Canonical Master Control Registry v1.1 workbook",
    "control-families.csv": "AIDCF-007A Canonical Master Control Registry v1.1 workbook",
    "controls.csv": "AIDCF-007A Canonical Master Control Registry v1.1 workbook",
    "critical-gates.csv": "AIDCF-010 Part VIII; AIDCF-002 section 35.1",
    "evidence-classes.csv": "registries/vocabularies/evidence-classes.csv (AIDCF-008 Part IV)",
    "evidence-quality.csv": "AIDCF-008 section 17 and Appendix B; registries/vocabularies/quality-dimensions.csv",
    "assessment-methods.csv": "registries/vocabularies/assessment-methods.csv; AIDCF-009 Part A B10 and B13",
    "finding-classes.csv": "schemas/tools/aidcf_model.py (FindingClass); AIDCF-012 Part IX.1; AIDCF-010 Part X",
    "unknown-types.csv": "registries/vocabularies/unknown-types.csv; AIDCF-008 section 35A",
    "unknown-severity.csv": "registries/vocabularies/unknown-severity.csv (AIDCF-010 Part IX)",
    "decision-states.csv": "registries/vocabularies/decision-states.csv; AIDCF-010 Part XII; registries/gates/critical-gates.csv",
    "report-types.csv": "AIDCF-012 Part III and report templates",
    "architecture-patterns.csv": "AIDCF-013 Reference patterns",
    "external-mappings.csv": "crosswalks/*/*-mapping.csv (AIDCF-019)",
    "deprecated-terms.csv": "registries/vocabularies/*-aliases.csv and legacy columns; AIDCF-014 section 9.1; AIDCF-002 section 41",
    "migration-rules.csv": "AIDCF-014 sections 11A and 27; registries/vocabularies/*-aliases.csv; AIDCF-016 section 14",
}


def conformance(fname, path):
    """Return (rowCount, missing columns) for a published registry file or folder."""
    required = COMMON + S17_BY_FILE[fname][1]
    p = REPO / path
    if p.is_dir():
        files = sorted(p.glob("*.csv"))
        missing = []
        for col in required:
            lacking = [f for f in files if col not in csv_header(f)]
            if lacking:
                missing.append(col if len(lacking) == len(files) else "%s (%d of %d files)" % (col, len(lacking), len(files)))
        # scoreValue applies only where a vocabulary carries a score (control results).
        if "scoreValue" not in csv_header(p / "control-results.csv"):
            missing.append("scoreValue (control-results.csv)")
        return sum(len(read_csv(f)) for f in files), missing
    head = csv_header(p)
    return len(read_csv(p)), [c for c in required if c not in head]


def build():
    out = {}
    arts, _missing = artifacts()
    out["artifacts.csv"] = render("artifacts.csv", arts)
    for fname, fn in BUILDERS.items():
        out[fname] = render(fname, fn())
    # Index (written after the generated files exist in memory).
    idx = []
    for fname, cols, owner, loc in S17:
        path = loc or "registries/catalogue/" + fname
        if loc is None:
            text = out[fname]
            head = next(csv.reader(io.StringIO(text)))
            n = len(list(csv.reader(io.StringIO(text)))) - 1
            miss = [c for c in COMMON + cols if c not in head]
        else:
            n, miss = conformance(fname, loc)
        idx.append(dict(registryFile=fname, path=path, owner=owner,
                        conformsToCommonColumns="yes" if not any(m.split(" ")[0] in COMMON for m in miss) else "no",
                        missingColumns=multi(miss), rowCount=str(n), sources=SOURCES[fname]))
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=["registryFile", "path", "owner", "conformsToCommonColumns", "missingColumns",
                                        "rowCount", "sources"], lineterminator="\n")
    w.writeheader()
    for r in idx:  # section 17 order
        w.writerow(r)
    out["registry-index.csv"] = buf.getvalue()
    return out, _missing


def main(argv):
    check = "--check" in argv
    out, missing = build()
    changed = []
    for fname, content in sorted(out.items()):
        p = OUT / fname
        cur = p.read_text(encoding="utf-8") if p.is_file() else None
        if cur != content:
            changed.append(fname)
            if not check:
                OUT.mkdir(parents=True, exist_ok=True)
                with p.open("w", encoding="utf-8", newline="\n") as f:
                    f.write(content)
    for m in missing:
        print("warning: README artifact link has no file: %s" % m, file=sys.stderr)
    if check:
        if changed:
            print("catalogue out of date: " + ", ".join(changed))
            return 1
        print("catalogue up to date (%d files)" % len(out))
        return 0
    print("wrote %d of %d files to %s" % (len(changed), len(out), OUT.relative_to(REPO)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
