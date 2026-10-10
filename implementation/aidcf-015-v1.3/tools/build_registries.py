#!/usr/bin/env python3
"""Copy the canonical registries and schema set into this package.

Usage: python -B tools/build_registries.py [--repo PATH]

Copies, from the repository root (default: two levels above the package), with no edits:
    registries/controls/{controls.csv,controls.json,gate-mappings.csv,evidence-profiles.csv,parameters.csv}
    registries/families/control-families.csv, registries/domains/domains.csv
    registries/gates/{critical-gates.csv,critical-gate-criteria.csv}, registries/states/states.csv
    registries/vocabularies/*.csv
    schemas/{json-schema,owl,jsonld,shacl}/
into registries/... and schemas/... of this package, keeping the repository layout.

Writes registries/registry-sources.json (source path, SHA-256, row count of each file) and checks:
15 domains, 90 families, 360 unique canonical control IDs; one evidence profile per control;
gate-mappings.csv consistent with the criticalGates/supportingGates columns of controls.csv;
every mapped gate present in critical-gates.csv. Exits non-zero on any problem.
Then rebuild the dataset (tools/build_dataset.py) and the manifest (tools/build_manifest.py),
and run tools/run_all.py.
"""
import argparse, csv, hashlib, json, re, shutil, sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
FILES = ["registries/controls/controls.csv", "registries/controls/controls.json", "registries/controls/gate-mappings.csv",
         "registries/controls/evidence-profiles.csv", "registries/controls/parameters.csv",
         "registries/families/control-families.csv", "registries/domains/domains.csv",
         "registries/gates/critical-gates.csv", "registries/gates/critical-gate-criteria.csv", "registries/states/states.csv"]
SCHEMA_DIRS = ["json-schema", "owl", "jsonld", "shacl"]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rows(p):
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(PKG.parents[1]))
    repo = Path(ap.parse_args().repo).resolve()
    sources = []
    reg = PKG / "registries"
    if reg.exists():
        shutil.rmtree(reg)
    for rel in FILES:
        s = repo / rel
        if not s.exists():
            sys.exit("missing registry source: %s" % s)
        d = PKG / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(s, d)
        e = {"source": rel, "target": rel, "sha256": sha(s), "bytes": s.stat().st_size}
        if s.suffix == ".csv":
            e["rows"] = len(rows(s))
        sources.append(e)
    vdir = repo / "registries/vocabularies"
    vfiles = sorted(vdir.glob("*.csv"))
    if not vfiles:
        sys.exit("missing vocabulary registry: %s" % vdir)
    (reg / "vocabularies").mkdir(parents=True)
    for s in vfiles:
        rel = "registries/vocabularies/" + s.name
        shutil.copyfile(s, PKG / rel)
        sources.append({"source": rel, "target": rel, "sha256": sha(s), "bytes": s.stat().st_size, "rows": len(rows(s))})
    for d in SCHEMA_DIRS:
        t = PKG / "schemas" / d
        if t.exists():
            shutil.rmtree(t)
        shutil.copytree(repo / "schemas" / d, t, ignore=shutil.ignore_patterns("README.md", "__pycache__"))
        for f in sorted(t.rglob("*")):
            if f.is_file():
                rel = "schemas/%s/%s" % (d, f.relative_to(t).as_posix())
                sources.append({"source": rel, "target": rel, "sha256": sha(f), "bytes": f.stat().st_size})
    (reg / "registry-sources.json").write_text(json.dumps(
        {"description": "Files copied into this package by tools/build_registries.py, unmodified, with SHA-256 at copy time.",
         "files": sources}, indent=2) + "\n", encoding="utf-8")

    controls = rows(reg / "controls/controls.csv")
    fams = rows(reg / "families/control-families.csv")
    doms = rows(reg / "domains/domains.csv")
    gm = rows(reg / "controls/gate-mappings.csv")
    ep = rows(reg / "controls/evidence-profiles.csv")
    gates = {r["gateId"] for r in rows(reg / "gates/critical-gates.csv")}
    ids = [r["controlId"] for r in controls]
    problems = []
    if len(ids) != 360 or len(set(ids)) != 360:
        problems.append("controls: %d rows, %d unique" % (len(ids), len(set(ids))))
    if len({r["familyId"] for r in fams}) != 90 or len(fams) != 90:
        problems.append("families != 90")
    if len({r["domainId"] for r in doms}) != 15 or len(doms) != 15:
        problems.append("domains != 15")
    bad = [i for i in ids if not re.fullmatch(r"MCF-[A-Z]{3}-(0[0-1][0-9]|02[0-4])", i)]
    if bad:
        problems.append("non-canonical control IDs: %s" % bad[:5])
    if sorted(r["controlId"] for r in ep) != sorted(ids):
        problems.append("evidence-profiles.csv does not have exactly one row per control")
    epc = {r["controlId"]: r for r in ep}
    for r in controls:
        if epc.get(r["controlId"], {}).get("claimType") != r["claimType"]:
            problems.append("claimType differs between controls.csv and evidence-profiles.csv for %s" % r["controlId"])
        crit = set(filter(None, r["criticalGates"].split(";")))
        sup = set(filter(None, r["supportingGates"].split(";")))
        mc = {m["gateId"] for m in gm if m["controlId"] == r["controlId"] and m["role"] == "CRITICAL"}
        ms = {m["gateId"] for m in gm if m["controlId"] == r["controlId"] and m["role"] == "SUPPORTING"}
        if crit != mc or sup != ms:
            problems.append("gate-mappings.csv differs from controls.csv gate columns for %s" % r["controlId"])
    unknown_gates = {m["gateId"] for m in gm} - gates
    if unknown_gates:
        problems.append("gate-mappings.csv names gates not in critical-gates.csv: %s" % sorted(unknown_gates))
    if {m["role"] for m in gm} - {"CRITICAL", "SUPPORTING"}:
        problems.append("gate-mappings.csv has roles other than CRITICAL/SUPPORTING")
    print("copied %d files; registry roles: %d CRITICAL and %d SUPPORTING mappings over %d gates"
          % (len(sources), sum(m["role"] == "CRITICAL" for m in gm), sum(m["role"] == "SUPPORTING" for m in gm),
             len({m["gateId"] for m in gm})))
    if problems:
        print("REGISTRY PROBLEMS:\n  " + "\n  ".join(problems[:20]))
        sys.exit(1)
    print("registry checks passed: 15 domains, 90 families, 360 controls")


if __name__ == "__main__":
    main()
