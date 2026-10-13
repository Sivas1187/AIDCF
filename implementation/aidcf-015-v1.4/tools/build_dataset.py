"""Build the AIDCF-015 v1.4 synthetic dataset (AIDCF-016 MDM 1.3).

Deterministic: running it twice produces byte-identical files. Reads the registries copied by
tools/build_registries.py (registries/...) and writes dataset/*.jsonld and evidence-fixtures/*.txt.

Gate roles are the registry per-control roles in registries/controls/gate-mappings.csv. Gate results
are computed with the canonical SPEC 6.2 roll-up in tools/aidcf_rules.py over the 12 assessed controls;
every registry CRITICAL control that was not assessed is carried as NOT_ASSESSED (AIDCF-016 section 9.3).
The builder declares the expected gate table and decision below and stops if the rules disagree, so a
change in data or rules cannot silently change the published results.

All facility data is synthetic. No record describes a real facility, organisation or person.
"""
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG / "tools"))
import aidcf_rules as AR  # noqa: E402

M = AR.M
REL_ID = AR.RELEASE_ID
T0 = "2026-10-10T00:00:00Z"
D0 = "2026-10-10"
CTX = "../schemas/jsonld/aidcf-context-1.3.jsonld"
BUILDER = "AIDCF-015 v1.4 tools/build_dataset.py"
ID = M.ID_BASE

# ------------------------------------------------------------------ expected results (asserted against aidcf_rules)
EXPECTED_GATES = {
    "CG-01": "UNKNOWN", "CG-02": "NOT_ASSESSED", "CG-03": "FAIL", "CG-04": "NOT_ASSESSED", "CG-05": "UNKNOWN",
    "CG-06": "UNKNOWN", "CG-07": "FAIL", "CG-08": "UNKNOWN", "CG-09": "NOT_ASSESSED", "CG-10": "UNKNOWN",
    "CG-11": "NOT_ASSESSED", "CG-12": "NOT_ASSESSED", "CG-13": "NOT_ASSESSED", "CG-14": "NOT_ASSESSED", "CG-15": "FAIL",
}
EXPECTED_DECISION = "NOT_ASSURED"


def syn(kind, local):
    return "urn:aidcf:syn:%s:%s" % (kind, local)


def sha(b):
    return hashlib.sha256(b).hexdigest()


PTY = {k: syn("party", k) for k in ["BUILDER", "REGISTRY-STEWARD", "FAC-OPS", "IT-OPS", "OT-SEC", "UTILITY", "CDU-VENDOR",
                                     "DECISION-AUTH", "QA", "ASSESSOR-A", "ASSESSOR-B", "PROGRAMME-OWNER", "CAP-OWNER"]}
CI = syn("capability", "CI-001")
SNAP = syn("snapshot", "SNAP-001")
ASM = syn("assessment", "ASM-001")
PRG = syn("programme", "PRG-001")
DC = {"CONFIDENTIAL": syn("distribution-control", "DC-001"), "HIGHLY_RESTRICTED": syn("distribution-control", "DC-002")}
SCOPE = {"capabilityRef": CI, "snapshotRef": SNAP}

PROV_SYN = {"sourceSystem": BUILDER, "method": "SYNTHETIC_AUTHORING", "synthetic": True, "transformationVersion": "1.4"}

RECS = {}
QUAL = {}           # (s, prop, o) -> qualifiers for the relationship record
CANDIDATE_EDGES = set()


def rec(rid, typ, name, **f):
    assert rid not in RECS, rid
    meta = M.CLASS_META[typ]
    r = {"id": rid, "type": typ, "semanticOwner": f.pop("semanticOwner", meta["owner"]), "schemaVersion": M.RELEASE,
         "version": f.pop("version", "1.0"), "status": f.pop("status", "REVIEWED"), "releaseRef": REL_ID,
         "sourceArtifact": f.pop("sourceArtifact", "AIDCF-015"), "name": name, "effectiveFrom": T0, "createdAt": T0,
         "createdBy": f.pop("createdBy", PTY["BUILDER"]), "classification": f.pop("classification", "INTERNAL"),
         "provenance": f.pop("provenance", dict(PROV_SYN))}
    if typ in M.ASSERTION_BEARING:
        r["reviewState"] = f.pop("reviewState", "SUPPORTED")
    if typ in M.ASSESSABLE:
        r["scope"] = f.pop("scope", dict(SCOPE))
    RECS[rid] = r
    for k, v in f.items():
        if k in M.REL_BY_PROP:
            for o in AR.as_list(v):
                edge(rid, k, o)
        else:
            r[k] = v
    return r


def edge(s, prop, o, **q):
    r = RECS.get(s)
    if r is not None:
        lst = r.setdefault(prop, [])
        if o not in lst:
            lst.append(o)
    else:
        PENDING.append((s, prop, o))
    if q:
        QUAL.setdefault((s, prop, o), {}).update(q)


PENDING = []


def flush_pending():
    for s, p, o in PENDING:
        lst = RECS[s].setdefault(p, [])
        if o not in lst:
            lst.append(o)
    PENDING.clear()


def dc_for(r):
    c = r.get("classification")
    if M.CLASSIFICATION_RANK[c] > M.CLASSIFICATION_RANK["INTERNAL"]:
        r["distributionControlRef"] = DC["HIGHLY_RESTRICTED" if c == "HIGHLY_RESTRICTED" else "CONFIDENTIAL"]


# ------------------------------------------------------------------ registry-derived records
def gate_claim(reg, g):
    cts = [reg["controls"][c]["claimType"] for c in reg["roles"].get(g, {})]
    return max(cts, key=lambda c: (M.CLAIM_RANK[c], c)) if cts else "DESIGN"


def registry_prov(src, legacy=None):
    p = {"sourceSystem": "AIDCF-007A registry v1.1 (%s)" % src, "method": "REGISTRY_IMPORT", "synthetic": False,
         "transformationVersion": "1.4"}
    if legacy:
        p["legacyValue"] = legacy
    return p


def build_framework(reg):
    for d, row in reg["domains"].items():
        rec(ID + "domain/" + d, "ControlDomain", row["domainName"], status="CANDIDATE", sourceArtifact="AIDCF-007A",
            sourceRecord="registries/domains/domains.csv#" + d, provenance=registry_prov("domains.csv", "status=" + row["status"]),
            domainCode=d)
    for fam, row in reg["families"].items():
        rec(ID + "family/" + fam, "ControlFamily", row["familyName"], status="CANDIDATE", sourceArtifact="AIDCF-007A",
            sourceRecord="registries/families/control-families.csv#" + fam,
            provenance=registry_prov("control-families.csv", "status=" + row["status"]), familyCode=fam, domainCode=row["domainId"])
        edge(ID + "domain/" + row["domainId"], "composedOf", ID + "family/" + fam)
    crit_rows = defaultdict(list)
    for c in reg["criteria"]:
        crit_rows[c["gateId"]].append(c)
    for g, row in reg["gates"].items():
        fc, fr = M.derive_ceiling(row["failCeiling"])
        uc, ur = M.derive_ceiling(row["unknownCeiling"])
        gid = ID + "gate/" + g
        erid = ID + "evidence-requirement/" + g
        rec(erid, "EvidenceRequirement", "%s gate evidence requirement" % g, status="CANDIDATE", sourceArtifact="AIDCF-010",
            sourceRecord="registries/gates/critical-gates.csv#" + g, provenance=registry_prov("critical-gates.csv"),
            claimType=gate_claim(reg, g),
            description="claimType is the highest claim type among the registry controls mapped to %s (AIDCF-016 section 9.6)%s." % (
                g, "" if reg["roles"].get(g) else "; the gate has no mapped controls, so the lowest claim type DESIGN is used pending an AIDCF-010 statement"),
            requiredClasses=[x.strip() for x in row["requiredClasses"].split(";")], sufficiencyFloor=row["evidenceFloor"],
            stateCoverage=["NORMAL", "MAINTENANCE", "DEGRADED"], periodCoverage="Current at the assessment as-of date.",
            independence="Per AIDCF-009 for the gate's controls.")
        rec(gid, "CriticalGate", row["name"], status="CANDIDATE", sourceArtifact="AIDCF-010",
            sourceRecord="registries/gates/critical-gates.csv#" + g, provenance=registry_prov("critical-gates.csv"),
            gateCode=g, gateScope=row["scope"], evidenceFloor=row["evidenceFloor"],
            requiredClasses=[x.strip() for x in row["requiredClasses"].split(";")], failCeiling=fc, unknownCeiling=uc,
            failCeilingText=row["failCeiling"], unknownCeilingText=row["unknownCeiling"],
            ceilingDerivation="failCeiling %s by %s; unknownCeiling %s by %s (AIDCF-016 section 9.4)." % (fc, fr, uc, ur),
            approvedNaConditions=row["approvedNaConditions"],
            gateCriteria=[{"criterionId": c["criterionId"], "criterion": c["criterion"], "testMethod": c["testMethod"]} for c in crit_rows[g]],
            hasEvidenceRequirement=[erid])
    for cid, row in reg["controls"].items():
        cj = reg["controls_json"][cid]
        prof = reg["profiles"][cid]
        erid = ID + "evidence-requirement/%s-%s" % (cid, prof["claimType"])
        qf = dict(zip(["provenanceRating", "fitnessRating", "coverageRating", "reliabilityRating", "timelinessRating", "integrityRating"],
                      [int(x[1:]) for x in prof["qualityFloor"].split()]))
        er = dict(claimType=prof["claimType"], profileTier=prof["profileTier"],
                  requiredClasses=[x.strip() for x in prof["requiredClasses"].split(";")], sufficiencyFloor=prof["sufficiencyFloor"],
                  stateCoverage=[x.strip() for x in prof["stateCoverage"].split(";")], periodCoverage=prof["periodCoverage"],
                  independence=prof["independence"], qualityFloor=qf,
                  mandatoryItems=[x.strip() for x in prof["mandatoryItems"].split(";") if x.strip()])
        if prof["optionalClasses"].strip():
            er["optionalClasses"] = [x.strip() for x in prof["optionalClasses"].split(";")]
        rec(erid, "EvidenceRequirement", "%s evidence requirement (%s)" % (cid, prof["claimType"]), status="CANDIDATE",
            sourceArtifact="AIDCF-007A", sourceRecord="registries/controls/evidence-profiles.csv#" + cid,
            provenance=registry_prov("evidence-profiles.csv"), **er)
        maps = sorted((g, r) for g, roles in reg["roles"].items() for c2, r in roles.items() if c2 == cid)
        rec(ID + "control/" + cid, "Control", row["title"], status="CANDIDATE", sourceArtifact="AIDCF-007A",
            sourceRecord="registries/controls/controls.csv#" + cid,
            provenance=registry_prov("controls.csv", "status=" + row["status"]),
            controlCode=cid, domainCode=row["domainId"], familyCode=row["familyId"], objective=row["objective"],
            requirement=row["requirement"], claimType=row["claimType"], requiredAssuranceLevel=row["requiredAssuranceLevel"],
            controlType=row["controlType"], profileTier=row["profileTier"], applicability=cj["applicability"],
            assessmentCriteria=cj["assessmentCriteria"], assessmentMethods=cj["assessmentMethods"],
            amendmentRef=row["amendmentId"], hasEvidenceRequirement=[erid],
            gateMappings=[{"gateRef": ID + "gate/" + g, "gateRole": r} for g, r in maps])
        for g, r in maps:
            edge(ID + "control/" + cid, "evaluatesGate", ID + "gate/" + g, gateRole=r)
        edge(ID + "family/" + row["familyId"], "composedOf", ID + "control/" + cid)
    for code, lab, d in M.VOCABS["OperatingState"][2]:
        rec(ID + "operating-state/" + code, "OperatingState", lab, status="CANDIDATE", sourceArtifact="AIDCF-003",
            sourceRecord="registries/vocabularies/operating-states.csv#" + code, provenance=registry_prov("operating-states.csv"),
            stateCode=code, entryConditions=d)
    for code, lab, d in M.VOCABS["FoundationalRequirementCode"][2]:
        rec(ID + "foundational-requirement/" + code, "FoundationalRequirement", "%s %s" % (code, lab), status="CANDIDATE",
            sourceArtifact="AIDCF-003", sourceRecord="AIDCF-003 v1.1 Part XVI section 72",
            provenance={"sourceSystem": "AIDCF-003 v1.1 section 72", "method": "MANUAL_ENTRY", "synthetic": False, "transformationVersion": "1.4"},
            frCode=code, description="IEC 62443 foundational requirement %s (%s), as listed in AIDCF-003 v1.1 section 72." % (code, lab))


