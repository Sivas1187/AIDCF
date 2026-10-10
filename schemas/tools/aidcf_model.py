"""AIDCF machine-executable data model, release 1.3 (AIDCF-016 MDM).

Single source of truth for the generated schema set in schemas/:
  - owl/aidcf-core-1.3.ttl          OWL 2 ontology + SKOS concept schemes
  - jsonld/aidcf-context-1.3.jsonld JSON-LD 1.1 context
  - shacl/aidcf-shapes-1.3.ttl      SHACL shapes (core + SPARQL-based)
  - json-schema/*.schema.json       JSON Schema 2020-12

Classes: the 48 canonical classes of AIDCF-014 v1.1 section 7 (definitions copied
verbatim), the AIDCF-003 reference classes Location, PartyEntity and Component
(AIDCF-014 section 7, "Reference classes"), supporting classes beyond the 48 that
are pending AIDCF-014 registration (AIDCF-003 v1.1 Part XVI IEC 62443 concepts
IACS, IACSZone, Conduit, SecurityLevel, FoundationalRequirement, and the AIDCF-002
Assertion), and one auxiliary structural class (RelationshipRecord) carrying the
AIDCF-014 section 10 relationship envelope.

Relationships: the 41 types of AIDCF-014 v1.1 section 9 with domain, range,
cardinality (out / in) and inverse exactly as published. Inverses are declared in
the ontology and are never serialised.

Controlled vocabularies: codes for the schemes bound to registries/vocabularies/*.csv
are read from those files at build time (VOCAB_FILES); the remaining schemes are
defined here with their source.
"""
import csv
import re
from pathlib import Path

NS = "https://w3id.org/aidcf/ontology#"
ONT = "https://w3id.org/aidcf/ontology"
VERSION_IRI = "https://w3id.org/aidcf/ontology/1.3"
VOCAB_NS = "https://w3id.org/aidcf/vocab/"
SHAPES_IRI = "https://w3id.org/aidcf/shapes/1.3"
SCHEMA_BASE = "https://w3id.org/aidcf/schema/1.3/"
CONTEXT_IRI = "https://w3id.org/aidcf/context/1.3"
ID_BASE = "https://w3id.org/aidcf/id/"
RELEASE = "1.3"
RELEASE_DATE = "2026-10-10"
REPO = Path(__file__).resolve().parents[2]

ARTIFACT_PATTERN = r"^AIDCF-(0(0[1-9]|1[0-9])A?|0(0[1-9]|1[0-9])-[A-Z]{3}|VR-[0-9]{3}|WP-[0-9]{3})$"
IRI_PATTERN = r"^(urn:[a-z0-9][a-z0-9-]*:|https://)[^\s]+$"
RELEASE_PATTERN = r"^AIDCF-REL-[0-9]{4}\.(0[1-9]|1[0-2])\.[1-9][0-9]*$"
DOMAINS = ["GOV", "CAP", "DEP", "PHY", "POW", "THM", "ENV", "CMP", "STO",
           "NET", "OPS", "RES", "SUP", "SEC", "EVA"]
DOM_ALT = "|".join(DOMAINS)
MCF_PATTERN = r"^MCF-(%s)-(0[0-1][0-9]|02[0-4])$" % DOM_ALT
FAMILY_PATTERN = r"^(%s)-0[1-6]$" % DOM_ALT
GATE_PATTERN = r"^CG-(0[1-9]|1[0-5])$"
SHA256_PATTERN = r"^[0-9a-f]{64}$"
SEMVER_PATTERN = r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"

# ---------------------------------------------------------------------------
# Controlled vocabularies: scheme -> (label, source, [(code, label, definition)])
# ---------------------------------------------------------------------------
def _c(*rows):
    return [(r[0], r[1], r[2] if len(r) > 2 else "") for r in rows]

