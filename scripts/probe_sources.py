#!/usr/bin/env python3
"""Download the six candidate datasets and measure rows, IDs and field fill rates.

Needs network access and, for the bathing-water Excel file, openpyxl.
Downloads go to a cache directory outside the repository; only the measured
summary is written to data/source_probes.json. This is a probe, not an import:
it does not deduplicate entities or decide launch readiness.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "open_data_gov-probe/1.0 (+https://github.com/zoooul/open_data_gov)"

PROBES: list[dict[str, Any]] = [
    {
        "project_id": "bathing-waters-de",
        "url": "https://sdi.eea.europa.eu/datashare/s/sptXqwkQr5g7Bp5/download?path=/eea_t_bathing-water-status_p_1990-2025_v01_r00&files=bw_assessment_eea_datahub_1990_2025.xlsx",
        "format": "xlsx",
        "id_field": "bathingWaterIdentifier",
        "filter": {"countryCode": "DE", "season": "2025"},
    },
    {
        "project_id": "museums-fr",
        "url": "https://ministere-culture.s3.sbg.io.cloud.ovh.net/POP/museofile.csv",
        "format": "csv",
        "delimiter": "|",
        "id_field": "Identifiant",
    },
    {
        "project_id": "schools-nrw",
        "url": "https://www.schulministerium.nrw.de/BiPo/OpenData/Schuldaten/schuldaten.csv",
        "format": "csv",
        "delimiter": ";",
        "id_field": "Schulnummer",
    },
    {
        "project_id": "food-hygiene-westminster",
        "url": "https://ratings.food.gov.uk/api/open-data-files/FHRS533en-GB.xml",
        "format": "fhrs_xml",
        "id_field": "FHRSID",
    },
    {
        "project_id": "research-organisations-de",
        "url": "https://api.ror.org/v2/organizations?filter=country.country_code:DE",
        "format": "ror_count",
        "id_field": "id",
    },
    {
        "project_id": "historic-monuments-fr",
        "url": "https://ministere-culture.s3.sbg.io.cloud.ovh.net/POP/merimee.csv",
        "format": "csv",
        "delimiter": "|",
        "id_field": "Reference",
    },
]


def fetch(url: str, cache: Path) -> tuple[int, Path]:
    """Download url into cache and return HTTP status and file path."""
    cache.mkdir(parents=True, exist_ok=True)
    target = cache / (hashlib.sha1(url.encode()).hexdigest()[:16] + "." + url.rsplit(".", 1)[-1][:4].strip("?/"))
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=600) as response, target.open("wb") as out:
        while chunk := response.read(1 << 20):
            out.write(chunk)
        return response.status, target


def csv_rows(path: Path, delimiter: str) -> Iterable[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    if text.startswith("sep="):
        text = text.split("\n", 1)[1]
    csv.field_size_limit(sys.maxsize)
    yield from csv.DictReader(io.StringIO(text), delimiter=delimiter)


def xlsx_rows(path: Path) -> Iterable[dict[str, str]]:
    try:
        import openpyxl
    except ImportError:
        raise SystemExit("Install openpyxl for the bathing-water probe: python -m pip install openpyxl")
    sheet = openpyxl.load_workbook(path, read_only=True).worksheets[0]
    rows = sheet.iter_rows(values_only=True)
    header = [str(h) for h in next(rows)]
    for row in rows:
        yield {k: "" if v is None else str(v) for k, v in zip(header, row)}


def fhrs_rows(path: Path) -> Iterable[dict[str, str]]:
    for detail in ET.parse(path).getroot().iter("EstablishmentDetail"):
        row: dict[str, str] = {}
        for child in detail:
            if len(child):
                for sub in child:
                    row[f"{child.tag}.{sub.tag}"] = (sub.text or "").strip()
            elif child.tag not in ("Geocode", "Scores"):
                row[child.tag] = (child.text or "").strip()
        yield row


def summarize(rows: Iterable[dict[str, str]], id_field: str, row_filter: dict[str, str]) -> dict[str, Any]:
    columns: dict[str, int] = {}
    ids: set[str] = set()
    count = 0
    for row in rows:
        if any(str(row.get(k, "")).split(".")[0] != v for k, v in row_filter.items()):
            continue
        count += 1
        ids.add(row.get(id_field, ""))
        for key, value in row.items():
            if not key:
                continue
            columns.setdefault(key, 0)
            if str(value).strip():
                columns[key] += 1
    return {
        "record_count": count,
        "unique_id_count": len(ids - {""}),
        "columns": [{"name": k, "filled_share": round(v / count, 3) if count else 0} for k, v in columns.items()],
    }


def probe(spec: dict[str, Any], cache: Path) -> dict[str, Any]:
    status, path = fetch(spec["url"], cache)
    result: dict[str, Any] = {
        "project_id": spec["project_id"],
        "url": spec["url"],
        "http_status": status,
        "bytes": path.stat().st_size,
        "format": spec["format"].split("_")[-1] if spec["format"] != "ror_count" else "json",
        "id_field": spec["id_field"],
        "filter": spec.get("filter", {}),
    }
    if spec["format"] == "ror_count":
        payload = json.loads(path.read_text(encoding="utf-8"))
        result.update(record_count=payload["number_of_results"], unique_id_count=None, columns=[],
                      note="API result count only; use the CC0 data dump for a full snapshot.")
        return result
    rows = {
        "csv": lambda: csv_rows(path, spec["delimiter"]),
        "xlsx": lambda: xlsx_rows(path),
        "fhrs_xml": lambda: fhrs_rows(path),
    }[spec["format"]]()
    result.update(summarize(rows, spec["id_field"], spec.get("filter", {})))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path.home() / ".cache/open_data_gov")
    parser.add_argument("--out", type=Path, default=ROOT / "data/source_probes.json")
    parser.add_argument("--only", nargs="*", help="Project IDs to probe")
    args = parser.parse_args()
    results = []
    for spec in PROBES:
        if args.only and spec["project_id"] not in args.only:
            continue
        print(f"probing {spec['project_id']} ...", file=sys.stderr)
        results.append(probe(spec, args.cache))
    out = {
        "schema_version": "1.0.0",
        "probed_at": dt.date.today().isoformat(),
        "description": "Measured download probes of the six candidate datasets. Raw record counts and field fill rates, before deduplication or quality review. Not an import and not launch approval.",
        "results": results,
    }
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
