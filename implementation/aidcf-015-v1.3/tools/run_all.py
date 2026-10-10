"""Run every AIDCF-016 validation layer over the AIDCF-015 v1.3 package.

Usage: python -B tools/run_all.py [--skip-fixtures] [--quiet]

Layers (AIDCF-016 section 11): REGISTRY, SYNTAX, SCHEMA, SHACL, BUSINESS_RULE, TRACEABILITY, GRAPH_QUERY, SCORE,
INTEGRITY, MANIFEST, VOCABULARY, EXPORT, FIXTURE. Every layer reports the number of checks it executed and the number
that failed; the process exits 1 if any check failed. Results are written to outputs/ only. outputs/ is excluded from
baseline/release-manifest.json, so running this tool never invalidates the manifest.

The tool never edits dataset, registry, schema, test or baseline files.
"""
import copy
import csv
import glob
import hashlib
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG / "tools"))
import aidcf_rules as AR  # noqa: E402

M = AR.M
SCHEMAS = PKG / "schemas"
OUT = PKG / "outputs"
NOW = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
QUIET = "--quiet" in sys.argv


class Layer:
    def __init__(self, name):
        self.name, self.checks, self.failures, self.warnings = name, 0, [], []

    def check(self, ok, rule, subject, message):
        self.checks += 1
        if not ok:
            self.failures.append({"ruleId": rule, "subject": subject, "message": message})
        return ok

    def warn(self, rule, subject, message):
        self.warnings.append({"ruleId": rule, "subject": subject, "message": message})


LAYERS = {}


def layer(name):
    LAYERS[name] = Layer(name)
    return LAYERS[name]


def sha_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dataset_files():
    return sorted(glob.glob(str(PKG / "dataset" / "*.jsonld")))


def load_context():
    return json.loads((SCHEMAS / "jsonld/aidcf-context-1.3.jsonld").read_text(encoding="utf-8"))["@context"]


# ------------------------------------------------------------------ REGISTRY
def run_registry(reg):
    L = layer("REGISTRY")
    c = reg["controls"]
    L.check(len(c) == 360, "REG-01", "controls.csv", "360 controls (found %d)" % len(c))
    ids = [r["controlId"] for r in AR.read_csv(PKG / "registries/controls/controls.csv")]
    L.check(len(ids) == len(set(ids)), "REG-02", "controls.csv", "control IDs unique")
    L.check(len({r["domainId"] for r in c.values()}) == 15 and len(reg["domains"]) == 15, "REG-03", "domains", "15 domains")
    L.check(len({r["familyId"] for r in c.values()}) == 90 and len(reg["families"]) == 90, "REG-04", "families", "90 families")
    for cid, r in c.items():
        L.check(r["familyId"].split("-")[0] == r["domainId"] == cid.split("-")[1], "REG-05", cid, "family and domain consistent with ID")
        L.check(cid in reg["profiles"] and reg["profiles"][cid]["claimType"] == r["claimType"], "REG-06", cid, "one evidence profile with the control claim type")
        crit = sorted(x for x in r["criticalGates"].split(";") if x.strip())
        sup = sorted(x for x in r["supportingGates"].split(";") if x.strip())
        mc = sorted(g for g, roles in reg["roles"].items() if roles.get(cid) == "CRITICAL")
        ms = sorted(g for g, roles in reg["roles"].items() if roles.get(cid) == "SUPPORTING")
        L.check(crit == mc and sup == ms, "REG-07", cid, "gate-mappings.csv agrees with controls.csv gate columns")
    for m in reg["mappings"]:
        L.check(m["role"] in ("CRITICAL", "SUPPORTING") and m["gateId"] in reg["gates"] and m["controlId"] in c, "REG-08",
                "%s/%s" % (m["controlId"], m["gateId"]), "mapping role and references valid")
    L.check(len(reg["gates"]) == 15, "REG-09", "critical-gates.csv", "15 gates")
    src = json.loads((PKG / "registries/registry-sources.json").read_text(encoding="utf-8"))
    for e in src["files"]:
        p = PKG / e["target"]
        L.check(p.exists() and sha_file(p) == e["sha256"], "REG-10", e["target"], "registry copy matches recorded source hash")
        srcp = PKG.parents[1] / e["source"]
        if srcp.exists():
            L.check(sha_file(srcp) == e["sha256"], "REG-11", e["source"], "package registry copy identical to repository source")
    return L