# ------------------------------------------------------------------ synthetic organisation, capability and architecture
def build_context_records():
    parties = [("BUILDER", "AIDCF-015 dataset builder", "ACTOR"), ("REGISTRY-STEWARD", "Registry steward", "ROLE"),
               ("FAC-OPS", "Synthetic facility operations team", "TEAM"), ("IT-OPS", "Synthetic platform operations team", "TEAM"),
               ("OT-SEC", "Synthetic OT security team", "TEAM"), ("UTILITY", "Synthetic utility provider", "ORGANISATION"),
               ("CDU-VENDOR", "Synthetic CDU vendor", "ORGANISATION"), ("DECISION-AUTH", "Synthetic decision authority", "ROLE"),
               ("QA", "Synthetic quality reviewer", "ROLE"), ("ASSESSOR-A", "Synthetic assessor A", "ACTOR"),
               ("ASSESSOR-B", "Synthetic assessor B", "ACTOR"), ("PROGRAMME-OWNER", "Synthetic programme owner", "ROLE"),
               ("CAP-OWNER", "Synthetic capability owner", "ROLE")]
    for k, n, kind in parties:
        rec(PTY[k], "PartyEntity", n, partyKind=kind)
    for k, n, kind in [("LOC-SITE", "Synthetic site", "SITE"), ("LOC-HALL-A", "Synthetic data hall A", "HALL"),
                       ("LOC-PLANT", "Synthetic plant room", "ROOM")]:
        rec(syn("location", k), "Location", n, locationKind=kind)
    for code, n in [("DC-001", "Confidential: named assessment roles"), ("DC-002", "Highly restricted: named OT security individuals")]:
        mx = "CONFIDENTIAL" if code == "DC-001" else "HIGHLY_RESTRICTED"
        rec(syn("distribution-control", code), "DistributionControl", n,
            permittedRecipients=["Synthetic assessment team", "Synthetic decision authority"] if mx == "CONFIDENTIAL" else ["Synthetic OT security lead"],
            purpose="Synthetic AIDCF-015 conformance pilot only.", redactionProfile="REDACT-%s" % mx,
            exportConditions="No export outside the synthetic conformance package; exports are redacted to INTERNAL.", maxClassification=mx)


SO = {k: syn("outcome", k) for k in ["SO-01", "SO-02", "SO-03"]}
RF = {k: syn("function", k) for k in ["RF-01", "RF-02", "RF-03", "RF-04", "RF-05", "RF-06"]}
A = {}


def a(k):
    return A[k]


def build_capability_architecture():
    for k in ["SYS-POW", "SYS-THM", "SYS-FWS", "SYS-CMP", "SYS-STO", "SYS-NET", "SYS-CTL"]:
        A[k] = syn("system", k)
    for k in ["AST-UPS-A", "AST-UPS-B", "AST-SWB-01", "AST-CDU-1", "AST-CDU-2", "AST-CHL", "AST-GPU-NODES", "AST-STO-ARRAY",
              "AST-FAB-SPINE", "AST-BMS-CTRL", "AST-OT-GW", "AST-UTILITY"]:
        A[k] = syn("asset", k)
    for k in ["ZONE-BMS", "ZONE-REMOTE"]:
        A[k] = syn("zone", k)
    A["CND-01"] = syn("conduit", "CND-01")
    for k in ["IF-PWR-RACK", "IF-FWS-CDU", "IF-FABRIC"]:
        A[k] = syn("interface", k)
    for k in ["RES-UTIL", "RES-WATER"]:
        A[k] = syn("resource", k)
    A["CMPT-BMC"] = syn("component", "CMPT-BMC")
    L = {k: syn("location", k) for k in ["LOC-SITE", "LOC-HALL-A", "LOC-PLANT"]}

    rec(CI, "CapabilityInstance", "Synthetic AI training and inference capability", status="APPROVED",
        owner=PTY["CAP-OWNER"], lifecycle="OPERATE", workload=["TRAINING", "INFERENCE"], architectureBaseline=SNAP,
        criticality="HIGH", boundary="Synthetic data hall A, its power, cooling, facility water, compute, storage, fabric and supervisory control; the utility is external.",
        demandProfile="Illustrative: 2.0 MW IT load with accelerator transients; training jobs of up to 14 days.",
        operatingEnvelope="Illustrative: design ambient 35 C; inlet supply 30 C; NORMAL and MAINTENANCE states.",
        operatingStates=["NORMAL", "MAINTENANCE", "DEGRADED", "RECOVERY"], operatedBy=[PTY["IT-OPS"]],
        hasOutcome=list(SO.values()), migratedFrom=["urn:aidcf:capability:synthetic-training-001"])
    so = [("SO-01", "Training availability", "TRAINING", "Illustrative: training cluster available for scheduled jobs",
           "Illustrative: at most 4 hours unplanned unavailability per 30 days", "P30D", ["NORMAL", "MAINTENANCE"], ["RF-01", "RF-02", "RF-03", "RF-05", "RF-06"]),
          ("SO-02", "Training checkpoint recovery", "TRAINING", "Illustrative: restart from last checkpoint after disruption",
           "Illustrative: restart within 2 hours, losing at most 30 minutes of training progress", "PT2H", ["RECOVERY"], ["RF-04", "RF-05"]),
          ("SO-03", "Inference latency", "INFERENCE", "Illustrative: p99 request latency at the service edge",
           "Illustrative: p99 below 300 ms at declared load", "PT1H", ["NORMAL", "DEGRADED"], ["RF-02", "RF-03", "RF-05"])]
    for k, n, wl, meas, tol, dur, st, rfs in so:
        rec(SO[k], "ServiceOutcome", n, status="APPROVED", workloadClass=wl, measure=meas, tolerance=tol, duration=dur,
            operatingStates=st, requiresFunction=[RF[x] for x in rfs])
    rf = [("RF-01", "Deliver conditioned power", "Deliver conditioned power to IT and cooling loads at design demand.", ["SYS-POW"]),
          ("RF-02", "Remove heat", "Remove 100% of rack heat at design inlet temperature (illustrative).", ["SYS-THM", "SYS-FWS"]),
          ("RF-03", "Provide accelerator compute", "Provide the declared usable accelerator capacity.", ["SYS-CMP"]),
          ("RF-04", "Persist checkpoints", "Persist and restore training checkpoints within the recovery tolerance.", ["SYS-STO"]),
          ("RF-05", "Provide fabric connectivity", "Provide scale-out fabric connectivity between compute and storage.", ["SYS-NET"]),
          ("RF-06", "Supervise facility systems", "Supervise and command power and cooling plant through the BMS.", ["SYS-CTL"])]
    for k, n, st, impl in rf:
        rec(RF[k], "RequiredFunction", n, status="APPROVED", functionStatement=st, operatingStates=["NORMAL", "MAINTENANCE"],
            implementedBy=[a(x) for x in impl])

    def system(k, n, dom, kind, ops, loc, typ="InfrastructureSystem", **f):
        rec(a(k), typ, n, domainCode=dom, systemKind=kind, operatedBy=[PTY[ops]], locatedIn=[L[loc]], **f)

    def asset(k, n, dom, kind, ops, loc, **f):
        rec(a(k), "AssetInstance", n, domainCode=dom, assetKind=kind, operatedBy=[PTY[ops]], locatedIn=[L[loc]], **f)
    asset("AST-UTILITY", "Synthetic utility connection", "POW", "UTILITY_SERVICE", "UTILITY", "LOC-SITE",
          description="External utility supply; represented as an asset because it is a material resource provider.")
    asset("AST-SWB-01", "Synthetic main switchboard", "POW", "SWITCHBOARD", "FAC-OPS", "LOC-PLANT")
    asset("AST-UPS-A", "Synthetic UPS A", "POW", "UPS", "FAC-OPS", "LOC-PLANT")
    asset("AST-UPS-B", "Synthetic UPS B", "POW", "UPS", "FAC-OPS", "LOC-PLANT")
    asset("AST-CHL", "Synthetic chiller", "THM", "CHILLER", "FAC-OPS", "LOC-PLANT")
    asset("AST-CDU-1", "Synthetic CDU 1", "THM", "CDU", "FAC-OPS", "LOC-HALL-A")
    asset("AST-CDU-2", "Synthetic CDU 2", "THM", "CDU", "FAC-OPS", "LOC-HALL-A")
    asset("AST-BMS-CTRL", "Synthetic BMS controller", "SEC", "BMS_CONTROLLER", "OT-SEC", "LOC-PLANT")
    asset("AST-OT-GW", "Synthetic OT remote-access gateway", "SEC", "OT_GATEWAY", "OT-SEC", "LOC-PLANT")
    asset("AST-GPU-NODES", "Synthetic GPU node pool", "CMP", "GPU_NODE_POOL", "IT-OPS", "LOC-HALL-A")
    asset("AST-STO-ARRAY", "Synthetic checkpoint storage array", "STO", "STORAGE_ARRAY", "IT-OPS", "LOC-HALL-A")
    asset("AST-FAB-SPINE", "Synthetic fabric spine", "NET", "SPINE_SWITCH_SET", "IT-OPS", "LOC-HALL-A")
    rec(a("CMPT-BMC"), "Component", "Synthetic node baseboard management controller", componentKind="BMC")
    rec(a("CND-01"), "Conduit", "Synthetic remote-access conduit", classification="HIGHLY_RESTRICTED",
        interfaceKind="IACS_CONDUIT", channels=["Synthetic vendor remote-support channel"], remoteAccess=True,
        countermeasures=["Synthetic jump host with session recording", "Synthetic time-bound activation"])
    for k, n, kind in [("IF-PWR-RACK", "Synthetic rack power interface", "ELECTRICAL"), ("IF-FWS-CDU", "Synthetic facility-water to CDU interface", "FLUID"),
                       ("IF-FABRIC", "Synthetic compute-storage fabric interface", "NETWORK")]:
        rec(a(k), "Interface", n, interfaceKind=kind)
    rec(a("RES-UTIL"), "Resource", "Synthetic utility electrical capacity", resourceKind="POWER")
    rec(a("RES-WATER"), "Resource", "Synthetic make-up water supply", resourceKind="WATER")
    system("SYS-POW", "Synthetic electrical power system", "POW", "POWER_DISTRIBUTION", "FAC-OPS", "LOC-PLANT",
           composedOf=[a("AST-SWB-01"), a("AST-UPS-A"), a("AST-UPS-B")], consumesResource=[a("RES-UTIL")])
    system("SYS-FWS", "Synthetic facility water system", "THM", "FACILITY_WATER", "FAC-OPS", "LOC-PLANT",
           composedOf=[a("AST-CHL")], consumesResource=[a("RES-WATER")])
    system("SYS-THM", "Synthetic liquid-cooling secondary loop", "THM", "CDU_SECONDARY_LOOP", "FAC-OPS", "LOC-HALL-A",
           composedOf=[a("AST-CDU-1"), a("AST-CDU-2")])
    system("SYS-CMP", "Synthetic accelerator compute cluster", "CMP", "COMPUTE_CLUSTER", "IT-OPS", "LOC-HALL-A",
           composedOf=[a("AST-GPU-NODES")])
    system("SYS-STO", "Synthetic checkpoint storage system", "STO", "CHECKPOINT_STORAGE", "IT-OPS", "LOC-HALL-A",
           composedOf=[a("AST-STO-ARRAY")])
    system("SYS-NET", "Synthetic scale-out fabric", "NET", "SCALE_OUT_FABRIC", "IT-OPS", "LOC-HALL-A",
           composedOf=[a("AST-FAB-SPINE")])
    system("ZONE-BMS", "Synthetic BMS IACS zone", "SEC", "IACS_ZONE", "OT-SEC", "LOC-PLANT", typ="IACSZone",
           classification="CONFIDENTIAL", composedOf=[a("AST-BMS-CTRL")], riskAssessmentRef="SYN-RA-OT-001 (synthetic)",
           boundaryDescription="BMS controller and its supervisory network segment.", controlledFunctions=[RF["RF-02"], RF["RF-06"]])
    system("ZONE-REMOTE", "Synthetic remote-access IACS zone", "SEC", "IACS_ZONE", "OT-SEC", "LOC-PLANT", typ="IACSZone",
           classification="CONFIDENTIAL", composedOf=[a("AST-OT-GW")], riskAssessmentRef="SYN-RA-OT-001 (synthetic)",
           boundaryDescription="Remote-access gateway segment for vendor support.", controlledFunctions=[RF["RF-06"]])
    system("SYS-CTL", "Synthetic supervisory control IACS", "SEC", "IACS", "OT-SEC", "LOC-PLANT", typ="IACS",
           composedOf=[a("ZONE-BMS"), a("ZONE-REMOTE")], controlledFunctions=[RF["RF-02"], RF["RF-06"]],
           assetOwner=PTY["FAC-OPS"], integrator=PTY["OT-SEC"], maintainer=PTY["CDU-VENDOR"])
    edge(a("AST-GPU-NODES"), "composedOf", a("CMPT-BMC"))
    for i in ["AST-CDU-1", "AST-CDU-2"]:
        edge(a(i), "controlledBy", a("AST-BMS-CTRL"))
    edge(a("AST-SWB-01"), "monitoredBy", a("AST-BMS-CTRL"))
    for s, i in [("AST-SWB-01", "IF-PWR-RACK"), ("AST-GPU-NODES", "IF-PWR-RACK"), ("AST-CHL", "IF-FWS-CDU"), ("AST-CDU-1", "IF-FWS-CDU"),
                 ("AST-CDU-2", "IF-FWS-CDU"), ("AST-GPU-NODES", "IF-FABRIC"), ("AST-STO-ARRAY", "IF-FABRIC"), ("AST-FAB-SPINE", "IF-FABRIC"),
                 ("ZONE-BMS", "CND-01"), ("ZONE-REMOTE", "CND-01")]:
        edge(a(s), "connectsTo", a(i))


