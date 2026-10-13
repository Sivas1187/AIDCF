# Implementation

| Item | Content |
|---|---|
| `AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0` (.md, .pdf) | The AIDCF-015 specification. It describes the v1.0 to v1.2 package design and is kept as a historical record; the v1.3 package README describes the current package. |
| [`aidcf-015-v1.4/`](aidcf-015-v1.4/README.md) | **Draft** successor to v1.3 (release AIDCF-REL-2026.10.2): the same package with seven more failure scenarios, FS-06 to FS-12, instantiated from AIDCF-004 library scenarios. Gate results and decision unchanged. v1.3 stays current until v1.4 is approved. |
| [`aidcf-015-v1.3/`](aidcf-015-v1.3/README.md) | **Current** synthetic reference implementation, built on the AIDCF-016 MDM 1.3 schema set in `../schemas/` and the AIDCF-007A registry v1.1 in `../registries/`. |
| `aidcf-015-v1.2/` | Previous package, left unchanged as released so its manifest and hashes stay valid. Its `registries/controls.csv` has placeholder control titles and requirement text. |

Earlier v1.1 is in `archive/historical-releases/`.

## Running v1.3

```bash
cd implementation/aidcf-015-v1.3
python3 -m pip install -r requirements.txt
python3 -B tools/run_all.py
```

The package imports the shared model from `../../schemas/tools/aidcf_model.py`, so run it from inside the repository, not from a copy of the folder alone. CI runs the same command on every push.

## What the result means

The synthetic package assesses 12 of the 360 controls (11 scored, 1 UNKNOWN), so coverage is 3.0556%. All 13 validation layers pass. The computed outcome is CG-03, CG-07 and CG-15 FAIL, CG-01, CG-05, CG-06, CG-08 and CG-10 UNKNOWN, the other gates NOT_ASSESSED, decision NOT_ASSURED (controlled by the CG-07 FAIL ceiling; the INCONCLUSIVE ceilings from CG-01, CG-05, the US5 UNKNOWN and low coverage are less restrictive), and band WITHHELD. This is the intended result: it shows the rules refusing a favourable conclusion on thin evidence, and reporting a demonstrated failure as such.

The package describes no real facility and establishes no assurance over one.