# ------------------------------------------------------------------ SYNTAX
def run_syntax():
    import rdflib
    L = layer("SYNTAX")
    for p in sorted(PKG.rglob("*.json")) + sorted(PKG.rglob("*.jsonld")):
        if "outputs" in p.parts or "tests" in p.parts and "invalid" in p.parts and p.name.startswith("syntax-"):
            continue
        try:
            json.loads(p.read_text(encoding="utf-8"))
            ok, msg = True, "valid JSON"
        except Exception as e:  # noqa: BLE001
            ok, msg = False, "JSON parse error: %s" % e
        L.check(ok, "SYN-01", str(p.relative_to(PKG)), msg)
    for p in sorted(SCHEMAS.rglob("*.ttl")):
        try:
            n = len(rdflib.Graph().parse(str(p), format="turtle"))
            ok, msg = n > 0, "%d triples" % n
        except Exception as e:  # noqa: BLE001
            ok, msg = False, "Turtle parse error: %s" % e
        L.check(ok, "SYN-02", str(p.relative_to(PKG)), msg)
    ctx = load_context()
    for p in dataset_files():
        try:
            d = json.loads(Path(p).read_text(encoding="utf-8"))
            d["@context"] = ctx
            n = len(rdflib.Graph().parse(data=json.dumps(d), format="json-ld"))
            ok, msg = n > 0, "%d triples" % n
        except Exception as e:  # noqa: BLE001
            ok, msg = False, "JSON-LD expansion error: %s" % e
        L.check(ok, "SYN-03", str(Path(p).relative_to(PKG)), msg)
    return L


def parse_rdf_text(text, fmt):
    import rdflib
    return rdflib.Graph().parse(data=text, format=fmt)


