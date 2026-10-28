#!/usr/bin/env python3
"""Validate source metadata locally. Does not check URLs, licenses or AZAV."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError:
    raise SystemExit("Install dependencies: python -m pip install -r requirements-validation.txt")

ROOT = Path(__file__).resolve().parents[1]


def validate_catalog(data: Any, schema: dict[str, Any]) -> list[str]:
    """Return schema errors and cross-record consistency errors."""
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda e: str(list(e.absolute_path)))
    ]
    if errors:
        return errors
    sources = data["sources"]
    if data["count"] != len(sources):
        errors.append("count must equal the number of source profiles")
    ids = [item["id"] for item in sources]
    if len(ids) != len(set(ids)):
        errors.append("source IDs must be unique")
    for item in sources:
        for field in ("documentation_checked_at", "payload_checked_at"):
            value = item[field]
            if value is not None and value > data["compiled_at"]:
                errors.append(f"{item['id']}/{field}: later than compiled_at")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "data/education_sources.json")
    parser.add_argument("--schema", type=Path, default=ROOT / "schemas/education_sources.schema.json")
    args = parser.parse_args()
    try:
        data = json.loads(args.catalog.read_text(encoding="utf-8"))
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
        errors = validate_catalog(data, schema)
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError) as exc:
        print(f"Cannot validate input: {exc}", file=sys.stderr)
        return 2
    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1
    print(f"OK: {data['count']} sources; schema, IDs, count and dates checked. No network tests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
