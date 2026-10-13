#!/usr/bin/env python3
"""Tests for AIDCF-VAL-001 v1.1 comparative validation (protocol section 10A).

Run: python3 -B research/back-testing/tests/test_comparative.py
Standard library only. Fixtures are FICTIONAL and built by make_fixtures.py.
Test IDs T-01 to T-12 and W1 to W10 refer to protocol v1.1 section 10A.
"""

import contextlib
import csv
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
FIX = HERE / "fixtures"
sys.path.insert(0, str(KIT))
import backtest_check as bc  # noqa: E402
import comparative as cp  # noqa: E402

D, P, ND, NA_, II, OOS, NAP = ("DETECTED", "PARTIALLY_DETECTED", "NOT_DETECTED", "NOT_ADDRESSED",
                               "INSUFFICIENT_INFORMATION", "OUT_OF_SCOPE", "NOT_APPLICABLE")


def cls(aidcf, baseline, reading):
    a = cp.side_value(aidcf, reading, "AIDCF")
    b = cp.combine_union(baseline, reading) if isinstance(baseline, dict) else cp.side_value(baseline, reading, "BASELINE")
    return cp.pair_class(a, b)


def run(*args, files=None):
    """Run backtest_check.main on a copy of the fixtures; returns (exit code, output)."""
    files = files or FIX
    argv = list(args) + [
        "--sheet", str(files / "coding-sheet.csv"), "--register", str(files / "incident-register.csv"),
        "--comparative-sheet", str(files / "comparative-sheet.csv"), "--baselines", str(files / "baselines.csv"),
        "--locks", str(files / "comparative-locks.csv")]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = bc.main(argv)
    return code, buf.getvalue()