# ------------------------------------------------------------------ SCHEMA
def schema_registry():
    from referencing import Registry, Resource
    resources = []
    for p in sorted((SCHEMAS / "json-schema").glob("*.schema.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        resources.append((s["$id"], Resource.from_contents(s)))
    return Registry().with_resources(resources)


VALIDATORS = {}


def validator_for(typ):
    from jsonschema import Draft202012Validator, FormatChecker
    if typ not in VALIDATORS:
        if typ not in M.CLASS_META:
            return None
        sid = M.SCHEMA_BASE + M.schema_file(typ)
        VALIDATORS[typ] = Draft202012Validator({"$ref": sid}, registry=SCHEMA_REG, format_checker=FormatChecker())
    return VALIDATORS[typ]


def schema_errors(rec):
    v = validator_for(rec.get("type"))
    if v is None:
        return ["type %r has no AIDCF-016 schema" % rec.get("type")]
    return ["%s: %s" % ("/".join(str(x) for x in e.absolute_path) or "(record)", e.message) for e in v.iter_errors(rec)]


def run_schema(records, manifest):
    from jsonschema import Draft202012Validator
    L = layer("SCHEMA")
    for p in sorted((SCHEMAS / "json-schema").glob("*.schema.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        try:
            Draft202012Validator.check_schema(s)
            ok, msg = True, "valid against the 2020-12 metaschema"
        except Exception as e:  # noqa: BLE001
            ok, msg = False, str(e)[:300]
        L.check(ok, "SCH-00", p.name, msg)
    for r in records + [manifest]:
        errs = schema_errors(r)
        L.check(not errs, "SCH-01", r.get("id"), "; ".join(errs[:3]) if errs else "valid")
    return L


# ------------------------------------------------------------------ SHACL
def data_graph(records, ont_text=None):
    import rdflib
    g = rdflib.Graph()
    g.parse(data=json.dumps({"@context": load_context(), "@graph": records}), format="json-ld")
    g.parse(data=ont_text or (SCHEMAS / "owl/aidcf-core-1.3.ttl").read_text(encoding="utf-8"), format="turtle")
    return g


SHAPES = None


def shapes_graph():
    global SHAPES
    import rdflib
    if SHAPES is None:
        SHAPES = rdflib.Graph().parse(str(SCHEMAS / "shacl/aidcf-shapes-1.3.ttl"), format="turtle")
    return SHAPES


HEAVY_GLOBAL = ["EdgeRecordShape"]  # graph-level; about 12 s per run in rdflib, so fixtures name it only when they need it


def shapes_without(names):
    """Copy of the shapes graph without the named node shapes (and the blank nodes they own)."""
    import rdflib
    key = tuple(sorted(names))
    if key not in SHAPES_LIGHT:
        g = rdflib.Graph()
        for t in shapes_graph():
            g.add(t)
        for n in names:
            stack = [rdflib.URIRef(M.NS + n)]
            while stack:
                x = stack.pop()
                for p, o in list(g.predicate_objects(x)):
                    if isinstance(o, rdflib.BNode):
                        stack.append(o)
                    g.remove((x, p, o))
        SHAPES_LIGHT[key] = g
    return SHAPES_LIGHT[key]


SHAPES_LIGHT = {}


def shacl_results(g, focus=None, shapes=None):
    """Validate g. With focus nodes, only shapes that target those nodes are evaluated (pyshacl applies use_shapes to
    focus nodes directly, ignoring targets, so shapes are excluded by removing them from a copy of the shapes graph)."""
    import pyshacl
    import rdflib
    SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
    kw = {}
    sg = shapes_graph()
    if focus:
        kw["focus_nodes"] = [rdflib.URIRef(f) for f in focus]
        sg = shapes_without([n for n in HEAVY_GLOBAL if n not in (shapes or [])])
    conforms, rg, _ = pyshacl.validate(g, shacl_graph=sg, inference="none", advanced=True, allow_warnings=True,
                                       inplace=True, **kw)
    out = []
    for r in rg.subjects(rdflib.RDF.type, SH.ValidationResult):
        out.append({"focus": str(rg.value(r, SH.focusNode)), "shape": str(rg.value(r, SH.sourceShape)),
                    "path": str(rg.value(r, SH.resultPath) or ""), "value": str(rg.value(r, SH.value) or ""),
                    "severity": str(rg.value(r, SH.resultSeverity)).rsplit("#", 1)[-1],
                    "message": str(rg.value(r, SH.resultMessage) or "")})
    return conforms, out


def run_shacl(records, manifest):
    L = layer("SHACL")
    g = data_graph(records + [manifest])
    t = time.time()
    conforms, res = shacl_results(g)
    viol = [r for r in res if r["severity"] == "Violation"]
    L.checks = 1
    for r in res:
        if r["severity"] == "Violation":
            L.failures.append({"ruleId": r["message"].split(":")[0] if r["message"][:4] in ("MDM-", "BR-0", "TR-1", "TR-0") else "SHACL",
                               "subject": r["focus"], "message": "%s [%s %s]" % (r["message"], r["path"], r["value"])})
        else:
            L.warn("SHACL", r["focus"], r["message"])
    L.extra = {"triples": len(g), "focusResults": len(res), "violations": len(viol), "seconds": round(time.time() - t, 1),
               "conforms": bool(conforms and not viol)}
    L.checks = len(records) + 1  # every record and the manifest are focus nodes of at least the envelope shape
    return L, g


# ------------------------------------------------------------------ BUSINESS_RULE, TRACEABILITY
def run_business(ix, reg):
    L = layer("BUSINESS_RULE")
    out = AR.business_rules(ix, reg)
    rules = ["BR-%03d" % i for i in range(1, 16)] + ["MDM-R%02d" % i for i in range(1, 21) if i not in (11,)]
    L.checks = len(rules)
    for o in out:
        if o["outcome"] == "FAIL":
            L.failures.append(o)
        else:
            L.warn(o["ruleId"], o["subject"], o["message"])
    L.extra = {"rulesEvaluated": rules}
    return L


def run_traceability(ix, reg):
    L = layer("TRACEABILITY")
    out, checks = AR.traceability(ix, reg)
    L.checks = sum(checks.values())
    L.failures.extend(out)
    L.extra = {"checksPerRule": checks}
    return L


# ------------------------------------------------------------------ GRAPH_QUERY
def run_queries(g):
    L = layer("GRAPH_QUERY")
    results = {}
    for q in sorted((PKG / "queries").glob("Q*.rq")):
        exp = json.loads((PKG / "queries/expected" / (q.stem + ".json")).read_text(encoding="utf-8"))
        try:
            rows = [[_py(v) for v in row] for row in g.query(q.read_text(encoding="utf-8"))]
            ok = sorted(map(json.dumps, rows)) == sorted(map(json.dumps, exp["rows"]))
            msg = "matches expected (%d rows)" % len(rows) if ok else "expected %s got %s" % (exp["rows"], rows)
        except Exception as e:  # noqa: BLE001
            rows, ok, msg = None, False, "query error: %s" % e
        results[q.stem] = {"rows": rows, "expected": exp["rows"], "match": ok}
        L.check(ok, "GQ-" + q.stem, q.name, msg)
    L.extra = results
    return L


def _py(v):
    if v is None:
        return None
    p = v.toPython() if hasattr(v, "toPython") else v
    return p if isinstance(p, (int, float, bool)) else str(p)


# ------------------------------------------------------------------ SCORE
def score_check(ix, reg, L):
    results = {k: v[0] for k, v in AR.control_results(ix).items()}
    open_us = [u for u in ix.of("UnknownRecord") if AR.open_unknown(u)]
    sc = AR.compute_score(reg, results, open_us)
    t = sc["total"]
    for s in ix.of("ScoreSnapshot"):
        cov = s.get("coverage", {})
        for k in ["inScopeCount", "notApplicableCount", "assessedCount", "scoredCount", "unknownCount", "notAssessedCount", "coveragePercent"]:
            L.check(cov.get(k) == t[k], "SCORE-01", s["id"], "coverage.%s recorded %s recomputed %s" % (k, cov.get(k), t[k]))
        L.check(s.get("meanScore") == t["meanScore"], "SCORE-02", s["id"], "meanScore recorded %s recomputed %s" % (s.get("meanScore"), t["meanScore"]))
        L.check(s.get("band") == t["band"], "SCORE-03", s["id"], "band recorded %s recomputed %s" % (s.get("band"), t["band"]))
        rec_inputs = sorted([i["controlRef"].rsplit("/", 1)[-1], i["controlResult"], i.get("scoreValue")] for i in s.get("scoreInputs", []))
        h_rec = hashlib.sha256(json.dumps({"method": AR.SCORE_METHOD, "weighting": s.get("weighting"), "inputs": rec_inputs}, sort_keys=True,
                                          separators=(",", ":")).encode("utf-8")).hexdigest()
        L.check(s.get("calculationHash") == h_rec, "SCORE-04", s["id"], "calculationHash binds the recorded scoreInputs")
        L.check(s.get("calculationHash") == sc["hash"], "SCORE-04", s["id"], "calculationHash equals the hash of the recomputed inputs")
        L.check(rec_inputs == sc["inputs"], "SCORE-05", s["id"], "scoreInputs equal the 360 registry controls with Control Assessment results")
        L.check(s.get("domainScores") == sc["domains"], "SCORE-06", s["id"], "domain scores recomputed")
        uo = {"us%dCount" % i: sum(1 for u in open_us if u["unknownSeverity"] == "US%d" % i) for i in range(1, 6)}
        L.check(s.get("unknownOverlay") == uo, "SCORE-07", s["id"], "UNKNOWN overlay recomputed")
    return sc


def run_score(ix, reg):
    L = layer("SCORE")
    sc = score_check(ix, reg, L)
    t = sc["total"]
    L.extra = {"assessed": t["assessedCount"], "inScope": t["inScopeCount"], "assessedPercent": round(100.0 * t["assessedCount"] / t["inScopeCount"], 4),
               "scored": t["scoredCount"], "coveragePercent": t["coveragePercent"], "meanScore": t["meanScore"], "band": t["band"],
               "bandWithheldReason": t["reason"], "calculationHash": sc["hash"], "domains": sc["domains"]}
    return L


# ------------------------------------------------------------------ INTEGRITY
def integrity_check(ix, L, read=lambda p: (PKG / p).read_bytes()):
    for e in ix.of("EvidenceObject"):
        try:
            b = read(e["fixturePath"])
        except FileNotFoundError:
            L.check(False, "INT-01", e["id"], "fixture %s missing" % e["fixturePath"])
            continue
        h = hashlib.sha256(b).hexdigest()
        L.check(h == e["sha256"], "INT-01", e["id"], "fixture sha256 %s recorded %s" % (h[:12], e["sha256"][:12]))
        L.check(len(b) == e["byteSize"], "INT-02", e["id"], "fixture byte size")
        L.check(e.get("provenance", {}).get("sha256") in (None, e["sha256"]), "INT-03", e["id"], "provenance sha256 equals record sha256")
    for p in ix.of("EvidencePackage"):
        members = sorted(ix.o(p["id"], "composedOf"))
        h = hashlib.sha256("\n".join(ix.get(m).get("sha256", "") for m in members).encode()).hexdigest()
        L.check(h == p["sha256"], "INT-04", p["id"], "package digest over member digests")


def run_integrity(ix):
    L = layer("INTEGRITY")
    integrity_check(ix, L)
    files = {e["fixturePath"] for e in ix.of("EvidenceObject")}
    on_disk = {"evidence-fixtures/" + p.name for p in (PKG / "evidence-fixtures").glob("*")}
    L.check(files == on_disk, "INT-05", "evidence-fixtures", "every fixture is referenced by exactly the evidence records (orphans: %s)" % sorted(on_disk - files))
    return L


# ------------------------------------------------------------------ MANIFEST
def jcs(obj):
    """RFC 8785 canonical form for JSON without floating-point numbers (the manifest contains none)."""
    def chk(o):
        if isinstance(o, float):
            raise ValueError("float in manifest: JCS number canonicalisation not implemented")
        if isinstance(o, dict):
            for v in o.values():
                chk(v)
        if isinstance(o, list):
            for v in o:
                chk(v)
    chk(obj)
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def package_files():
    import build_manifest  # noqa: E402
    return build_manifest.package_files()


def manifest_check(man, records, L, read=lambda p: (PKG / p).read_bytes()):
    listed = {e["filePath"]: e for e in man.get("artifactManifest", [])}
    for path, e in sorted(listed.items()):
        try:
            b = read(path)
        except FileNotFoundError:
            L.check(False, "MAN-01", path, "listed file missing")
            continue
        L.check(hashlib.sha256(b).hexdigest() == e["sha256"] and len(b) == e["byteSize"], "MAN-01", path, "sha256 and size match the manifest")
    actual = set(package_files())
    L.check(actual == set(listed), "MAN-02", "baseline/release-manifest.json",
            "manifest lists every package file except excluded paths (unlisted %s; stale %s)" % (sorted(actual - set(listed))[:5], sorted(set(listed) - actual)[:5]))
    for x in man.get("excludedPaths", []):
        L.check(not any(p.startswith(x) for p in listed), "MAN-03", x, "excluded path not listed")
    L.check("outputs/" in man.get("excludedPaths", []), "MAN-03", "outputs/", "outputs/ excluded from the manifest")
    rels = {r.get("releaseRef") for r in records}
    L.check(rels == {man.get("releaseId")}, "MAN-04", man.get("releaseId"), "every record releaseRef equals the manifest releaseId (MDM-R20): %s" % sorted(map(str, rels)))
    integ = man.get("integrity", {})
    body = copy.deepcopy(man)
    body.get("integrity", {}).pop("manifestDigest", None)
    L.check(hashlib.sha256(jcs(body)).hexdigest() == integ.get("manifestDigest"), "MAN-05", "integrity.manifestDigest", "RFC 8785 digest of the manifest body")
    L.check(integ.get("signatureStatus") == "PENDING" and not integ.get("signaturePath"), "MAN-06", "integrity.signatureStatus",
            "no signature is claimed (signatureStatus PENDING, no signature file)")
    L.check(all(a.get("approvalOutcome") != "APPROVED" for a in man.get("approvals", [])) and man.get("releaseStatus") in ("DRAFT", "CANDIDATE", "REVIEWED"),
            "MAN-07", "approvals", "no approval is claimed for the release")
    ids = {r["id"] for r in records}
    for k in man.get("knownIssues", []) + man.get("migrationSet", []):
        L.check(k in ids, "MAN-08", k, "known issue or migration record present in the dataset")
    ki = json.loads(read(man["knownIssuesFile"]).decode("utf-8"))
    L.check(any("3.3333" in json.dumps(ki) for _ in [0]), "MAN-09", man["knownIssuesFile"], "known issues state the 12 of 360 (3.3333%) coverage")


def run_manifest(man, records):
    L = layer("MANIFEST")
    manifest_check(man, records, L)
    return L


# ------------------------------------------------------------------ VOCABULARY
def run_vocabulary(g):
    import rdflib
    L = layer("VOCABULARY")
    SKOS = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
    owl_codes = defaultdict(set)
    for c in g.subjects(rdflib.RDF.type, SKOS.Concept):
        s = str(c)
        if s.startswith(M.VOCAB_NS):
            scheme, code = s[len(M.VOCAB_NS):].split("/", 1)
            owl_codes[scheme].add(code)
    vocabs = M.load_registry_vocabs(PKG / "registries/vocabularies")
    for scheme, (title, fn, codes) in vocabs.items():
        want = {c for c, _, _ in codes}
        got = owl_codes.get(M.kebab(scheme), set())
        L.check(want == got, "VOC-01", scheme, "OWL SKOS concepts equal %s codes (missing %s, extra %s)" % (fn, sorted(want - got), sorted(got - want)))
        defs = json.loads((SCHEMAS / "json-schema/definitions.schema.json").read_text(encoding="utf-8"))["$defs"]
        L.check(set(defs["code-" + scheme]["enum"]) == want, "VOC-02", scheme, "JSON Schema enum equals %s codes" % fn)
    for fn, col, scheme in [("control-result-aliases.csv", "canonicalCode", "ControlResult"), ("decision-aliases.csv", "canonicalCode", None),
                            ("relationship-aliases.csv", "canonicalType", "RelationshipType")]:
        for r in AR.read_csv(PKG / "registries/vocabularies" / fn):
            v = r[col]
            if scheme:
                ok = v in {c for c, _, _ in M.VOCABS[scheme][2]}
            else:
                ok = v == "" or v in {c for c, _, _ in M.VOCABS["DecisionState"][2]} | {c for c, _, _ in M.VOCABS["DecisionLifecycle"][2]}
            L.check(ok, "VOC-03", "%s:%s" % (fn, list(r.values())[0]), "alias maps to a canonical code (%r)" % v)
    return L


# ------------------------------------------------------------------ EXPORT (CT-09)
def run_export(records):
    L = layer("EXPORT")
    keep = [r for r in records if M.CLASSIFICATION_RANK[r["classification"]] <= M.CLASSIFICATION_RANK["INTERNAL"]]
    ids = {r["id"] for r in keep}
    exported = []
    for r in keep:
        x = {}
        for k, v in r.items():
            if k in M.REL_BY_PROP:
                v = [o for o in v if o in ids or not (o.startswith("urn:aidcf:syn:") or o.startswith(M.ID_BASE))]
                if not v:
                    continue
            x[k] = v
        exported.append(x)
    for r in exported:
        L.check(M.CLASSIFICATION_RANK[r["classification"]] <= 1, "CT-09-1", r["id"], "exported record at or below INTERNAL")
        if r["type"] == "RelationshipRecord":
            L.check(r["sourceRef"] in ids and (r["targetRef"] in ids or not r["targetRef"].startswith(("urn:aidcf:syn:", M.ID_BASE))), "CT-09-2", r["id"],
                    "exported edge record has both endpoints in the export")
    removed = len(records) - len(exported)
    L.check(removed > 0, "CT-09-3", "export", "records above INTERNAL withheld (%d)" % removed)
    OUT.mkdir(exist_ok=True)
    (OUT / "export-internal.jsonld").write_text(json.dumps({"@context": "../schemas/jsonld/aidcf-context-1.3.jsonld", "@graph": exported}, indent=1) + "\n",
                                                encoding="utf-8")
    L.extra = {"exported": len(exported), "withheld": removed}
    return L


# ------------------------------------------------------------------ FIXTURE
def set_path(obj, path, value, op):
    parts = path.split(".")
    for p in parts[:-1]:
        obj = obj[int(p)] if isinstance(obj, list) else obj[p]
    last = parts[-1]
    if isinstance(obj, list):
        last = int(last)
    if op == "set":
        obj[last] = value
    elif op == "delete":
        del obj[last]
    elif op == "append":
        obj.setdefault(last, []).append(value)
    elif op == "remove_value":
        obj[last] = [v for v in obj[last] if v != value]
        if not obj[last]:
            del obj[last]


def apply_patch(records, patch):
    by = {r["id"]: r for r in records}
    touched = set()
    for op in patch:
        if op["op"] == "add_record":
            records.append(op["record"])
            by[op["record"]["id"]] = op["record"]
            touched.add(op["record"]["id"])
        elif op["op"] == "remove_record":
            records[:] = [r for r in records if r["id"] != op["id"]]
            touched.add(op["id"])
        else:
            set_path(by[op["id"]], op["field"], op.get("value"), op["op"])
            touched.add(op["id"])
            for v in (op.get("value") if isinstance(op.get("value"), list) else [op.get("value")]):
                if isinstance(v, str) and v in by:
                    touched.add(v)
    return touched


def run_fixtures(records, reg, man):
    L = layer("FIXTURE")
    results = []
    base_cache = {}
    fixtures = sorted((PKG / "tests").glob("*/*.json"))
    for fp in fixtures:
        fx = json.loads(fp.read_text(encoding="utf-8"))
        kind = fp.parent.name
        exp_fail = fx["expect"] == "FAIL"
        got_fail, detail = run_one(fx, fp, records, reg, man, base_cache)
        ok = got_fail == exp_fail
        L.check(ok, "FIX-" + kind.upper(), str(fp.relative_to(PKG)),
                "%s expected %s at %s%s; observed %s: %s" % (fx["fixtureId"], fx["expect"], fx["layer"],
                                                         (" for " + fx["expectedRule"]) if fx.get("expectedRule") else "",
                                                         "FAIL" if got_fail else "PASS", detail[:400]))
        results.append({"fixture": str(fp.relative_to(PKG)), "fixtureId": fx["fixtureId"], "kind": kind, "layer": fx["layer"],
                        "expect": fx["expect"], "observed": "FAIL" if got_fail else "PASS", "asExpected": ok,
                        "expectedRule": fx.get("expectedRule"), "detail": detail})
    for legacy in ["valid", "invalid"]:
        for fp in sorted((PKG / "legacy/v1.1/tests" / legacy).glob("*.json")):
            from jsonschema import Draft202012Validator
            s = json.loads((PKG / "legacy/v1.1/schemas/capability.schema.json").read_text(encoding="utf-8"))
            errs = [e.message for e in Draft202012Validator(s).iter_errors(json.loads(fp.read_text(encoding="utf-8")))]
            ok = (not errs) if legacy == "valid" else bool(errs)
            L.check(ok, "FIX-LEGACY", str(fp.relative_to(PKG)), "v1.1 fixture against v1.1 schema: %s" % ("; ".join(errs) or "valid"))
            results.append({"fixture": str(fp.relative_to(PKG)), "fixtureId": "LEGACY-" + fp.stem, "kind": "legacy-" + legacy, "layer": "SCHEMA",
                            "expect": "PASS" if legacy == "valid" else "FAIL", "observed": "FAIL" if errs else "PASS", "asExpected": ok,
                            "detail": "; ".join(errs)})
    L.extra = results
    return L


def matches(fx, items):
    """items: list of (ruleId, message). Returns matching messages."""
    rule, text = fx.get("expectedRule"), fx.get("expectedText")
    return [m for r, m in items if (not rule or r == rule or m.startswith(rule)) and (not text or text in m)]


def run_one(fx, fp, records, reg, man, base_cache):
    layer_ = fx["layer"]
    if layer_ == "SYNTAX":
        raw = (fp.parent / fx["rawFile"]).read_text(encoding="utf-8")
        try:
            if fx["format"] == "json":
                json.loads(raw)
            elif fx["format"] == "json-ld":
                d = json.loads(raw)
                d["@context"] = load_context()
                parse_rdf_text(json.dumps(d), "json-ld")
            else:
                parse_rdf_text(raw, fx["format"])
            return False, "parsed without error"
        except Exception as e:  # noqa: BLE001
            msg = "%s: %s" % (type(e).__name__, e)
            return bool(not fx.get("expectedText") or fx["expectedText"] in msg), msg
    if layer_ == "SCHEMA" and "record" in fx:
        errs = schema_errors(fx["record"])
        if fx["expect"] == "PASS":
            return bool(errs), "; ".join(errs) or "valid"
        hit = [e for e in errs if fx.get("expectedText", "") in e]
        return bool(hit), "; ".join(hit or errs) or "valid"
    recs = copy.deepcopy(records)
    touched = apply_patch(recs, fx.get("patch", []))
    if layer_ == "SCHEMA":
        errs = [e for r in recs if r["id"] in touched for e in schema_errors(r)]
        hit = [e for e in errs if fx.get("expectedText", "") in e]
        return (bool(hit) if fx["expect"] == "FAIL" else bool(errs)), "; ".join(hit or errs) or "valid"
    if layer_ == "SHACL":
        focus = sorted(touched | set(fx.get("focus", [])) | {M.ONT})
        _, res = shacl_results(data_graph(recs), focus, fx.get("shapes"))
        items = [(r["message"].split(":")[0], "%s [%s]" % (r["message"], r["focus"])) for r in res if r["severity"] == "Violation"]
        if fx["expect"] == "PASS":
            return bool(items), "; ".join(m for _, m in items[:5]) or "no violations on focus nodes"
        hit = matches(fx, items)
        if hit:
            # the full-dataset SHACL run (SHACL layer) is the baseline: the defect's violation must be absent from it
            base = [(f["ruleId"], f["message"]) for f in LAYERS["SHACL"].failures]
            if matches(fx, base):
                return False, "expected violation also present without the defect: %s" % hit[0]
        return bool(hit), "; ".join(hit[:3]) or "violations: " + "; ".join(m for _, m in items[:3])
    ix = AR.Index(recs)
    if layer_ in ("BUSINESS_RULE", "TRACEABILITY"):
        out = AR.business_rules(ix, reg) if layer_ == "BUSINESS_RULE" else AR.traceability(ix, reg)[0]
        items = [(o["ruleId"], o["message"]) for o in out if o["outcome"] == "FAIL"]
    elif layer_ == "SCORE":
        L = Layer("tmp")
        score_check(ix, reg, L)
        items = [(f["ruleId"], f["message"]) for f in L.failures]
    elif layer_ == "INTEGRITY":
        L = Layer("tmp")
        over = fx.get("overrideFile", {})
        integrity_check(ix, L, read=lambda p: over["content"].encode() if p == over.get("path") else (PKG / p).read_bytes())
        items = [(f["ruleId"], f["message"]) for f in L.failures]
    elif layer_ == "MANIFEST":
        L = Layer("tmp")
        over = fx.get("overrideFile", {})
        m2 = copy.deepcopy(man)
        for op in fx.get("manifestPatch", []):
            set_path(m2, op["field"], op.get("value"), op["op"])
        manifest_check(m2, recs, L, read=lambda p: (PKG / p).read_bytes() + over["append"].encode() if p == over.get("path") else (PKG / p).read_bytes())
        items = [(f["ruleId"], f["message"]) for f in L.failures]
    else:
        return False, "unknown layer %s" % layer_
    if fx["expect"] == "PASS":
        return bool(items), "; ".join("%s %s" % i for i in items[:5]) or "no rule failures"
    hit = matches(fx, items)
    return bool(hit), "; ".join(hit[:3]) or ("other failures: " + "; ".join("%s %s" % i for i in items[:3]) if items else "no rule failures")


# ------------------------------------------------------------------ outputs
def validation_records():
    out = []
    for name, L in LAYERS.items():
        out.append({"id": "urn:aidcf:syn:validation:%s" % name, "type": "ValidationResult", "semanticOwner": "AIDCF-016",
                    "schemaVersion": M.RELEASE, "version": "1.0", "status": "CANDIDATE", "releaseRef": AR.RELEASE_ID, "sourceArtifact": "AIDCF-015",
                    "name": "Validation layer %s" % name, "effectiveFrom": NOW, "createdAt": NOW, "createdBy": "urn:aidcf:syn:party:BUILDER",
                    "classification": "INTERNAL",
                    "provenance": {"sourceSystem": "AIDCF-015 v1.3 tools/run_all.py", "method": "VALIDATION_RUN", "synthetic": True},
                    "validationLayer": name, "ruleId": "LAYER-" + name, "outcome": "FAIL" if L.failures else "PASS",
                    "message": "%d checks, %d failed, %d warnings" % (L.checks, len(L.failures), len(L.warnings)),
                    "validator": "AIDCF-015 v1.3 tools/run_all.py (self-validation; not independent)", "executedAt": NOW})
        for i, f in enumerate(L.failures[:200], 1):
            out.append({**out[-1 - (i - 1)], "id": "urn:aidcf:syn:validation:%s-F%04d" % (name, i), "ruleId": f["ruleId"], "outcome": "FAIL",
                        "name": "%s failure %d" % (name, i), "message": str(f["message"])[:1000], "subjectPaths": [str(f["subject"])]})
    return out


def main():
    global SCHEMA_REG
    t0 = time.time()
    OUT.mkdir(exist_ok=True)
    reg = AR.load_registry()
    run_registry(reg)
    run_syntax()
    records = AR.load_records(dataset_files())
    man = json.loads((PKG / "baseline/release-manifest.json").read_text(encoding="utf-8"))
    ix = AR.Index(records)
    SCHEMA_REG = schema_registry()
    run_schema(records, man)
    LS, g = run_shacl(records, man)
    run_business(ix, reg)
    run_traceability(ix, reg)
    run_queries(g)
    run_score(ix, reg)
    run_integrity(ix)
    run_manifest(man, records)
    run_vocabulary(g)
    run_export(records)
    if "--skip-fixtures" not in sys.argv:
        run_fixtures(records, reg, man)
    # impact analysis output
    ev = ix.of("Event")
    impact = {e["id"]: {"subject": e["subjectRef"], "affected": AR.impact(ix, e["subjectRef"]),
                        "byClass": dict(Counter(ix.type(a) for a in AR.impact(ix, e["subjectRef"])))} for e in ev}
    vr = validation_records()
    vr_errs = [e for r in vr for e in schema_errors(r)]
    summary = {"tool": "tools/run_all.py", "release": AR.RELEASE_ID, "executedAt": NOW, "seconds": round(time.time() - t0, 1),
               "independent": False, "note": "Self-validation by the package author's tooling; no independent execution.",
               "layers": {n: {"checks": L.checks, "failed": len(L.failures), "warnings": len(L.warnings), "outcome": "FAIL" if L.failures else "PASS"}
                          for n, L in LAYERS.items()},
               "validationResultRecordsSchemaErrors": len(vr_errs)}
    (OUT / "validation-results.json").write_text(json.dumps(summary, indent=1) + "\n", encoding="utf-8")
    (OUT / "validation-results.jsonld").write_text(json.dumps({"@context": "../schemas/jsonld/aidcf-context-1.3.jsonld", "@graph": vr}, indent=1) + "\n",
                                                   encoding="utf-8")
    (OUT / "validation-failures.json").write_text(json.dumps({n: {"failures": L.failures, "warnings": L.warnings} for n, L in LAYERS.items()}, indent=1) + "\n",
                                                  encoding="utf-8")
    for n, fn in [("GRAPH_QUERY", "graph-query-results.json"), ("SCORE", "score-reperformance.json"), ("FIXTURE", "fixture-results.json"),
                  ("SHACL", "shacl-summary.json"), ("TRACEABILITY", "traceability-checks.json")]:
        if n in LAYERS and hasattr(LAYERS[n], "extra"):
            (OUT / fn).write_text(json.dumps(LAYERS[n].extra, indent=1, default=str) + "\n", encoding="utf-8")
    (OUT / "impact-analysis.json").write_text(json.dumps(impact, indent=1) + "\n", encoding="utf-8")
    width = max(len(n) for n in LAYERS)
    print("AIDCF-015 v1.3 run_all (%s, %.1fs)" % (AR.RELEASE_ID, time.time() - t0))
    for n, L in LAYERS.items():
        print("  %-*s %5d checks  %4d failed  %4d warnings  %s" % (width, n, L.checks, len(L.failures), len(L.warnings), "FAIL" if L.failures else "PASS"))
        if not QUIET:
            for f in L.failures[:8]:
                print("      - %s %s: %s" % (f["ruleId"], str(f["subject"])[-60:], str(f["message"])[:300]))
    if vr_errs:
        print("  ValidationResult records failed their own schema: %s" % vr_errs[:3])
    bad = any(L.failures for L in LAYERS.values()) or bool(vr_errs)
    print("RESULT: %s" % ("FAIL" if bad else "PASS"))
    sys.exit(1 if bad else 0)


SCHEMA_REG = None
if __name__ == "__main__":
    main()