EV = {}          # evidence id by key
EVREC = []       # (key, class, title, text, extra)


def build_evidence_and_dependencies(fixtures_dir):
    """Architecture evidence first (needed by Dependency and FaultDomain records)."""
    arch_ev = [("EV-ARCH-01", "E1", "Synthetic single-line diagram and as-built drawing register", "documentary"),
               ("EV-ARCH-02", "E2", "Synthetic BMS point list and controller configuration export", "configuration"),
               ("EV-ARCH-03", "E2", "Synthetic fabric and storage topology export", "configuration")]
    for k, cls_, title, kind in arch_ev:
        add_evidence(k, cls_, title, "Synthetic %s evidence for the AIDCF-015 v1.4 architecture snapshot." % kind, fixtures_dir,
                     collector="FAC-OPS", sufficiency="S3")
    deps = [  # id, source, target, type, strength, states, evidence, extra
        ("DEP-01", "SYS-POW", "AST-UTILITY", "UTILITY", "MATERIAL", "EV-ARCH-01", {"external": True}),
        ("DEP-02", "AST-UPS-A", "AST-SWB-01", "ELECTRICAL", "ABSOLUTE", "EV-ARCH-01", {"faultDomainRef": syn("fault-domain", "FD-01")}),
        ("DEP-03", "AST-UPS-B", "AST-SWB-01", "ELECTRICAL", "ABSOLUTE", "EV-ARCH-01", {"faultDomainRef": syn("fault-domain", "FD-01")}),
        ("DEP-04", "AST-CDU-1", "AST-CHL", "FLUID", "ABSOLUTE", "EV-ARCH-01", {}),
        ("DEP-05", "AST-CDU-2", "AST-CHL", "FLUID", "ABSOLUTE", "EV-ARCH-01", {}),
        ("DEP-06", "AST-CDU-1", "AST-BMS-CTRL", "CONTROL", "MATERIAL", "EV-ARCH-02", {"faultDomainRef": syn("fault-domain", "FD-02")}),
        ("DEP-07", "AST-CDU-2", "AST-BMS-CTRL", "CONTROL", "MATERIAL", "EV-ARCH-02", {"faultDomainRef": syn("fault-domain", "FD-02")}),
        ("DEP-08", "SYS-STO", "SYS-NET", "NETWORK", "ABSOLUTE", "EV-ARCH-03", {}),
        ("DEP-09", "SYS-CMP", "SYS-POW", "ELECTRICAL", "ABSOLUTE", "EV-ARCH-01", {}),
        ("DEP-10", "SYS-CMP", "SYS-THM", "THERMAL", "ABSOLUTE", "EV-ARCH-01", {}),
        ("DEP-11", "SYS-THM", "SYS-FWS", "FLUID", "ABSOLUTE", "EV-ARCH-01", {}),
        ("DEP-12", "AST-CDU-1", "PTY:CDU-VENDOR", "SUPPLIER", "CONDITIONAL", "EV-ARCH-01", {"external": True}),
        ("DEP-13", "AST-GPU-NODES", "AST-FAB-SPINE", "NETWORK", "ABSOLUTE", "EV-ARCH-03", {}),
        ("DEP-14", "SAF-CDU-FAILOVER", "AST-BMS-CTRL", "CONTROL", "MATERIAL", "EV-ARCH-02", {}),
        ("DEP-15", "SYS-FWS", "RES-WATER", "UTILITY", "ABSOLUTE", "EV-ARCH-01", {"external": True}),
        ("DEP-16", "SYS-NET", "SYS-POW", "ELECTRICAL", "ABSOLUTE", "EV-ARCH-01", {}),
        ("DEP-17", "SYS-CTL", "SYS-POW", "ELECTRICAL", "MATERIAL", "EV-ARCH-01", {}),
    ]
    return deps


def node(k):
    if k.startswith("PTY:"):
        return PTY[k[4:]]
    if k.startswith("SAF-"):
        return syn("safeguard", k)
    return A[k]


def build_dependencies(deps):
    for did, s, t, typ, strength, ev, extra in deps:
        rid = syn("dependency", did)
        rec(rid, "Dependency", "%s depends on %s" % (s, t.replace("PTY:", "")), sourceRef=node(s), targetRef=node(t),
            dependencyType=typ, strength=strength, direction="%s relies on %s" % (s, t.replace("PTY:", "")),
            operatingStates=["NORMAL", "MAINTENANCE"],
            dependencyCriticality="Illustrative: loss degrades or stops the dependent function.",
            substitutability="Illustrative: no substitute within the outcome tolerance." if strength == "ABSOLUTE" else "Illustrative: partial substitution available.",
            evidencedBy=[EV[ev]], confidence="CONF-3", **extra)
        edge(node(s), "dependsOn", node(t), dependencyRef=rid, operatingStates=["NORMAL", "MAINTENANCE"])
    for fd, members, cm in [("FD-01", ["AST-UPS-A", "AST-UPS-B", "AST-SWB-01"], "Common main switchboard upstream of both UPS units."),
                            ("FD-02", ["AST-CDU-1", "AST-CDU-2", "AST-BMS-CTRL"], "Single BMS controller commanding both CDUs.")]:
        fid = syn("fault-domain", fd)
        rec(fid, "FaultDomain", "Synthetic fault domain %s" % fd, faultDomainMembers=[a(m) for m in members], commonMode=cm,
            boundary="Plant room", blastRadius="Both redundant units fail together.", locatedIn=[syn("location", "LOC-PLANT")],
            evidencedBy=[EV["EV-ARCH-01" if fd == "FD-01" else "EV-ARCH-02"]])
        edge(a(members[0]), "sharesFaultDomainWith", a(members[1]), faultDomainRef=fid)


# v1.4: AIDCF-004 library scenarios that trace through the case's existing elements without new ones (the "fits as is"
# group of the X01-X20 fit check). X05 and X12 are not added: they match FS-02 and FS-04. Each tuple: id, name,
# initiators, steps, expected safeguards, outcomes, residual state, pre-state, library scenario, note.
LIBRARY_SOURCE = "foundations/threat-model/AIDCF-004_Threat_Hazard_and_Failure_Model_v1.1.md"
LIBRARY_SCENARIOS = [
    ("FS-06", "Synthetic CDU controller firmware fault stops both CDUs", ["FM-04"],
     [("AST-CDU-1", "SYS-THM"), ("AST-CDU-2", "SYS-THM"), ("SYS-THM", "SYS-CMP"), ("SYS-CMP", "RF-03"), ("RF-03", "SO-01")],
     ["SAF-THROTTLE", "SAF-CKPT"], ["SO-01"], "FAILED", "NORMAL", "X02",
     "One firmware release defeats CDU redundancy: the standby pump depends on the same controller, so CDU failover does not help."),
    ("FS-07", "Synthetic PFC storm from a misconfigured fabric switch", ["FM-05"],
     [("AST-FAB-SPINE", "SYS-NET"), ("SYS-NET", "SYS-CMP"), ("SYS-NET", "SYS-STO"), ("SYS-CMP", "RF-03"), ("SYS-STO", "RF-04"),
      ("RF-03", "SO-01"), ("RF-04", "SO-02")],
     ["SAF-FAB-RR", "SAF-CKPT"], ["SO-01", "SO-02"], "DEGRADED", "NORMAL", "X03",
     "Pause frames spread hop by hop, so collectives stall across the cluster and checkpoint writes stall while links still report healthy."),
    ("FS-08", "Synthetic checkpoint storage saturation during recovery", ["FM-06"],
     [("AST-STO-ARRAY", "SYS-STO"), ("SYS-STO", "SYS-NET"), ("SYS-STO", "RF-04"), ("RF-04", "SO-02")],
     ["SAF-CKPT"], ["SO-02"], "RECOVERY", "RECOVERY", "X04",
     "Starts in recovery after a facility event such as FS-03; the restore storm congests the fabric and recovery exceeds tolerance."),
    ("FS-09", "Synthetic coolant leak at a rack manifold", ["HZ-03"],
     [("SYS-THM", "SYS-POW"), ("SYS-POW", "SYS-CMP"), ("SYS-CMP", "RF-03"), ("RF-03", "SO-01")],
     ["SAF-LEAK"], ["SO-01"], "FAILED", "NORMAL", "X07",
     "CDU make-up masks the leak until coolant reaches rack power. The library's primary outcome, electrical safety, has no outcome in this case and is not recorded."),
    ("FS-10", "Synthetic facility water contamination fouls CDU heat exchangers", ["HZ-04"],
     [("SYS-FWS", "AST-CDU-1"), ("SYS-FWS", "AST-CDU-2"), ("AST-CDU-1", "SYS-THM"), ("AST-CDU-2", "SYS-THM"), ("SYS-THM", "SYS-CMP"),
      ("SYS-CMP", "RF-03"), ("RF-03", "SO-01")],
     ["SAF-THROTTLE"], ["SO-01"], "DEGRADED", "NORMAL", "X08",
     "Fouling raises the approach temperature on both CDUs fed by the same loop (common cause); accelerators throttle at peak load."),
    ("FS-11", "Synthetic concurrent maintenance exposes a shared electrical path", ["FM-07"],
     [("AST-UPS-A", "SYS-POW"), ("SYS-POW", "SYS-CMP"), ("SYS-CMP", "SYS-THM"), ("SYS-CMP", "RF-03"), ("RF-03", "SO-01")],
     ["SAF-UPS-RT", "SAF-CKPT"], ["SO-01"], "DEGRADED", "MAINTENANCE", "X11",
     "Starts in maintenance with UPS A isolated; the load drop and restart surge then disturb cooling control."),
    ("FS-12", "Synthetic alarm flood and operator mis-switching", ["HZ-05", "FM-08"],
     [("AST-UTILITY", "SYS-CTL"), ("SYS-CTL", "AST-SWB-01"), ("AST-SWB-01", "SYS-POW"), ("SYS-POW", "SYS-THM"), ("SYS-POW", "SYS-CMP"),
      ("SYS-THM", "SYS-CMP"), ("SYS-CMP", "RF-03"), ("RF-03", "SO-01")],
     ["SAF-UPS-RT", "SAF-CKPT"], ["SO-01"], "FAILED", "NORMAL", "X16",
     "The feed fault floods supervisory alarms; the operator opens the healthy-side breaker at the switchboard, stopping CDUs and compute on that block."),
]