class Mutated:
    """A temporary copy of the fixtures with one change."""

    def __enter__(self):
        self.dir = Path(tempfile.mkdtemp()) / "fixtures"
        shutil.copytree(FIX, self.dir)
        # point FILE locks at the copies (same bytes, so the same digests)
        cols, rows = self.rows("comparative-locks.csv")
        for r in rows:
            if r["artefact"].startswith("FILE:tests/fixtures/"):
                r["artefact"] = "FILE:" + str(self.dir / r["artefact"][len("FILE:tests/fixtures/"):])
        self.write("comparative-locks.csv", cols, rows)
        return self

    def relock(self):
        """Re-lock every FILE artefact after a mutation, so a test reaches the rule it is about."""
        import hashlib
        cols, rows = self.rows("comparative-locks.csv")
        for r in rows:
            if r["artefact"].startswith("FILE:"):
                path = Path(r["artefact"][len("FILE:"):])
                if path.exists():
                    r["value"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.write("comparative-locks.csv", cols, rows)

    def __exit__(self, *exc):
        shutil.rmtree(self.dir.parent)

    def rows(self, name):
        with open(self.dir / name, encoding="utf-8", newline="") as fh:
            r = csv.DictReader(fh)
            return r.fieldnames, list(r)

    def write(self, name, cols, rows):
        with open(self.dir / name, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)

    def edit(self, name, pred, **changes):
        cols, rows = self.rows(name)
        hit = 0
        for r in rows:
            if pred(r) and not hit:
                r.update(changes)
                hit = 1
        assert hit, "mutation matched no row"
        self.write(name, cols, rows)

    def drop(self, name, pred):
        cols, rows = self.rows(name)
        keep = [r for r in rows if not pred(r)]
        assert len(keep) < len(rows), "drop matched no row"
        self.write(name, cols, keep)


def is_base(inc, fid, m):
    return lambda r: (r["record_type"] == "BASELINE" and r["incident_id"] == "INC-EXAMPLE-%02d" % inc and
                      r["factor_id"] == fid and r["baseline_id"] == m and r["coding_round"] == "RECONCILED")


class WorkedExamples(unittest.TestCase):
    """T-12: fixtures W1 to W9 give the expected strict and inclusive classes (section 10A.5.5)."""

    def test_w1(self):
        self.assertEqual((cls(D, NA_, "strict"), cls(D, NA_, "inclusive")), ("b", "b"))

    def test_w2(self):
        self.assertEqual((cls(P, D, "strict"), cls(P, D, "inclusive")), ("c", "a"))

    def test_w3(self):
        self.assertEqual((cls(ND, P, "strict"), cls(ND, P, "inclusive")), ("d", "c"))
        self.assertEqual(cp.miss_subtype(ND, "strict"), "ADDRESSED_NOT_DETECTED")
        self.assertEqual(cp.miss_subtype(P, "strict"), "PARTIAL")

    def test_w4(self):
        self.assertEqual((cls(NA_, OOS, "strict"), cls(NA_, OOS, "inclusive")), ("d", "d"))
        self.assertEqual(cp.miss_subtype(OOS, "strict"), "DECLARED_EXCLUSION")

    def test_w5(self):
        self.assertEqual(cls(D, II, "strict"), "EXCLUDED_INDETERMINATE_BASELINE")

    def test_w6(self):
        self.assertEqual(cls(II, D, "inclusive"), "EXCLUDED_INDETERMINATE_AIDCF")

    def test_w7(self):
        union = {"BL-ENG": ND, "BL-OT": NAP, "BL-CX": II, "BL-TIER": NA_, "BL-ISMS": NA_, "BL-TDD": NA_}
        self.assertEqual(cls(D, union, "strict"), "EXCLUDED_INDETERMINATE_BASELINE")
        self.assertEqual(cls(D, union, "inclusive"), "EXCLUDED_INDETERMINATE_BASELINE")

    def test_w8(self):
        union = {m: NAP for m in cp.METHODS}
        self.assertEqual(cls(D, union, "strict"), "EXCLUDED_NOT_APPLICABLE")

    def test_w9(self):
        union = {"BL-TIER": NA_, "BL-CX": P, "BL-ENG": NA_, "BL-OT": NA_, "BL-ISMS": NA_, "BL-TDD": NA_}
        self.assertEqual((cls(P, union, "strict"), cls(P, union, "inclusive")), ("d", "a"))

    def test_union_credit_needs_every_applicable_method_determinate(self):
        # AIDCF-only against the union only when every applicable method is a determinate miss
        self.assertEqual(cls(D, {"BL-ENG": NA_, "BL-CX": OOS, "BL-OT": NAP}, "strict"), "b")
        self.assertEqual(cls(D, {"BL-ENG": NA_, "BL-CX": II, "BL-OT": NAP}, "strict"), "EXCLUDED_INDETERMINATE_BASELINE")
        self.assertEqual(cls(D, {"BL-ENG": II, "BL-CX": D, "BL-OT": NAP}, "strict"), "a")

    def test_invalid_values_rejected(self):
        with self.assertRaises(ValueError):
            cp.side_value("OUT_OF_SCOPE", "strict", "AIDCF")
        with self.assertRaises(ValueError):
            cp.side_value("MAYBE", "strict", "BASELINE")


class IncidentLevel(unittest.TestCase):
    """T-07 to T-09 (section 10A.5.4)."""

    def data(self, aidcf, base):
        keys = [("INC-X", "CF-%02d" % (i + 1)) for i in range(len(aidcf))]
        factors = {k: {"factor_origin": "AIDCF", "knowability": "DISCOVERABLE", "coding_phase": "PRE_REVEAL",
                       "eod_sampled": "N"} for k in keys}
        return keys, {"active": ["BL-OT"], "best": dict(zip(keys, aidcf)), "factors": factors,
                      "base": {k: {"BL-OT": b} for k, b in zip(keys, base)}, "disp": {}}

    def test_w10_over_half_indeterminate_excludes_incident(self):
        keys, data = self.data([D, D, ND, D], [II, II, II, NA_])
        counts, excluded = cp.incident_level(data, keys, "BL-OT", "strict", 0.5)
        self.assertEqual(sum(counts.values()), 0)
        self.assertEqual(dict(excluded), {"over 50% indeterminate": 1})
        counts, excluded = cp.incident_level(data, keys, "BL-OT", "strict", 1.0)
        self.assertEqual(dict(counts), {"b": 1})

    def test_common_set_ignores_factors_indeterminate_on_either_side(self):
        # factor 1 is surfaced only by the baseline but AIDCF is indeterminate: it must not give the baseline the incident
        keys, data = self.data([II, D], [D, NA_])
        counts, _ = cp.incident_level(data, keys, "BL-OT", "strict", 0.5)
        self.assertEqual(dict(counts), {"b": 1})

    def test_not_applicable_is_not_indeterminate(self):
        keys, data = self.data([D, D, D], [NAP, NAP, NA_])
        counts, excluded = cp.incident_level(data, keys, "BL-OT", "strict", 0.25)
        self.assertEqual((dict(counts), dict(excluded)), ({"b": 1}, {}))

    def test_no_eligible_pair(self):
        keys, data = self.data([D], [NAP])
        counts, excluded = cp.incident_level(data, keys, "BL-OT", "strict", 0.5)
        self.assertEqual(dict(excluded), {"no eligible pair": 1})

    def test_no_interval_below_ten_incidents_and_no_metric_when_empty(self):
        keys, data = self.data([D, ND], [NA_, D])
        ci, n = cp.bootstrap(data, keys, "BL-OT", "strict", 1)
        self.assertIsNone(ci)
        self.assertEqual(cp.net({}), (None, 0))

    def test_net_incremental(self):
        self.assertEqual(cp.net({"a": 1, "b": 3, "c": 1, "d": 5}), (0.2, 10))
        self.assertEqual(cp.net({"b": 0, "c": 2, "a": 0, "d": 2}), (-0.5, 4))


class RoundAgreement(unittest.TestCase):
    """Baseline rounds A and B are reconciled as in v1.0 section 13, with kappa reported."""

    def test_hand_computed_kappa(self):
        def row(k, rnd, j):
            return {"record_type": "BASELINE", "baseline_id": "BL-ENG", "coding_round": rnd, "incident_id": "INC-X",
                    "factor_id": k, "detection_judgement": j}
        keys = [("INC-X", "CF-%02d" % i) for i in range(1, 5)]
        a = [D, D, ND, ND]
        b = [D, ND, ND, ND]
        rows = [row(k[1], "A", x) for k, x in zip(keys, a)] + [row(k[1], "B", x) for k, x in zip(keys, b)]
        po, kappa, n = cp.round_agreement(rows, keys, "BL-ENG")
        # po = 3/4; pe = (2*1 + 2*3)/16 = 0.5; kappa = (0.75 - 0.5) / 0.5 = 0.5
        self.assertEqual((po, kappa, n), (0.75, 0.5, 4))

    def test_reported(self):
        _, out = run("--comparative")
        self.assertIn("comparable factors coded by both: 10; percentage agreement 0.800; Cohen's kappa 0.750", out)


class Labels(unittest.TestCase):
    """BL-ANY-3 and the six-method BL-ANY cannot be confused."""

    def test_labels(self):
        self.assertEqual(cp.union_label(["BL-CX", "BL-ENG", "BL-OT"]), "BL-ANY-3")
        self.assertEqual(cp.union_label(cp.METHODS), "BL-ANY")
        self.assertIn("has not been evaluated", cp.union_note(["BL-CX", "BL-ENG", "BL-OT"]))

    def test_report_never_labels_three_methods_as_bl_any(self):
        code, out = run("--comparative")
        self.assertEqual(code, 0, out)
        import re
        for line in out.splitlines():
            if re.search(r"BL-ANY(?!-)", line):
                self.assertIn("six-method BL-ANY has not been evaluated", line)
        self.assertIn("BL-ANY-3  strict", out)


class Report(unittest.TestCase):
    """End-to-end results on the fictional fixtures."""

    def test_matches_expected_output(self):
        code, out = run("--comparative")
        self.assertEqual(code, 0, out)
        self.assertEqual(out, (FIX / "expected-comparative.txt").read_text(encoding="utf-8"))

    def test_deterministic(self):
        self.assertEqual(run("--comparative"), run("--comparative"))

    def test_hand_computed_bl_ot_strict(self):
        # From make_fixtures.FACTORS by hand: a 1 (8/1), b 1 (7/4), c 2 (5/2, 8/2), d 1 (2/1),
        # 3 indeterminate on the baseline side (7/1-3), 13 not applicable.
        _, out = run("--comparative")
        line = next(l for l in out.splitlines() if l.startswith("BL-OT     strict"))
        self.assertIn("a shared 1 | b AIDCF-only 1 | c baseline-only 2 | d neither 1 | N 5", line)
        self.assertIn("'EXCLUDED_INDETERMINATE_BASELINE': 3, 'EXCLUDED_NOT_APPLICABLE': 13", line)
        self.assertIn("net incremental -0.200", line)

    def test_negative_and_indeterminate_results_are_reported(self):
        _, out = run("--comparative")
        self.assertIn("net incremental -0.", out)
        self.assertIn("EXCLUDED_INDETERMINATE_AIDCF", out)
        self.assertIn("FLAG: differs by more than 10 points", out)
        self.assertIn("over 50% indeterminate", out)
        section = out.split("== Baseline-only results")[1].split("Gap dispositions")[0]
        self.assertEqual(section.count("disposition "), 5)
        self.assertIn("exploratory", out)
        self.assertIn("not observed performance", out)

    def test_dispositions_never_change_the_tables(self):
        """T-10/T-11 invariance: every disposition value gives the same paired tables."""
        _, base = run("--comparative")
        with Mutated() as m:
            cols, rows = m.rows("comparative-sheet.csv")
            for r in rows:
                if r["record_type"] == "GAP_DISPOSITION":
                    r.update(gap_disposition="DISPUTED", disposition_citation="", notes="FICTIONAL both positions")
            m.write("comparative-sheet.csv", cols, rows)
            m.relock()
            code, out = run("--comparative", files=m.dir)
        self.assertEqual(code, 0, out)
        self.assertEqual(base.split("== Baseline-only")[0], out.split("== Baseline-only")[0])


class Validation(unittest.TestCase):
    """T-01 to T-06, T-10, T-11 and the frozen-specification and independence rules."""

    def check(self, mutate, expected, mode="--check", relock=True):
        with Mutated() as m:
            mutate(m)
            if relock:
                m.relock()
            code, out = run(mode, files=m.dir)
        self.assertEqual(code, 1, out)
        self.assertIn(expected, out)

    def test_fixtures_are_valid(self):
        code, out = run("--check")
        self.assertEqual(code, 0, out)

    def test_t01_vocabulary(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-01", "BL-CX"), detection_judgement="MAYBE"),
                   "detection_judgement must be one of")

    def test_t02_out_of_scope_needs_declared_exclusion(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", is_base(2, "CF-02", "BL-ENG"), exclusion_id="EXC-09"),
                   "OUT_OF_SCOPE must cite an EXC-NN declared")

    def test_t03_not_applicable_needs_declared_rule(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-01", "BL-OT"), applicability_rule=""),
                   "NOT_APPLICABLE must cite an APP-NN declared")

    def test_t04_determinate_needs_citation(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-02", "BL-CX"), baseline_criteria=""),
                   "DETECTED requires baseline_criteria")

    def test_t05_eod_only_on_sampled_factors(self):
        def mut(m):
            cols, rows = m.rows("comparative-sheet.csv")
            unsampled = {(r["incident_id"], r["factor_id"]) for r in rows if r["record_type"] == "FACTOR" and r["eod_sampled"] == "N"}
            for r in rows:
                if r["record_type"] == "BASELINE" and (r["incident_id"], r["factor_id"]) in unsampled:
                    r.update(eod="LIKELY", eod_assumptions="x", eod_confidence="LOW")
                    break
            m.write("comparative-sheet.csv", cols, rows)
        self.check(mut, "EOD is coded only for factors in the EOD sample")

    def test_t05_sample_must_equal_seeded_draw(self):
        def mut(m):
            cols, rows = m.rows("comparative-sheet.csv")
            for r in rows:
                if r["record_type"] == "FACTOR" and r["eod_sampled"] == "N" and r["knowability"] in cp.KNOWABLE \
                        and r["coding_phase"] == "PRE_REVEAL":
                    r["eod_sampled"] = "Y"
                    break
            m.write("comparative-sheet.csv", cols, rows)
        self.check(mut, "does not match the seeded draw")

    def test_t06_eod_needs_assumptions_and_confidence(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", lambda r: r["record_type"] == "AIDCF_EOD", eod_confidence=""),
                   "requires eod_assumptions and eod_confidence")

    def test_not_evaluated_method_cannot_be_judged(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-01", "BL-OT"), baseline_id="BL-TIER"),
                   "NOT_EVALUATED in this run")

    def test_t10_missing_disposition_blocks_results(self):
        self.check(lambda m: m.drop("comparative-sheet.csv", lambda r: r["record_type"] == "GAP_DISPOSITION" and
                                    r["incident_id"] == "INC-EXAMPLE-05"),
                   "without a GAP_DISPOSITION row", mode="--comparative")

    def test_t10_disposition_only_on_baseline_only_pairs(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", lambda r: r["record_type"] == "GAP_DISPOSITION",
                                    factor_id="CF-01", incident_id="INC-EXAMPLE-01", baseline_id="BL-ENG"),
                   "is not on a baseline-only pair", mode="--comparative")

    def test_t11_actionable_gap_cites_gap_record(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", lambda r: r["gap_disposition"] == "ACTIONABLE_GAP",
                                    disposition_citation="see report"),
                   "ACTIONABLE_GAP cites the G1, G2 or G3 gap record")

    def test_frozen_specification(self):
        self.check(lambda m: m.edit("baselines.csv", lambda r: r["baseline_id"] == "BL-OT", scope="widened after results"),
                   "differs from its BASELINES lock")

    def test_unapproved_specification_blocks_results(self):
        def mut(m):
            m.edit("baselines.csv", lambda r: r["baseline_id"] == "BL-CX", approval_status="DRAFT", approved_on="", reviewer_id="")
            cols, rows = m.rows("comparative-locks.csv")
            import hashlib
            for r in rows:
                if r["artefact"] == "BASELINES":
                    r["value"] = hashlib.sha256((m.dir / "baselines.csv").read_bytes()).hexdigest()
            m.write("comparative-locks.csv", cols, rows)
        self.check(mut, "BL-CX is not APPROVED", mode="--comparative")

    def test_baseline_coder_independent_of_author(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-01", "BL-CX"), independent_of_author="N"),
                   "independent of the framework author")

    def test_factor_list_matches_coding_sheet(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", lambda r: r["record_type"] == "FACTOR", knowability="STATED_KNOWN"),
                   "must match the consolidated factor")
        self.check(lambda m: m.drop("comparative-sheet.csv", lambda r: r["record_type"] == "FACTOR" and
                                    r["incident_id"] == "INC-EXAMPLE-11"),
                   "missing from the FACTOR list")

    def test_missing_baseline_judgement_blocks_results(self):
        self.check(lambda m: m.drop("comparative-sheet.csv", is_base(3, "CF-01", "BL-ENG")),
                   "has no RECONCILED BL-ENG judgement", mode="--comparative")

    def test_dictionary_matches_columns(self):
        with open(KIT / "comparative-sheet-dictionary.csv", encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
        by_file = lambda f: [r["column"] for r in rows if r["file"] == f]
        self.assertEqual(by_file("comparative-sheet.csv"), cp.SHEET_COLUMNS)
        self.assertEqual(by_file("baselines.csv"), cp.BASELINE_COLUMNS)
        self.assertEqual(by_file("run-log/comparative-locks.csv"), cp.LOCK_COLUMNS)

    def test_t05_eod_required_for_both_sides_on_sampled_factors(self):
        self.check(lambda m: m.drop("comparative-sheet.csv", lambda r: r["record_type"] == "AIDCF_EOD"),
                   "has no RECONCILED AIDCF_EOD estimate", mode="--comparative")

        def blank(m):
            cols, rows = m.rows("comparative-sheet.csv")
            sampled = {(r["incident_id"], r["factor_id"]) for r in rows if r["record_type"] == "FACTOR" and r["eod_sampled"] == "Y"}
            for r in rows:
                if r["record_type"] == "BASELINE" and r["coding_round"] == "RECONCILED" and r["baseline_id"] == "BL-CX" \
                        and (r["incident_id"], r["factor_id"]) in sampled and r["detection_judgement"] != "NOT_APPLICABLE":
                    r.update(eod="", eod_assumptions="", eod_confidence="")
                    break
            m.write("comparative-sheet.csv", cols, rows)
        self.check(blank, "has no RECONCILED BL-CX EOD estimate", mode="--comparative")

    def test_eod_indeterminate_states_why(self):
        self.check(lambda m: m.edit("comparative-sheet.csv", lambda r: r["eod"] == "INDETERMINATE", eod_assumptions=""),
                   "INDETERMINATE states in eod_assumptions why")

    def test_locks_are_set_once(self):
        def mut(m):
            cols, rows = m.rows("comparative-locks.csv")
            rows.append(dict(rows[-1]))
            m.write("comparative-locks.csv", cols, rows)
        self.check(mut, "is locked once")


class LockIntegrity(unittest.TestCase):
    """KAI pre-merge review: the final report fails closed on missing, changed or unreadable locks."""

    def fails(self, mutate, expected, mode="--comparative"):
        with Mutated() as m:
            mutate(m)
            code, out = run(mode, files=m.dir)
        self.assertEqual(code, 1, out)
        self.assertIn(expected, out)
        self.assertNotIn("== Factor level", out)  # no results of any kind

    def drop_lock(self, pred):
        return lambda m: m.drop("comparative-locks.csv", pred)

    def test_complete_locks_report(self):
        code, out = run("--comparative")
        self.assertEqual(code, 0, out)

    def test_each_required_lock_missing(self):
        cases = {
            "BOOTSTRAP_SEED": "BOOTSTRAP_SEED is not locked",
            "BASELINES": "BASELINES is not locked",
            "EOD_FRAME": "EOD_SEED and EOD_FRAME are not both locked",
            "EOD_SEED": "EOD_SEED and EOD_FRAME are not both locked",
            "FILE:coding-sheet.csv": "coding-sheet.csv is not locked",
            "FILE:comparative-sheet.csv": "comparative-sheet.csv is not locked",
        }
        for artefact, expected in cases.items():
            with self.subTest(artefact=artefact):
                if artefact.startswith("FILE:"):
                    pred = lambda r, n=artefact[5:]: r["artefact"].startswith("FILE:") and r["artefact"].endswith("/" + n)
                else:
                    pred = lambda r, a=artefact: r["artefact"] == a
                self.fails(self.drop_lock(pred), expected)

    def test_report_function_requires_bootstrap_seed(self):
        with Mutated() as m:
            m.drop("comparative-locks.csv", lambda r: r["artefact"] == "BOOTSTRAP_SEED")
            chk = bc.Checker()
            _, coding = m.rows("coding-sheet.csv")
            rows, spec, locks = cp.check_comparative(m.dir / "comparative-sheet.csv", m.dir / "baselines.csv",
                                                     m.dir / "comparative-locks.csv", coding, lambda i: "X", chk)
        with self.assertRaisesRegex(ValueError, "BOOTSTRAP_SEED is not locked"):
            cp.comparative_report(rows, spec, locks, coding, lambda i: "X")

    def test_changed_locked_judgement(self):
        # a reconciled baseline judgement edited after the comparative sheet was locked
        self.fails(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-01", "BL-CX"),
                                    detection_judgement="NOT_DETECTED", baseline_criteria="FICTIONAL clause 4.2"),
                   "the file has changed since it was locked")
        # an AIDCF judgement edited after the coding sheet was locked
        self.fails(lambda m: m.edit("coding-sheet.csv", lambda r: r["detection_judgement"] == "DETECTED",
                                    detection_judgement="PARTIALLY_DETECTED"),
                   "the file has changed since it was locked")
        # a coder's locked round-A snapshot edited
        self.fails(lambda m: m.edit("locked/C21-BL-ENG-round-A.csv", lambda r: True, detection_judgement="DETECTED"),
                   "the file has changed since it was locked")

    def test_replaced_or_missing_locked_file(self):
        def replace(m):
            (m.dir / "coding-sheet.csv").write_text((FIX / "comparative-sheet.csv").read_text(encoding="utf-8"), encoding="utf-8")
        with Mutated() as m:
            replace(m)
            code, out = run("--comparative", files=m.dir)
        self.assertEqual(code, 1)  # rejected at the header check or the lock, never reported
        self.assertNotIn("== Factor level", out)
        self.fails(lambda m: (m.dir / "locked/C21-BL-ENG-round-A.csv").unlink(), "the locked file cannot be read")

    def test_changed_lock_fails_check_too(self):
        self.fails(lambda m: m.edit("comparative-sheet.csv", is_base(1, "CF-01", "BL-CX"), notes="FICTIONAL edited"),
                   "the file has changed since it was locked", mode="--check")

    def test_file_locked_twice(self):
        def dup(m):
            cols, rows = m.rows("comparative-locks.csv")
            rows.append(dict(next(r for r in rows if r["artefact"].endswith("coding-sheet.csv"))))
            m.write("comparative-locks.csv", cols, rows)
        self.fails(dup, "is locked once")

    def test_empty_eod_sample_cannot_bypass_frozen_frame(self):
        def clear(m):
            cols, rows = m.rows("comparative-sheet.csv")
            for r in rows:
                if r["record_type"] == "FACTOR":
                    r["eod_sampled"] = "N"
            m.write("comparative-sheet.csv", cols, [r for r in rows if r["record_type"] != "AIDCF_EOD"])
            cols, rows = m.rows("comparative-sheet.csv")
            for r in rows:
                r.update(eod="", eod_assumptions="", eod_confidence="")
            m.write("comparative-sheet.csv", cols, rows)
            m.relock()  # even with fresh file locks
        self.fails(clear, "eod_sampled does not match the seeded draw from the locked frame")

        def clear_and_unlock(m):
            clear(m)
            m.drop("comparative-locks.csv", lambda r: r["artefact"] == "EOD_FRAME")
        self.fails(clear_and_unlock, "EOD_SEED and EOD_FRAME are not both locked")

    def test_changed_factor_frame(self):
        with Mutated() as m:
            cols, rows = m.rows("comparative-sheet.csv")
            target = next(r for r in rows if r["record_type"] == "FACTOR" and r["knowability"] == "DISCOVERABLE"
                          and r["eod_sampled"] == "N" and r["coding_phase"] == "PRE_REVEAL")
            key = (target["incident_id"], target["factor_id"])
        def drop_factor(m):
            # remove one unsampled factor from the frame on both sheets, with fresh file locks
            m.drop("comparative-sheet.csv", lambda r: (r["incident_id"], r["factor_id"]) == key)
            m.drop("coding-sheet.csv", lambda r: (r["incident_id"], r["factor_id"]) == key)
            m.relock()
        self.fails(drop_factor, "the frozen EOD frame has changed")


