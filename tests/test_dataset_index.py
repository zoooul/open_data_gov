"""Offline tests: the generated dataset index matches its sources and schema."""
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.build_dataset_index import LICENSES, outputs


class DatasetIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "data/datasets.json").read_text(encoding="utf-8"))
        cls.probes = json.loads((ROOT / "data/source_probes.json").read_text(encoding="utf-8"))
        cls.projects = json.loads((ROOT / "data/verified_directory_projects.json").read_text(encoding="utf-8"))

    def test_generated_files_up_to_date(self):
        for path, content in outputs().items():
            self.assertEqual(path.read_text(encoding="utf-8"), content, f"{path.name} is stale")

    def test_schema(self):
        schema = json.loads((ROOT / "schemas/datasets.schema.json").read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(self.index))
        self.assertEqual(errors, [])

    def test_ids_unique_and_count(self):
        ids = [d["id"] for d in self.index["datasets"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(self.index["count"], len(ids))

    def test_license_ids_known(self):
        for d in self.index["datasets"]:
            self.assertIn(d["license_id"], LICENSES)

    def test_unknown_license_never_commercial(self):
        for d in self.index["datasets"]:
            if d["license_id"] == "unknown":
                self.assertEqual(d["commercial_use"], "unknown", d["id"])

    def test_every_candidate_probed_above_threshold(self):
        probed = {r["project_id"]: r for r in self.probes["results"]}
        for p in self.projects["projects"]:
            self.assertIn(p["id"], probed)
            self.assertEqual(probed[p["id"]]["http_status"], 200)
            self.assertGreaterEqual(probed[p["id"]]["record_count"], self.projects["minimum_source_entities"])

    def test_probe_does_not_grant_launch(self):
        for p in self.projects["projects"]:
            self.assertFalse(p["launch_ready"])


if __name__ == "__main__":
    unittest.main()