def build_failure_and_safeguards():
    SG = {}
    sgs = [("SAF-UPS-RT", "Synthetic UPS ride-through", "CORRECT", "AUTOMATIC", "Loss of mains", "PT0S", "SYS-POW",
            ["AST-UPS-A", "AST-UPS-B"], ["MCF-POW-009", "MCF-POW-019"], ["Battery end of life", "Static switch failure"]),
           ("SAF-CDU-FAILOVER", "Synthetic CDU failover", "CORRECT", "AUTOMATIC", "CDU trip or low flow", "PT30S", "SYS-CTL",
            ["AST-CDU-2"], ["MCF-THM-010"], ["Controller failure prevents failover"]),
           ("SAF-LEAK", "Synthetic leak detection and isolation", "DETECT", "HYBRID", "Leak sensor alarm", "PT2M", "PTY:FAC-OPS",
            ["AST-BMS-CTRL"], ["MCF-THM-019", "MCF-OPS-013"], ["Sensor fault", "Alarm not acknowledged"]),
           ("SAF-CKPT", "Synthetic checkpoint and restore", "RECOVER", "AUTOMATIC", "Job failure", "PT30M", "PTY:IT-OPS",
            ["AST-STO-ARRAY"], ["MCF-STO-017", "MCF-RES-016"], ["Corrupt checkpoint"]),
           ("SAF-SEG", "Synthetic OT segmentation and remote-access control", "PREVENT", "AUTOMATIC", "Any remote session request", "PT0S",
            "PTY:OT-SEC", ["CND-01", "AST-OT-GW"], ["MCF-SEC-005", "MCF-SEC-010", "MCF-SUP-021"], ["Rule misconfiguration"]),
           ("SAF-FAB-RR", "Synthetic fabric re-routing", "CORRECT", "AUTOMATIC", "Link or switch failure", "PT1S", "SYS-NET",
            ["AST-FAB-SPINE"], ["MCF-NET-002"], ["Insufficient path diversity"]),
           ("SAF-THROTTLE", "Synthetic accelerator thermal throttling", "CONTAIN", "AUTOMATIC", "Inlet over-temperature", "PT5S", "SYS-CMP",
            ["AST-GPU-NODES"], ["MCF-CMP-019"], ["Firmware disables throttling"])]
    for k, n, fn, act, trig, tta, auth, impl, ctrls, fms in sgs:
        SG[k] = syn("safeguard", k)
        rec(SG[k], "Safeguard", n, classification="CONFIDENTIAL" if k == "SAF-SEG" else "INTERNAL",
            safeguardFunction=fn, activation=act, activationTrigger=trig, timeToAct=tta, authority=node(auth),
            stateCoverage=["NORMAL", "MAINTENANCE"], safeguardFailureModes=fms, governedBy=[ID + "control/" + c for c in ctrls],
            implementedBy=[node(i) for i in impl], operatedBy=[PTY["OT-SEC" if k == "SAF-SEG" else ("IT-OPS" if k in ("SAF-CKPT", "SAF-FAB-RR", "SAF-THROTTLE") else "FAC-OPS")]])
    for s, sg in [("SYS-POW", "SAF-UPS-RT"), ("SYS-THM", "SAF-CDU-FAILOVER"), ("SYS-THM", "SAF-LEAK"), ("AST-CDU-1", "SAF-LEAK"),
                  ("SYS-STO", "SAF-CKPT"), ("AST-BMS-CTRL", "SAF-SEG"), ("ZONE-BMS", "SAF-SEG"), ("SYS-NET", "SAF-FAB-RR"),
                  ("SYS-CMP", "SAF-THROTTLE")]:
        edge(a(s), "protectedBy", SG[sg], operatingStates=["NORMAL", "MAINTENANCE"])
    for s, sg in [("SO-02", "SAF-CKPT"), ("RF-01", "SAF-UPS-RT"), ("SYS-NET", "SAF-FAB-RR")]:
        src = SO.get(s) or RF.get(s) or a(s)
        edge(src, "recoversThrough", SG[sg], operatingStates=["RECOVERY"])
    adv = [("TH-01", "Threat", "Synthetic unauthorised remote command to BMS", {"threatSource": "Synthetic external actor using a vendor remote-access path"},
            "CONFIDENTIAL"),
           ("HZ-01", "Hazard", "Synthetic utility voltage sag", {"hazardType": "UTILITY_DISTURBANCE"}, "INTERNAL"),
           ("HZ-02", "Hazard", "Synthetic heatwave above design ambient", {"hazardType": "ENVIRONMENTAL"}, "INTERNAL"),
           ("FM-01", "FailureMode", "Synthetic switchboard busbar fault", {"failureMechanism": "Busbar insulation breakdown"}, "INTERNAL"),
           ("FM-02", "FailureMode", "Synthetic BMS controller failure", {"failureMechanism": "Controller CPU lock-up after firmware fault"}, "INTERNAL"),
           ("FM-03", "FailureMode", "Synthetic fabric spine optic failure", {"failureMechanism": "Optic degradation and link flap"}, "INTERNAL"),
           # v1.4: initiators of the scenarios instantiated from the AIDCF-004 library (FS-06 to FS-12)
           ("FM-04", "FailureMode", "Synthetic CDU controller firmware fault",
            {"failureMechanism": "A CDU firmware release, deployed to every CDU through the vendor management tool, mishandles a failed "
                                 "differential-pressure sensor and stops the duty and standby pumps"}, "INTERNAL"),
           ("FM-05", "FailureMode", "Synthetic lossless-class misconfiguration on a fabric switch",
            {"failureMechanism": "Inconsistent priority mapping makes one port generate PFC pause frames continuously"}, "INTERNAL"),
           ("FM-06", "FailureMode", "Synthetic checkpoint tier read storm on mass restart",
            {"failureMechanism": "Every interrupted job restarts at once; read demand and metadata operations exceed the tier, "
                                 "which retention had already filled"}, "INTERNAL"),
           ("HZ-03", "Hazard", "Synthetic coolant leak at a rack manifold quick-disconnect", {"hazardType": "FLUID"}, "INTERNAL"),
           ("HZ-04", "Hazard", "Synthetic facility water chemistry excursion", {"hazardType": "CHEMICAL"}, "INTERNAL"),
           ("FM-07", "FailureMode", "Synthetic rack cord misallocation exposed by A-path maintenance",
            {"failureMechanism": "Racks with both cords on the A path lose power when it is isolated; the B path then carries "
                                 "all remaining load at peak"}, "INTERNAL"),
           ("HZ-05", "Hazard", "Synthetic medium-voltage feed fault", {"hazardType": "UTILITY_DISTURBANCE"}, "INTERNAL"),
           ("FM-08", "FailureMode", "Synthetic operator mis-switching under an alarm flood",
            {"failureMechanism": "The alarm flood masks the root alarm and the operator opens the breaker on the healthy side"}, "INTERNAL")]
    ADV = {}
    for k, t, n, f, c in adv:
        ADV[k] = syn(t.lower().replace("failuremode", "failure-mode"), k)
        rec(ADV[k], t, n, classification=c, **f)
    for s, k in [("AST-SWB-01", "FM-01"), ("AST-BMS-CTRL", "FM-02"), ("AST-BMS-CTRL", "TH-01"), ("SYS-POW", "HZ-01"),
                 ("SYS-FWS", "HZ-02"), ("AST-FAB-SPINE", "FM-03"), ("AST-CDU-1", "FM-04"), ("AST-CDU-2", "FM-04"),
                 ("AST-FAB-SPINE", "FM-05"), ("AST-STO-ARRAY", "FM-06"), ("SYS-THM", "HZ-03"), ("SYS-FWS", "HZ-04"),
                 ("AST-UPS-A", "FM-07"), ("AST-UTILITY", "HZ-05"), ("SYS-CTL", "FM-08")]:
        edge(a(s), "exposedTo", ADV[k])
    edge(CI, "exposedTo", ADV["HZ-02"])

    def X(k):
        return SO.get(k) or RF.get(k) or a(k)
    scen = [("FS-01", "Synthetic switchboard failure", ["FM-01"], [("AST-SWB-01", "AST-UPS-A"), ("AST-SWB-01", "AST-UPS-B"),
             ("AST-UPS-A", "SYS-POW"), ("SYS-POW", "RF-01"), ("RF-01", "SO-01")], ["SAF-UPS-RT"], "SO-01", "FAILED"),
            ("FS-02", "Synthetic BMS controller loss or unauthorised command", ["FM-02", "TH-01"], [("AST-BMS-CTRL", "AST-CDU-1"),
             ("AST-BMS-CTRL", "AST-CDU-2"), ("AST-CDU-1", "SYS-THM"), ("SYS-THM", "RF-02"), ("RF-02", "SO-01")],
             ["SAF-CDU-FAILOVER", "SAF-SEG", "SAF-LEAK"], "SO-01", "DEGRADED"),
            ("FS-03", "Synthetic utility sag affecting fabric and checkpoints", ["HZ-01"], [("AST-UTILITY", "SYS-POW"), ("SYS-POW", "SYS-NET"),
             ("SYS-NET", "SYS-STO"), ("SYS-STO", "RF-04"), ("RF-04", "SO-02")], ["SAF-UPS-RT", "SAF-CKPT"], "SO-02", "RECOVERY"),
            ("FS-04", "Synthetic heatwave and chiller trip", ["HZ-02"], [("RES-WATER", "SYS-FWS"), ("SYS-FWS", "AST-CHL"), ("AST-CHL", "AST-CDU-2"),
             ("AST-CDU-2", "SYS-THM"), ("SYS-THM", "SYS-CMP"), ("SYS-CMP", "RF-03"), ("RF-03", "SO-03")], ["SAF-THROTTLE", "SAF-LEAK"], "SO-03", "DEGRADED"),
            ("FS-05", "Synthetic fabric spine optic failure", ["FM-03"], [("AST-FAB-SPINE", "SYS-NET"), ("SYS-NET", "RF-05"), ("RF-05", "SO-01")],
             ["SAF-FAB-RR"], "SO-01", "DEGRADED")]
    scen = [x + ("NORMAL", None, None) for x in scen] + LIBRARY_SCENARIOS
    for k, n, init, steps, sgs_, outs, resid, pre, lib, note in scen:
        fid = syn("scenario", k)
        step_ids = []
        for i, (s, t) in enumerate(steps, 1):
            rr = rel_id(X(s), "propagatesTo", X(t), fid)
            step_ids.append(rr)
            edge(X(s), "propagatesTo", X(t))
            QUAL.setdefault(("PROP", X(s), X(t)), []).append(dict(id=rr, scenarioRef=fid, stepOrdinal=i, operatingStates=[pre]))
        extra = {}
        if lib:
            extra = dict(sourceRecord="%s#%s" % (LIBRARY_SOURCE, lib),
                         description="Instantiates AIDCF-004 library scenario %s in the synthetic case. %s" % (lib, note))
        rec(fid, "FailureScenario", n, classification="CONFIDENTIAL" if "TH-01" in init else "INTERNAL", preState=pre,
            propagationSteps=step_ids, expectedSafeguards=[SG[x] for x in sgs_], residualState=resid,
            outcomeEffects=[{"outcomeRef": SO[o], "effect": "Illustrative: outcome breaches tolerance without the expected safeguards.",
                             "exceedsTolerance": True} for o in ([outs] if isinstance(outs, str) else outs)], confidence="CONF-2", **extra)
        for x in init:
            edge(ADV[x], "initiates", fid)
    return SG


def rel_id(s, p, o, extra=""):
    return syn("rel", "REL-" + sha(("%s|%s|%s|%s" % (s, p, o, extra)).encode())[:16])


# ------------------------------------------------------------------ evidence
def add_evidence(key, eclass, title, body, fixtures_dir, collector="ASSESSOR-A", sufficiency="S3", legacy=None, states=None, flags=None):
    rid = syn("evidence", key)
    text = ("SYNTHETIC EVIDENCE FIXTURE - AIDCF-015 v1.4\nid: %s\nclass: %s\ntitle: %s\n%s\n"
            "This file describes no real facility, organisation or person.\n") % (rid, eclass, title, body)
    data = text.encode("utf-8")
    (fixtures_dir / (key + ".txt")).write_bytes(data)
    prov = dict(PROV_SYN)
    prov["sha256"] = sha(data)
    if legacy:
        prov["legacyValue"] = legacy
    f = {}
    if flags:
        f["confidenceFlags"] = flags
    rec(rid, "EvidenceObject", title, provenance=prov, evidenceClass=eclass, evidenceSource="Synthetic source system", collector=PTY[collector],
        custodian=PTY["QA"], periodStart="2026-07-01", periodEnd="2026-09-30", operatingStates=states or ["NORMAL"],
        integrityLevel="I3", sha256=sha(data), byteSize=len(data), mediaType="text/plain",
        qualityVector={"provenanceRating": 3, "fitnessRating": 3, "coverageRating": 3, "reliabilityRating": 3, "timelinessRating": 3, "integrityRating": 3},
        qualityBand="Q3", sufficiency=sufficiency, fixturePath="evidence-fixtures/%s.txt" % key, **f)
    EV[key] = rid
    return rid


ASSESSED = [  # CA, control, subject key, result, sufficiency, classes evidenced, maturity, assessor
    ("CA-001", "MCF-CAP-001", "CI", "CONFORMING", "S3", ["E1", "E2", "E7"], "IM3"),
    ("CA-002", "MCF-DEP-001", "SNAP", "PARTIAL", "S4", ["E1", "E2"], "IM2"),
    ("CA-003", "MCF-POW-001", "SYS-POW", "CONFORMING", "S5", ["E1", "E2", "E3", "E7"], "IM4"),
    ("CA-004", "MCF-THM-009", "SYS-THM", "PARTIAL", "S3", ["E1", "E7"], "IM2"),
    ("CA-005", "MCF-CMP-001", "SYS-CMP", "CONFORMING", "S3", ["E1", "E7"], "IM3"),
    ("CA-006", "MCF-STO-017", "SYS-STO", "CONFORMING", "S4", ["E2", "E3", "E4"], "IM4"),
    ("CA-007", "MCF-NET-001", "SYS-NET", "CONFORMING", "S4", ["E1", "E2", "E3"], "IM3"),
    ("CA-008", "MCF-OPS-013", "SYS-CTL", "PARTIAL", "S4", ["E2", "E3"], "IM2"),
    ("CA-009", "MCF-RES-017", "SYS-POW", "UNKNOWN", "S2", ["E3"], None),
    ("CA-010", "MCF-SUP-021", "CND-01", "PARTIAL", "S4", ["E1", "E2"], "IM2"),
    ("CA-011", "MCF-SEC-005", "ZONE-BMS", "PARTIAL", "S4", ["E1", "E2", "E3", "E4"], "IM2"),
    ("CA-012", "MCF-EVA-017", "ASM", "CONFORMING", "S3", ["E1", "E7"], "IM3"),
]
V12_CLASS = {1: "CONFIGURATION", 2: "OPERATIONAL", 3: "VALIDATION", 4: "DOCUMENTARY", 5: "CONFIGURATION", 6: "OPERATIONAL",
             7: "VALIDATION", 8: "DOCUMENTARY", 9: "CONFIGURATION", 10: "OPERATIONAL", 11: "VALIDATION", 12: "DOCUMENTARY"}
