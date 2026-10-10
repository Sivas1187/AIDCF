"""Render the per-domain AIDCF-007A v1.1 control catalogues (standards/aidcf-007a/registry/controls/) from registries/controls/controls.json."""
import json,csv,collections
import os
R=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))+'/'; D=R+'standards/aidcf-007a/registry/'
C=json.load(open(R+'registries/controls/controls.json'))['controls']
doms={d['domainId']:d['domainName'] for d in csv.DictReader(open(R+'registries/domains/domains.csv'))}
fams={f['familyId']:f['familyName'] for f in csv.DictReader(open(R+'registries/families/control-families.csv'))}
gates={g['gateId']:g['name'] for g in csv.DictReader(open(R+'registries/gates/critical-gates.csv'))}
guides={'GOV':'AIDCF-018-GOV_Governance_Domain_Guide_v1.0.md'}
import glob,os
for p in glob.glob(R+'standards/aidcf-018-domain-guides/*.md'): guides[os.path.basename(p)[10:13]]=os.path.basename(p)
os.makedirs(D+'controls',exist_ok=True)
esc=lambda s:str(s).replace('|','\\|')
for dom in doms:
    cs=[c for c in C if c['controlId'][4:7]==dom]
    o=[f"# AIDCF-007A Control Catalogue — {dom} {doms[dom]}",'',f"Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-{dom}](../../../aidcf-018-domain-guides/{guides.get(dom,'')}).",'','## Summary','','| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |','|---|---|---|---|---|---|---|']
    for c in cs:
        cr=', '.join(g['gateId'] for g in c['gateMappings'] if g['role']=='CRITICAL') or '—'
        sp=', '.join(g['gateId'] for g in c['gateMappings'] if g['role']=='SUPPORTING') or '—'
        o.append(f"| [{c['controlId']}](#{c['controlId'].lower()}) | {esc(c['title'])} | {c['controlType']} | {c['evidenceProfile']['claimType']} | {c['requiredAssuranceLevel']} | {cr} | {sp} |")
    cur=None
    for c in cs:
        if c['familyId']!=cur:
            cur=c['familyId']; o+=['',f"## {cur} {fams[cur]}"]
        ep=c['evidenceProfile']
        o+=['',f"### {c['controlId']}",'',f"**{c['title']}** · {c['controlType']} · claim type {ep['claimType']} · required {c['requiredAssuranceLevel']}",'',f"**Objective.** {c['objective']}",'',f"**Requirement.** {c['requirement']}",'','**Assessment criteria**','']
        o+=[f"{i+1}. {x}" for i,x in enumerate(c['assessmentCriteria'])]
        if c['parameters']:
            o+=['','**Capability-profile parameters**','','| Parameter | Unit | Illustrative default | Basis |','|---|---|---|---|']+[f"| {esc(p.get('name'))} | {esc(p.get('unit'))} | {esc(p.get('illustrativeDefault'))} | {esc(p.get('basis'))} |" for p in c['parameters']]
        o+=['','**Minimum evidence**','']+[f"- {x}" for x in c['minimumEvidence']]
        o+=['','**Evidence requirement profile**','','| Field | Value |','|---|---|']
        for k in ["profileTier","requiredClasses","optionalClasses","qualityFloor","sufficiencyFloor","stateCoverage","periodCoverage","independence","mandatoryItems","acceptableAlternatives","unknownEffect","reassessmentTriggers"]:
            v=ep[k]; o.append(f"| {k} | {esc('; '.join(v) if isinstance(v,list) else v)} |")
        o+=['',f"**Assessment methods.** {', '.join(c['assessmentMethods'])}",'','**Assessment procedure**','']+[f"{i+1}. {x}" for i,x in enumerate(c['assessmentProcedure'])]
        o+=['',f"**Gate mappings.** "+('; '.join(f"{g['gateId']} {gates[g['gateId']]} ({g['role']})" for g in c['gateMappings']) or 'None'),
            '',f"**Applicability.** {c['applicability']}",'',f"**Lifecycle stages.** {', '.join(c['lifecycleStages'])} · **Operating states.** {', '.join(c['operatingStates'])}",
            '',f"**Failure modes addressed.** {'; '.join(c['failureModes'])}",'',f"**Testing safety.** {c['testingSafety']}",'',f"**UNKNOWN rule.** {c['unknownRule']}",
            '',f"**Ontology classes.** {', '.join(c['ontologyClasses'])} · **Related controls.** {', '.join(c['relatedControls']) or '—'}",'',f"**Informative references.** {'; '.join(c['informativeReferences']) or '—'}"]
    open(D+f"controls/AIDCF-007A_Controls_{dom}_v1.1.md",'w').write('\n'.join(o)+'\n')
print('ok')
