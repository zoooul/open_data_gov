"""Offline contract tests for source metadata, not for external services."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.validate_education import validate_catalog


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "data/education_sources.json").read_text(encoding="utf-8"))
        cls.schema = json.loads((ROOT / "schemas/education_sources.schema.json").read_text(encoding="utf-8"))

    def setUp(self):
        self.data = copy.deepcopy(self.catalog)

    def assert_invalid(self):
        self.assertTrue(validate_catalog(self.data, self.schema))

    def test_actual_catalog(self):
        self.assertEqual(validate_catalog(self.data, self.schema), [])

    def test_count_mismatch(self):
        self.data["count"] += 1
        self.assert_invalid()

    def test_duplicate_id(self):
        self.data["sources"][1]["id"] = self.data["sources"][0]["id"]
        self.assert_invalid()

    def test_invalid_calendar_date(self):
        self.data["compiled_at"] = "2026-02-30"
        self.assert_invalid()

    def test_open_license_requires_evidence(self):
        self.data["sources"][0]["reuse_status"] = "open_license_indicated"
        self.assert_invalid()

    def test_unexpected_access_mode(self):
        self.data["sources"][0]["access_mode"] = "unlimited_free_api"
        self.assert_invalid()

    def test_non_https_source(self):
        self.data["sources"][0]["url"] = "file:///etc/passwd"
        self.assert_invalid()

    def test_future_payload_check(self):
        self.data["sources"][0]["payload_checked_at"] = "2099-01-01"
        self.assert_invalid()

    def test_missing_required_field(self):
        del self.data["sources"][0]["azav_role"]
        self.assert_invalid()


if __name__ == "__main__":
    unittest.main()