VOCABS = {
 "GateRole": ("Control-to-gate role", "AIDCF-014 section 9 (EVALUATES_GATE); SPEC 6.1", _c(
    ("CRITICAL", "Critical", "The gate cannot PASS unless this control is CONFORMING at its required claim type when in scope."),
    ("SUPPORTING", "Supporting", "Informs the gate; a NONCONFORMING result requires a documented gate-level evaluation."))),
 "GateApplicability": ("Gate applicability", "AIDCF-014 section 8A (GateResult profile)", _c(
    ("IN_SCOPE", "In scope"), ("APPROVED_NA", "Approved not applicable"))),
 "CriterionOutcome": ("Gate criterion outcome", "AIDCF-014 section 8A (GateResult profile: criteria evaluated and outcome); AIDCF-016", _c(
    ("MET", "Met", "Criterion demonstrated met with evidence at or above the gate floor."),
    ("NOT_MET", "Not met", "Criterion demonstrated not met (gate FAIL)."),
    ("UNKNOWN", "Unknown", "Criterion evaluated but cannot be determined; an UNKNOWN Record is attached."),
    ("NOT_EVALUATED", "Not evaluated", "Criterion not yet evaluated in this assessment."))),
 "RecordLifecycle": ("Record lifecycle", "AIDCF-014 section 11A.1", _c(
    ("DRAFT", "Draft", "Being prepared; not for use in assessment."), ("CANDIDATE", "Candidate", "Proposed (often by automation); awaiting review."),
    ("REVIEWED", "Reviewed", "Reviewed; not yet approved."), ("APPROVED", "Approved", "Approved by the accountable authority."),
    ("ACTIVE", "Active", "Approved and in use."), ("SUSPENDED", "Suspended", "Temporarily not to be relied on, pending reassessment."),
    ("WITHDRAWN", "Withdrawn", "Removed from use before expiry; retained for history."),
    ("SUPERSEDED", "Superseded", "Replaced by a newer record (SUPERSEDES)."), ("RETIRED", "Retired", "End of life without replacement; retained for history."))),
 "AssertionState": ("Assertion review state", "AIDCF-014 section 11A.2", _c(
    ("CANDIDATE", "Candidate", "Asserted but not reviewed."), ("SUPPORTED", "Supported", "Reviewed; supported by evidence meeting the applicable floor."),
    ("CHALLENGED", "Challenged", "Subject to an unresolved CHALLENGES edge."), ("QUALIFIED", "Qualified", "Holds only under the conditions stated by QUALIFIES edges."),
    ("CONFLICTING", "Conflicting", "Supported and challenged by evidence of comparable quality."),
    ("UNKNOWN", "Unknown", "Cannot be determined; HAS_UNKNOWN is mandatory."), ("SUPERSEDED", "Superseded", "Replaced by a newer assertion."))),
 "Classification": ("Classification", "AIDCF-014 section 11A.8", _c(
    ("PUBLIC", "Public", "Approved for public release."), ("INTERNAL", "Internal", "For the owning organisation and its assessors."),
    ("CLIENT_RESTRICTED", "Client restricted", "For named client parties under agreement."),
    ("CONFIDENTIAL", "Confidential", "Need-to-know within named roles; disclosure would cause commercial or security harm."),
    ("HIGHLY_RESTRICTED", "Highly restricted", "Exploitable detail (for example OT access paths, protection settings); named individuals only."))),
 "Weighting": ("Score weighting", "SPEC 5.12", _c(
    ("UNWEIGHTED", "Unweighted mean"), ("PROFILE_WEIGHTED", "Weighted by an approved capability profile"))),
 "Domain": ("Control domain", "AIDCF-007A; registries/domains/domains.csv", _c(
    ("GOV", "Governance, Accountability and Assurance Direction"),
    ("CAP", "AI Capability, Service Outcome and Demand Management"),
    ("DEP", "Dependency, Concentration and External Reliance Management"),
    ("PHY", "Physical Site, Building and Security Infrastructure"),
    ("POW", "Electrical Power Infrastructure and Energy Continuity"),
    ("THM", "Cooling, Thermal and Fluid Infrastructure"),
    ("ENV", "Environmental and Resource Performance"),
    ("CMP", "AI Compute Infrastructure"), ("STO", "AI Storage and Data Infrastructure"),
    ("NET", "AI Network and Interconnect Architecture"),
    ("OPS", "Building Operations and Service Management"),
    ("RES", "Resilience, Continuity and Recovery"),
    ("SUP", "Supply Chain, OEM and Ecosystem Assurance"),
    ("SEC", "Digital, OT and Control-Plane Security"),
    ("EVA", "Evidence, Assessment and Assurance Management"))),
 "Criticality": ("Capability criticality", "AIDCF-003; AIDCF-007A CAP-03", _c(
    ("CRITICAL", "Critical"), ("HIGH", "High"), ("MEDIUM", "Medium"), ("LOW", "Low"))),
 "WorkloadClass": ("Workload class", "AIDCF-014 section 8A (Capability profile: workload)", _c(
    ("TRAINING", "Training"), ("FINE_TUNING", "Fine-tuning"), ("INFERENCE", "Inference"), ("DATA_PROCESSING", "Data processing"))),
 "ReconciliationStatus": ("As-built reconciliation status", "AIDCF-013", _c(
    ("RECONCILED", "Reconciled"), ("PARTIALLY_RECONCILED", "Partially reconciled"),
    ("NOT_RECONCILED", "Not reconciled"), ("UNKNOWN", "Unknown"))),
 "DependencyType": ("Dependency type", "AIDCF-014 section 8A (Dependency profile); AIDCF-003", _c(
    ("ELECTRICAL", "Electrical"), ("THERMAL", "Thermal"), ("FLUID", "Fluid"), ("NETWORK", "Network"), ("CONTROL", "Control"),
    ("TIMING", "Timing"), ("IDENTITY", "Identity"), ("CONFIGURATION", "Configuration"), ("DATA", "Data"), ("HUMAN", "Human"),
    ("SUPPLIER", "Supplier"), ("UTILITY", "Utility"), ("RECOVERY", "Recovery"))),
 "DependencyStrength": ("Dependency strength", "AIDCF-014 section 8A (Dependency profile); AIDCF-003", _c(
    ("ABSOLUTE", "Absolute"), ("MATERIAL", "Material"), ("CONDITIONAL", "Conditional"), ("SUPPORTING", "Supporting"),
    ("RECOVERY_ONLY", "Recovery only"), ("UNKNOWN", "Unknown"))),
 "SafeguardFunction": ("Safeguard function", "AIDCF-014 section 8A (Safeguard profile); AIDCF-004", _c(
    ("PREVENT", "Prevent"), ("DETECT", "Detect"), ("CONTAIN", "Contain"), ("CORRECT", "Correct"), ("RECOVER", "Recover"))),
 "Activation": ("Safeguard activation", "AIDCF-014 section 8A (Safeguard profile)", _c(
    ("AUTOMATIC", "Automatic"), ("MANUAL", "Manual"), ("HYBRID", "Hybrid"))),
 "ReviewType": ("Review type", "AIDCF-014 section 9 (APPROVED_BY) and section 24 (approveRecord)", _c(
    ("REVIEW", "Review", "A recorded human review."), ("APPROVAL", "Approval", "A recorded approval by an authorised person; target of APPROVED_BY."))),
 "ApprovalOutcome": ("Release approval outcome", "AIDCF-014 section 4 (approvals)", _c(
    ("APPROVED", "Approved"), ("PENDING", "Pending"), ("REJECTED", "Rejected"))),
 "ConstraintType": ("Constraint type", "AIDCF-014 section 9 (CONSTRAINS)", _c(
    ("CEILING", "Ceiling"), ("CONDITION", "Condition"), ("LIMITATION", "Limitation"), ("BAND_WITHHELD", "Band withheld"), ("GATE_EFFECT", "Gate effect"))),
 "SecurityLevelKind": ("Security level kind", "AIDCF-003 v1.1 Part XVI section 72 (IEC 62443 series)", _c(
    ("SL-T", "Target", "Level required for a zone or conduit by the risk assessment."),
    ("SL-C", "Capability", "Level a component or system can provide when properly configured."),
    ("SL-A", "Achieved", "Level actually provided by the deployed zone or conduit as assessed."))),
 "FoundationalRequirementCode": ("IEC 62443 foundational requirement", "AIDCF-003 v1.1 Part XVI section 72", _c(
    ("FR1", "Identification and authentication control"), ("FR2", "Use control"), ("FR3", "System integrity"),
    ("FR4", "Data confidentiality"), ("FR5", "Restricted data flow"), ("FR6", "Timely response to events"),
    ("FR7", "Resource availability"))),
 "PartyKind": ("Party kind", "AIDCF-014 section 7 (PartyEntity: organisation, role, actor or team)", _c(
    ("ORGANISATION", "Organisation"), ("ROLE", "Role"), ("ACTOR", "Actor"), ("TEAM", "Team"))),
 "LocationKind": ("Location kind", "AIDCF-014 section 7 (Location)", _c(
    ("SITE", "Site"), ("BUILDING", "Building"), ("HALL", "Hall"), ("ROOM", "Room"), ("ROW", "Row"),
    ("RACK_POSITION", "Rack position"), ("LOGICAL", "Logical placement"))),
 "HazardType": ("Hazard type", "AIDCF-004; SPEC 6 (CG-04 scope)", _c(
    ("ELECTRICAL", "Electrical shock or arc flash"), ("FIRE", "Fire"), ("FLUID", "Hazardous fluid or leak"),
    ("CHEMICAL", "Chemical"), ("REFRIGERANT", "Refrigerant"), ("BATTERY_THERMAL", "Battery thermal runaway"),
    ("CONFINED_SPACE", "Confined space"), ("UTILITY_DISTURBANCE", "Utility disturbance"), ("ENVIRONMENTAL", "Environmental"))),
 "FindingClass": ("Finding class", "AIDCF-010", _c(
    ("OBSERVATION", "Observation"), ("IMPROVEMENT", "Improvement"), ("WEAKNESS", "Weakness"),
    ("SIGNIFICANT_WEAKNESS", "Significant weakness"), ("CRITICAL_FINDING", "Critical finding"))),
 "FindingStatus": ("Finding status", "AIDCF-011", _c(
    ("OPEN", "Open"), ("IN_REMEDIATION", "In remediation"),
    ("CLOSED_PENDING_VERIFICATION", "Closed pending verification"), ("CLOSED", "Closed"))),
 "UnknownStatus": ("UNKNOWN record status", "AIDCF-016", _c(
    ("OPEN", "Open", "No disposition recorded."),
    ("DISPOSITIONED", "Dispositioned", "Owner, evidence needed, due date and decision effect recorded; still unresolved."),
    ("RESOLVED", "Resolved", "Resolved by evidence and reassessment (CLOSED_BY)."))),
 "ReviewIndependence": ("Review independence", "AIDCF-011", _c(
    ("SELF", "Self-review"), ("INTERNAL_INDEPENDENT", "Internally independent"),
    ("EXTERNAL_INDEPENDENT", "Externally independent"))),
 "ReviewOutcome": ("Review outcome", "AIDCF-011", _c(
    ("ACCEPTED", "Accepted"), ("ACCEPTED_WITH_COMMENTS", "Accepted with comments"), ("REJECTED", "Rejected"))),
 "ReportClass": ("Report class", "AIDCF-012 report types", _c(
    ("R1", "Executive Assurance Report"), ("R2", "Technical Assessment Report"), ("R3", "Domain Report"),
    ("R4", "Evidence Package"), ("R5", "Gate and Decision Package"), ("R6", "Customer/Second-Party Statement"),
    ("R7", "Regulatory Support Package"), ("R8", "Public Summary"), ("R9", "Continuing-Assurance Report"),
    ("R10", "Remediation/Closure Report"))),
 "ActionStatus": ("Action status", "AIDCF-011", _c(
    ("OPEN", "Open"), ("IN_PROGRESS", "In progress"), ("COMPLETE", "Complete"), ("VERIFIED", "Verified"),
    ("CANCELLED", "Cancelled"))),
 "TriggerState": ("Reassessment trigger state", "AIDCF-011", _c(
    ("CANDIDATE", "Candidate"), ("ACCEPTED", "Accepted"), ("REJECTED", "Rejected"), ("ACTIONED", "Actioned"))),
 "EventType": ("Event type", "AIDCF-014 section 21", _c(
    ("ARCHITECTURE_CHANGED", "Architecture changed"), ("CAPACITY_THRESHOLD_BREACHED", "Capacity threshold breached"),
    ("CONFIGURATION_CHANGED", "Configuration changed"), ("PROVIDER_CHANGED", "Provider changed"),
    ("SOURCE_UNAVAILABLE", "Source unavailable"), ("EVIDENCE_EXPIRED", "Evidence expired"),
    ("EVIDENCE_CONFLICT", "Evidence conflict"), ("INCIDENT_DETECTED", "Incident detected"),
    ("TEST_FAILED", "Test failed"), ("GATE_STATUS_CHANGED", "Gate status changed"),
    ("FINDING_CLOSED", "Finding closed"), ("CONTROL_DRIFT", "Control drift"),
    ("DEPENDENCY_DRIFT", "Dependency drift"), ("DECISION_SUSPENDED", "Decision suspended"),
    ("REPORT_WITHDRAWN", "Report withdrawn"))),
 "SourceHealth": ("Event source health", "AIDCF-014 section 20", _c(
    ("HEALTHY", "Healthy"), ("DEGRADED", "Degraded"), ("UNAVAILABLE", "Unavailable"), ("UNKNOWN", "Unknown"))),
 "EventSeverity": ("Event severity", "AIDCF-014 section 20 (candidate until reviewed)", _c(
    ("LOW", "Low"), ("MODERATE", "Moderate"), ("HIGH", "High"), ("CRITICAL", "Critical"))),
 "Materiality": ("Materiality determination", "AIDCF-014 section 20 (candidate until reviewed)", _c(
    ("MATERIAL", "Material"), ("NOT_MATERIAL", "Not material"), ("UNDETERMINED", "Undetermined"))),
 "HumanDisposition": ("Human disposition", "AIDCF-014 section 20", _c(
    ("PENDING", "Pending"), ("ACCEPTED", "Accepted"), ("REJECTED", "Rejected"))),
 "HandoffType": ("Integration handoff type", "AIDCF-005", _c(
    ("DECISION_SUMMARY", "Decision summary"), ("GATE_STATUS", "Gate status"),
    ("UNKNOWN_REGISTER", "UNKNOWN register"), ("EVIDENCE_REFERENCE", "Evidence reference"), ("SHARED_IDENTITY", "Shared identity"))),
 "MappingType": ("Cross-framework mapping type", "AIDCF-005", _c(
    ("EXACT", "Exact"), ("CLOSE", "Close"), ("PARTIAL", "Partial"), ("RELATED", "Related"), ("NO_MAPPING", "No mapping"))),
 "ValidationLayer": ("Validation layer", "AIDCF-016 section 11", _c(
    ("REGISTRY", "Registry"), ("SYNTAX", "Syntax"), ("SCHEMA", "JSON Schema"), ("SHACL", "SHACL"),
    ("BUSINESS_RULE", "Business rule"), ("TRACEABILITY", "Traceability (AIDCF-014 TR-01 to TR-18)"),
    ("GRAPH_QUERY", "Graph query"), ("SCORE", "Score reperformance"), ("INTEGRITY", "Evidence integrity"),
    ("MANIFEST", "Release manifest"), ("VOCABULARY", "Vocabulary alignment"),
    ("EXPORT", "Export and redaction (AIDCF-014 section 11A.8; AIDCF-016 CT-09)"), ("FIXTURE", "Conformance fixture"))),
 "ValidationOutcome": ("Validation outcome", "AIDCF-014 section 31A (Validation Result template)", _c(
    ("PASS", "Pass"), ("FAIL", "Fail"), ("WARNING", "Warning"))),
 "ChangeType": ("Migration change type", "AIDCF-014 section 27", _c(
    ("IDENTIFIER", "Identifier change"), ("VOCABULARY", "Vocabulary change"), ("RESULT_REINTERPRETATION", "Result re-evaluated under the canonical rule"),
    ("STRUCTURE", "Structural change"), ("ADDED", "Added"), ("REMOVED", "Removed"))),
 "BaselineStatus": ("Baseline issue status", "AIDCF-014 section 6", _c(
    ("BLOCKED", "Blocked"), ("CONDITIONALLY_BASELINED", "Conditionally baselined"), ("RESOLVED", "Resolved"))),
 "SignatureStatus": ("Signature status", "AIDCF-016", _c(
    ("PENDING", "Pending", "No signature has been produced."), ("SIGNED", "Signed"), ("VERIFIED", "Signature verified"))),
 "ProvenanceMethod": ("Provenance method", "AIDCF-014 section 26; AIDCF-016", _c(
    ("REGISTRY_IMPORT", "Imported from a canonical registry"), ("SYNTHETIC_AUTHORING", "Authored as synthetic data"),
    ("AUTOMATED_DISCOVERY", "Automated discovery (candidate until reviewed)"), ("INFERENCE", "Inferred (candidate until reviewed)"),
    ("MIGRATION", "Migrated from a previous release"), ("VALIDATION_RUN", "Produced by a validation run"),
    ("MANUAL_ENTRY", "Manual entry"))),
}

# Schemes whose codes are read from registries/vocabularies/*.csv (TDS-REQ-043).
# scheme -> (file, label column or None, definition columns, filter (column, value) or None, title)
VOCAB_FILES = {
 "ClaimType": ("claim-types.csv", "name", ["meaning"], None, "Claim type"),
 "AssuranceLevel": ("assurance-levels.csv", "name", ["permittedConclusion"], None, "Assurance level"),
 "ControlResult": ("control-results.csv", None, ["meaning"], None, "Control result"),
 "ImplementationMaturity": ("implementation-maturity.csv", "name", ["definition"], None, "Implementation maturity (diagnostic only)"),
 "GateState": ("gate-results.csv", None, ["meaning"], None, "Gate result"),
 "DecisionState": ("decision-states.csv", None, ["meaning"], None, "Decision state"),
 "DecisionLifecycle": ("decision-lifecycle.csv", None, ["meaning"], None, "Decision lifecycle"),
 "Confidence": ("confidence.csv", "name", ["meaning"], ("kind", "level"), "Confidence"),
 "ConfidenceFlag": ("confidence.csv", "name", ["meaning"], ("kind", "flag"), "Confidence flag"),
 "EvidenceClass": ("evidence-classes.csv", "name", ["primaryClaimSupported"], None, "Evidence class"),
 "QualityDimension": ("quality-dimensions.csv", "name", ["question"], None, "Evidence quality dimension"),
 "QualityBand": ("evidence-quality-bands.csv", "name", ["rule"], None, "Evidence quality band"),
 "Sufficiency": ("sufficiency-levels.csv", "name", ["meaning"], None, "Evidence sufficiency"),
 "IntegrityLevel": ("integrity-levels.csv", "name", ["anchor"], None, "Evidence integrity level"),
 "ControlProfileTier": ("control-profile-tiers.csv", "name", ["use"], None, "Control evidence profile tier"),
 "EvidenceConformanceLevel": ("evidence-system-conformance-levels.csv", "name", ["minimumExpectation"], None, "Evidence-system conformance level"),
 "UnknownType": ("unknown-types.csv", "name", ["definition"], None, "UNKNOWN type"),
 "UnknownSeverity": ("unknown-severity.csv", "name", ["test", "decisionEffect"], None, "UNKNOWN severity"),
 "OperatingState": ("operating-states.csv", None, ["definition"], None, "Operating state"),
 "AssessmentMethod": ("assessment-methods.csv", None, ["meaning"], None, "Assessment method"),
 "ControlType": ("control-types.csv", None, ["meaning"], None, "Control type"),
 "LifecycleStage": ("lifecycle-stages.csv", None, ["meaning"], None, "Lifecycle stage"),
 "ScoreBand": ("score-bands.csv", "name", ["reportingCondition"], None, "Score band"),
}


