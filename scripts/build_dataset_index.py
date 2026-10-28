#!/usr/bin/env python3
"""Build data/datasets.json, data/datasets.csv and data/portals.csv from the topic catalogs.

The topic files stay the source of truth. This script only flattens them into one
table with the same columns for every dataset, adds a normalized license
classification (curated below) and merges measured download probes.
Run it after changing any file in data/. Offline; standard library only.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

# Normalized license facts per license id. commercial_use: yes | conditional | no | unknown
LICENSES: dict[str, dict[str, Any]] = {
    "CC0-1.0": {"commercial_use": "yes", "attribution_required": False, "share_alike": False},
    "CC-BY-4.0": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "CC-BY": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "Etalab-2.0": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "DL-DE-BY-2.0": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "OGL-3.0": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "ODC-By-1.0": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "ODbL-1.0": {"commercial_use": "yes", "attribution_required": True, "share_alike": True},
    "CC-BY-SA-3.0-DE": {"commercial_use": "yes", "attribution_required": True, "share_alike": True},
    "AGPL-3.0-or-commercial": {"commercial_use": "conditional", "attribution_required": True, "share_alike": True},
    "per-item": {"commercial_use": "conditional", "attribution_required": None, "share_alike": None},
    "public-information": {"commercial_use": "yes", "attribution_required": True, "share_alike": False},
    "unknown": {"commercial_use": "unknown", "attribution_required": None, "share_alike": None},
}

# Curated classification of topic sources: (license_id, access).
# access: bulk_download | api | bulk_and_api | search_only | provider_feed | reference | software
SOURCES: dict[str, tuple[str, str]] = {
    "edu-mein-now": ("unknown", "search_only"),
    "edu-kursnet-openqcat": ("unknown", "provider_feed"),
    "edu-iwwb": ("unknown", "search_only"),
    "edu-berlin-vhs": ("CC-BY", "bulk_download"),
    "edu-europass-qdr": ("unknown", "bulk_and_api"),
    "edu-hamburg-wisy": ("CC-BY-SA-3.0-DE", "search_only"),
    "edu-wis-ihk": ("unknown", "search_only"),
    "edu-hoch-und-weit": ("unknown", "search_only"),
    "edu-esco": ("unknown", "bulk_and_api"),
    "edu-ba-azav": ("unknown", "reference"),
    "edu-dakks-azav": ("unknown", "reference"),
    "psy-metapsy-depression": ("ODC-By-1.0", "bulk_and_api"),
    "psy-metapsy-inpatients": ("ODC-By-1.0", "bulk_and_api"),
    "psy-metapsy-ptsd": ("ODC-By-1.0", "bulk_and_api"),
    "psy-openneuro-hypnosis": ("CC0-1.0", "bulk_download"),
    "psy-psycharchives": ("per-item", "api"),
    "psy-pmc-openaccess": ("per-item", "bulk_and_api"),
    "psy-aact": ("unknown", "bulk_download"),
    "psy-osm-practices": ("ODbL-1.0", "bulk_and_api"),
    "psy-annomi": ("unknown", "bulk_download"),
    "eso-osm": ("ODbL-1.0", "bulk_and_api"),
    "eso-erara": ("per-item", "api"),
    "eso-tarot-commons": ("per-item", "api"),
    "eso-wikidata": ("CC0-1.0", "bulk_and_api"),
    "eso-gutenberg": ("per-item", "bulk_download"),
    "eso-usno": ("public-information", "api"),
    "eso-swisseph": ("AGPL-3.0-or-commercial", "software"),
    "eso-correspondences": ("unknown", "search_only"),
}

TOPICS = [
    ("education", "data/education_sources.json", "docs/education/WEITERBILDUNG_DE_AZAV.md"),
    ("psychotherapy-hypnosis", "data/psychotherapy_sources.json", "docs/psychotherapy-hypnosis/VERIFIED_DATASETS.md"),
    ("esotericism-history", "data/esotericism_sources.json", "docs/esotericism/VERIFIED_SOURCES.md"),
]

COLUMNS = [
    "id", "name", "topic", "kind", "url", "download_url", "formats", "access",
    "license_id", "license_note", "license_evidence_url", "commercial_use", "attribution_required", "share_alike",
    "count_value", "count_relation", "count_unit", "count_scope", "count_basis",
    "measured_record_count", "measured_unique_ids", "measured_at",
    "documentation_checked_at", "doc", "notes",
]


def load(path: str) -> Any:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def license_fields(license_id: str) -> dict[str, Any]:
    if license_id not in LICENSES:
        raise SystemExit(f"Unknown license id {license_id!r}; add it to LICENSES")
    return {"license_id": license_id, **LICENSES[license_id]}


def project_rows(probes: dict[str, dict[str, Any]], probed_at: str | None) -> list[dict[str, Any]]:
    data = load("data/verified_directory_projects.json")
    rows = []
    for p in data["projects"]:
        count, probe = p["source_count"], probes.get(p["id"], {})
        rows.append({
            "id": p["id"], "name": p["name"], "topic": "directory-candidates", "kind": "directory_candidate",
            "url": p["source_url"], "download_url": probe.get("url") or p["access"].get("entry_url"),
            "formats": p["access"]["formats"],
            "access": "api" if p["id"] == "research-organisations-de" else "bulk_download",
            **license_fields(p["license"]["id"]), "license_note": None,
            "license_evidence_url": p["license"]["evidence_url"],
            "count_value": count["value"], "count_relation": count["relation"], "count_unit": p["entity_unit"],
            "count_scope": count["scope"], "count_basis": count["basis"],
            "measured_record_count": probe.get("record_count"), "measured_unique_ids": probe.get("unique_id_count"),
            "measured_at": probed_at if probe else None,
            "documentation_checked_at": data["reviewed_at"],
            "doc": "docs/strategy/DIRECTORY_PROJECT_PRIORITIES.md",
            "notes": " ".join(p["limitations"]),
        })
    return rows


def source_rows() -> list[dict[str, Any]]:
    rows = []
    for topic, path, doc in TOPICS:
        for s in load(path)["sources"]:
            if s["id"] not in SOURCES:
                raise SystemExit(f"{s['id']} missing from SOURCES classification")
            license_id, access = SOURCES[s["id"]]
            quantity = s.get("observed_quantity") or {}
            formats = s.get("formats") or (s["access"] if isinstance(s.get("access"), list) else [])
            notes = s.get("limitations") or s.get("caveats") or ""
            rows.append({
                "id": s["id"], "name": s["name"], "topic": topic, "kind": "source_profile",
                "url": s.get("url") or s["evidence_urls"][0], "download_url": None,
                "formats": formats, "access": access,
                **license_fields(license_id),
                "license_note": s.get("license_label") or s.get("license_summary"),
                "license_evidence_url": s.get("license_evidence_url"),
                "count_value": quantity.get("value"), "count_relation": "eq" if quantity.get("value") is not None else None,
                "count_unit": quantity.get("unit"), "count_scope": quantity.get("scope"),
                "count_basis": quantity.get("method") or quantity.get("basis"),
                "measured_record_count": None, "measured_unique_ids": None, "measured_at": s.get("payload_checked_at"),
                "documentation_checked_at": s["documentation_checked_at"], "doc": doc,
                "notes": " ".join(notes) if isinstance(notes, list) else notes,
            })
    return rows


def build() -> dict[str, Any]:
    probe_file = load("data/source_probes.json")
    probes = {r["project_id"]: r for r in probe_file["results"]}
    rows = project_rows(probes, probe_file["probed_at"]) + source_rows()
    return {
        "schema_version": "1.0.0",
        "generated_by": "scripts/build_dataset_index.py",
        "description": "All datasets described in this repository, one row each, with normalized license and access fields. Generated from the topic files; edit those, not this file.",
        "count": len(rows),
        "datasets": [{c: r.get(c) for c in COLUMNS} for r in rows],
    }


def to_csv(rows: list[dict[str, Any]], columns: list[str]) -> str:
    out = []
    for r in rows:
        out.append({c: "; ".join(r[c]) if isinstance(r.get(c), list) else ("" if r.get(c) is None else r[c]) for c in columns})
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(out)
    return buffer.getvalue()


def outputs() -> dict[Path, str]:
    index = build()
    portals = load("data/portals.json")["portals"]
    portal_columns = ["id", "name", "url", "category", "context"]
    return {
        ROOT / "data/datasets.json": json.dumps(index, ensure_ascii=False, indent=1) + "\n",
        ROOT / "data/datasets.csv": to_csv(index["datasets"], COLUMNS),
        ROOT / "data/portals.csv": to_csv(portals, portal_columns),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are out of date")
    args = parser.parse_args()
    stale = []
    for path, content in outputs().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            if args.check:
                stale.append(path.relative_to(ROOT))
            else:
                path.write_text(content, encoding="utf-8")
                print(f"wrote {path.relative_to(ROOT)}")
    if stale:
        print("Out of date, run scripts/build_dataset_index.py: " + ", ".join(map(str, stale)), file=sys.stderr)
        return 1
    if args.check:
        print("OK: generated dataset index is up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
