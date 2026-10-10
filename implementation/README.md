# Implementation

- `AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0` (.md/.pdf): the AIDCF-015 specification.
- `aidcf-015-v1.2/`: the canonical-baseline-aligned synthetic reference implementation. Run `python tools/run_all.py` from inside that folder.

The synthetic implementation assesses only 12 representative controls (3.3333% of the canonical control universe) and does not establish assurance over a real facility. Earlier v1.1 is in `archive/historical-releases/`.

Known issue: `aidcf-015-v1.2/registries/controls.csv` carries placeholder control titles and requirement text. Control IDs, families and gate mappings are correct. The corrected registry is `registries/controls/controls.csv`; the package is left unchanged so its release manifest and hashes stay valid. To be corrected in the next package release.