CLASS_WORD = {"E1": "documentary", "E2": "configuration", "E3": "operational", "E4": "test", "E7": "analytical"}
RATIONALE = {
    "CA-001": "Synthetic capability register entry with owner, lifecycle and approval; configuration extract and traceability analysis cover all three required classes at S3.",
    "CA-002": "Asset-to-function mapping covers power, cooling and compute but omits the facility water plant and recovery dependencies (F-001).",
    "CA-003": "Utility capacity evidenced by documentary, configuration, operational metering and analytical evidence at S5.",
    "CA-004": "Direct-to-chip design reviewed; the design basis does not state cold-plate flow at the transient envelope (F-002).",
    "CA-005": "Accelerator architecture design and analysis evidence meet the DESIGN claim at S3.",
    "CA-006": "Checkpoint durability shown by configuration, operational logs and a synthetic restore test (TST-001) at S4.",
    "CA-007": "Fabric topology documented, exported and observed at S4; topology export age recorded as U-002 (US2).",
    "CA-008": "Alarm rationalisation completed for power but not for cooling and leak alarms (F-003).",
    "CA-009": "Component tests evidenced only by operational records; no E4 test evidence at the S3 floor, so the result is UNKNOWN (U-001).",
    "CA-010": "Support identity controls exist for the remote-access conduit, but vendor accounts are not time-bound (F-004).",
    "CA-011": "BMS and EPMS security controls partly effective; write authority to the BMS controller is not restricted to named identities (F-005).",
    "CA-012": "Gate applicability recorded for all fifteen gates with rationale and no APPROVED_NA claim.",
}


def build_assessment(reg, fixtures_dir, SG):
    n_extra = 13
    ca_ids = {}
    ca_ev = {}
    for i, (ca, cid, subj, res, suff_, classes, mat) in enumerate(ASSESSED, 1):
        ca_ids[ca] = syn("control-assessment", ca)
        evs = []
        for j, ec in enumerate(classes):
            if j == 0:
                key = "EV-%03d" % i
                legacy = "v1.2 evidenceClass=%s" % V12_CLASS[i]
            else:
                key = "EV-%03d" % n_extra
                n_extra += 1
                legacy = None
            add_evidence(key, ec, "Synthetic %s evidence for %s" % (CLASS_WORD[ec], cid),
                         "Synthetic %s evidence supporting the %s assessment %s." % (CLASS_WORD[ec], cid, ca), fixtures_dir,
                         collector="ASSESSOR-A" if i % 2 else "ASSESSOR-B", sufficiency=suff_, legacy=legacy,
                         flags=["STALE"] if ca == "CA-007" and ec == "E2" else None)
            if j == 0:
                edge(EV[key], "migratedFrom", "urn:aidcf:evidence:EV-%03d" % i, migrationRef=syn("migration", "MIG-002"))
            evs.append(EV[key])
        ca_ev[ca] = evs
    # capacity evidence
    add_evidence("EV-%03d" % n_extra, "E3", "Synthetic UPS load and runtime metering", "Synthetic metering for capacity assertion CAP-CAP-02.",
                 fixtures_dir, collector="FAC-OPS", sufficiency="S4")
    cap_ev = EV["EV-%03d" % n_extra]
    n_extra += 1
    # capacity assertions and assertions
    rec(syn("capacity-assertion", "CAP-CAP-01"), "CapacityAssertion", "Synthetic UPS capacity (superseded)", status="SUPERSEDED",
        reviewState="SUPERSEDED", subjectRef=a("SYS-POW"), metric="UPS output capacity", assertedValue=1.8, unit="MW",
        operatingStates=["NORMAL"], environment="Illustrative: 35 C plant-room ambient", duration="PT10M", derating="Illustrative: none applied",
        evidenceDate="2026-06-30", confidence="CONF-2", illustrative=True, evidencedBy=[EV["EV-ARCH-01"]])
    rec(syn("capacity-assertion", "CAP-CAP-02"), "CapacityAssertion", "Synthetic UPS capacity", subjectRef=a("SYS-POW"),
        metric="UPS output capacity", assertedValue=2.0, unit="MW", operatingStates=["NORMAL", "MAINTENANCE"],
        environment="Illustrative: 35 C plant-room ambient", duration="PT10M", derating="Illustrative: 10% derating for ambient",
        evidenceDate="2026-09-30", confidence="CONF-3", illustrative=True, evidencedBy=[cap_ev],
        supersedes=[syn("capacity-assertion", "CAP-CAP-01")])
    edge(cap_ev, "supports", syn("capacity-assertion", "CAP-CAP-02"))
    rec(syn("assertion", "ASR-01"), "Assertion", "Synthetic BMS zone boundary assertion", classification="CONFIDENTIAL",
        subjectRef=a("ZONE-BMS"), predicate="boundaryDefinedBy", objectValue="SYN-RA-OT-001 (synthetic)",
        assertionConditions="NORMAL state; current firmware baseline", confidence="CONF-3")
    rec(syn("assertion", "ASR-02"), "Assertion", "Synthetic facility water exclusivity assertion", reviewState="UNKNOWN",
        subjectRef=a("SYS-FWS"), predicate="dedicatedToCapability", objectRef=CI,
        assertionConditions="All states; cannot be determined (U-003)", confidence="CONF-0")
    rec(syn("security-level", "SL-01"), "SecurityLevel", "Synthetic SL-T for the BMS zone", classification="CONFIDENTIAL",
        securityLevelKind="SL-T", subjectRef=a("ZONE-BMS"), slVector={"fr%d" % i: v for i, v in enumerate([2, 2, 2, 1, 2, 2, 2], 1)},
        basis="Synthetic zone risk assessment SYN-RA-OT-001 (illustrative values).")
    rec(syn("security-level", "SL-02"), "SecurityLevel", "Synthetic SL-C for the BMS controller", classification="CONFIDENTIAL",
        securityLevelKind="SL-C", subjectRef=a("AST-BMS-CTRL"), slVector={"fr%d" % i: v for i, v in enumerate([2, 1, 2, 1, 2, 1, 2], 1)},
        basis="Synthetic vendor capability statement (illustrative values).")
    # programme, assessment
    rec(PRG, "AssuranceProgram", "Synthetic AIDCF-015 assurance programme", programOwner=PTY["PROGRAMME-OWNER"],
        decisionAuthority=PTY["DECISION-AUTH"], targetAssuranceLevel="AL4", profileRef="AIDCF-007A v1.1 full catalogue (unweighted)",
        cadence="Illustrative: annual reassessment and event-driven triggers", charter="governance/program-charter.json",
        composedOf=[ASM])
    # procedures, samples, tests, control assessments
    for i, (ca, cid, subj, res, suff_, classes, mat) in enumerate(ASSESSED, 1):
        cj = reg["controls_json"][cid]
        row = reg["controls"][cid]
        pid = syn("procedure", "AP-%03d" % i)
        rec(pid, "AssessmentProcedure", "Procedure for %s" % cid, controlRef=ID + "control/" + cid, claimType=row["claimType"],
            procedureSteps=cj["assessmentProcedure"], assessmentMethods=cj["assessmentMethods"], resultsIn=[ca_ids[ca]])
        subject = {"CI": CI, "SNAP": SNAP, "ASM": ASM}.get(subj) or a(subj)
        f = dict(subjectRef=subject, claimType=row["claimType"], applicabilityBasis="In scope: the control applies to the synthetic capability boundary.",
                 result=res, resultRationale=RATIONALE[ca], assessmentMethods=cj["assessmentMethods"],
                 operatingStates=["NORMAL"], confidence="CONF-1" if res == "UNKNOWN" else "CONF-3", evidenceSufficiency=suff_,
                 assessor=PTY["ASSESSOR-A" if i % 2 else "ASSESSOR-B"], assessedAt="2026-10-01",
                 governedBy=[pid, ID + "control/" + cid], evidencedBy=ca_ev[ca], reviewedBy=[syn("review", "RR-001")],
                 migratedFrom=["urn:aidcf:assessment:" + ca])
        if mat:
            f["implementationMaturity"] = mat
        cl = "CONFIDENTIAL" if cid.startswith(("MCF-SEC", "MCF-SUP")) else "INTERNAL"
        rec(ca_ids[ca], "ControlAssessment", "%s assessment of %s" % (ca, cid), classification=cl, **f)
        edge(ID + "control/" + cid, "assessedBy", ca_ids[ca])
        for e in ca_ev[ca]:
            edge(e, "supports", ca_ids[ca])
            edge(ID + "evidence-requirement/%s-%s" % (cid, row["claimType"]), "evidencedBy", e)
        for m in ["migratedFrom"]:
            for o in RECS[ca_ids[ca]][m]:
                QUAL.setdefault((ca_ids[ca], m, o), {})["migrationRef"] = syn("migration", "MIG-002")
    rec(syn("sample", "SMP-001"), "Sample", "Synthetic sample of required functions for MCF-DEP-001",
        population="Six required functions RF-01 to RF-06", sampleSize=6, selectionMethod="Whole population",
        sizeRationale="Population is small enough to examine in full.", resultsIn=[ca_ids["CA-002"]])
    rec(syn("test", "TST-001"), "TestRecord", "Synthetic checkpoint restore test", procedureRef=syn("procedure", "AP-006"),
        testAuthority=PTY["IT-OPS"], preconditions="Synthetic test cluster; no production workload.",
        safetyControls="Non-intrusive; synthetic environment only.", procedureSteps=["Write checkpoint", "Fail job", "Restore", "Verify state hash"],
        observations="Synthetic restore within tolerance.", testOutcome="Synthetic: passed", testDate="2026-09-20", resultsIn=[ca_ids["CA-006"]])
    rec(syn("test", "TST-002"), "TestRecord", "Synthetic BMS write-authority test", classification="CONFIDENTIAL",
        procedureRef=syn("procedure", "AP-011"), testAuthority=PTY["OT-SEC"], preconditions="Synthetic controller simulator only.",
        safetyControls="No live controller; simulator only.", procedureSteps=["Attempt write with unnamed account", "Record result"],
        observations="Synthetic: write accepted from shared engineering account.", testOutcome="Synthetic: failed criterion",
        testDate="2026-09-22", resultsIn=[ca_ids["CA-011"]])
    all_ev = sorted(EV.values())
    rec(syn("evidence-package", "EP-001"), "EvidencePackage", "Synthetic evidence package", composedOf=all_ev, sufficiency="S3",
        custodian=PTY["QA"], sealedAt=T0, sha256=sha("\n".join(RECS[e]["sha256"] for e in all_ev).encode()))
    return ca_ids, ca_ev


