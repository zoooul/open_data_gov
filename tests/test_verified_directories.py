"""Offline regression tests: evidence metadata is not imported directory stock."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.validate_verified_directories import validate


class VerifiedDirectoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "data/verified_directory_projects.json").read_text(encoding="utf-8"))

    def setUp(self):
        self.data = copy.deepcopy(self.base)
        self.item = self.data["projects"][0]

    def invalid(self):
        self.assertTrue(validate(self.data))

    def test_actual_catalog(self):
        self.assertEqual(validate(self.data), [])

    def test_small_stock(self):
        self.item["source_count"]["value"] = 12
        self.invalid()

    def test_incompatible_unit(self):
        self.item["entity_unit"] = "downloads"
        self.invalid()

    def test_missing_license(self):
        self.item["license"]["id"] = "free_to_view"
        self.invalid()

    def test_missing_license_evidence(self):
        self.item["license"]["evidence_url"] = None
        self.invalid()

    def test_duplicate_ids(self):
        self.data["projects"][1]["id"] = self.item["id"]
        self.invalid()

    def test_missing_reference_period(self):
        self.item["source_count"]["reference_period"] = ""
        self.invalid()

    def test_false_launch_claim(self):
        self.item["launch_ready"] = True
        self.invalid()

    def test_false_imported_count(self):
        self.item["qualified_entry_count"] = 2291
        self.invalid()

    def test_estimate_is_not_evidence(self):
        self.item["source_count"]["basis"] = "assumed_from_market_size"
        self.invalid()

    def test_address_only(self):
        self.item["documented_content"] = ["name", "address"]
        self.invalid()

    def test_bad_count(self):
        self.data["count"] += 1
        self.invalid()

    def test_bad_date(self):
        self.data["reviewed_at"] = "2026-02-30"
        self.invalid()

    def test_file_url(self):
        self.item["source_url"] = "file:///etc/passwd"
        self.invalid()


if __name__ == "__main__":
    unittest.main()
