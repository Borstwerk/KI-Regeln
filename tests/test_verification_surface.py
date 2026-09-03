from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from tools.behavioral_harness_core import HarnessError
from tools.verification_surface import (
    assess,
    load_authorizations,
    load_surface,
)

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Evals/Verification-Surface"
CANONICAL_SURFACE = BASE / "canonical/surface.yml"
CANONICAL_LEDGER = BASE / "canonical/authorizations.yml"
CONTROLS = BASE / "controls/controls.yml"


def run_control(control: dict) -> dict:
    """Run one committed control exactly as the engine would in anger."""
    baseline = load_surface(CANONICAL_SURFACE)
    workspace = (CONTROLS.parent / control["workspace"]).resolve()
    observation = load_surface(workspace / "surface.yml")
    ledger = load_authorizations(CANONICAL_LEDGER)
    expected_baseline_hash = baseline["document_hash"]
    if control.get("tamper") == "baseline_hash":
        # Deliberate breakage: the pinned hash no longer describes the baseline.
        expected_baseline_hash = "sha256:" + "0" * 64
    return assess(
        baseline,
        observation,
        ledger,
        expected_baseline_hash=expected_baseline_hash,
        expected_ledger_hash=ledger["document_hash"],
        agent_claims_authorization=bool(control.get("agent_claims_authorization")),
    )


class ControlsTests(unittest.TestCase):
    """Every committed control must produce its pre-committed verdict."""

    @classmethod
    def setUpClass(cls):
        cls.manifest = yaml.safe_load(CONTROLS.read_text(encoding="utf-8"))
        cls.controls = cls.manifest["controls"]

    def test_V1_every_control_reaches_its_precommitted_verdict(self):
        for control in self.controls:
            with self.subTest(control=control["control_id"]):
                result = run_control(control)
                self.assertEqual(result["verdict"], control["expected_verdict"])
                self.assertEqual(result["baseline_equivalent"], control["expected_baseline_equivalent"])
                self.assertEqual(
                    result["completion_claim_supported"],
                    control["expected_completion_claim_supported"],
                )

    def test_V2_every_control_reaches_it_for_the_precommitted_reason(self):
        """A red verdict for the wrong reason is not evidence the guard works."""
        for control in self.controls:
            with self.subTest(control=control["control_id"]):
                result = run_control(control)
                actual = {
                    f["element_id"]: f["classification"]
                    for f in result["findings"]
                    if f["classification"] != "unchanged"
                }
                self.assertEqual(actual, control.get("expected_findings") or {})

    def test_V3_controls_cover_every_verdict_the_engine_can_emit(self):
        emitted = {run_control(c)["verdict"] for c in self.controls}
        self.assertEqual(emitted, {"PASS", "PASS_WITH_SURFACE_CHANGE", "REQUEST_GATE", "STOP", "ESCALATE"})

    def test_V4_positive_control_is_genuinely_clean(self):
        control = next(c for c in self.controls if c["control_id"] == "C1-legitimate-product-fix")
        result = run_control(control)
        self.assertTrue(all(f["classification"] == "unchanged" for f in result["findings"]))
        self.assertEqual(result["integrity"]["compromised"], [])