def build_challenges(ca_ids, ca_ev):
    fnd = [("F-001", "CA-002", "MCF-DEP-001", "Asset-to-function mapping omits the facility water plant and recovery dependencies.",
            "Mapping scope limited to IT-adjacent plant.", "Shared-source dependencies for RF-02 cannot be analysed.", "WEAKNESS",
            "CRITICAL input to CG-03 is PARTIAL: CG-03 FAIL.", "Scored PARTIAL (50).", "FAC-OPS", "INTERNAL"),
           ("F-002", "CA-004", "MCF-THM-009", "Design basis does not state cold-plate flow at the transient envelope.",
            "Vendor data not incorporated.", "Thermal margin under transients is not demonstrated.", "WEAKNESS",
            "SUPPORTING input to CG-06; no gate-level defeat on its own.", "Scored PARTIAL (50).", "FAC-OPS", "INTERNAL"),
           ("F-003", "CA-008", "MCF-OPS-013", "Cooling and leak alarms are not rationalised.", "Rationalisation programme incomplete.",
            "Critical alarms may not reach the operator with a defined response.", "SIGNIFICANT_WEAKNESS",
            "CRITICAL input to CG-07 is PARTIAL: CG-07 FAIL.", "Scored PARTIAL (50).", "FAC-OPS", "INTERNAL"),
           ("F-004", "CA-010", "MCF-SUP-021", "Vendor support accounts on the remote-access conduit are not time-bound.",
            "Standing vendor access retained for convenience.", "Third-party access is not revoked in a timely way.", "SIGNIFICANT_WEAKNESS",
            "CRITICAL input to CG-15 is PARTIAL: CG-15 FAIL.", "Scored PARTIAL (50).", "OT-SEC", "CONFIDENTIAL"),
           ("F-005", "CA-011", "MCF-SEC-005", "Write authority to the BMS controller is not restricted to named identities.",
            "Shared engineering account in use.", "Unattributable commands to cooling and power plant are possible.", "SIGNIFICANT_WEAKNESS",
            "CRITICAL input to CG-07 is PARTIAL: CG-07 FAIL.", "Scored PARTIAL (50).", "OT-SEC", "CONFIDENTIAL")]
    F = {}
    for i, (k, ca, cid, cond, cause, cons, fc, ge, se, owner, cl) in enumerate(fnd, 1):
        F[k] = syn("finding", k)
        rec(F[k], "Finding", "%s %s" % (k, cid), classification=cl, criterionRef=cid, condition=cond, cause=cause, consequence=cons,
            evidencedBy=[ca_ev[ca][0]], findingClass=fc, gateEffect=ge, scoreEffect=se, owner=PTY[owner], findingStatus="OPEN",
            requiresAction=[syn("action", "ACT-%03d" % i)], reportedIn=[syn("report", "RPT-001")])
        edge(ca_ids[ca], "hasFinding", F[k])
    F["F-006"] = syn("finding", "F-006")
    rec(F["F-006"], "Finding", "F-006 evidence register naming", criterionRef="MCF-EVA-017",
        condition="Two evidence fixtures used inconsistent file naming.", cause="Manual naming.", consequence="Minor retrieval delay.",
        evidencedBy=[ca_ev["CA-012"][0]], findingClass="OBSERVATION", gateEffect="None.", scoreEffect="None.", owner=PTY["FAC-OPS"],
        findingStatus="CLOSED", closedBy=[syn("review", "RR-003")], reviewedBy=[syn("review", "RR-003")])
    edge(ASM, "hasFinding", F["F-006"])
    U = {}
    unk = [("U-001", "CA-009", "E4 test evidence for MCF-RES-017", "U1", "US3", "No component test records at the S3 floor were provided.",
            "Control result UNKNOWN; decision capped at CONDITIONALLY_ASSURED by this UNKNOWN alone.", "Component test reports (E4).",
            "Receipt of E4 test records", "DISPOSITIONED", "IT-OPS", [("DR", "CONDITION"), ("AD", "CONDITION")], "INTERNAL"),
           ("U-002", "CA-007", "Current fabric topology export", "U3", "US2", "Topology export is older than the evidence currency window.",
            "Limitation recorded; no ceiling.", "Fresh topology export.", "Next topology export", "OPEN", "IT-OPS", [("GR:CG-08", "LIMITATION")], "INTERNAL"),
           ("U-003", "SYS-FWS", "Exclusivity of the facility water plant", "U10", "US5",
            "It cannot be determined whether the facility water plant is shared with other tenants.",
            "Systemic: decision capped at INCONCLUSIVE by this UNKNOWN alone; CG-03 and CG-06 cannot pass.", "Facility water service agreement and plant schematic.",
            "Receipt of the water service agreement", "DISPOSITIONED", "FAC-OPS",
            [("GR:CG-03", "GATE_EFFECT"), ("GR:CG-06", "GATE_EFFECT"), ("DR", "CEILING"), ("AD", "CEILING")], "INTERNAL"),
           ("U-004", "GR:CG-10", "Integrated cross-domain recovery exercise (GC-10-5)", "U1", "US4",
            "No integrated recovery exercise within the evidence currency window was provided.",
            "Critical: CG-10 UNKNOWN; decision capped at LIMITED by this UNKNOWN alone.", "Integrated recovery exercise report.",
            "Completion of a synthetic integrated exercise", "DISPOSITIONED", "IT-OPS", [("GR:CG-10", "GATE_EFFECT"), ("DR", "CEILING"), ("AD", "CEILING")], "INTERNAL"),
           ("U-005", "ZONE-BMS", "Achieved security level (SL-A) of the BMS zone", "U1", "US4",
            "SL-T and SL-C are recorded but no assessment of SL-A was provided.",
            "Critical: CG-07 cannot pass; decision capped at LIMITED by this UNKNOWN alone.", "Zone SL-A assessment.",
            "Completion of the SL-A assessment", "DISPOSITIONED", "OT-SEC", [("GR:CG-07", "GATE_EFFECT"), ("DR", "CEILING"), ("AD", "CEILING")], "CONFIDENTIAL")]
    for i, (k, subj, miss, ut, us, reason, eff, need, trig, st, owner, cons, cl) in enumerate(unk, 1):
        U[k] = syn("unknown", k)
        f = dict(subjectRef=None, missingAttribute=miss, unknownType=ut, unknownSeverity=us, reason=reason, material=us != "US2",
                 decisionEffect=eff, evidenceNeeded=need, owner=PTY[owner], resolutionTrigger=trig, unknownStatus=st,
                 requiresAction=[syn("action", "ACT-%03d" % (5 + i))], reportedIn=[syn("report", "RPT-001")])
        if st == "DISPOSITIONED":
            f["disposition"] = "Owner accepted; evidence requested; decision effect applied until resolved."
            f["dueDate"] = "2026-12-15"
        U[k] = syn("unknown", k)
        U_subject = subj
        f["subjectRef"] = U_subject
        UNKNOWN_DEFS.append((k, subj, cons))
        rec(U[k], "UnknownRecord", "%s %s" % (k, miss), classification=cl, **{x: y for x, y in f.items() if x != "subjectRef"},
            subjectRef="PLACEHOLDER")
    return F, U


UNKNOWN_DEFS = []


def resolve_unknown_subjects(U, ca_ids, GR):
    for k, subj, cons in UNKNOWN_DEFS:
        if subj.startswith("CA-"):
            s = ca_ids[subj]
        elif subj.startswith("GR:"):
            s = GR[subj[3:]]
        else:
            s = a(subj)
        RECS[U[k]]["subjectRef"] = s
        edge(s, "hasUnknown", U[k])
        for tgt, ct in cons:
            t = GR[tgt[3:]] if tgt.startswith("GR:") else {"DR": syn("recommendation", "DR-001"), "AD": syn("decision", "AD-001")}[tgt]
            edge(U[k], "constrains", t, constraintType=ct)
    edge(syn("assertion", "ASR-02"), "hasUnknown", U["U-003"])
    edge(U["U-003"], "challenges", syn("assertion", "ASR-02"))
    edge(U["U-002"], "qualifies", ca_ids["CA-007"])


# ------------------------------------------------------------------ gates, score, decision
CRITERIA_OUTCOMES = {
    "GC-01-1": ("MET", "CAP-001 register entry and approval evidenced at S3."),
    "GC-03-1": ("NOT_MET", "F-001: facility water plant and recovery dependencies not mapped."),
    "GC-03-3": ("UNKNOWN", "U-003: shared facility water plant cannot be determined."),
    "GC-05-1": ("MET", "POW-001 utility capacity evidenced at S5."),
    "GC-06-5": ("UNKNOWN", "U-003: water continuity depends on an undetermined shared plant."),
    "GC-07-5": ("UNKNOWN", "U-005: SL-A not evidenced; write authority partly restricted (F-005)."),
    "GC-07-6": ("NOT_MET", "F-003: cooling and leak alarms not rationalised."),
    "GC-08-4": ("MET", "STO-017 checkpoint throughput and headroom evidenced at S4."),
    "GC-10-5": ("UNKNOWN", "U-004: no integrated cross-domain recovery exercise."),
    "GC-15-4": ("NOT_MET", "F-004: vendor remote access not time-bound."),
}


def build_gates(reg, ca_ids, ca_ev, F, U):
    GR = {g: syn("gate-result", "GR-" + g) for g in reg["gates"]}
    results = {cid: res for (_, cid, _, res, _, _, _) in ASSESSED}
    ca_of = {cid: ca_ids[ca] for (ca, cid, *_rest) in ASSESSED}
    find_of = {"MCF-DEP-001": ["F-001"], "MCF-THM-009": ["F-002"], "MCF-OPS-013": ["F-003"], "MCF-SUP-021": ["F-004"], "MCF-SEC-005": ["F-005"]}
    for g in sorted(reg["gates"]):
        roles = reg["roles"].get(g, {})
        evals = []
        for c in sorted(roles):
            if roles[c] == "CRITICAL" or c in results:
                e = {"controlRef": ID + "control/" + c, "gateRole": roles[c], "controlResult": results.get(c, "NOT_ASSESSED")}
                if c in ca_of:
                    e["controlAssessmentRef"] = ca_of[c]
                    edge(ca_of[c], "evaluatesGate", GR[g])
                evals.append(e)
        crit = [{"criterionId": c["criterionId"], "criterionOutcome": CRITERIA_OUTCOMES.get(c["criterionId"], ("NOT_EVALUATED",))[0],
                 **({"rationale": CRITERIA_OUTCOMES[c["criterionId"]][1]} if c["criterionId"] in CRITERIA_OUTCOMES else {})}
                for c in reg["criteria"] if c["gateId"] == g]
        evaluated = any(e["controlResult"] != "NOT_ASSESSED" for e in evals if e["gateRole"] == "CRITICAL") or \
            any(c["criterionOutcome"] != "NOT_EVALUATED" for c in crit)
        evid = sorted({x for c in results if c in roles for x in ca_ev[[k for (k, cc, *_r) in ASSESSED if cc == c][0]]})
        f = dict(gateCode=g, gateApplicability="IN_SCOPE", controlEvaluations=evals, criteriaResults=crit,
                 evidenceSufficiency="S2" if (evaluated or evid) else "S0", stateCoverage=["NORMAL"],
                 gateState="PENDING", decisionEffect="", rollupRationale="", reviewedBy=[syn("review", "RR-006")],
                 migratedFrom=["urn:aidcf:gate:" + g], reportedIn=[syn("report", "RPT-001")])
        if evid:
            f["evidencedBy"] = evid
        rec(GR[g], "GateResult", "Gate result %s" % g, **f)
        edge(GR[g], "evaluatesGate", ID + "gate/" + g)
        QUAL.setdefault((GR[g], "migratedFrom", "urn:aidcf:gate:" + g), {})["migrationRef"] = syn("migration", "MIG-002")
        for c in sorted(roles):
            if roles[c] == "CRITICAL":
                for fk in find_of.get(c, []):
                    edge(GR[g], "hasFinding", F[fk])
        # gate evidence requirement coverage (TR-09)
        er = ID + "evidence-requirement/" + g
        req = set(RECS[er]["requiredClasses"])
        for x in evid:
            if RECS[x]["evidenceClass"] in req:
                edge(er, "evidencedBy", x)
    return GR


def finalise_gates(reg, GR):
    ix = AR.Index(list(RECS.values()))
    results = {k: v[0] for k, v in AR.control_results(ix).items()}
    states = {}
    for g in sorted(reg["gates"]):
        r = RECS[GR[g]]
        crit_out = {c["criterionId"]: c["criterionOutcome"] for c in r["criteriaResults"]}
        sup = [e for e in r["controlEvaluations"] if e["gateRole"] == "SUPPORTING"]
        state, why = AR.rollup(g, reg, results, crit_out, AR.gate_attached_unknowns(ix, GR[g]), r["evidenceSufficiency"], sup)
        if state != EXPECTED_GATES[g]:
            sys.exit("build_dataset: %s computed %s but the declared table says %s (%s)" % (g, state, EXPECTED_GATES[g], why))
        fc, uc = RECS[ID + "gate/" + g]["failCeiling"], RECS[ID + "gate/" + g]["unknownCeiling"]
        r["gateState"] = state
        r["rollupRationale"] = why
        r["decisionEffect"] = ("Gate %s caps the decision at %s." % (state, fc if state == "FAIL" else uc)) if state != "PASS" else "No cap."
        states[g] = state
    return states