def load_registry_vocabs(vdir=None):
    vdir = Path(vdir or (REPO / "registries" / "vocabularies"))
    out = {}
    for scheme, (fn, labcol, defcols, flt, title) in VOCAB_FILES.items():
        p = vdir / fn
        if not p.exists():
            raise FileNotFoundError("vocabulary registry file missing: %s" % p)
        with p.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        codes = []
        for r in rows:
            if flt and r.get(flt[0]) != flt[1]:
                continue
            code = r["code"].strip()
            lab = (r.get(labcol) or "").strip() if labcol else ""
            if not lab:
                lab = code.replace("_", " ").capitalize()
            d = " ".join((r.get(c) or "").strip() for c in defcols if (r.get(c) or "").strip())
            codes.append((code, lab, d))
        out[scheme] = (title, "registries/vocabularies/" + fn, codes)
    return out


VOCABS.update(load_registry_vocabs())

# AIDCF-010 order (Gate ceilings; derivation pseudocode ORDER): NOT_ASSURED is the most restrictive state, below INCONCLUSIVE.
DECISION_RANK = {"REASONABLY_ASSURED": 5, "CONDITIONALLY_ASSURED": 4, "LIMITED": 3, "INCONCLUSIVE": 2, "NOT_ASSURED": 1}
CLAIM_RANK = {"DESIGN": 2, "IMPLEMENTATION": 3, "OPERATION": 4, "EFFECTIVENESS": 5, "RESILIENCE": 5}
CLAIM_MIN_AL = {"DESIGN": "AL2", "IMPLEMENTATION": "AL3", "OPERATION": "AL4", "EFFECTIVENESS": "AL5", "RESILIENCE": "AL5"}
CLASSIFICATION_RANK = {"PUBLIC": 0, "INTERNAL": 1, "CLIENT_RESTRICTED": 2, "CONFIDENTIAL": 3, "HIGHLY_RESTRICTED": 4}
SCORE_VALUE = {"CONFORMING": 100, "PARTIAL": 50, "NONCONFORMING": 0}

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------
ARCH = ["InfrastructureSystem", "AssetInstance", "Interface", "Resource"]

# 48 canonical classes: name -> (superclass, owner artifact, label, definition (AIDCF-014 v1.1 section 7, verbatim), chain step)
CLASSES = {
 "ReleaseManifest": ("GovernanceRecord", "AIDCF-014", "Release Manifest", "Signed, immutable bill of materials pinning every artifact, registry, vocabulary, schema and ontology version of one release.", "Context"),
 "BaselineIssue": ("GovernanceRecord", "AIDCF-014", "Baseline Issue", "Recorded conflict between pinned sources, with original values, status and resolution lineage.", "Context"),
 "CapabilityInstance": ("CapabilityElement", "AIDCF-003", "Capability Instance", "A specific deployment of an AI capability bounded by ownership, location, architecture, capacity, criticality and obligations.", "2"),
 "ServiceOutcome": ("CapabilityElement", "AIDCF-003", "Service Outcome", "A measurable or assessable result the CapabilityInstance must achieve, with tolerance, duration and operating-state conditions.", "3"),
 "RequiredFunction": ("CapabilityElement", "AIDCF-003", "Required Function", "A function whose loss or degradation materially affects one or more ServiceOutcomes (for example \"remove 100% of rack heat at design inlet temperature\").", "4"),
 "ArchitectureSnapshot": ("ArchitectureRecord", "AIDCF-013", "Architecture Snapshot", "A versioned, approved and immutable view of the architecture in scope at a point in time, against which assessments are performed.", "5"),
 "InfrastructureSystem": ("ArchitectureElement", "AIDCF-003", "Infrastructure System", "A coordinated set of assets and interfaces providing one or more functions (for example a CDU secondary loop, a UPS system, a scale-out fabric).", "5"),
 "AssetInstance": ("ArchitectureElement", "AIDCF-003", "Asset Instance", "An identifiable real-world item, service, procedure or resource provider represented where material (for example a switchboard, a CDU, a GPU node).", "5"),
 "Interface": ("ArchitectureElement", "AIDCF-003", "Interface", "A defined point or mechanism of exchange between entities (electrical, thermal, fluid, network, management, data, physical, operational, provider).", "5"),
 "Resource": ("ArchitectureElement", "AIDCF-003", "Resource", "A consumable or constrained input required for operation (electrical capacity, cooling capacity, water, fuel, rack space, accelerator hours).", "5"),
 "Dependency": ("ArchitectureRecord", "AIDCF-003", "Dependency", "A reified reliance of one entity on another entity, resource, condition or decision, with direction, strength, states and substitutability.", "6"),
 "FaultDomain": ("ArchitectureRecord", "AIDCF-003", "Fault Domain", "A set of entities expected to be affected together by a common cause of failure, with its boundary and blast radius.", "6"),
 "OperatingState": ("ArchitectureRecord", "AIDCF-003", "Operating State", "A defined condition of operation (NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN).", "Context"),
 "CapacityAssertion": ("ArchitectureRecord", "AIDCF-003", "Capacity Assertion", "A conditioned claim about a capacity value: metric, unit, subject, operating state, environment, duration, derating, evidence date and confidence.", "5"),
 "Threat": ("AdverseCondition", "AIDCF-004", "Threat", "An actor-driven or intentional source of potential harm (for example unauthorised remote command of a cooling controller).", "7"),
 "Hazard": ("AdverseCondition", "AIDCF-004", "Hazard", "A non-intentional source of potential harm (for example utility voltage sag, coolant leak, heatwave, battery thermal runaway).", "7"),
 "FailureMode": ("AdverseCondition", "AIDCF-004", "Failure Mode", "The manner in which an entity fails to perform its function (for example pump seizure, breaker failure to trip, optic degradation).", "7"),
 "FailureScenario": ("FailureRecord", "AIDCF-004", "Failure Scenario", "An ordered path from initiating source through propagation steps and safeguards to residual state and outcome effect, from a stated pre-state.", "7"),
 "Safeguard": ("FailureRecord", "AIDCF-004", "Safeguard", "A real-world measure that prevents, detects, contains, corrects or recovers from a failure, threat or hazard.", "8"),
 "ControlDomain": ("ControlFrameworkElement", "AIDCF-007A", "Control Domain", "One of the 15 AIDCF-007A control domains.", "9"),
 "ControlFamily": ("ControlFrameworkElement", "AIDCF-007A", "Control Family", "One of the 90 AIDCF-007A control families (six per domain).", "9"),
 "Control": ("ControlFrameworkElement", "AIDCF-007A", "Control", "One of the 360 AIDCF-007A normative controls: objective, requirement, criteria, evidence profile, procedure and gate mappings.", "9"),
 "EvidenceRequirement": ("EvidenceElement", "AIDCF-008", "Evidence Requirement", "The evidence a control or gate needs for a claim type: classes, quality and sufficiency floors, state and period coverage, independence.", "10"),
 "EvidenceObject": ("EvidenceElement", "AIDCF-008", "Evidence Object", "A record or observation, with provenance and integrity, used to support, challenge or qualify an assertion.", "11"),
 "EvidencePackage": ("EvidenceElement", "AIDCF-008", "Evidence Package", "A sealed, manifest-listed set of EvidenceObjects collected for an assessment or gate, with custody and integrity metadata.", "11"),
 "AssuranceProgram": ("GovernanceRecord", "AIDCF-011", "Assurance Program", "The programme within which assessments are planned and decisions issued: assurance level target, profile, cadence and authority.", "1"),
 "Assessment": ("AssessmentElement", "AIDCF-009", "Assessment", "One bounded assessment answering one decision question for one CapabilityInstance, scope and ArchitectureSnapshot.", "1, 12"),
 "AssessmentProcedure": ("AssessmentElement", "AIDCF-009", "Assessment Procedure", "The ordered method steps used to assess one control for one claim type, using canonical assessment methods.", "12"),
 "Sample": ("AssessmentElement", "AIDCF-009", "Sample", "A defined selection of population items examined by a procedure, with population, selection method and size rationale.", "12"),
 "TestRecord": ("AssessmentElement", "AIDCF-009", "Test Record", "The record of an authorised test or scenario exercise: authority, preconditions, safety controls, steps, observations and outcome.", "12"),
 "ControlAssessment": ("AssessmentElement", "AIDCF-009", "Control Assessment", "The result of assessing one control, for one claim type, in one scope: result code, confidence, evidence, method, assessor and lifecycle.", "12"),
 "Finding": ("AssuranceChallenge", "AIDCF-009", "Finding", "A documented deficiency against a stated criterion, with condition, cause, consequence, evidence and gate and score effect.", "13"),
 "UnknownRecord": ("AssuranceChallenge", "AIDCF-008", "UNKNOWN Record", "A material fact that cannot be determined, with type (U1–U10), severity (US1–US5), reason, decision effect, evidence needed and owner.", "13"),
 "CriticalGate": ("ControlFrameworkElement", "AIDCF-010", "Critical Gate", "One of the 15 non-compensating critical gates CG-01 to CG-15, with scope, criteria and evidence floor.", "14"),
 "GateResult": ("DecisionElement", "AIDCF-010", "Gate Result", "The evaluated status of one CriticalGate in one assessment scope (PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED) with its inputs.", "14"),
 "ScoreSnapshot": ("DecisionElement", "AIDCF-010", "Score Snapshot", "An immutable, reproducible computation of control, family and domain scores, coverage and band from pinned inputs and profile.", "15"),
 "DecisionRecommendation": ("DecisionElement", "AIDCF-010", "Decision Recommendation", "The decision state, conditions, ceilings and limitations proposed from gate results, UNKNOWNs and scores, before authority review.", "15"),
 "ReviewRecord": ("DecisionElement", "AIDCF-009", "Review Record", "A recorded human review or approval: reviewer, authority, independence, scope reviewed, outcome and date.", "16"),
 "AssuranceDecision": ("DecisionElement", "AIDCF-010", "Assurance Decision", "The decision of the accountable authority: decision state, conditions, scope, validity period and lifecycle.", "16"),
 "AssuranceStatement": ("ReportingElement", "AIDCF-012", "Assurance Statement", "The bounded, disclosed wording of an AssuranceDecision for a named audience, which cannot exceed the decision.", "Loop"),
 "AssuranceReport": ("ReportingElement", "AIDCF-012", "Assurance Report", "The issued report carrying statements, scope, findings, UNKNOWNs, limitations, distribution and validity.", "Loop"),
 "Action": ("ContinuingAssuranceElement", "AIDCF-011", "Action", "A remediation, evidence-collection or condition-fulfilment task with owner, due date and closure criteria.", "Loop"),
 "ReassessmentTrigger": ("ContinuingAssuranceElement", "AIDCF-011", "Reassessment Trigger", "A declared rule describing which events or conditions require reassessment of which records.", "Loop"),
 "Event": ("ContinuingAssuranceElement", "AIDCF-014", "Event", "An observed or reported occurrence (change, incident, test failure, evidence expiry) ingested for impact analysis.", "Loop"),
 "IntegrationHandoff": ("ContinuingAssuranceElement", "AIDCF-005", "Integration Handoff", "A reviewed exchange of identity or findings between AIDCF and the AI Trust Graph, preserving each framework's ownership.", "Context"),
 "ValidationResult": ("GovernanceRecord", "AIDCF-014", "Validation Result", "The outcome of a structural, semantic or business-rule validation of a record or package against a pinned release.", "Context"),
 "MigrationRecord": ("GovernanceRecord", "AIDCF-014", "Migration Record", "The record of converting data between versions or vocabularies: source, target, rule, mapping, exceptions and validation.", "Context"),
 "DistributionControl": ("GovernanceRecord", "AIDCF-014", "Distribution Control", "The classification-bound disclosure rule for a record, edge, package or report: permitted audiences, purpose, redaction and expiry.", "Context"),
}
assert len(CLASSES) == 48

