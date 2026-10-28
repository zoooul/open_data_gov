#!/usr/bin/env python3
"""Offline metadata validation. Does not test websites, legal clearance or SEO."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
BASES = {"api_country_facet", "publisher_dataset_count", "official_scope_statistic"}
UNITS = {"reported_bathing_water", "museum", "school", "food_business", "organisation", "protected_immovable_property"}
LICENSES = {"CC-BY-4.0", "Etalab-2.0", "DL-DE-BY-2.0", "OGL-3.0", "CC0-1.0"}


def https(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.hostname)


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or not isinstance(data.get("projects"), list):
        return ["Expected an object with a projects array"]
    try:
        date.fromisoformat(data.get("reviewed_at", ""))
    except (ValueError, TypeError):
        errors.append("reviewed_at must be an ISO calendar date")
    threshold = data.get("minimum_source_entities")
    if type(threshold) is not int or threshold < 1000:
        errors.append("minimum_source_entities must be an integer >= 1000")
        threshold = 1000
    projects = data["projects"]
    if data.get("count") != len(projects):
        errors.append("count differs from projects length")
    seen: set[str] = set()
    for index, item in enumerate(projects):
        if not isinstance(item, dict):
            errors.append(f"projects/{index}: expected object")
            continue
        key = item.get("id")
        prefix = str(key or index)
        if not isinstance(key, str) or not key or key in seen:
            errors.append(f"{prefix}: missing or duplicate ID")
        else:
            seen.add(key)
        if item.get("entity_unit") not in UNITS:
            errors.append(f"{prefix}: unsupported unit; clicks, people and connectors are not directory entities")
        count = item.get("source_count", {})
        if not isinstance(count, dict):
            errors.append(f"{prefix}: invalid source_count")
            count = {}
        value = count.get("value")
        if type(value) is not int or value < threshold:
            errors.append(f"{prefix}: stock below threshold or not a numeric sourced count")
        if count.get("relation") not in {"eq", "gt", "ge"}:
            errors.append(f"{prefix}: preserve exact count versus lower bound")
        if count.get("basis") not in BASES:
            errors.append(f"{prefix}: unaccepted count evidence basis")
        for field in ("scope", "reference_period"):
            if not isinstance(count.get(field), str) or not count[field].strip():
                errors.append(f"{prefix}: missing count {field}")
        license_info = item.get("license", {})
        if not isinstance(license_info, dict):
            license_info = {}
        if license_info.get("id") not in LICENSES:
            errors.append(f"{prefix}: no documented open data license")
        access = item.get("access", {})
        if not isinstance(access, dict):
            access = {}
        for label, value_url in (
            ("source", item.get("source_url")),
            ("count evidence", count.get("evidence_url")),
            ("license evidence", license_info.get("evidence_url")),
            ("access", access.get("entry_url")),
        ):
            if not https(value_url):
                errors.append(f"{prefix}: invalid {label} URL")
        fields = item.get("documented_content")
        if not isinstance(fields, list) or len(fields) < 4 or not all(isinstance(v, str) and v for v in fields):
            errors.append(f"{prefix}: insufficient documented content")
        if not item.get("limitations") or not item.get("deduplication"):
            errors.append(f"{prefix}: limitations and entity handling required")
        imported = item.get("full_import_tested")
        qualified = item.get("qualified_entry_count")
        ready = item.get("launch_ready")
        if type(imported) is not bool or type(ready) is not bool:
            errors.append(f"{prefix}: import and readiness flags must be booleans")
        if imported is False and qualified is not None:
            errors.append(f"{prefix}: no qualified count without a full import test")
        if qualified is not None and (type(qualified) is not int or qualified < 0):
            errors.append(f"{prefix}: invalid qualified count")
        if ready is True and (imported is not True or type(qualified) is not int or qualified < threshold):
            errors.append(f"{prefix}: launch approval requires counted qualified records")
        if item.get("source_stock_supported") is not True:
            errors.append(f"{prefix}: unsupported candidates belong outside this shortlist")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=ROOT / "data/verified_directory_projects.json")
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {data['count']} source-stock candidates; metadata only, no network or launch verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