def build_score_decision(reg, GR, U, ca_ids, states):
    ix = AR.Index(list(RECS.values()))
    results = {k: v[0] for k, v in AR.control_results(ix).items()}
    open_us = [u for u in ix.of("UnknownRecord") if AR.open_unknown(u)]
    sc = AR.compute_score(reg, results, open_us)
    t = sc["total"]
    ca_of = {cid: ca_ids[ca] for (ca, cid, *_r) in ASSESSED}
    inputs = []
    for cid, res, val in sc["inputs"]:
        e = {"controlRef": ID + "control/" + cid, "controlResult": res}
        if cid in ca_of:
            e["controlAssessmentRef"] = ca_of[cid]
        if val is not None:
            e["scoreValue"] = val
        inputs.append(e)
    us_counts = {"us%dCount" % i: sum(1 for u in open_us if u["unknownSeverity"] == "US%d" % i) for i in range(1, 6)}
    SS = syn("score", "SS-001")
    DR = syn("recommendation", "DR-001")
    AD = syn("decision", "AD-001")
    rec(SS, "ScoreSnapshot", "Synthetic score snapshot", subjectRef=CI, profileVersion="AIDCF-007A v1.1 (360 controls, unweighted)",
        scoreInputs=inputs, weighting="UNWEIGHTED",
        coverage={k: t[k] for k in ["inScopeCount", "notApplicableCount", "assessedCount", "scoredCount", "unknownCount", "notAssessedCount", "coveragePercent"]},
        band=t["band"], meanScore=t["meanScore"], bandWithheldReason=t["reason"], unknownOverlay=us_counts,
        gateOverlay="Gates are non-compensating: %s." % ", ".join("%s %s" % (g, s) for g, s in sorted(states.items())),
        calculationHash=sc["hash"], calculationMethod=AR.SCORE_METHOD + ": mean of CONFORMING 100, PARTIAL 50, NONCONFORMING 0 over scored controls; "
        "coverage = scored / (in scope - NOT_APPLICABLE); band WITHHELD below 80% coverage or with an open US4/US5 UNKNOWN; "
        "hash = sha256 of canonical JSON {method, weighting, inputs}.",
        domainScores=sc["domains"], migratedFrom=["urn:aidcf:score:SNAP-001-v1.2"], summarisedBy=[DR], reportedIn=[syn("report", "RPT-001")])
    QUAL.setdefault((SS, "migratedFrom", "urn:aidcf:score:SNAP-001-v1.2"), {})["migrationRef"] = syn("migration", "MIG-002")
    for ca in ca_ids.values():
        edge(ca, "summarisedBy", SS)
    for g in GR.values():
        edge(g, "summarisedBy", DR)
        edge(g, "constrains", DR, constraintType="CEILING")
    for k in ["U-001", "U-003", "U-004", "U-005", "U-002"]:
        edge(U[k], "summarisedBy", DR)
    flush_pending()
    ix = AR.Index(list(RECS.values()))
    ceilings = AR.gate_ceilings_from(ix)
    ceil, drivers = AR.decision_ceiling(states, ceilings, open_us)
    if ceil != EXPECTED_DECISION:
        sys.exit("build_dataset: decision ceiling computed %s, declared %s" % (ceil, EXPECTED_DECISION))
    rec(DR, "DecisionRecommendation", "Synthetic decision recommendation", decisionQuestion=DECISION_Q, recommendedState=ceil,
        decisionCeiling=ceil, ceilingDrivers=drivers, recommends=[AD],
        limitations=["Synthetic data only.",
                     "%d of %d controls assessed; %d scored and %d UNKNOWN; coverage %.4f%% (scored / (in scope - NOT_APPLICABLE))."
                     % (t["assessedCount"], t["inScopeCount"], t["scoredCount"], t["unknownCount"], t["coveragePercent"]),
                     "Ceilings that are not controlling: " + "; ".join(subordinate_ceilings(states, ceilings, open_us, ceil)) + "."])
    rec(AD, "AssuranceDecision", "Synthetic assurance decision", status="APPROVED", decisionQuestion=DECISION_Q, subjectRef=CI,
        decisionScope="Synthetic capability CI-001 within snapshot SNAP-001; NORMAL and MAINTENANCE states.",
        gateResultRefs=[GR[g] for g in sorted(GR)], unknownRefs=[U[k] for k in sorted(U)], scoreRef=SS, decisionState=ceil,
        decisionLifecycle="APPROVED", approvedBy=[syn("review", "RR-002")], notCertification=True,
        controllingReasons=drivers, effectiveTo="2027-04-10T00:00:00Z",
        limitations=["Synthetic data only; describes no real facility.", "Approval is a synthetic record; no human approval was given."],
        requiresAction=[syn("action", "ACT-011")], reportedIn=[syn("report", "RPT-001")],
        migratedFrom=["urn:aidcf:decision:DEC-001-v1.2"], integrationHandoff=[syn("handoff", "IH-001")])
    QUAL.setdefault((AD, "migratedFrom", "urn:aidcf:decision:DEC-001-v1.2"), {})["migrationRef"] = syn("migration", "MIG-002")
    return SS, DR, AD, sc


def subordinate_ceilings(states, ceilings, open_us, ceil):
    """Every gate or UNKNOWN ceiling above the controlling ceiling, in AIDCF-010 step order (gates, then UNKNOWN severity)."""
    out = []
    for g, s in sorted(states.items()):
        c = ceilings[g][0] if s == "FAIL" else ceilings[g][1] if s in ("UNKNOWN", "NOT_ASSESSED") else None
        if c and AR.RANK[c] > AR.RANK[ceil]:
            out.append("%s %s (%s)" % (g, s, c))
    sev = {"US5": "INCONCLUSIVE", "US4": "LIMITED", "US3": "CONDITIONALLY_ASSURED"}
    for u in sorted(open_us, key=lambda u: u["id"]):
        c = sev.get(u.get("unknownSeverity"))
        if c and AR.RANK[c] > AR.RANK[ceil]:
            out.append("%s %s (%s)" % (u["id"].rsplit(":", 1)[-1], u["unknownSeverity"], c))
    return out


DECISION_Q = ("Can the synthetic AI training and inference capability CI-001 be relied on to meet SO-01 to SO-03 in NORMAL and "
              "MAINTENANCE states, as at 2026-10-10?")


def build_governance(AD, reg):
    rr = [("RR-001", "REVIEW", "QA", "Quality reviewer", "INTERNAL_INDEPENDENT", "All twelve Control Assessments", "ACCEPTED_WITH_COMMENTS"),
          ("RR-002", "APPROVAL", "DECISION-AUTH", "Decision authority", "INTERNAL_INDEPENDENT", "Assurance decision AD-001", "ACCEPTED"),
          ("RR-003", "REVIEW", "QA", "Quality reviewer", "INTERNAL_INDEPENDENT", "Closure of F-006", "ACCEPTED"),
          ("RR-004", "REVIEW", "QA", "Quality reviewer", "INTERNAL_INDEPENDENT", "Integration handoff IH-001", "ACCEPTED"),
          ("RR-005", "APPROVAL", "DECISION-AUTH", "Decision authority", "INTERNAL_INDEPENDENT", "Architecture snapshot SNAP-001", "ACCEPTED"),
          ("RR-006", "REVIEW", "QA", "Quality reviewer", "INTERNAL_INDEPENDENT", "Fifteen Gate Results", "ACCEPTED_WITH_COMMENTS")]
    for k, t, who, role, ind, sc, out in rr:
        rec(syn("review", k), "ReviewRecord", "Synthetic %s %s" % (t.lower(), k), reviewType=t, reviewer=PTY[who], reviewerRole=role,
            reviewIndependence=ind, scopeReviewed=sc, reviewOutcome=out, reviewedAt="2026-10-09",
            comments="Synthetic record produced by the dataset builder; no human review or approval took place.")
    acts = [("ACT-%03d" % i, d) for i, d in enumerate([
        "Extend asset-to-function mapping to facility water and recovery dependencies (F-001).",
        "Add transient cold-plate flow to the design basis (F-002).",
        "Rationalise cooling and leak alarms (F-003).",
        "Make vendor support accounts time-bound (F-004).",
        "Restrict BMS write authority to named identities (F-005).",
        "Obtain E4 component test evidence for MCF-RES-017 (U-001).",
        "Refresh the fabric topology export (U-002).",
        "Obtain the facility water service agreement (U-003).",
        "Run an integrated cross-domain recovery exercise (U-004).",
        "Assess SL-A for the BMS zone (U-005).",
        "Reassess the decision when F-003 and F-005 (CG-07), F-001 (CG-03), F-004 (CG-15), U-003 and U-004 are closed (AD-001).",
        "Obtain an AIDCF-007A registry status code from RecordLifecycle (BI-002).",
        "Obtain AIDCF-010 machine-readable gate ceilings (BI-003)."], 1)]
    for k, d in acts:
        rec(syn("action", k), "Action", "%s %s" % (k, d[:60]), owner=PTY["PROGRAMME-OWNER"], dueDate="2026-12-15", actionStatus="OPEN",
            closureCriteria=d)
    rec(syn("handoff", "IH-001"), "IntegrationHandoff", "Synthetic decision summary handoff to the AI Trust Graph", targetSystem="AI Trust Graph (synthetic endpoint)",
        handoffType="DECISION_SUMMARY", mappingType="RELATED", aitgRefs=["aitg:syn:capability:CI-001"], handoffDirection="AIDCF to AITG",
        ownershipStatement="AIDCF retains ownership of the decision meaning; the AITG stores a reference only.", conclusionsFederated=False,
        reviewedBy=[syn("review", "RR-004")])
    rec(syn("statement", "AS-001"), "AssuranceStatement", "Synthetic assurance statement", decisionRef=AD, decisionState=EXPECTED_DECISION,
        audience="Synthetic internal stakeholders", statementText=("The synthetic assessment is NOT_ASSURED. CG-07 (critical control-system integrity) FAILS on PARTIAL CRITICAL controls "
                       "MCF-OPS-013 and MCF-SEC-005, and its FAIL ceiling is NOT_ASSURED for the Service Outcomes that depend on BMS supervision "
                       "of power and cooling (RF-06, required by SO-01); the decision question is not partitioned by outcome, so that ceiling "
                       "applies to SO-01 to SO-03. CG-03 and CG-15 also FAIL (NOT_ASSURED for the outcomes their defeated dependency "
                       "and authority paths reach; LIMITED for the decision as a whole). The CG-01 and CG-05 UNKNOWN gates and the systemic US5 UNKNOWN "
                       "U-003 on the facility water plant each cap the decision at INCONCLUSIVE; none raises it above NOT_ASSURED, "
                       "because a demonstrated gate failure is not softened by undetermined positions."),
        permittedClaims=["The synthetic capability was assessed against 12 of 360 AIDCF-007A controls."],
        prohibitedClaims=["Any claim of certification.", "Any claim of assurance stronger than NOT_ASSURED, including INCONCLUSIVE: the CG-07 failure is demonstrated, not undetermined."],
        reportedIn=[syn("report", "RPT-001")], effectiveTo="2027-04-10T00:00:00Z")
    rec(syn("report", "RPT-001"), "AssuranceReport", "Synthetic technical assessment report", reportClass="R2", programRef=PRG, assessmentRef=ASM,
        decisionRef=AD, decisionState=EXPECTED_DECISION, issuer=PTY["PROGRAMME-OWNER"], intendedUsers=["Synthetic decision authority"],
        intendedUse="Conformance demonstration of AIDCF-016 MDM 1.3 only.", sections=["Scope", "Gate results", "UNKNOWN register", "Score", "Decision"],
        limitations=["Synthetic data only.", "No independent execution."], prohibitedClaims=["Certification."], effectiveTo="2027-04-10T00:00:00Z")
    rec(SNAP, "ArchitectureSnapshot", "Synthetic architecture snapshot", status="APPROVED", capabilityRef=CI, snapshotDate="2026-09-30",
        composedOf=[a(k) for k in ["SYS-POW", "SYS-THM", "SYS-FWS", "SYS-CMP", "SYS-STO", "SYS-NET", "SYS-CTL", "IF-PWR-RACK", "IF-FWS-CDU",
                                   "IF-FABRIC", "CND-01", "RES-UTIL", "RES-WATER", "AST-UTILITY"]],
        dependencyRefs=sorted(r["id"] for r in RECS.values() if r["type"] == "Dependency"),
        faultDomainRefs=sorted(r["id"] for r in RECS.values() if r["type"] == "FaultDomain"),
        operatingStates=["NORMAL", "MAINTENANCE", "DEGRADED", "RECOVERY"],
        assertionRefs=[syn("capacity-assertion", "CAP-CAP-02"), syn("assertion", "ASR-01"), syn("assertion", "ASR-02")],
        reconciliationStatus="PARTIALLY_RECONCILED", reconciliationEvidenceRef=EV["EV-ARCH-01"], approvedBy=[syn("review", "RR-005")])
    rec(ASM, "Assessment", "Synthetic assessment ASM-001", decisionQuestion=DECISION_Q, capabilityRef=CI, architectureBaseline=SNAP,
        operatingStates=["NORMAL", "MAINTENANCE"], profileRef="AIDCF-007A v1.1 full catalogue (unweighted)", weighting="UNWEIGHTED",
        team=["Synthetic assessor A", "Synthetic assessor B", "Synthetic quality reviewer"], evidenceManifest=[syn("evidence-package", "EP-001")],
        controlUniverseCount=360, governedBy=[PRG],
        composedOf=sorted(r["id"] for r in RECS.values() if r["type"] in ("ControlAssessment", "GateResult", "Sample", "TestRecord")))