# AIDCF-003 reference classes (AIDCF-014 section 7) and supporting classes pending AIDCF-014 registration.
# name -> (superclass, owner, label, definition, status note)
REFERENCE_CLASSES = {
 "Location": ("ReferenceEntity", "AIDCF-003", "Location", "A site, building, hall, room, row, rack position or logical placement.", "AIDCF-014 v1.1 section 7 reference class (range of LOCATED_IN)."),
 "PartyEntity": ("ReferenceEntity", "AIDCF-003", "Party Entity", "An organisation, role, actor or team.", "AIDCF-014 v1.1 section 7 reference class (range of OPERATED_BY, CONTROLLED_BY, DEPENDS_ON)."),
 "Component": ("ReferenceEntity", "AIDCF-003", "Component", "A constituent part of an asset represented where material.", "AIDCF-014 v1.1 section 7 reference class (range of COMPOSED_OF)."),
}
SUPPORTING_CLASSES = {
 "IACS": ("InfrastructureSystem", "AIDCF-003", "Industrial Automation and Control System",
          "Industrial Automation and Control System: the personnel, hardware, software and policies that operate, monitor and protect a physical process. In AIDCF, the control systems of power, cooling, fire and building services, including their engineering workstations, historians and gateways. Subclass of InfrastructureSystem.",
          "AIDCF-003 v1.1 section 72; supporting class beyond the 48 canonical classes, pending AIDCF-014 registration."),
 "IACSZone": ("InfrastructureSystem", "AIDCF-003", "IACS Zone",
              "A grouping of logical or physical assets that share common security requirements, defined through a security risk assessment (IEC 62443-3-2). Distinct from a physical security zone (AIDCF-003).",
              "AIDCF-003 v1.1 section 72; mapped by AIDCF-003 to an InfrastructureSystem grouping; supporting class pending AIDCF-014 registration."),
 "Conduit": ("Interface", "AIDCF-003", "Conduit",
             "A logical grouping of communication channels connecting two or more zones that share common security requirements (IEC 62443-3-2).",
             "AIDCF-003 v1.1 section 72; mapped by AIDCF-003 to an Interface; supporting class pending AIDCF-014 registration."),
 "SecurityLevel": ("SupportingRecord", "AIDCF-003", "Security Level",
                   "A level 0 to 4 expressing the protection a zone, conduit or component provides against increasingly capable violation, recorded per foundational requirement as a seven-element vector. Kinds: SL-T (target), SL-C (capability), SL-A (achieved).",
                   "AIDCF-003 v1.1 section 72; supporting class pending AIDCF-014 registration."),
 "FoundationalRequirement": ("SupportingRecord", "AIDCF-003", "Foundational Requirement",
                             "One of the seven IEC 62443 foundational requirements against which security levels are expressed (FR1 to FR7).",
                             "AIDCF-003 v1.1 section 72; supporting class pending AIDCF-014 registration."),
 "Assertion": ("SupportingRecord", "AIDCF-002", "Assertion",
               "A precise testable proposition to which evidence is attached (AIDCF-002 section 19.4); expressed as subject, predicate and object or value with scope, conditions and effective time (AIDCF-003 v1.1).",
               "AIDCF-002 class; not among the AIDCF-014 v1.1 48 classes; supporting class pending AIDCF-014 registration."),
}
AUX_CLASSES = {
 "RelationshipRecord": ("AidcfRecord", "AIDCF-014", "Relationship Record", "Auxiliary structural class (not one of the 48 classes) carrying the AIDCF-014 section 10 relationship envelope for one asserted edge.", "AIDCF-014 section 10."),
}
ABSTRACT = {
 "AidcfRecord": (None, "Enveloped record", "Any AIDCF record carrying the common object envelope (AIDCF-014 section 8)."),
 "GovernanceRecord": ("AidcfRecord", "Governance record", "Release, baseline, programme, validation, migration and distribution records."),
 "CapabilityElement": ("AidcfRecord", "Capability element", "Capability, outcome and function records (chain steps 2 to 4)."),
 "ArchitectureRecord": ("AidcfRecord", "Architecture record", "Architecture, dependency, fault-domain, state and capacity records (chain steps 5 and 6)."),
 "ArchitectureElement": ("ArchitectureRecord", "Architecture element", "InfrastructureSystem, AssetInstance, Interface or Resource (AIDCF-014 section 9 conventions)."),
 "FailureRecord": ("AidcfRecord", "Failure record", "Adverse conditions, failure scenarios and safeguards (chain steps 7 and 8)."),
 "AdverseCondition": ("FailureRecord", "Adverse condition", "Common superclass of Threat, Hazard and FailureMode."),
 "ControlFrameworkElement": ("AidcfRecord", "Control framework element", "Domains, families, controls and critical gates."),
 "EvidenceElement": ("AidcfRecord", "Evidence element", "Evidence requirements, objects and packages (chain steps 10 and 11)."),
 "AssessmentElement": ("AidcfRecord", "Assessment element", "Assessments, procedures, samples, tests and control assessments (chain step 12)."),
 "AssuranceChallenge": ("AidcfRecord", "Assurance challenge", "Findings and UNKNOWN Records (chain step 13)."),
 "DecisionElement": ("AidcfRecord", "Decision element", "Gate results, scores, recommendations, reviews and decisions (chain steps 14 to 16)."),
 "ReportingElement": ("AidcfRecord", "Reporting element", "Statements and reports."),
 "ContinuingAssuranceElement": ("AidcfRecord", "Continuing assurance element", "Actions, triggers, events and handoffs that close the loop."),
 "ReferenceEntity": ("AidcfRecord", "Reference entity", "AIDCF-003 reference classes used in AIDCF-014 relationship ranges."),
 "SupportingRecord": ("AidcfRecord", "Supporting record", "Supporting classes beyond the 48 canonical classes, pending AIDCF-014 registration."),
}

def all_class_meta():
    m = {}
    for n, v in CLASSES.items():
        m[n] = dict(sup=v[0], owner=v[1], label=v[2], definition=v[3], chain=v[4], group="canonical")
    for n, v in REFERENCE_CLASSES.items():
        m[n] = dict(sup=v[0], owner=v[1], label=v[2], definition=v[3], note=v[4], group="reference")
    for n, v in SUPPORTING_CLASSES.items():
        m[n] = dict(sup=v[0], owner=v[1], label=v[2], definition=v[3], note=v[4], group="supporting")
    for n, v in AUX_CLASSES.items():
        m[n] = dict(sup=v[0], owner=v[1], label=v[2], definition=v[3], note=v[4], group="auxiliary")
    return m

CLASS_META = all_class_meta()
CONCRETE = list(CLASS_META)

def superclasses(c):
    out = []
    while c:
        out.append(c)
        c = CLASS_META[c]["sup"] if c in CLASS_META else ABSTRACT.get(c, (None,))[0]
    return out

# Assertion-bearing classes: reviewState mandatory (AIDCF-014 section 8) and the range of CHALLENGES / QUALIFIES.
ASSERTION_BEARING = ["CapacityAssertion", "Dependency", "FaultDomain", "ControlAssessment", "GateResult", "FailureScenario",
                     "Finding", "UnknownRecord", "Event", "Assertion", "SecurityLevel", "RelationshipRecord"]
# Assessable classes: envelope scope mandatory (AIDCF-014 section 8).
ASSESSABLE = ["Assessment", "ControlAssessment", "GateResult", "Finding", "UnknownRecord", "ScoreSnapshot",
              "DecisionRecommendation", "AssuranceDecision", "AssuranceStatement", "AssuranceReport", "RelationshipRecord"]

# ---------------------------------------------------------------------------
# Relationships (AIDCF-014 v1.1 section 9): code, property, definition, domain, range, card, inverse, extra
# card = dict(out=(min, max), inn=(min, max), outBy={class: (min, max, targetClass)}, inBy={class: (min, max, fromClass)})
# max None = unbounded. domain/range None = any record.
# ---------------------------------------------------------------------------
def card(out="0..*", inn="0..*", **kw):
    def p(s):
        a, b = s.split("..")
        return (int(a), None if b == "*" else int(b))
    d = dict(out=p(out), inn=p(inn))
    d.update(kw)
    return d

