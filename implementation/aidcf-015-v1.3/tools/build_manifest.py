"""Write baseline/release-manifest.json for AIDCF-015 v1.3 (AIDCF-016 section 13).

The manifest lists every package file except the excluded paths (outputs/ and the manifest itself) with its SHA-256
and size, pins registry, vocabulary and schema versions, and records an RFC 8785 (JCS) digest of the manifest body.
No signature is produced and no approval is claimed: signatureStatus is PENDING and every approval is PENDING.
Run it last, after every other file in the package has been written.
"""
import hashlib
import json
import mimetypes
import sys
from pathlib import Path

sys.dont_write_bytecode = True
PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG / "tools"))
import aidcf_rules as AR  # noqa: E402

M = AR.M
MANIFEST = "baseline/release-manifest.json"
EXCLUDED = ["outputs/", MANIFEST]
T0 = "2026-10-10T00:00:00Z"


def package_files():
    out = []
    for p in sorted(PKG.rglob("*")):
        if not p.is_file() or "__pycache__" in p.parts or p.suffix == ".pyc":
            continue
        rel = p.relative_to(PKG).as_posix()
        if any(rel == x or rel.startswith(x) for x in EXCLUDED):
            continue
        out.append(rel)
    return out


def media(rel):
    ext = Path(rel).suffix
    return {".jsonld": "application/ld+json", ".ttl": "text/turtle", ".rq": "application/sparql-query", ".csv": "text/csv",
            ".md": "text/markdown", ".py": "text/x-python", ".json": "application/json", ".txt": "text/plain"}.get(
        ext, mimetypes.guess_type(rel)[0] or "application/octet-stream")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def entry(rel):
    b = (PKG / rel).read_bytes()
    return {"filePath": rel, "sha256": sha(b), "byteSize": len(b), "mediaType": media(rel)}


def main():
    from run_all import jcs  # same canonicalisation as the verifier
    files = package_files()
    src = json.loads((PKG / "registries/registry-sources.json").read_text(encoding="utf-8"))
    regv, vocv = [], []
    for e in src["files"]:
        t = e["target"]
        if not t.startswith("registries/"):
            continue
        v = {"name": Path(t).name, "version": "1.1" if "vocabularies" not in t else "1.1", "sha256": e["sha256"], "filePath": t}
        if "rows" in e:
            v["recordCount"] = e["rows"]
        (vocv if "/vocabularies/" in t else regv).append(v)
    schv = []
    for rel in files:
        if rel.startswith("schemas/") and rel.endswith((".ttl", ".jsonld", ".schema.json")):
            schv.append({"name": Path(rel).name, "version": M.RELEASE, "sha256": sha((PKG / rel).read_bytes()), "filePath": rel})
    tests = [f for f in files if f.startswith(("tests/", "legacy/v1.1/tests/"))]
    suite_digest = sha("\n".join("%s %s" % (f, sha((PKG / f).read_bytes())) for f in tests).encode())
    recs = AR.load_records(sorted((PKG / "dataset").glob("*.jsonld")))
    man = {
        "id": "urn:aidcf:syn:release-manifest:AIDCF-REL-2026.10.1", "type": "ReleaseManifest", "semanticOwner": "AIDCF-014",
        "schemaVersion": M.RELEASE, "version": "1.0", "status": "CANDIDATE", "releaseRef": AR.RELEASE_ID, "sourceArtifact": "AIDCF-015",
        "name": "AIDCF-015 v1.3 reference package release manifest", "effectiveFrom": T0, "createdAt": T0,
        "createdBy": "urn:aidcf:syn:party:BUILDER", "classification": "INTERNAL",
        "provenance": {"sourceSystem": "AIDCF-015 v1.3 tools/build_manifest.py", "method": "SYNTHETIC_AUTHORING", "synthetic": True,
                       "transformationVersion": "1.3"},
        "description": "Bill of materials for the AIDCF-015 v1.3 synthetic reference package. Draft for controlled review; not signed; not approved.",
        "releaseId": AR.RELEASE_ID, "releaseStatus": "CANDIDATE",
        "artifactManifest": [entry(f) for f in files], "registryVersions": regv, "vocabularyVersions": vocv, "schemaVersions": schv,
        "approvedCardinality": "15 domains, 90 families, 360 controls (AIDCF-007A v1.1 registry; AIDCF-007A-AMD-001).",
        "knownIssues": sorted(r["id"] for r in recs if r["type"] == "BaselineIssue"), "knownIssuesFile": "baseline/known-issues.json",
        "migrationSet": sorted(r["id"] for r in recs if r["type"] == "MigrationRecord"),
        "testSuite": {"suiteVersion": "1.3", "sha256": suite_digest, "validationResultsPath": "outputs/validation-results.json"},
        "approvals": [{"approverRole": "Accountable methodology authority", "approvalOutcome": "PENDING"},
                      {"approverRole": "Independent T7 reviewer", "approvalOutcome": "PENDING"}],
        "integrity": {"digestAlgorithm": "SHA-256", "canonicalisation": "RFC 8785 (JCS) over the manifest with integrity.manifestDigest removed",
                      "signatureStatus": "PENDING"},
        "excludedPaths": EXCLUDED, "supersedesRelease": "AIDCF-015 v1.2 (no release identifier was assigned)",
    }
    man["integrity"]["manifestDigest"] = sha(jcs(man))
    (PKG / MANIFEST).write_text(json.dumps(man, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("manifest: %d files, digest %s, signature PENDING" % (len(files), man["integrity"]["manifestDigest"][:16]))


if __name__ == "__main__":
    main()