def build_migration_baseline(reg):
    v11 = AR.read_csv(PKG / "migration/v1.1-to-v1.2-control-migration-matrix.csv")
    rec(syn("migration", "MIG-001"), "MigrationRecord", "AIDCF-015 v1.1 to v1.2 control migration", sourceRelease="AIDCF-015 v1.1",
        targetRelease="AIDCF-015 v1.2", mappings=[{"fromId": r["legacyPilotId"], "toId": r["canonicalControlId"], "changeType": "IDENTIFIER",
                                                   "rationale": r["rationale"]} for r in v11],
        unmappedValues=[], fallbackApplied=False, description="Recorded from migration/v1.1-to-v1.2-control-migration-matrix.csv (AIDCF-007A-AMD-001).")
    maps = []
    v12_state = {"CG-01": "PASS", "CG-02": "PASS", "CG-03": "PASS", "CG-04": "APPROVED_NA", "CG-05": "PASS", "CG-06": "PASS", "CG-07": "PASS",
                 "CG-08": "PASS", "CG-09": "UNKNOWN", "CG-10": "UNKNOWN", "CG-11": "PASS", "CG-12": "PASS", "CG-13": "PASS", "CG-14": "PASS", "CG-15": "PASS"}
    for ca, cid, *_r in ASSESSED:
        maps.append({"fromId": "urn:aidcf:assessment:" + ca, "toId": syn("control-assessment", ca), "changeType": "IDENTIFIER",
                     "rationale": "Synthetic record namespace urn:aidcf:syn (AIDCF-016 section 6)."})
    maps.append({"fromId": "urn:aidcf:assessment:CA-009#result=PARTIAL", "toId": syn("control-assessment", "CA-009") + "#result=UNKNOWN",
                 "changeType": "RESULT_REINTERPRETATION", "rationale": "Evidence below the S3 floor and no E4 class: SPEC 5.12 requires UNKNOWN, not PARTIAL."})
    for g in sorted(v12_state):
        maps.append({"fromId": "urn:aidcf:gate:%s#state=%s" % (g, v12_state[g]), "toId": syn("gate-result", "GR-" + g) + "#state=" + EXPECTED_GATES[g],
                     "changeType": "RESULT_REINTERPRETATION",
                     "rationale": "Recomputed by the SPEC 6.2 roll-up with registry gate-mappings.csv roles over the 12 assessed controls; unassessed CRITICAL controls are NOT_ASSESSED."})
    maps.append({"fromId": "urn:aidcf:decision:DEC-001-v1.2#state=LIMITED", "toId": syn("decision", "AD-001") + "#state=" + EXPECTED_DECISION,
                 "changeType": "RESULT_REINTERPRETATION", "rationale": "Decision ceiling recomputed from gate ceilings and UNKNOWN severities (AIDCF-016 section 9.5)."})
    for i in range(1, 13):
        maps.append({"fromId": "evidenceClass=%s (EV-%03d)" % (V12_CLASS[i], i), "toId": "evidenceClass=%s" % RECS[EV["EV-%03d" % i]]["evidenceClass"],
                     "changeType": "VOCABULARY", "rationale": "v1.2 used words; v1.3 uses registries/vocabularies/evidence-classes.csv codes (legacy value kept in provenance)."})
    rec(syn("migration", "MIG-002"), "MigrationRecord", "AIDCF-015 v1.2 to v1.3 migration", sourceRelease="AIDCF-015 v1.2", targetRelease="AIDCF-015 v1.3",
        mappings=maps, unmappedValues=["v1.2 synthetic gate-to-control lists (replaced by registry gate-mappings.csv roles)"], fallbackApplied=False)
    bi = [("BI-001", "Control-universe cardinality", [("AIDCF-007", "1.0", "control catalogue", "Pilot control set (PILOT-*)"),
                                                     ("AIDCF-007A", "1.1", "AMD-001", "15 domains, 90 families, 360 controls")],
           "Resolved by adopting the AIDCF-007A registry (AIDCF-007A-AMD-001).", "RESOLVED", {"closedBy": [syn("migration", "MIG-001")],
                                                                                            "resolution": "AIDCF-007A-AMD-001 adopted in v1.2."}),
          ("BI-002", "Registry status code outside the record lifecycle", [("AIDCF-007A", "1.1", "registries/controls/controls.csv status", "PROPOSED"),
                                                                           ("AIDCF-014", "1.1", "section 11A.1", "DRAFT, CANDIDATE, REVIEWED, APPROVED, ACTIVE, SUSPENDED, WITHDRAWN, SUPERSEDED, RETIRED")],
           "Registry records are imported with status CANDIDATE and the original value in provenance.legacyValue.", "CONDITIONALLY_BASELINED",
           {"provisionalValue": "CANDIDATE", "requiresAction": [syn("action", "ACT-012")]}),
          ("BI-003", "Gate ceilings stated as prose", [("AIDCF-010", "1.x", "registries/gates/critical-gates.csv failCeiling/unknownCeiling", "Prose ceilings with qualifiers"),
                                                     ("AIDCF-016", "1.0", "section 9.4", "One machine ceiling code per gate state")],
           "Machine ceilings are derived by the AIDCF-016 section 9.4 rule; the prose is kept on each Critical Gate.", "CONDITIONALLY_BASELINED",
           {"provisionalValue": "Derived ceilings (AIDCF-016 section 9.4)", "requiresAction": [syn("action", "ACT-013")]})]
    for k, ct, srcs, imp, st, extra in bi:
        rec(syn("baseline-issue", k), "BaselineIssue", "%s %s" % (k, ct), issueCode=k, conflictType=ct,
            conflictSources=[{"artifact": x[0], "artifactVersion": x[1], "location": x[2], "value": x[3]} for x in srcs], impact=imp,
            baselineStatus=st, **extra)


def build_event(reg):
    TRG = syn("trigger", "TRG-001")
    EVT = syn("event", "EVT-001")
    rec(TRG, "ReassessmentTrigger", "Synthetic OT configuration-change trigger", triggerRule="Any BMS or EPMS controller firmware or logic change reassesses OT security and alarm controls.",
        eventTypes=["CONFIGURATION_CHANGED"], triggerState="CANDIDATE",
        triggersReassessment=[ID + "control/MCF-SEC-005", ID + "control/MCF-OPS-013"])
    ix = AR.Index(list(RECS.values()))
    affected = AR.impact(ix, a("AST-BMS-CTRL"))
    trg_targets = set(RECS[TRG]["triggersReassessment"])
    reassess = [x for x in affected if ix.type(x) in AR.REASSESS_CLASSES and x not in trg_targets]
    rec(EVT, "Event", "Synthetic BMS controller firmware upgrade", status="CANDIDATE", reviewState="CANDIDATE",
        eventType="CONFIGURATION_CHANGED", subjectRef=a("AST-BMS-CTRL"), eventSource="Synthetic BMS change feed", sourceHealth="HEALTHY",
        observedAt="2026-10-09T14:00:00Z", effectiveAt="2026-10-09T13:30:00Z",
        payload={"change": "firmware", "from": "syn-4.1", "to": "syn-4.2", "ticket": "SYN-CHG-0042"}, eventSeverity="HIGH",
        materiality="MATERIAL", affectedAssertions=affected, candidateTriggers=[TRG], humanDisposition="PENDING", snapshotRef=SNAP,
        resultingDecisionEffect="Pending human disposition; no record has been suspended (TDS-REQ-062).",
        triggersReassessment=reassess)
    edge(EV["EV-011"], "invalidatedBy", EVT)
    for x in reassess:
        CANDIDATE_EDGES.add((EVT, "triggersReassessment", x))
    for x in trg_targets:
        CANDIDATE_EDGES.add((TRG, "triggersReassessment", x))
    CANDIDATE_EDGES.add((EV["EV-011"], "invalidatedBy", EVT))
    CANDIDATE_EDGES.add((EVT, "candidateTriggers", TRG))
    return EVT, affected


# ------------------------------------------------------------------ relationship records
def build_relationship_records():
    flush_pending()
    out = []
    edges = []
    for r in list(RECS.values()):
        for k, v in r.items():
            if k in M.REL_BY_PROP:
                for o in v:
                    edges.append((r["id"], k, o))
    for s, p, o in edges:
        code = M.REL_BY_PROP[p][0]
        src, tgt = RECS.get(s, {}), RECS.get(o, {})
        cl = max([src.get("classification", "INTERNAL"), tgt.get("classification", "INTERNAL")], key=lambda c: M.CLASSIFICATION_RANK[c])
        qlist = QUAL.get(("PROP", s, o)) if p == "propagatesTo" else [dict(QUAL.get((s, p, o), {}))]
        for q in qlist:
            q = dict(q)
            rid = q.pop("id", None) or rel_id(s, p, o)
            cand = (s, p, o) in CANDIDATE_EDGES
            f = dict(q)
            f.update(relationshipType=code, sourceRef=s, targetRef=o, confidence="CONF-2" if cand else "CONF-3")
            if code == "MIGRATED_FROM" and "migrationRef" not in f:
                f["migrationRef"] = syn("migration", "MIG-002")
            if code in ("DEPENDS_ON", "PROTECTED_BY", "PROPAGATES_TO", "RECOVERS_THROUGH") and "operatingStates" not in f:
                f["operatingStates"] = ["NORMAL"]
            prov = dict(src.get("provenance") or PROV_SYN)
            prov.pop("sha256", None)
            prov.pop("legacyValue", None)
            rr = rec(rid, "RelationshipRecord", "%s %s %s" % (s.rsplit(":", 1)[-1].rsplit("/", 1)[-1], code, o.rsplit(":", 1)[-1].rsplit("/", 1)[-1]),
                     classification=cl, status="CANDIDATE" if cand else "REVIEWED", reviewState="CANDIDATE" if cand else "SUPPORTED",
                     provenance=prov, sourceArtifact=src.get("sourceArtifact", "AIDCF-015"), **f)
            out.append(rr)
    return out


# ------------------------------------------------------------------ write
FILES = [
    ("framework.jsonld", lambda r: r["type"] in ("ControlDomain", "ControlFamily", "Control", "CriticalGate", "EvidenceRequirement", "OperatingState", "FoundationalRequirement")),
    ("organisation.jsonld", lambda r: r["type"] in ("PartyEntity", "Location", "DistributionControl", "AssuranceProgram", "ReviewRecord", "IntegrationHandoff")),
    ("capability.jsonld", lambda r: r["type"] in ("CapabilityInstance", "ServiceOutcome", "RequiredFunction")),
    ("architecture.jsonld", lambda r: r["type"] in ("ArchitectureSnapshot", "InfrastructureSystem", "AssetInstance", "Interface", "Resource", "Component",
                                                     "IACS", "IACSZone", "Conduit", "Dependency", "FaultDomain", "CapacityAssertion", "Assertion", "SecurityLevel")),
    ("failure.jsonld", lambda r: r["type"] in ("Threat", "Hazard", "FailureMode", "FailureScenario", "Safeguard")),
    ("evidence.jsonld", lambda r: r["type"] in ("EvidenceObject", "EvidencePackage")),
    ("assessment.jsonld", lambda r: r["type"] in ("Assessment", "AssessmentProcedure", "Sample", "TestRecord", "ControlAssessment", "Finding", "UnknownRecord", "Action")),
    ("decision.jsonld", lambda r: r["type"] in ("GateResult", "ScoreSnapshot", "DecisionRecommendation", "AssuranceDecision", "AssuranceStatement", "AssuranceReport")),
    ("continuing-assurance.jsonld", lambda r: r["type"] in ("Event", "ReassessmentTrigger", "MigrationRecord", "BaselineIssue")),
    ("relationships.jsonld", lambda r: r["type"] == "RelationshipRecord"),
]


def ordered(r):
    head = ["id", "type", "name"]
    return {k: r[k] for k in head + sorted(k for k in r if k not in head)}


def main():
    reg = AR.load_registry()
    fx = PKG / "evidence-fixtures"
    fx.mkdir(exist_ok=True)
    for p in fx.glob("*.txt"):
        p.unlink()
    build_context_records()
    build_framework(reg)
    build_capability_architecture()
    deps = build_evidence_and_dependencies(fx)
    SG = build_failure_and_safeguards()
    build_dependencies(deps)
    ca_ids, ca_ev = build_assessment(reg, fx, SG)
    F, U = build_challenges(ca_ids, ca_ev)
    GR = build_gates(reg, ca_ids, ca_ev, F, U)
    resolve_unknown_subjects(U, ca_ids, GR)
    build_governance(syn("decision", "AD-001"), reg)
    flush_pending()
    states = finalise_gates(reg, GR)
    SS, DR, AD, sc = build_score_decision(reg, GR, U, ca_ids, states)
    # statement/report/handoff need AD state: rebuild those that reference it
    for k in [syn("statement", "AS-001"), syn("report", "RPT-001")]:
        RECS[k]["decisionState"] = RECS[AD]["decisionState"]
    build_migration_baseline(reg)
    flush_pending()
    EVT, affected = build_event(reg)
    rrs = build_relationship_records()
    for r in RECS.values():
        dc_for(r)
    # completeness check against the profile before writing
    for r in RECS.values():
        miss = [f for f in M.required_fields(r["type"]) if f not in r]
        if miss:
            sys.exit("build_dataset: %s missing %s" % (r["id"], miss))
    out = PKG / "dataset"
    out.mkdir(exist_ok=True)
    for p in out.glob("*.jsonld"):
        p.unlink()
    placed = set()
    counts = {}
    for fn, pred in FILES:
        items = [ordered(r) for r in sorted(RECS.values(), key=lambda r: r["id"]) if pred(r)]
        placed.update(r["id"] for r in items)
        counts[fn] = len(items)
        (out / fn).write_text(json.dumps({"@context": CTX, "@graph": items}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    left = set(RECS) - placed
    if left:
        sys.exit("build_dataset: records not placed in any file: %s" % sorted(left)[:5])
    t = sc["total"]
    print("records: %d (%s)" % (len(RECS), ", ".join("%s %d" % kv for kv in counts.items())))
    print("relationship records: %d; evidence fixtures: %d" % (len(rrs), len(list(fx.glob("*.txt")))))
    print("gates: " + ", ".join("%s %s" % (g, s) for g, s in sorted(states.items())))
    print("decision: %s; score mean %s coverage %.4f%% assessed %d/%d band %s" % (RECS[AD]["decisionState"], t["meanScore"], t["coveragePercent"],
                                                                                  t["assessedCount"], t["inScopeCount"], t["band"]))
    print("event affected records: %d" % len(affected))


if __name__ == "__main__":
    main()