REL = [
 ("HAS_OUTCOME", "hasOutcome", "The capability instance is required to achieve the target service outcome.",
  ["CapabilityInstance"], ["ServiceOutcome"], card("1..*", "1..1"), "outcomeOf", {}),
 ("REQUIRES_FUNCTION", "requiresFunction", "Achieving the outcome requires the target function to be delivered.",
  ["ServiceOutcome"], ["RequiredFunction"], card("1..*", "1..*"), "functionRequiredBy", {}),
 ("IMPLEMENTED_BY", "implementedBy", "The function, or the safeguard, is realised by the target architecture element.",
  ["RequiredFunction", "Safeguard"], ["InfrastructureSystem", "AssetInstance", "Interface"], card("1..*", "0..*"), "implements", {}),
 ("COMPOSED_OF", "composedOf", "Whole-part structure: the source contains the target as a constituent. Acyclic.",
  ["ArchitectureSnapshot", "InfrastructureSystem", "AssetInstance", "ControlDomain", "ControlFamily", "AssuranceProgram", "Assessment", "EvidencePackage"],
  ["InfrastructureSystem", "AssetInstance", "Component", "Interface", "Resource", "ControlFamily", "Control", "Assessment", "ControlAssessment", "GateResult", "Sample", "TestRecord", "EvidenceObject"],
  card("0..*", "0..*", inBy={"ControlFamily": (1, 1, "ControlDomain"), "Control": (1, 1, "ControlFamily")}), "partOf",
  {"acyclic": True, "pairs": {"ArchitectureSnapshot": ARCH, "InfrastructureSystem": ARCH + ["Component"], "AssetInstance": ["Component", "Interface"],
                              "ControlDomain": ["ControlFamily"], "ControlFamily": ["Control"], "AssuranceProgram": ["Assessment"],
                              "Assessment": ["ControlAssessment", "GateResult", "Sample", "TestRecord"], "EvidencePackage": ["EvidenceObject"]}}),
 ("CONNECTS_TO", "connectsTo", "The source is an endpoint of the target interface. Physical or logical connection only; implies no dependency, causality or reachability.",
  ["InfrastructureSystem", "AssetInstance"], ["Interface"], card("0..*", "2..*"), "hasEndpoint", {}),
 ("CONSUMES_RESOURCE", "consumesResource", "The source draws on the target constrained resource (power, cooling, water, fuel, space, accelerator capacity).",
  ["RequiredFunction", "InfrastructureSystem", "AssetInstance"], ["Resource"], card(), "consumedBy", {}),
 ("DEPENDS_ON", "dependsOn", "The source relies on the target to perform its function; each edge references exactly one Dependency record carrying type, strength and states.",
  ["RequiredFunction", "Safeguard"] + ARCH, ARCH + ["Safeguard", "PartyEntity"], card(), "dependencyOf",
  {"qualifiers": ["dependencyRef"], "conditions": True}),
 ("SHARES_FAULT_DOMAIN_WITH", "sharesFaultDomainWith", "Source and target are members of the same FaultDomain and can fail together from its common cause. Symmetric; each edge references the FaultDomain record.",
  ARCH + ["Safeguard"], ARCH + ["Safeguard"], card(), None, {"symmetric": True, "qualifiers": ["faultDomainRef"]}),
 ("LOCATED_IN", "locatedIn", "The source is physically or logically placed in the target location.",
  ["InfrastructureSystem", "AssetInstance", "FaultDomain"], ["Location"], card("0..1", "0..*"), "locationOf", {}),
 ("OPERATED_BY", "operatedBy", "The target party holds operational responsibility for the source.",
  ["CapabilityInstance", "InfrastructureSystem", "AssetInstance", "Safeguard"], ["PartyEntity"], card("1..*", "0..*"), "operates", {}),
 ("CONTROLLED_BY", "controlledBy", "The target control system or actor can command the source's state or setpoints.",
  ["InfrastructureSystem", "AssetInstance"], ["InfrastructureSystem", "AssetInstance", "PartyEntity"], card(), "controls", {}),
 ("MONITORED_BY", "monitoredBy", "The target observes the source and is relied on to detect its condition.",
  ARCH + ["Safeguard", "Dependency"], ["InfrastructureSystem", "AssetInstance"], card(), "monitors", {}),
 ("PROTECTED_BY", "protectedBy", "The target safeguard acts to prevent, detect, contain, correct or recover from failure of, or harm to, the source.",
  ["ServiceOutcome", "RequiredFunction"] + ARCH, ["Safeguard"], card("0..*", "1..*"), "protects", {"conditions": True}),
 ("EXPOSED_TO", "exposedTo", "The source is credibly susceptible to the target threat, hazard or failure mode.",
  ["CapabilityInstance"] + ARCH + ["Safeguard"], ["Threat", "Hazard", "FailureMode"], card(), "exposes", {}),
 ("INITIATES", "initiates", "The threat, hazard or failure mode is the initiating source of the target scenario.",
  ["Threat", "Hazard", "FailureMode"], ["FailureScenario"], card("0..*", "1..*"), "initiatedBy", {}),
 ("PROPAGATES_TO", "propagatesTo", "Within a named scenario, failure of the source causes failure or degradation of the target; carries scenarioRef and step ordinal.",
  ARCH + ["RequiredFunction"], ARCH + ["RequiredFunction", "ServiceOutcome"], card(), "propagatedFrom",
  {"qualifiers": ["scenarioRef", "stepOrdinal"], "conditions": True}),
 ("RECOVERS_THROUGH", "recoversThrough", "The source is restored to tolerance by means of the target recovery path, alternate capacity or recovery safeguard.",
  ["ServiceOutcome", "RequiredFunction"] + ARCH, ARCH + ["Safeguard"], card(), "recoveryPathFor", {"conditions": True}),
 ("GOVERNED_BY", "governedBy", "The source is subject to the requirements, method or disclosure rule of the target.",
  None, ["Control", "AssessmentProcedure", "AssuranceProgram", "DistributionControl"],
  card("0..*", "0..*", outBy={"Assessment": (1, 1, "AssuranceProgram")}), "governs",
  {"pairs": {"Safeguard": ["Control"], "ControlAssessment": ["AssessmentProcedure", "Control"], "Assessment": ["AssuranceProgram"], "*": ["DistributionControl"]}}),
 ("HAS_EVIDENCE_REQUIREMENT", "hasEvidenceRequirement", "The control or gate requires the target evidence requirement for a stated claim type.",
  ["Control", "CriticalGate"], ["EvidenceRequirement"], card("1..*", "1..1"), "requirementOf", {}),
 ("EVIDENCED_BY", "evidencedBy", "The source is offered the target evidence. Records that evidence was presented, not that it is sufficient.",
  ["EvidenceRequirement", "CapacityAssertion", "Dependency", "FaultDomain", "ControlAssessment", "GateResult", "Finding"], ["EvidenceObject", "EvidencePackage"], card(), "evidences", {}),
 ("SUPPORTS", "supports", "After review, the source evidence corroborates the target claim.",
  ["EvidenceObject"], ["CapacityAssertion", "Dependency", "FaultDomain", "ControlAssessment", "GateResult", "FailureScenario"], card(), "supportedBy", {}),
 ("CHALLENGES", "challenges", "The source contradicts or undermines the target claim (defeater). Alias: DISPUTES.",
  ["EvidenceObject", "Finding", "UnknownRecord", "ReviewRecord", "BaselineIssue"], ASSERTION_BEARING, card(), "challengedBy", {}),
 ("QUALIFIES", "qualifies", "The source limits the scope, states or conditions under which the target claim holds, without contradicting it.",
  ["EvidenceObject", "ReviewRecord", "UnknownRecord"], ASSERTION_BEARING, card(), "qualifiedBy", {}),
 ("ASSESSED_BY", "assessedBy", "The control is assessed, for one claim type in one scope, by the target control assessment.",
  ["Control"], ["ControlAssessment"], card("0..*", "1..1"), "assesses", {}),
 ("RESULTS_IN", "resultsIn", "Execution of the procedure, sample or test produced (contributes to) the target control assessment.",
  ["AssessmentProcedure", "Sample", "TestRecord"], ["ControlAssessment"], card("0..*", "1..*"), "resultOf", {}),
 ("HAS_FINDING", "hasFinding", "The source result or gate evaluation records the target finding.",
  ["ControlAssessment", "GateResult", "Assessment"], ["Finding"], card("0..*", "1..*"), "findingOf", {}),
 ("HAS_UNKNOWN", "hasUnknown", "The source has a material undetermined fact recorded by the target UNKNOWN record.",
  None, ["UnknownRecord"], card("0..*", "1..*"), "unknownOf", {}),
 ("EVALUATES_GATE", "evaluatesGate", "Control to CriticalGate: registry gate mapping, mandatory attribute gateRole (CRITICAL or SUPPORTING). ControlAssessment to GateResult: the result is an input to that gate evaluation. GateResult to CriticalGate: the result evaluates that gate.",
  ["Control", "ControlAssessment", "GateResult"], ["CriticalGate", "GateResult"], card("0..*", "0..*", outBy={"GateResult": (1, 1, "CriticalGate")}), "evaluatedBy",
  {"pairs": {"Control": ["CriticalGate"], "ControlAssessment": ["GateResult"], "GateResult": ["CriticalGate"]}, "qualifiers_for": {"Control": ["gateRole"]}}),
 ("CONSTRAINS", "constrains", "The source imposes a ceiling, condition, limitation or band withholding on the target. Attribute constraintType: CEILING, CONDITION, LIMITATION, BAND_WITHHELD, GATE_EFFECT.",
  ["GateResult", "UnknownRecord", "Finding"], ["GateResult", "ScoreSnapshot", "DecisionRecommendation", "AssuranceDecision", "AssuranceStatement"], card(), "constrainedBy",
  {"qualifiers": ["constraintType"]}),
 ("SUMMARISED_BY", "summarisedBy", "The source results are aggregated into the target score snapshot or recommendation.",
  ["ControlAssessment", "GateResult", "ScoreSnapshot", "UnknownRecord"], ["ScoreSnapshot", "DecisionRecommendation"], card("0..*", "1..*"), "summarises", {}),
 ("RECOMMENDS", "recommends", "The recommendation proposes the decision state and conditions taken up (or departed from, with reasons) by the target decision.",
  ["DecisionRecommendation"], ["AssuranceDecision"], card("0..1", "1..1"), "recommendedBy", {}),
 ("REVIEWED_BY", "reviewedBy", "The source record has been reviewed in the target review record.",
  None, ["ReviewRecord"], card("0..*", "1..*"), "reviews", {}),
 ("APPROVED_BY", "approvedBy", "The source record has been approved by the authority recorded in the target review record (reviewType APPROVAL).",
  ["AssuranceDecision", "AssuranceStatement", "AssuranceReport", "ReleaseManifest", "MigrationRecord", "ArchitectureSnapshot", "BaselineIssue", "Control"],
  ["ReviewRecord"], card("0..*", "1..*", outBy={"AssuranceDecision": (1, None, "ReviewRecord")}), "approves", {}),
 ("REPORTED_IN", "reportedIn", "The source is disclosed in the target report.",
  ["AssuranceDecision", "AssuranceStatement", "Finding", "UnknownRecord", "GateResult", "ScoreSnapshot"], ["AssuranceReport"], card(), "reports", {}),
 ("REQUIRES_ACTION", "requiresAction", "The source requires the target action to be completed (remediation, evidence collection, decision condition).",
  ["Finding", "UnknownRecord", "AssuranceDecision", "BaselineIssue"], ["Action"], card("0..*", "1..*"), "actionFor", {}),
 ("CLOSED_BY", "closedBy", "The source is closed by the target closure evidence, reassessment result or review.",
  ["Finding", "UnknownRecord", "Action", "BaselineIssue"], ["ReviewRecord", "EvidenceObject", "ControlAssessment", "MigrationRecord"], card(), "closes", {}),
 ("INVALIDATED_BY", "invalidatedBy", "The source can no longer be relied on because of the target event (evidence expiry, configuration drift, incident, test failure).",
  ["EvidenceObject", "CapacityAssertion", "ControlAssessment", "GateResult", "ScoreSnapshot", "AssuranceDecision", "AssuranceStatement"], ["Event"], card(), "invalidates", {}),
 ("TRIGGERS_REASSESSMENT", "triggersReassessment", "The source event or trigger rule requires reassessment of the target.",
  ["Event", "ReassessmentTrigger"], ["Control", "ControlAssessment", "GateResult", "Assessment", "AssuranceDecision", "ServiceOutcome"], card(), "reassessmentTriggeredBy", {}),
 ("SUPERSEDES", "supersedes", "The source replaces the target record of the same class; the target is retained with status SUPERSEDED. Acyclic.",
  None, None, card("0..*", "0..1"), "supersededBy", {"acyclic": True, "same_class": True}),
 ("MIGRATED_FROM", "migratedFrom", "The source was produced from the target (prior version, legacy vocabulary or legacy record) by the migration recorded in migrationRef.",
  None, None, card(), "migratedTo", {"qualifiers": ["migrationRef"], "external_target": True}),
 ("INTEGRATION_HANDOFF", "integrationHandoff", "The source AIDCF record is exchanged with the AI Trust Graph through the target reviewed handoff record (AIDCF-005).",
  None, ["IntegrationHandoff"], card("0..*", "1..*"), "handoffOf", {}),
]
assert len(REL) == 41
REL_BY_CODE = {r[0]: r for r in REL}
REL_BY_PROP = {r[1]: r for r in REL}
INVERSES = {r[6]: r[1] for r in REL if r[6]}

# ---------------------------------------------------------------------------
# Properties: name -> dict(kind, many, ...). kinds: str text date datetime int num bool code ref json obj list reflist
# ---------------------------------------------------------------------------
P = {}
def prop(name, kind, many=False, label=None, definition="", **kw):
    P[name] = dict(kind=kind, many=many, label=label or name, definition=definition, **kw)

for code, pname, d, dom, rng, cd, inv, extra in REL:
    prop(pname, "ref", True, label=code, definition=d, rel=code, domain=dom, range=rng)