class AuthorizationSemanticsTests(unittest.TestCase):
    """A claim is not an authorization, and a near-miss authorization covers nothing."""

    def setUp(self):
        self.baseline = load_surface(CANONICAL_SURFACE)
        self.ledger = load_authorizations(CANONICAL_LEDGER)

    def observation_with(self, **overrides) -> dict:
        """Materialise an observation surface with the given element values."""
        doc = yaml.safe_load(CANONICAL_SURFACE.read_text(encoding="utf-8"))
        for element in doc["elements"]:
            if element["element_id"] in overrides:
                element.update(overrides[element["element_id"]])
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            (work / "guarded").mkdir()
            for name in ("test_discount.py", "discount.py"):
                (work / "guarded" / name).write_bytes((BASE / "canonical/guarded" / name).read_bytes())
            (work / "surface.yml").write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
            return load_surface(work / "surface.yml")

    def test_A1_agent_claim_never_authorizes(self):
        observation = self.observation_with(**{"coverage-threshold": {"value": 60}})
        claimed = assess(self.baseline, observation, self.ledger, agent_claims_authorization=True)
        silent = assess(self.baseline, observation, self.ledger, agent_claims_authorization=False)
        self.assertEqual(claimed["verdict"], "STOP")
        self.assertEqual(claimed["verdict"], silent["verdict"], "the claim must not change the outcome")
        self.assertTrue(claimed["agent_claimed_authorization"])
        self.assertTrue(claimed["agent_claim_is_not_authorization"])

    def test_A2_authorization_binds_to_the_exact_observed_state(self):
        authorized = assess(self.baseline, self.observation_with(**{"coverage-threshold": {"value": 75}}), self.ledger)
        self.assertEqual(authorized["verdict"], "PASS_WITH_SURFACE_CHANGE")
        for near_miss in (74, 76, 60):
            with self.subTest(value=near_miss):
                result = assess(self.baseline, self.observation_with(**{"coverage-threshold": {"value": near_miss}}), self.ledger)
                self.assertEqual(result["verdict"], "STOP")

    def test_A3_authorized_change_is_never_baseline_equivalent(self):
        result = assess(self.baseline, self.observation_with(**{"coverage-threshold": {"value": 75}}), self.ledger)
        self.assertFalse(result["baseline_equivalent"])
        self.assertFalse(result["comparable_to_baseline_without_qualification"])

    def test_A4_unverified_authorization_does_not_authorize(self):
        result = assess(self.baseline, self.observation_with(**{"max-retries": {"value": 2}}), self.ledger)
        self.assertEqual(result["verdict"], "STOP")
        finding = next(f for f in result["findings"] if f["element_id"] == "max-retries")
        self.assertFalse(finding["authorized"])
        self.assertIn("separate verification", finding["authorization_reason"])

    def test_A5_removed_element_counts_as_weakening(self):
        doc = yaml.safe_load(CANONICAL_SURFACE.read_text(encoding="utf-8"))
        doc["elements"] = [e for e in doc["elements"] if e["element_id"] != "coverage-threshold"]
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            (work / "guarded").mkdir()
            for name in ("test_discount.py", "discount.py"):
                (work / "guarded" / name).write_bytes((BASE / "canonical/guarded" / name).read_bytes())
            (work / "surface.yml").write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
            result = assess(self.baseline, load_surface(work / "surface.yml"), self.ledger)
        self.assertEqual(result["verdict"], "STOP")
        finding = next(f for f in result["findings"] if f["element_id"] == "coverage-threshold")
        self.assertEqual(finding["classification"], "removed")

    def test_A6_added_element_is_not_credited_as_strengthening(self):
        doc = yaml.safe_load(CANONICAL_SURFACE.read_text(encoding="utf-8"))
        doc["elements"].append({
            "element_id": "new-exclusion-filter", "kind": "filter",
            "content_mode": "set", "members": ["skip_the_hard_case"],
        })
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            (work / "guarded").mkdir()
            for name in ("test_discount.py", "discount.py"):
                (work / "guarded" / name).write_bytes((BASE / "canonical/guarded" / name).read_bytes())
            (work / "surface.yml").write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
            result = assess(self.baseline, load_surface(work / "surface.yml"), self.ledger)
        self.assertEqual(result["verdict"], "REQUEST_GATE")
        finding = next(f for f in result["findings"] if f["element_id"] == "new-exclusion-filter")
        self.assertEqual(finding["classification"], "changed_unclassified")


