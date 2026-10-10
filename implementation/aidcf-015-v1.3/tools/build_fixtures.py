"""Write the conformance fixtures in tests/valid, tests/invalid and tests/business (AIDCF-016 section 12).

Each fixture is a JSON file: fixtureId, description, layer, expect (PASS or FAIL), expectedRule and/or expectedText
(the reason the fixture must fail), and either a standalone record or a patch applied to a copy of the dataset.
tools/run_all.py (FIXTURE layer) executes every fixture and checks that it fails at the stated layer for the stated
reason, and, for SHACL fixtures, that the same violation is absent from the unpatched dataset.
"""
import copy
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG / "tools"))
import aidcf_rules as AR  # noqa: E402

S = "urn:aidcf:syn:"
ID = AR.M.ID_BASE


def main():
    recs = {r["id"]: r for r in AR.load_records(sorted((PKG / "dataset").glob("*.jsonld")))}
    ci = recs[S + "capability:CI-001"]
    ca = recs[S + "control-assessment:CA-001"]
    gr = recs[S + "gate-result:GR-CG-03"]
    rr_dep = next(r for r in recs.values() if r["type"] == "RelationshipRecord" and r["relationshipType"] == "DEPENDS_ON")
    dep = recs[S + "dependency:DEP-02"]
    ctrl = recs[ID + "control/MCF-DEP-001"]
    f004 = recs[S + "finding:F-004"]
    rr_gate = next(r for r in recs.values() if r["type"] == "RelationshipRecord" and r["relationshipType"] == "EVALUATES_GATE"
                   and r["sourceRef"] == ID + "control/MCF-DEP-001" and r["targetRef"] == ID + "gate/CG-03")
    evt = recs[S + "event:EVT-001"]

    def drop(r, *ks):
        r = copy.deepcopy(r)
        for k in ks:
            r.pop(k, None)
        return r

    def with_(r, **kv):
        r = copy.deepcopy(r)
        r.update(kv)
        return r
    F = {}
    # ---------------------------------------------------------------- valid
    F["valid/V-001-capability.json"] = dict(layer="SCHEMA", expect="PASS", description="v1.3 Capability Instance from the dataset (successor of the v1.1 capability-valid fixture).", record=ci)
    F["valid/V-002-control-assessment.json"] = dict(layer="SCHEMA", expect="PASS", description="Control Assessment CA-001 from the dataset.", record=ca)
    F["valid/V-003-gate-result.json"] = dict(layer="SCHEMA", expect="PASS", description="Gate Result GR-CG-03 (FAIL) from the dataset.", record=gr)
    F["valid/V-004-relationship-record.json"] = dict(layer="SCHEMA", expect="PASS", description="DEPENDS_ON relationship record with its qualifiers.", record=rr_dep)
    F["valid/V-005-dispose-unknown.json"] = dict(layer="BUSINESS_RULE", expect="PASS",
        description="Dispositioning U-002 with a disposition and due date keeps every business rule satisfied.",
        patch=[{"op": "set", "id": S + "unknown:U-002", "field": "unknownStatus", "value": "DISPOSITIONED"},
               {"op": "set", "id": S + "unknown:U-002", "field": "disposition", "value": "Owner accepted; fresh export requested."},
               {"op": "set", "id": S + "unknown:U-002", "field": "dueDate", "value": "2026-11-30"}])
    F["valid/V-006-shacl-gate.json"] = dict(layer="SHACL", expect="PASS", description="The dataset Gate Results and decision conform to the SHACL shapes.",
        patch=[], focus=[S + "gate-result:GR-" + g for g in ["CG-03", "CG-07", "CG-10"]] + [S + "decision:AD-001"])
    F["valid/V-007-traceability.json"] = dict(layer="TRACEABILITY", expect="PASS", description="The unpatched dataset satisfies TR-01 to TR-18.", patch=[])
    F["valid/V-008-score.json"] = dict(layer="SCORE", expect="PASS", description="The unpatched score snapshot reperforms exactly.", patch=[])
    # ---------------------------------------------------------------- invalid (schema)
    F["invalid/I-SCH-001-capability-missing-owner.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="'owner' is a required property",
        description="Restored v1.1 negative test, re-expressed in v1.3: a Capability Instance without its accountable owner.", record=drop(ci, "owner"))
    F["invalid/I-SCH-002-additional-property.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="Additional properties are not allowed",
        description="Closed schemas: an undeclared property is rejected (v1.2 defect: additionalProperties true).", record=with_(gr, passedBy="assessor"))
    F["invalid/I-SCH-003-gate-state-code.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="'PASSED' is not one of",
        description="Gate state outside registries/vocabularies/gate-results.csv.", record=with_(gr, gateState="PASSED"))
    F["invalid/I-SCH-004-control-code.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="does not match",
        description="Control code outside the MCF-DOM-NNN pattern.", record=with_(ctrl, controlCode="MCF-XYZ-999"))
    F["invalid/I-SCH-005-release-ref.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="does not match",
        description="releaseRef not in the AIDCF-REL-YYYY.MM.N pattern.", record=with_(ci, releaseRef="AIDCF-REL-2026.13.1"))
    F["invalid/I-SCH-006-confidential-without-dc.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="'distributionControlRef' is a required property",
        description="A CONFIDENTIAL record must carry a DistributionControl (AIDCF-014 BR-012).", record=drop(f004, "distributionControlRef"))
    F["invalid/I-SCH-007-missing-review-state.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="'reviewState' is a required property",
        description="Assertion-bearing class without reviewState.", record=drop(dep, "reviewState"))
    F["invalid/I-SCH-008-inverse-property.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="Additional properties are not allowed",
        description="Inverse property asserted in JSON (MDM-R11).", record=with_(ca, assesses=[ID + "control/MCF-CAP-001"]))
    F["invalid/I-SCH-009-schema-version.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="'1.3' was expected",
        description="Record claims an older data-model release.", record=with_(ci, schemaVersion="1.2"))
    F["invalid/I-SCH-010-missing-envelope.json"] = dict(layer="SCHEMA", expect="FAIL", expectedText="'provenance' is a required property",
        description="Envelope field provenance missing.", record=drop(ca, "provenance"))
    # ---------------------------------------------------------------- invalid (syntax)
    F["invalid/I-SYN-001-malformed-json.json"] = dict(layer="SYNTAX", expect="FAIL", format="json", rawFile="syntax-malformed.jsonld.txt",
        expectedText="JSONDecodeError", description="Truncated JSON-LD document.")
    F["invalid/I-SYN-002-broken-turtle.json"] = dict(layer="SYNTAX", expect="FAIL", format="turtle", rawFile="syntax-broken.ttl.txt",
        description="Turtle with an unterminated statement; an RDF parse failure is a counted failure (v1.2 defect).")
    # ---------------------------------------------------------------- invalid (SHACL)
    sh = [
        ("I-SHA-001-partial-gate-pass", "GatePartialNeverPass: CG-03 recorded PASS with a PARTIAL CRITICAL input.", "MDM-R02",
         "a CRITICAL input is PARTIAL", [{"op": "set", "id": S + "gate-result:GR-CG-03", "field": "gateState", "value": "PASS"}]),
        ("I-SHA-002-positive-decision", "Decision REASONABLY_ASSURED with FAIL and UNKNOWN gates.", "MDM-R03 / BR-005", None,
         [{"op": "set", "id": S + "decision:AD-001", "field": "decisionState", "value": "REASONABLY_ASSURED"}]),
        ("I-SHA-003-unknown-without-record", "UNKNOWN result without an UNKNOWN Record.", "TR-11", "UNKNOWN result without",
         [{"op": "delete", "id": S + "control-assessment:CA-009", "field": "hasUnknown"}]),
        ("I-SHA-004-depends-on-qualifier", "DEPENDS_ON relationship record without dependencyRef.", "MDM-R10", "lacks mandatory qualifier dependencyRef",
         [{"op": "delete", "id": rr_dep["id"], "field": "dependencyRef"}]),
        ("I-SHA-005-assurance-level", "IMPLEMENTATION control with requiredAssuranceLevel AL2.", "MDM-R08", None,
         [{"op": "set", "id": ID + "control/MCF-DEP-001", "field": "requiredAssuranceLevel", "value": "AL2"}]),
        ("I-SHA-006-approval-type", "APPROVED_BY pointing to a REVIEW record.", "MDM-R17", None,
         [{"op": "set", "id": S + "decision:AD-001", "field": "approvedBy", "value": [S + "review:RR-001"]}]),
        ("I-SHA-007-statement-rank", "Statement claims LIMITED while the decision is NOT_ASSURED.", "BR-007", "statement",
         [{"op": "set", "id": S + "statement:AS-001", "field": "decisionState", "value": "LIMITED"}]),
        ("I-SHA-008-classification-dc", "CONFIDENTIAL finding without a DistributionControl.", "BR-012", None,
         [{"op": "delete", "id": S + "finding:F-004", "field": "distributionControlRef"}]),
        ("I-SHA-009-gate-code", "Gate Result gateCode differs from the evaluated gate.", "MDM-R01", "gateCode",
         [{"op": "set", "id": S + "gate-result:GR-CG-03", "field": "gateCode", "value": "CG-04"}]),
        ("I-SHA-010-gate-pass-unknown", "CG-10 recorded PASS while US4 U-004 is attached.", "MDM-R09", "gate PASS while",
         [{"op": "set", "id": S + "gate-result:GR-CG-10", "field": "gateState", "value": "PASS"}]),
        ("I-SHA-011-edge-without-record", "Asserted edge without a relationship record.", "MDM-R10", "asserted edge has no relationship record",
         [{"op": "append", "id": S + "system:SYS-STO", "field": "dependsOn", "value": S + "system:SYS-CMP"}]),
        ("I-SHA-012-conforming-below-floor", "CONFORMING result with evidence below the control floor.", "MDM-R07", None,
         [{"op": "set", "id": S + "control-assessment:CA-003", "field": "evidenceSufficiency", "value": "S3"}]),
    ]
    for k, d, rule, text, patch in sh:
        F["invalid/%s.json" % k] = dict(layer="SHACL", expect="FAIL", expectedRule=rule, expectedText=text, description=d, patch=patch,
                                        shapes=["EdgeRecordShape"] if "asserted edge" in (text or "") else None)
    # ---------------------------------------------------------------- business
    bz = [
        ("B-001-gate-pass-on-partial", "CG-07 recorded PASS although its CRITICAL inputs OPS-013 and SEC-005 are PARTIAL (v1.2 defect).", "MDM-R01",
         [{"op": "set", "id": S + "gate-result:GR-CG-07", "field": "gateState", "value": "PASS"}]),
        ("B-002-gate-pass-on-one-control", "CG-02 recorded PASS with none of its 3 registry CRITICAL controls assessed (v1.2: PASS on 1 of 72).", "BR-004",
         [{"op": "set", "id": S + "gate-result:GR-CG-02", "field": "gateState", "value": "PASS"}]),
        ("B-003-positive-decision", "Decision REASONABLY_ASSURED while gates FAIL and a US5 UNKNOWN is open.", "MDM-R03",
         [{"op": "set", "id": S + "decision:AD-001", "field": "decisionState", "value": "REASONABLY_ASSURED"}]),
        ("B-004-us5-ceiling", "Decision LIMITED although the open US5 U-003 caps it at INCONCLUSIVE (the computed ceiling is NOT_ASSURED).", "MDM-R04",
         [{"op": "set", "id": S + "decision:AD-001", "field": "decisionState", "value": "LIMITED"}]),
        ("B-005-silent-resolution", "U-004 marked RESOLVED without closure evidence.", "BR-008",
         [{"op": "set", "id": S + "unknown:U-004", "field": "unknownStatus", "value": "RESOLVED"}]),
        ("B-006-band-not-withheld", "Score band B4 reported at 3.0556% coverage.", "BR-006",
         [{"op": "set", "id": S + "score:SS-001", "field": "band", "value": "B4"}]),
        ("B-007-conforming-without-evidence", "MCF-RES-017 recorded CONFORMING with S2 evidence and no E4 class.", "MDM-R07",
         [{"op": "set", "id": S + "control-assessment:CA-009", "field": "result", "value": "CONFORMING"}]),
        ("B-008-role-swap", "MCF-DEP-001 evaluated as SUPPORTING on CG-03 (registry role CRITICAL).", "MDM-R02",
         [{"op": "set", "id": S + "gate-result:GR-CG-03", "field": "controlEvaluations.%d.gateRole" % _idx(gr, "MCF-DEP-001"), "value": "SUPPORTING"}]),
        ("B-009-event-impact", "Event affectedAssertions truncated to one record.", "BR-013",
         [{"op": "set", "id": evt["id"], "field": "affectedAssertions", "value": evt["affectedAssertions"][:1]}]),
        ("B-010-edge-gate-role", "Control-to-gate relationship record carries a role that differs from gate-mappings.csv.", "MDM-R10",
         [{"op": "set", "id": rr_gate["id"], "field": "gateRole", "value": "SUPPORTING"}]),
        ("B-011-federated-handoff", "Integration handoff federates AIDCF conclusions.", "BR-010",
         [{"op": "set", "id": S + "handoff:IH-001", "field": "conclusionsFederated", "value": True}]),
        ("B-012-recommendation-ceiling", "Recommendation ceiling LIMITED although the computed ceiling is NOT_ASSURED (CG-07 FAIL).", "MDM-R06",
         [{"op": "set", "id": S + "recommendation:DR-001", "field": "decisionCeiling", "value": "LIMITED"}]),
        ("B-026-fail-not-softened", "Decision, recommendation, statement and report set to INCONCLUSIVE: the US5 U-003 and the CG-01 UNKNOWN "
         "(INCONCLUSIVE) do not raise the CG-07 FAIL ceiling (NOT_ASSURED); the computed ceiling stays NOT_ASSURED (AIDCF-010 order, no tie-break).", "MDM-R06",
         [{"op": "set", "id": S + "recommendation:DR-001", "field": "decisionCeiling", "value": "INCONCLUSIVE"},
          {"op": "set", "id": S + "recommendation:DR-001", "field": "recommendedState", "value": "INCONCLUSIVE"},
          {"op": "set", "id": S + "decision:AD-001", "field": "decisionState", "value": "INCONCLUSIVE"},
          {"op": "set", "id": S + "statement:AS-001", "field": "decisionState", "value": "INCONCLUSIVE"},
          {"op": "set", "id": S + "report:RPT-001", "field": "decisionState", "value": "INCONCLUSIVE"}],
         "differs from computed ceiling NOT_ASSURED"),
        ("B-013-statement-validity", "Statement valid beyond the decision validity.", "BR-007",
         [{"op": "set", "id": S + "statement:AS-001", "field": "effectiveTo", "value": "2028-01-01T00:00:00Z"}]),
        ("B-014-report-overclaim", "Report states REASONABLY_ASSURED.", "BR-007",
         [{"op": "set", "id": S + "report:RPT-001", "field": "decisionState", "value": "REASONABLY_ASSURED"}]),
        ("B-015-release-ref", "Record bound to a different release.", "MDM-R20",
         [{"op": "set", "id": S + "capability:CI-001", "field": "releaseRef", "value": "AIDCF-REL-2026.09.1"}]),
        ("B-016-reassessment-gap", "Event no longer triggers reassessment of an impacted Gate Result.", "TR-17",
         [{"op": "remove_value", "id": evt["id"], "field": "triggersReassessment", "value": S + "gate-result:GR-CG-07"}]),
        ("B-017-na-without-rationale", "NOT_APPLICABLE result without rationale and review.", "BR-002",
         [{"op": "set", "id": S + "control-assessment:CA-012", "field": "result", "value": "NOT_APPLICABLE"},
          {"op": "delete", "id": S + "control-assessment:CA-012", "field": "reviewedBy"}]),
        ("B-018-auto-suspend", "Decision suspended by a pending event without human disposition.", "BR-011",
         [{"op": "set", "id": S + "decision:AD-001", "field": "decisionLifecycle", "value": "SUSPENDED"},
          {"op": "append", "id": S + "decision:AD-001", "field": "invalidatedBy", "value": S + "event:EVT-001"}]),
        ("B-019-self-closure", "F-006 closure reviewed by the finding owner.", "BR-008",
         [{"op": "set", "id": S + "review:RR-003", "field": "reviewer", "value": S + "party:FAC-OPS"}]),
        ("B-020-registry-tamper", "Control claim type differs from the registry.", "MDM-R13",
         [{"op": "set", "id": ID + "control/MCF-POW-001", "field": "claimType", "value": "DESIGN"}]),
    ]
    for k, d, rule, patch, *text in bz:
        F["business/%s.json" % k] = dict(layer="BUSINESS_RULE" if not rule.startswith("TR-") else "TRACEABILITY", expect="FAIL", expectedRule=rule,
                                         expectedText=text[0] if text else None, description=d, patch=patch)
    F["business/B-021-score-coverage.json"] = dict(layer="SCORE", expect="FAIL", expectedRule="SCORE-01", description="Coverage inflated to 85%.",
        patch=[{"op": "set", "id": S + "score:SS-001", "field": "coverage.coveragePercent", "value": 85.0}])
    F["business/B-022-score-hash.json"] = dict(layer="SCORE", expect="FAIL", expectedRule="SCORE-04", description="Score input changed without recomputing the hash.",
        patch=[{"op": "set", "id": S + "score:SS-001", "field": "scoreInputs.0.controlResult", "value": "PARTIAL"}])
    F["business/B-023-evidence-tamper.json"] = dict(layer="INTEGRITY", expect="FAIL", expectedRule="INT-01", description="Evidence fixture altered after hashing.",
        patch=[], overrideFile={"path": "evidence-fixtures/EV-001.txt", "content": "tampered"})
    F["business/B-024-manifest-tamper.json"] = dict(layer="MANIFEST", expect="FAIL", expectedRule="MAN-01", description="Dataset file changed after the manifest was built.",
        patch=[], overrideFile={"path": "dataset/capability.jsonld", "append": " "})
    F["business/B-025-signature-claim.json"] = dict(layer="MANIFEST", expect="FAIL", expectedRule="MAN-06", description="Manifest claims a signature that does not exist.",
        patch=[], manifestPatch=[{"op": "set", "field": "integrity.signatureStatus", "value": "SIGNED"}])
    for d in ["valid", "invalid", "business"]:
        for p in (PKG / "tests" / d).glob("*.json"):
            p.unlink()
    for path, fx in F.items():
        fid = Path(path).stem.split("-")
        fx = {"fixtureId": "-".join(fid[:3]) if fid[0] == "I" else "-".join(fid[:2]), **fx}
        fx = {k: v for k, v in fx.items() if v is not None}
        (PKG / "tests" / path).write_text(json.dumps(fx, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (PKG / "tests/invalid/syntax-malformed.jsonld.txt").write_text('{"@context": "../schemas/jsonld/aidcf-context-1.3.jsonld", "@graph": [ {"id": "urn:aidcf:syn:x:1", "type": "Action"\n',
                                                                   encoding="utf-8")
    (PKG / "tests/invalid/syntax-broken.ttl.txt").write_text("@prefix aidcf: <https://w3id.org/aidcf/ontology#> .\n<urn:aidcf:syn:x:1> a aidcf:Action ;\n  aidcf:name \"unterminated\n",
                                                             encoding="utf-8")
    print("fixtures: %d valid, %d invalid, %d business" % tuple(sum(1 for p in F if p.startswith(d)) for d in ["valid", "invalid", "business"]))


def _idx(gr, cid):
    for i, e in enumerate(gr["controlEvaluations"]):
        if e["controlRef"].endswith("/" + cid):
            return i
    raise KeyError(cid)


if __name__ == "__main__":
    main()