# envelope
prop("semanticOwner", "str", pattern=ARTIFACT_PATTERN, definition="Artifact that owns the meaning of this record's class.")
prop("schemaVersion", "str", const=RELEASE, definition="Data-model release the record conforms to (AIDCF-016).")
prop("version", "str", pattern=SEMVER_PATTERN, definition="Version of this record (AIDCF-014 section 27), separate from identity.")
prop("status", "code", scheme="RecordLifecycle", definition="Record lifecycle (AIDCF-014 section 11A.1).")
prop("releaseRef", "str", pattern=RELEASE_PATTERN, definition="releaseId of the ReleaseManifest against which the record is valid.")
prop("sourceArtifact", "str", pattern=ARTIFACT_PATTERN, definition="Artifact the record was derived from.")
prop("sourceRecord", "str", definition="Originating record in a source system or registry (typed reference as scheme:value).")
prop("name", "str", definition="Human-readable name.", sub="http://www.w3.org/2000/01/rdf-schema#label")
prop("description", "text", definition="Definition or narrative.")
prop("scope", "obj", obj="Scope", definition="CapabilityInstance, boundary and ArchitectureSnapshot the record applies to.")
prop("effectiveFrom", "datetime", definition="Start of validity.")
prop("effectiveTo", "datetime", definition="End of validity (evidence expiry, decision validity).")
prop("createdAt", "datetime"); prop("createdBy", "ref", range=["PartyEntity"], definition="Party that created the record.")
prop("modifiedAt", "datetime"); prop("modifiedBy", "ref", range=["PartyEntity"])
prop("classification", "code", scheme="Classification", definition="Sensitivity of the record (AIDCF-014 section 11A.8).")
prop("distributionControlRef", "ref", range=["DistributionControl"], definition="Disclosure rule; mandatory when classification is above INTERNAL.")
prop("provenance", "obj", obj="Provenance", definition="Provenance of the record (AIDCF-014 section 26).")
prop("reviewState", "code", scheme="AssertionState", definition="Assertion review state (AIDCF-014 section 11A.2); mandatory for assertion-bearing classes.")
prop("externalIdentifiers", "obj", True, obj="ExternalIdentifier", definition="Typed external keys (scheme, value).")
prop("extensions", "json", definition="Extension properties keyed by registered namespace prefix (AIDCF-014 section 33), carried as rdf:JSON.")
prop("nullReasons", "json", definition="Map of profile attribute name to explicit null reason (NOT_APPLICABLE with rationale reference, or UNKNOWN with UnknownRecord reference).")
# nested
prop("sourceSystem", "str"); prop("method", "code", scheme="ProvenanceMethod"); prop("transformationVersion", "str")
prop("synthetic", "bool", definition="True when the record is synthetic and describes no real facility.")
prop("legacyValue", "str", definition="Original value preserved on migration (TDS-REQ-044).")
prop("identifierScheme", "str"); prop("identifierValue", "str")
prop("capabilityRef", "ref", range=["CapabilityInstance"]); prop("snapshotRef", "ref", range=["ArchitectureSnapshot"])
prop("boundaryNote", "text")
# capability
prop("owner", "ref", range=["PartyEntity"], definition="Accountable PartyEntity.")
prop("lifecycle", "code", scheme="LifecycleStage")
prop("workload", "code", True, scheme="WorkloadClass"); prop("workloadCharacteristics", "text")
prop("criticality", "code", scheme="Criticality"); prop("boundary", "text")
prop("demandProfile", "text"); prop("operatingEnvelope", "text")
prop("operatingStates", "code", True, scheme="OperatingState")
prop("decisionQuestion", "text", definition="The decision question the assessment answers.")
prop("architectureBaseline", "ref", range=["ArchitectureSnapshot"])
prop("measure", "text"); prop("tolerance", "text"); prop("duration", "str"); prop("workloadClass", "code", scheme="WorkloadClass")
prop("functionStatement", "text")
prop("snapshotDate", "date"); prop("reconciliationStatus", "code", scheme="ReconciliationStatus")
prop("reconciliationEvidenceRef", "ref", range=["EvidenceObject"])
prop("faultDomainRefs", "ref", True, range=["FaultDomain"]); prop("dependencyRefs", "ref", True, range=["Dependency"])
prop("assertionRefs", "ref", True, range=["CapacityAssertion", "Assertion"])
prop("domainCode", "code", scheme="Domain")
prop("systemKind", "str"); prop("assetKind", "str"); prop("interfaceKind", "str"); prop("resourceKind", "str"); prop("componentKind", "str")
prop("locationKind", "code", scheme="LocationKind"); prop("partyKind", "code", scheme="PartyKind")
prop("faultDomainMembers", "ref", True, range=ARCH + ["Safeguard"]); prop("commonMode", "text"); prop("blastRadius", "text")
prop("stateCode", "code", scheme="OperatingState"); prop("entryConditions", "text"); prop("transitionRules", "text")
prop("subjectRef", "ref", definition="The record the record is about.")
prop("metric", "str"); prop("assertedValue", "num"); prop("unit", "str"); prop("environment", "text"); prop("derating", "text")
prop("evidenceDate", "date"); prop("illustrative", "bool")
prop("sourceRef", "ref"); prop("targetRef", "ref")
prop("dependencyType", "code", scheme="DependencyType"); prop("strength", "code", scheme="DependencyStrength")
prop("direction", "text"); prop("dependencyCriticality", "text", definition="Effect on ServiceOutcome if lost.")
prop("substitutability", "text", definition="Alternatives and time to substitute.")
prop("faultDomainRef", "ref", range=["FaultDomain"]); prop("external", "bool")
prop("confidence", "code", scheme="Confidence"); prop("confidenceFlags", "code", True, scheme="ConfidenceFlag")
prop("threatSource", "text"); prop("hazardType", "code", scheme="HazardType"); prop("failureMechanism", "text")
prop("preState", "code", scheme="OperatingState"); prop("residualState", "code", scheme="OperatingState")
prop("propagationSteps", "reflist", definition="Ordered PROPAGATES_TO relationship records of this scenario (rdf:List).")
prop("expectedSafeguards", "ref", True, range=["Safeguard"], definition="Safeguards expected to act in the scenario (they protect the affected elements via PROTECTED_BY).")
prop("outcomeEffects", "obj", True, obj="OutcomeEffect")
prop("outcomeRef", "ref", range=["ServiceOutcome"]); prop("effect", "text"); prop("exceedsTolerance", "bool")
prop("safeguardFunction", "code", scheme="SafeguardFunction"); prop("activation", "code", scheme="Activation")
prop("activationTrigger", "text"); prop("timeToAct", "str")
prop("authority", "ref", range=["PartyEntity", "InfrastructureSystem"], definition="PartyEntity or control system authorised to activate.")
prop("stateCoverage", "code", True, scheme="OperatingState"); prop("safeguardFailureModes", "str", True)
# control framework
prop("controlCode", "str", pattern=MCF_PATTERN, definition="Canonical control identifier MCF-DOM-NNN.")
prop("familyCode", "str", pattern=FAMILY_PATTERN); prop("gateCode", "str", pattern=GATE_PATTERN)
prop("objective", "text"); prop("requirement", "text"); prop("applicability", "text")
prop("assessmentCriteria", "str", True); prop("assessmentMethods", "code", True, scheme="AssessmentMethod")
prop("controlType", "code", scheme="ControlType"); prop("claimType", "code", scheme="ClaimType")
prop("requiredAssuranceLevel", "code", scheme="AssuranceLevel"); prop("profileTier", "code", scheme="ControlProfileTier")
prop("amendmentRef", "str")
prop("gateMappings", "obj", True, obj="GateMapping")
prop("gateRef", "ref", range=["CriticalGate"]); prop("gateRole", "code", scheme="GateRole")
prop("gateScope", "text"); prop("evidenceFloor", "code", scheme="Sufficiency")
prop("failCeiling", "code", scheme="DecisionState", definition="Decision-level ceiling applied when this gate is FAIL, derived from the AIDCF-010 prose ceiling (AIDCF-016 section 9.4).")
prop("unknownCeiling", "code", scheme="DecisionState", definition="Decision-level ceiling applied when this gate is UNKNOWN or NOT_ASSESSED, derived from the AIDCF-010 prose ceiling.")
prop("failCeilingText", "text"); prop("unknownCeilingText", "text"); prop("ceilingDerivation", "text")
prop("approvedNaConditions", "text")
prop("gateCriteria", "obj", True, obj="GateCriterion")
prop("criterionId", "str", pattern=r"^GC-(0[1-9]|1[0-5])-[0-9]+$"); prop("criterion", "text"); prop("testMethod", "text")
# evidence
prop("requiredClasses", "code", True, scheme="EvidenceClass"); prop("optionalClasses", "code", True, scheme="EvidenceClass")
prop("qualityFloor", "obj", obj="QualityVector"); prop("sufficiencyFloor", "code", scheme="Sufficiency")
prop("periodCoverage", "text"); prop("independence", "text"); prop("mandatoryItems", "str", True)
prop("evidenceClass", "code", scheme="EvidenceClass"); prop("evidenceSource", "str")
prop("collector", "ref", range=["PartyEntity"]); prop("custodian", "ref", range=["PartyEntity"])
prop("periodStart", "date"); prop("periodEnd", "date"); prop("integrityLevel", "code", scheme="IntegrityLevel")
prop("sha256", "str", pattern=SHA256_PATTERN); prop("byteSize", "int", minimum=0); prop("mediaType", "str"); prop("fixturePath", "str")
prop("qualityVector", "obj", obj="QualityVector"); prop("qualityBand", "code", scheme="QualityBand")
for q in ["provenanceRating", "fitnessRating", "coverageRating", "reliabilityRating", "timelinessRating", "integrityRating"]:
    prop(q, "int", minimum=0, maximum=5)
prop("sufficiency", "code", scheme="Sufficiency"); prop("sealedAt", "datetime")
# programme / assessment
prop("programOwner", "ref", range=["PartyEntity"]); prop("decisionAuthority", "ref", range=["PartyEntity"])
prop("targetAssuranceLevel", "code", scheme="AssuranceLevel"); prop("cadence", "text"); prop("charter", "text")
prop("profileRef", "str"); prop("team", "str", True)
prop("evidenceManifest", "ref", True, range=["EvidencePackage"])
prop("controlUniverseCount", "int", minimum=0)
prop("population", "text"); prop("sampleSize", "int", minimum=0); prop("selectionMethod", "text"); prop("sizeRationale", "text")
prop("procedureSteps", "list", definition="Ordered method steps (rdf:List).")
prop("controlRef", "ref", range=["Control"])
prop("testAuthority", "ref", range=["PartyEntity"]); prop("preconditions", "text"); prop("safetyControls", "text")
prop("observations", "text"); prop("testOutcome", "text"); prop("testDate", "date"); prop("procedureRef", "ref", range=["AssessmentProcedure"])
prop("result", "code", scheme="ControlResult"); prop("resultRationale", "text"); prop("assessor", "ref", range=["PartyEntity"])
prop("assessedAt", "date"); prop("evidenceSufficiency", "code", scheme="Sufficiency"); prop("applicabilityBasis", "text")
prop("implementationMaturity", "code", scheme="ImplementationMaturity"); prop("naRationale", "text")
prop("criterionRef", "str"); prop("condition", "text"); prop("cause", "text"); prop("consequence", "text")
prop("findingClass", "code", scheme="FindingClass"); prop("gateEffect", "text"); prop("scoreEffect", "text")
prop("findingStatus", "code", scheme="FindingStatus")
prop("missingAttribute", "str"); prop("unknownType", "code", scheme="UnknownType"); prop("unknownSeverity", "code", scheme="UnknownSeverity")
prop("reason", "text"); prop("material", "bool"); prop("decisionEffect", "text")
prop("evidenceNeeded", "text"); prop("resolutionTrigger", "text"); prop("disposition", "text"); prop("dueDate", "date")
prop("unknownStatus", "code", scheme="UnknownStatus")
# gates, scores, decisions
prop("gateApplicability", "code", scheme="GateApplicability")
prop("gateState", "code", scheme="GateState"); prop("controlEvaluations", "obj", True, obj="ControlEvaluation")
prop("criteriaResults", "obj", True, obj="CriterionResult"); prop("criterionOutcome", "code", scheme="CriterionOutcome")
prop("controlAssessmentRef", "ref", range=["ControlAssessment"])
prop("controlResult", "code", scheme="ControlResult"); prop("gateLevelEvaluation", "text"); prop("rollupRationale", "text")
prop("profileVersion", "str"); prop("scoreInputs", "obj", True, obj="ScoreInput"); prop("scoreValue", "num", minimum=0, maximum=100)
prop("weighting", "code", scheme="Weighting")
prop("coverage", "obj", obj="Coverage")
for n in ["inScopeCount", "notApplicableCount", "scoredCount", "unknownCount", "notAssessedCount", "assessedCount",
          "us1Count", "us2Count", "us3Count", "us4Count", "us5Count"]:
    prop(n, "int", minimum=0)