class EodDraw(unittest.TestCase):
    """KAI clarification 2: the sample is drawn from the locked frame before any detection judgement."""

    def test_draw_refused_once_judgements_exist(self):
        code, out = run("--draw-eod-sample")
        self.assertEqual(code, 1)
        self.assertIn("must be drawn before them", out)

    def test_draw_reproduces_fixture_sample(self):
        with Mutated() as m:
            cols, rows = m.rows("comparative-sheet.csv")
            m.write("comparative-sheet.csv", cols, [dict(r, eod_sampled="N") for r in rows if r["record_type"] == "FACTOR"])
            ccols, _ = m.rows("coding-sheet.csv")
            m.write("coding-sheet.csv", ccols, [])
            # the state before the draw: no EOD_FRAME and no file locks yet
            lcols, locks = m.rows("comparative-locks.csv")
            m.write("comparative-locks.csv", lcols, [r for r in locks if r["artefact"] in {"BASELINES", "BOOTSTRAP_SEED", "EOD_SEED"}])
            code, out = run("--draw-eod-sample", files=m.dir)
        self.assertEqual(code, 0, out)
        drawn = {tuple(l.split()[1:3]) for l in out.splitlines() if l.startswith("SAMPLED")}
        _, rows = Mutated.rows(type("x", (), {"dir": FIX})(), "comparative-sheet.csv")
        expected = {(r["incident_id"], r["factor_id"]) for r in rows if r["record_type"] == "FACTOR" and r["eod_sampled"] == "Y"}
        self.assertEqual(drawn, expected)
        incidents = {r["incident_id"] for r in rows if r["record_type"] == "FACTOR" and r["knowability"] in cp.KNOWABLE
                     and r["coding_phase"] == "PRE_REVEAL"}
        self.assertEqual({i for i, _ in drawn}, incidents)  # at least one per incident


class V10Regression(unittest.TestCase):
    """v1.0 behaviour on the canonical files is unchanged."""

    def real(self, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = bc.main(list(args))
        return code, buf.getvalue()

    def test_check(self):
        code, out = self.real("--check")
        self.assertEqual(code, 0, out)
        self.assertEqual(out.splitlines()[0], (FIX / "v1.0-check.txt").read_text(encoding="utf-8").splitlines()[0])

    def test_metrics(self):
        code, out = self.real("--metrics", "--include-examples")
        self.assertEqual((code, out), (0, (FIX / "v1.0-metrics-include-examples.txt").read_text(encoding="utf-8")))

    def test_agreement(self):
        code, out = self.real("--agreement", "--include-examples")
        self.assertEqual((code, out), (0, (FIX / "v1.0-agreement-include-examples.txt").read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main(verbosity=1)