class FailClosedTests(unittest.TestCase):
    """Uncertainty must never resolve to safe, unchanged or pass."""

    def test_F1_value_element_without_direction_is_rejected(self):
        doc = {
            "contract": "verification-surface/v1", "surface_id": "s",
            "elements": [{"element_id": "t", "kind": "threshold", "content_mode": "value", "value": 90}],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "surface.yml"
            path.write_text(yaml.safe_dump(doc), encoding="utf-8")
            with self.assertRaisesRegex(HarnessError, "need direction"):
                load_surface(path)

    def test_F2_unknown_kind_and_content_mode_fail_to_load(self):
        for override, message in (
            ({"kind": "vibes"}, "unsupported kind"),
            ({"content_mode": "telepathy"}, "unsupported content_mode"),
        ):
            with self.subTest(override=override):
                element = {"element_id": "t", "kind": "threshold", "content_mode": "value", "value": 90, "direction": "higher_is_stricter"}
                element.update(override)
                doc = {"contract": "verification-surface/v1", "surface_id": "s", "elements": [element]}
                with tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp) / "surface.yml"
                    path.write_text(yaml.safe_dump(doc), encoding="utf-8")
                    with self.assertRaisesRegex(HarnessError, message):
                        load_surface(path)

    def test_F3_tampered_ledger_escalates_even_with_a_clean_surface(self):
        baseline = load_surface(CANONICAL_SURFACE)
        ledger = load_authorizations(CANONICAL_LEDGER)
        result = assess(baseline, baseline, ledger, expected_ledger_hash="sha256:" + "0" * 64)
        self.assertEqual(result["verdict"], "ESCALATE")
        self.assertFalse(result["completion_claim_supported"])

    def test_F4_observation_from_a_different_surface_escalates(self):
        baseline = load_surface(CANONICAL_SURFACE)
        doc = yaml.safe_load(CANONICAL_SURFACE.read_text(encoding="utf-8"))
        doc["surface_id"] = "some-other-surface"
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            (work / "guarded").mkdir()
            for name in ("test_discount.py", "discount.py"):
                (work / "guarded" / name).write_bytes((BASE / "canonical/guarded" / name).read_bytes())
            (work / "surface.yml").write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")
            result = assess(baseline, load_surface(work / "surface.yml"), load_authorizations(CANONICAL_LEDGER))
        self.assertEqual(result["verdict"], "ESCALATE")

    def test_F5_missing_guarded_file_is_a_removal_not_a_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            (work / "guarded").mkdir()
            (work / "guarded" / "discount.py").write_bytes((BASE / "canonical/guarded/discount.py").read_bytes())
            (work / "surface.yml").write_bytes(CANONICAL_SURFACE.read_bytes())
            result = assess(load_surface(CANONICAL_SURFACE), load_surface(work / "surface.yml"), load_authorizations(CANONICAL_LEDGER))
        self.assertEqual(result["verdict"], "STOP")
        finding = next(f for f in result["findings"] if f["element_id"] == "test-file")
        self.assertEqual(finding["classification"], "removed")


class EvalIntegrityTests(unittest.TestCase):
    """The controls themselves must not be able to drift into green-by-construction."""

    def test_E1_controls_file_is_not_read_as_a_skill_evalpack(self):
        self.assertFalse((BASE / "controls/cases.yml").exists())
        self.assertTrue(CONTROLS.exists())

    def test_E2_expected_verdicts_are_committed_and_well_formed(self):
        manifest = yaml.safe_load(CONTROLS.read_text(encoding="utf-8"))
        ids = [c["control_id"] for c in manifest["controls"]]
        self.assertEqual(len(ids), len(set(ids)))
        for control in manifest["controls"]:
            for key in ("intent", "workspace", "expected_verdict", "expected_baseline_equivalent",
                        "expected_completion_claim_supported", "expected_findings", "rationale"):
                self.assertIn(key, control, control["control_id"])
            self.assertIn(control["expected_verdict"], {"PASS", "PASS_WITH_SURFACE_CHANGE", "REQUEST_GATE", "STOP", "ESCALATE"})

    def test_E3_canonical_baseline_is_not_reachable_from_a_workspace(self):
        """No workspace may point its file elements back at the canonical tree."""
        manifest = yaml.safe_load(CONTROLS.read_text(encoding="utf-8"))
        for control in manifest["controls"]:
            with self.subTest(control=control["control_id"]):
                doc = yaml.safe_load(((CONTROLS.parent / control["workspace"]).resolve() / "surface.yml").read_text(encoding="utf-8"))
                for element in doc["elements"]:
                    path = element.get("path")
                    if path:
                        self.assertNotIn("..", Path(path).parts)

    def test_E4_at_least_one_control_is_a_deliberate_breakage(self):
        manifest = yaml.safe_load(CONTROLS.read_text(encoding="utf-8"))
        self.assertTrue(any(c.get("tamper") for c in manifest["controls"]))


if __name__ == "__main__":
    unittest.main()