prop("coveragePercent", "num", minimum=0, maximum=100)
prop("band", "code", scheme="ScoreBand"); prop("bandWithheldReason", "text"); prop("gateOverlay", "text")
prop("unknownOverlay", "obj", obj="UnknownOverlay")
prop("calculationHash", "str", pattern=SHA256_PATTERN); prop("calculationMethod", "text")
prop("domainScores", "obj", True, obj="DomainScore"); prop("meanScore", "num", minimum=0, maximum=100)
prop("recommendedState", "code", scheme="DecisionState"); prop("decisionCeiling", "code", scheme="DecisionState")
prop("ceilingDrivers", "str", True)
prop("scoreRef", "ref", range=["ScoreSnapshot"])
prop("gateResultRefs", "ref", True, range=["GateResult"]); prop("unknownRefs", "ref", True, range=["UnknownRecord"])
prop("reviewType", "code", scheme="ReviewType"); prop("reviewer", "ref", range=["PartyEntity"]); prop("reviewerRole", "str")
prop("reviewIndependence", "code", scheme="ReviewIndependence"); prop("scopeReviewed", "text")
prop("reviewedAt", "date"); prop("reviewOutcome", "code", scheme="ReviewOutcome"); prop("comments", "text")
prop("decisionScope", "text")
prop("conditions", "obj", True, obj="DecisionCondition"); prop("conditionText", "text"); prop("relatedRefs", "ref", True)
prop("decisionState", "code", scheme="DecisionState"); prop("decisionLifecycle", "code", scheme="DecisionLifecycle")
prop("notCertification", "bool"); prop("controllingReasons", "str", True); prop("limitations", "str", True)
prop("decisionRef", "ref", range=["AssuranceDecision"])
prop("statementText", "text"); prop("prohibitedClaims", "str", True); prop("permittedClaims", "str", True); prop("audience", "str")
prop("reportClass", "code", scheme="ReportClass"); prop("issuer", "ref", range=["PartyEntity"]); prop("intendedUsers", "str", True)
prop("intendedUse", "text"); prop("sections", "str", True)
prop("programRef", "ref", range=["AssuranceProgram"]); prop("assessmentRef", "ref", range=["Assessment"])
prop("closureCriteria", "text"); prop("actionStatus", "code", scheme="ActionStatus")
prop("triggerRule", "text"); prop("triggerState", "code", scheme="TriggerState"); prop("eventTypes", "code", True, scheme="EventType")
prop("eventType", "code", scheme="EventType"); prop("eventSource", "str"); prop("observedAt", "datetime"); prop("effectiveAt", "datetime")
prop("payload", "json"); prop("sourceHealth", "code", scheme="SourceHealth"); prop("eventSeverity", "code", scheme="EventSeverity")
prop("materiality", "code", scheme="Materiality"); prop("affectedAssertions", "ref", True)
prop("candidateTriggers", "ref", True, range=["ReassessmentTrigger"]); prop("humanDisposition", "code", scheme="HumanDisposition")
prop("resultingDecisionEffect", "text")
prop("targetSystem", "str"); prop("handoffType", "code", scheme="HandoffType"); prop("mappingType", "code", scheme="MappingType")
prop("aitgRefs", "str", True); prop("handoffDirection", "str"); prop("ownershipStatement", "text"); prop("conclusionsFederated", "bool")
prop("validationLayer", "code", scheme="ValidationLayer"); prop("ruleId", "str"); prop("outcome", "code", scheme="ValidationOutcome")
prop("message", "text"); prop("validator", "str"); prop("executedAt", "datetime"); prop("subjectPaths", "str", True)
prop("sourceRelease", "str"); prop("targetRelease", "str"); prop("mappings", "obj", True, obj="MigrationMapping")
prop("fromId", "str"); prop("toId", "str"); prop("changeType", "code", scheme="ChangeType"); prop("rationale", "text")
prop("unmappedValues", "str", True); prop("fallbackApplied", "bool")
prop("issueCode", "str", pattern=r"^BI-[0-9]{3}$"); prop("conflictType", "str")
prop("conflictSources", "obj", True, obj="ConflictSource"); prop("artifact", "str"); prop("artifactVersion", "str")
prop("location", "str"); prop("value", "text")
prop("impact", "text"); prop("baselineStatus", "code", scheme="BaselineStatus"); prop("provisionalValue", "text"); prop("resolution", "text")
prop("releaseId", "str", pattern=RELEASE_PATTERN); prop("releaseStatus", "code", scheme="RecordLifecycle")
prop("artifactManifest", "obj", True, obj="ManifestEntry"); prop("filePath", "str"); prop("publicId", "str")
prop("registryVersions", "obj", True, obj="VersionEntry"); prop("vocabularyVersions", "obj", True, obj="VersionEntry")
prop("schemaVersions", "obj", True, obj="VersionEntry"); prop("recordCount", "int", minimum=0)
prop("approvedCardinality", "text"); prop("knownIssues", "ref", True, range=["BaselineIssue"]); prop("knownIssuesFile", "str")
prop("migrationSet", "ref", True, range=["MigrationRecord"]); prop("testSuite", "obj", obj="TestSuite")
prop("suiteVersion", "str"); prop("validationResultsPath", "str")
prop("approvals", "obj", True, obj="Approval"); prop("approverRole", "str"); prop("approvalOutcome", "code", scheme="ApprovalOutcome")
prop("reviewRef", "ref", range=["ReviewRecord"])
prop("supersedesRelease", "str"); prop("integrity", "obj", obj="Integrity")
prop("digestAlgorithm", "str"); prop("canonicalisation", "str"); prop("signatureStatus", "code", scheme="SignatureStatus")
prop("signatureMethod", "str"); prop("signaturePath", "str"); prop("manifestDigest", "str", pattern=SHA256_PATTERN)
prop("excludedPaths", "str", True)
prop("permittedRecipients", "str", True); prop("purpose", "text"); prop("redactionProfile", "str"); prop("exportConditions", "text")
prop("maxClassification", "code", scheme="Classification")
prop("relationshipType", "code", scheme="RelationshipType")
prop("dependencyRef", "ref", range=["Dependency"]); prop("scenarioRef", "ref", range=["FailureScenario"])
prop("stepOrdinal", "int", minimum=1); prop("constraintType", "code", scheme="ConstraintType")
prop("migrationRef", "ref", range=["MigrationRecord"]); prop("edgeEvidenceRefs", "ref", True, range=["EvidenceObject", "EvidencePackage"])
# supporting classes
prop("controlledFunctions", "ref", True, range=["RequiredFunction"])
prop("assetOwner", "ref", range=["PartyEntity"]); prop("integrator", "ref", range=["PartyEntity"]); prop("maintainer", "ref", range=["PartyEntity"])
prop("riskAssessmentRef", "str"); prop("boundaryDescription", "text")
prop("channels", "str", True); prop("remoteAccess", "bool"); prop("countermeasures", "str", True)
prop("securityLevelKind", "code", scheme="SecurityLevelKind"); prop("slVector", "obj", obj="SLVector"); prop("basis", "text")
for i in range(1, 8):
    prop("fr%d" % i, "int", minimum=0, maximum=4)
prop("frCode", "code", scheme="FoundationalRequirementCode")
prop("predicate", "str"); prop("objectRef", "ref"); prop("objectValue", "text"); prop("assertionConditions", "text")

VOCABS["RelationshipType"] = ("Relationship type", "AIDCF-014 section 9", [(r[0], r[0].replace("_", " ").capitalize(), r[2]) for r in REL])

NESTED = {
 "Provenance": (["sourceSystem", "method", "synthetic"], ["transformationVersion", "legacyValue", "sha256"]),
 "Scope": (["capabilityRef"], ["snapshotRef", "boundaryNote"]),
 "ExternalIdentifier": (["identifierScheme", "identifierValue"], []),
 "GateMapping": (["gateRef", "gateRole"], []),
 "GateCriterion": (["criterionId", "criterion", "testMethod"], []),
 "CriterionResult": (["criterionId", "criterionOutcome"], ["rationale"]),
 "QualityVector": (["provenanceRating", "fitnessRating", "coverageRating", "reliabilityRating", "timelinessRating", "integrityRating"], []),
 "OutcomeEffect": (["outcomeRef", "effect", "exceedsTolerance"], []),
 "ControlEvaluation": (["controlRef", "gateRole", "controlResult"], ["controlAssessmentRef", "gateLevelEvaluation"]),
 "ScoreInput": (["controlRef", "controlResult"], ["controlAssessmentRef", "scoreValue"]),
 "Coverage": (["inScopeCount", "notApplicableCount", "assessedCount", "scoredCount", "unknownCount", "notAssessedCount", "coveragePercent"], []),
 "UnknownOverlay": (["us1Count", "us2Count", "us3Count", "us4Count", "us5Count"], []),
 "DomainScore": (["domainCode", "inScopeCount", "scoredCount", "coveragePercent", "band"], ["meanScore", "bandWithheldReason"]),
 "DecisionCondition": (["conditionText", "owner", "dueDate"], ["relatedRefs"]),
 "MigrationMapping": (["fromId", "toId", "changeType", "rationale"], []),
 "ConflictSource": (["artifact", "artifactVersion", "location", "value"], []),
 "ManifestEntry": (["filePath", "sha256", "byteSize", "mediaType"], ["publicId", "version", "status"]),
 "VersionEntry": (["name", "version", "sha256"], ["recordCount", "filePath"]),
 "TestSuite": (["suiteVersion", "sha256", "validationResultsPath"], []),
 "Approval": (["approverRole", "approvalOutcome"], ["reviewRef"]),
 "Integrity": (["digestAlgorithm", "canonicalisation", "signatureStatus"], ["signatureMethod", "signaturePath", "manifestDigest"]),
 "SLVector": (["fr1", "fr2", "fr3", "fr4", "fr5", "fr6", "fr7"], []),
}

ENVELOPE_REQUIRED = ["id", "type", "semanticOwner", "schemaVersion", "version", "status", "releaseRef", "sourceArtifact",
                     "name", "effectiveFrom", "createdAt", "createdBy", "classification", "provenance"]
ENVELOPE_OPTIONAL = ["sourceRecord", "description", "scope", "effectiveTo", "modifiedAt", "modifiedBy", "distributionControlRef",
                     "reviewState", "supersedes", "externalIdentifiers", "extensions", "nullReasons",
                     "hasUnknown", "reviewedBy", "migratedFrom", "integrationHandoff", "governedBy"]
ANY_RECORD_RELS = ["hasUnknown", "reviewedBy", "supersedes", "migratedFrom", "integrationHandoff", "governedBy"]

# Per-class profile: class -> (required, optional, minItems overrides)
R = {}
def cls(name, req, opt=(), mins=None):
    R[name] = (list(req), list(opt), mins or {})

cls("ReleaseManifest", ["releaseId", "releaseStatus", "artifactManifest", "registryVersions", "vocabularyVersions", "schemaVersions",
                        "approvedCardinality", "knownIssues", "knownIssuesFile", "migrationSet", "testSuite", "approvals", "integrity", "excludedPaths"],
    ["supersedesRelease", "approvedBy"], {"artifactManifest": 1, "approvals": 1})
cls("BaselineIssue", ["issueCode", "conflictType", "conflictSources", "impact", "baselineStatus"],
    ["provisionalValue", "condition", "resolution", "closedBy", "challenges", "requiresAction", "approvedBy"], {"conflictSources": 2})
cls("CapabilityInstance", ["owner", "lifecycle", "workload", "architectureBaseline", "hasOutcome", "criticality", "boundary",
                           "demandProfile", "operatingEnvelope", "operatingStates", "operatedBy"],
    ["workloadCharacteristics", "exposedTo"], {"hasOutcome": 1, "operatedBy": 1})
cls("ServiceOutcome", ["workloadClass", "measure", "tolerance", "duration", "operatingStates", "requiresFunction"],
    ["protectedBy", "recoversThrough"], {"requiresFunction": 1, "operatingStates": 1})
cls("RequiredFunction", ["functionStatement", "operatingStates", "implementedBy"],
    ["dependsOn", "consumesResource", "protectedBy", "propagatesTo", "recoversThrough"], {"implementedBy": 1})
cls("ArchitectureSnapshot", ["capabilityRef", "snapshotDate", "composedOf", "dependencyRefs", "faultDomainRefs", "operatingStates",
                             "assertionRefs", "reconciliationStatus", "reconciliationEvidenceRef"], ["approvedBy"], {"composedOf": 1})
SYS_OPT = ["composedOf", "connectsTo", "consumesResource", "dependsOn", "sharesFaultDomainWith", "locatedIn", "controlledBy",
           "monitoredBy", "protectedBy", "exposedTo", "propagatesTo", "recoversThrough"]
LEAF_OPT = ["dependsOn", "sharesFaultDomainWith", "monitoredBy", "protectedBy", "exposedTo", "propagatesTo", "recoversThrough"]
cls("InfrastructureSystem", ["domainCode", "systemKind", "operatedBy"], SYS_OPT, {"operatedBy": 1})
cls("AssetInstance", ["domainCode", "assetKind", "operatedBy"], SYS_OPT, {"operatedBy": 1})
cls("Interface", ["interfaceKind"], LEAF_OPT)
cls("Resource", ["resourceKind"], LEAF_OPT)
cls("Dependency", ["sourceRef", "targetRef", "dependencyType", "strength", "direction", "operatingStates", "dependencyCriticality",
                   "substitutability", "evidencedBy", "confidence"], ["faultDomainRef", "external", "monitoredBy"], {"evidencedBy": 1})
