"""List the rows where an AI cross-check disagrees with the screener's exclusion.

Usage: python3 compare.py response-kai-batch-1.csv [more response files ...]
Reads the batch-*.csv files in this folder for the screener's decisions.
Stdlib only."""
import csv, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
screener = {}
for f in sorted(glob.glob(os.path.join(HERE, "batch-*.csv"))):
    for r in csv.DictReader(open(f, encoding="utf-8")):
        screener[r["incident_id"]] = r

seen, flagged, problems = set(), [], []
for f in sys.argv[1:]:
    text = open(f, encoding="utf-8-sig").read().strip()
    text = "\n".join(l for l in text.splitlines() if not l.startswith("```"))
    for r in csv.DictReader(text.splitlines()):
        r = {k.strip(): (v or "").strip() for k, v in r.items() if k}
        iid = r.get("incident_id", "")
        if iid not in screener:
            problems.append("%s: unknown incident_id %r" % (os.path.basename(f), iid))
            continue
        seen.add(iid)
        verdict = r.get("verdict", "").upper()
        if verdict != "AGREE" or r.get("your_code", "") != screener[iid]["exclusion_code"]:
            flagged.append((iid, verdict, r.get("your_detail_level", ""), r.get("your_code", ""), r.get("evidence", "")))

missing = sorted(set(screener) - seen)
print("rows checked: %d of %d" % (len(seen), len(screener)))
print("rows needing a human decision: %d" % len(flagged))
for iid, v, lvl, code, ev in flagged:
    s = screener[iid]
    print("\n%s  %s (%s)\n  screener: %s  |  model: %s, level %s, code %s\n  model evidence: %s\n  source: %s"
          % (iid, s["neutral_descriptor"], s["operator_name_as_published"], s["exclusion_code"], v, lvl, code, ev, s["primary_source_url"]))
if missing:
    print("\nnot yet checked: %s" % ", ".join(missing))
for p in problems:
    print("WARNING " + p)
