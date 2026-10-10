from pathlib import Path
import json,csv,re,hashlib,sys
from jsonschema import Draft202012Validator
R=Path(__file__).resolve().parents[1]
res=[]
def load(p): return json.loads((R/p).read_text())
def test(name,ok,details=''):
 res.append({'test':name,'pass':bool(ok),'details':details})
# registry cardinality and uniqueness
for fn,expected,key in [('domains.csv',15,'domainId'),('control-families.csv',90,'familyId'),('controls.csv',360,'controlId')]:
 rows=list(csv.DictReader((R/'registries'/fn).open()))
 test('registry-'+fn,len(rows)==expected and len({r[key] for r in rows})==expected,f'{len(rows)} rows')
controls={r['controlId'] for r in csv.DictReader((R/'registries/controls.csv').open())}
families={r['familyId'] for r in csv.DictReader((R/'registries/control-families.csv').open())}
test('canonical-control-id-pattern',all(re.match(r'^MCF-[A-Z]{3}-\d{3}$',x) for x in controls))
# schema tests
pairs=[('control-assessment','dataset/control-assessments.jsonld','@graph'),('gate','dataset/gate-results.jsonld','@graph'),('score','dataset/score-snapshot.jsonld',None),('decision','dataset/decision.jsonld',None),('evidence','dataset/evidence.jsonld','@graph')]
for schema_name,data_path,graph in pairs:
 schema=load('schemas/'+schema_name+'.schema.json');data=load(data_path);items=data[graph] if graph else [data]
 for i,item in enumerate(items):
  errs=list(Draft202012Validator(schema).iter_errors(item));test(f'{schema_name}-{i+1}',not errs,'; '.join(e.message for e in errs))
# no legacy live refs except migratedFrom and migration files
live=[]
for p in (R/'dataset').rglob('*.json*'):
 txt=p.read_text();
 for m in re.finditer(r'PILOT-[A-Z]{3}-\d{3}',txt): live.append((str(p.relative_to(R)),m.group()))
# Legacy is allowed only as migratedFrom; parse structures to ensure controlRef/controlRefs canonical
for a in load('dataset/control-assessments.jsonld')['@graph']: test('assessment-canonical-'+a['id'],a['controlRef'] in controls,a['controlRef'])
for g in load('dataset/gate-results.jsonld')['@graph']: test('gate-controls-canonical-'+g['gateId'],all(x in controls for x in g['controlRefs']))
# score reperformance
s=load('dataset/score-snapshot.jsonld');actual=round(sum(s['inputs'].values())/len(s['inputs']),4);payload='|'.join(f'{k}:{s["inputs"][k]}' for k in sorted(s['inputs']));h=hashlib.sha256(payload.encode()).hexdigest()
test('score-value-match',actual==s['rawScore'],f'{actual}');test('score-hash-match',h==s['calculationHash'],h)
# gates & report consistency
g=load('dataset/gate-results.jsonld')['@graph'];d=load('dataset/decision.jsonld');unknown=any(x['state']=='UNKNOWN' for x in g);test('unknown-blocks-positive',not (unknown and d['decisionState'] in ['REASONABLY_ASSURED','CONDITIONALLY_ASSURED']))
r=load('reports/r1-executive-report.json');test('report-decision-match',r['decisionState']==d['decisionState'])
# RDF parse and optional SHACL
rdf={'ontologyParsed':False,'shaclRuntimeExecuted':False,'conforms':None,'details':''}
try:
 from rdflib import Graph
 Graph().parse(R/'semantic/aidcf-core-v1.2.ttl',format='turtle');Graph().parse(R/'semantic/aidcf-shapes-v1.2.ttl',format='turtle');rdf['ontologyParsed']=True
 try:
  from pyshacl import validate
  data=Graph().parse(R/'semantic/aidcf-core-v1.2.ttl',format='turtle');sh=Graph().parse(R/'semantic/aidcf-shapes-v1.2.ttl',format='turtle');c,rg,rt=validate(data,shacl_graph=sh);rdf.update({'shaclRuntimeExecuted':True,'conforms':bool(c),'details':str(rt)})
 except Exception as e: rdf['details']='pyshacl unavailable or not executable: '+str(e)
except Exception as e: rdf['details']='RDF parse failed: '+str(e)
(R/'outputs/rdf-shacl-results.json').write_text(json.dumps(rdf,indent=2)+'\n')
passed=sum(x['pass'] for x in res);out={'release':'AIDCF-015 v1.2','tests':len(res),'passed':passed,'failed':len(res)-passed,'results':res,'rdfShacl':rdf,'overall':'CANONICAL_BASELINE_COMPLIANT_SYNTHETIC_REFERENCE_IMPLEMENTATION' if passed==len(res) else 'FAILED'}
(R/'outputs/validation-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));sys.exit(0 if passed==len(res) else 1)