cls("FaultDomain", ["faultDomainMembers", "commonMode", "boundary", "blastRadius"], ["locatedIn", "evidencedBy"], {"faultDomainMembers": 2})
cls("OperatingState", ["stateCode", "entryConditions"], ["transitionRules"])
cls("CapacityAssertion", ["subjectRef", "metric", "assertedValue", "unit", "operatingStates", "environment", "duration", "derating",
                          "evidenceDate", "confidence", "illustrative"], ["evidencedBy", "invalidatedBy"])
cls("Threat", ["threatSource"], ["initiates"])
cls("Hazard", ["hazardType"], ["initiates"])
cls("FailureMode", ["failureMechanism"], ["initiates"])
cls("FailureScenario", ["preState", "propagationSteps", "expectedSafeguards", "residualState", "outcomeEffects", "confidence"], [],
    {"expectedSafeguards": 1, "outcomeEffects": 1})
cls("Safeguard", ["safeguardFunction", "activation", "activationTrigger", "timeToAct", "authority", "stateCoverage",
                  "safeguardFailureModes", "governedBy", "implementedBy", "operatedBy"],
    ["dependsOn", "sharesFaultDomainWith", "monitoredBy", "exposedTo", "recoversThrough"],
    {"governedBy": 1, "implementedBy": 1, "operatedBy": 1, "stateCoverage": 1})
cls("ControlDomain", ["domainCode", "composedOf"], [], {"composedOf": 6})
cls("ControlFamily", ["familyCode", "domainCode", "composedOf"], [], {"composedOf": 4})
cls("Control", ["controlCode", "domainCode", "familyCode", "objective", "requirement", "claimType", "requiredAssuranceLevel",
                "controlType", "profileTier", "hasEvidenceRequirement", "gateMappings"],
    ["applicability", "assessmentCriteria", "assessmentMethods", "amendmentRef", "evaluatesGate", "assessedBy", "approvedBy"],
    {"hasEvidenceRequirement": 1})
cls("EvidenceRequirement", ["claimType", "requiredClasses", "sufficiencyFloor", "stateCoverage", "periodCoverage", "independence"],
    ["profileTier", "optionalClasses", "qualityFloor", "mandatoryItems", "evidencedBy"], {"requiredClasses": 1})
cls("EvidenceObject", ["evidenceClass", "evidenceSource", "collector", "custodian", "periodStart", "periodEnd",
                       "operatingStates", "integrityLevel", "sha256", "byteSize", "mediaType", "qualityVector", "qualityBand", "sufficiency"],
    ["fixturePath", "confidenceFlags", "supports", "challenges", "qualifies", "invalidatedBy"])
cls("EvidencePackage", ["composedOf", "sufficiency", "custodian", "sealedAt", "sha256"], [], {"composedOf": 1})
cls("AssuranceProgram", ["programOwner", "decisionAuthority", "targetAssuranceLevel", "profileRef", "cadence", "charter", "composedOf"], [])
cls("Assessment", ["decisionQuestion", "capabilityRef", "architectureBaseline", "operatingStates", "profileRef", "weighting", "team",
                   "evidenceManifest", "controlUniverseCount", "composedOf", "governedBy"],
    ["hasFinding"], {"composedOf": 1, "evidenceManifest": 1})
cls("AssessmentProcedure", ["controlRef", "claimType", "procedureSteps", "assessmentMethods", "resultsIn"], [], {"resultsIn": 1})
cls("Sample", ["population", "sampleSize", "selectionMethod", "sizeRationale", "resultsIn"], [], {"resultsIn": 1})
cls("TestRecord", ["procedureRef", "testAuthority", "preconditions", "safetyControls", "procedureSteps", "observations",
                   "testOutcome", "testDate", "resultsIn"], [], {"resultsIn": 1})
cls("ControlAssessment", ["subjectRef", "claimType", "applicabilityBasis", "result", "resultRationale", "assessmentMethods",
                          "operatingStates", "confidence", "evidenceSufficiency", "assessor", "assessedAt", "governedBy"],
    ["evidencedBy", "evaluatesGate", "hasFinding", "summarisedBy", "implementationMaturity", "naRationale", "invalidatedBy"],
    {"assessmentMethods": 1})
cls("Finding", ["criterionRef", "condition", "cause", "consequence", "evidencedBy", "findingClass", "gateEffect", "scoreEffect",
                "owner", "findingStatus"], ["requiresAction", "challenges", "constrains", "closedBy", "reportedIn"], {"evidencedBy": 1})
cls("UnknownRecord", ["subjectRef", "missingAttribute", "unknownType", "unknownSeverity", "reason", "material", "decisionEffect",
                      "evidenceNeeded", "owner", "resolutionTrigger", "unknownStatus"],
    ["disposition", "dueDate", "constrains", "requiresAction", "challenges", "qualifies", "closedBy", "summarisedBy", "reportedIn"])
cls("CriticalGate", ["gateCode", "gateScope", "evidenceFloor", "requiredClasses", "failCeiling", "unknownCeiling", "failCeilingText",
                     "unknownCeilingText", "ceilingDerivation", "approvedNaConditions", "gateCriteria", "hasEvidenceRequirement"], [],
    {"hasEvidenceRequirement": 1, "gateCriteria": 1})
cls("GateResult", ["evaluatesGate", "gateCode", "gateApplicability", "controlEvaluations", "criteriaResults", "evidenceSufficiency",
                   "stateCoverage", "gateState", "decisionEffect", "rollupRationale"],
    ["evidencedBy", "hasFinding", "constrains", "summarisedBy", "reportedIn", "naRationale", "invalidatedBy"], {"evaluatesGate": 1})
cls("ScoreSnapshot", ["subjectRef", "profileVersion", "scoreInputs", "weighting", "coverage", "band", "unknownOverlay", "gateOverlay",
                      "calculationHash", "calculationMethod", "domainScores"],
    ["meanScore", "bandWithheldReason", "summarisedBy", "reportedIn", "invalidatedBy"], {"scoreInputs": 1})
cls("DecisionRecommendation", ["decisionQuestion", "recommendedState", "decisionCeiling", "ceilingDrivers", "recommends"],
    ["conditions", "limitations"], {"recommends": 1})
cls("ReviewRecord", ["reviewType", "reviewer", "reviewerRole", "reviewIndependence", "scopeReviewed", "reviewOutcome", "reviewedAt"],
    ["comments", "challenges", "qualifies"])
cls("AssuranceDecision", ["decisionQuestion", "subjectRef", "decisionScope", "gateResultRefs", "unknownRefs", "scoreRef",
                          "decisionState", "decisionLifecycle", "approvedBy", "notCertification", "controllingReasons", "effectiveTo"],
    ["conditions", "limitations", "reportedIn", "requiresAction", "invalidatedBy"], {"gateResultRefs": 15, "approvedBy": 1})
cls("AssuranceStatement", ["decisionRef", "decisionState", "audience", "statementText", "permittedClaims", "prohibitedClaims", "reportedIn"],
    ["approvedBy", "invalidatedBy", "effectiveTo"])
cls("AssuranceReport", ["reportClass", "programRef", "assessmentRef", "decisionRef", "decisionState", "issuer", "intendedUsers",
                        "intendedUse", "sections", "limitations", "prohibitedClaims", "effectiveTo"], ["approvedBy"])
cls("Action", ["owner", "dueDate", "actionStatus", "closureCriteria"], ["closedBy"])
cls("ReassessmentTrigger", ["triggerRule", "eventTypes", "triggerState", "triggersReassessment"], [], {"triggersReassessment": 1})
cls("Event", ["eventType", "subjectRef", "eventSource", "sourceHealth", "observedAt", "effectiveAt", "payload", "eventSeverity",
              "materiality", "affectedAssertions", "candidateTriggers", "humanDisposition", "snapshotRef", "resultingDecisionEffect"],
    ["triggersReassessment"])
cls("IntegrationHandoff", ["targetSystem", "handoffType", "mappingType", "aitgRefs", "handoffDirection", "ownershipStatement",
                           "conclusionsFederated"], [])
cls("ValidationResult", ["validationLayer", "ruleId", "outcome", "message", "validator", "executedAt"], ["subjectPaths", "subjectRef"])
cls("MigrationRecord", ["sourceRelease", "targetRelease", "mappings", "unmappedValues", "fallbackApplied"], ["approvedBy"], {"mappings": 1})
cls("DistributionControl", ["permittedRecipients", "purpose", "redactionProfile", "exportConditions", "maxClassification"], [])
cls("Location", ["locationKind"], [])
cls("PartyEntity", ["partyKind"], [])
cls("Component", ["componentKind"], [])
cls("IACS", ["domainCode", "systemKind", "operatedBy", "controlledFunctions"], SYS_OPT + ["assetOwner", "integrator", "maintainer"], {"operatedBy": 1})
cls("IACSZone", ["domainCode", "systemKind", "operatedBy", "riskAssessmentRef", "boundaryDescription", "controlledFunctions"], SYS_OPT, {"operatedBy": 1})
cls("Conduit", ["interfaceKind", "channels", "remoteAccess", "countermeasures"], LEAF_OPT)
cls("SecurityLevel", ["securityLevelKind", "subjectRef", "slVector", "basis"], [])
cls("FoundationalRequirement", ["frCode"], [])
cls("Assertion", ["subjectRef", "predicate", "assertionConditions", "confidence"], ["objectRef", "objectValue"])
cls("RelationshipRecord", ["relationshipType", "sourceRef", "targetRef", "confidence"],
    ["operatingStates", "dependencyRef", "faultDomainRef", "scenarioRef", "stepOrdinal", "gateRole", "constraintType", "migrationRef",
     "edgeEvidenceRefs"])
assert set(R) == set(CLASS_META), set(CLASS_META) ^ set(R)


def required_fields(c):
    """Envelope + profile required fields for class c, including class-determined conditional envelope fields."""
    req = list(ENVELOPE_REQUIRED) + list(R[c][0])
    if c in ASSERTION_BEARING:
        req.append("reviewState")
    if c in ASSESSABLE:
        req.append("scope")
    return req


SCHEMA_FILE = {
 "CapabilityInstance": "capability", "ArchitectureSnapshot": "architecture", "EvidenceObject": "evidence",
 "ScoreSnapshot": "score", "AssuranceDecision": "decision", "AssuranceReport": "report",
 "InfrastructureSystem": "system", "AssuranceProgram": "program",
}
def kebab(n):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", n).lower().replace("i-a-c-s", "iacs")
def schema_file(c):
    return SCHEMA_FILE.get(c, kebab(c)) + ".schema.json"

REQUIRED_SCHEMA_FILES = ["common-envelope", "definitions", "capability", "service-outcome", "required-function", "architecture", "dependency",
    "failure-scenario", "safeguard", "control", "evidence-requirement", "evidence", "control-assessment", "finding",
    "unknown-record", "gate-result", "score", "decision", "report", "event", "integration-handoff", "validation-result",
    "release-manifest", "system", "relationship-record"]


def derive_ceiling(text):
    """Derive a decision-level ceiling code from AIDCF-010 prose (registries/gates/critical-gates.csv).

    Rule (AIDCF-016 section 9.4): (1) a code stated "for the decision as a whole" or "for the whole decision" wins;
    (2) otherwise a code stated without an outcome or claim qualifier at the start of the text ("LIMITED." or
    "LIMITED;"); (3) otherwise the lowest-ranked decision code mentioned anywhere under the AIDCF-010 order (conservative); (4) no code: NOT_ASSURED.
    Returns (code, rule).
    """
    codes = ["REASONABLY_ASSURED", "CONDITIONALLY_ASSURED", "NOT_ASSURED", "INCONCLUSIVE", "LIMITED"]
    m = re.search(r"\b(%s)\b for the (decision as a whole|whole decision)" % "|".join(codes), text)
    if m:
        return m.group(1), "rule 1 (stated for the decision as a whole)"
    m = re.match(r"\s*(%s)\s*[.;]" % "|".join(codes), text)
    if m:
        return m.group(1), "rule 2 (unqualified leading code)"
    found = [c for c in codes if re.search(r"\b%s\b" % c, text)]
    if not found:
        return "NOT_ASSURED", "rule 4 (no code in text; conservative default)"
    found.sort(key=lambda c: DECISION_RANK[c])
    return found[0], "rule 3 (lowest-ranked code mentioned; conservative)"
