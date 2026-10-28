# Für Entwickler: Daten laden und ein Verzeichnis bauen

[README](../README.md) · [Prüfmethode](METHODIK.md) · [Zusammenhänge](ZUSAMMENHAENGE.md)

Diese Seite ist für alle, die aus den beschriebenen Quellen ein MVP, ein Verzeichnis oder eine Datenpipeline bauen wollen. Sie zeigt, welche Datei man zuerst liest, wie die sechs geprüften Rohdaten technisch aussehen und welche Stolperfallen beim Import gemessen wurden.

## 1. Der schnellste Einstieg: eine Tabelle für alles

[`data/datasets.csv`](../data/datasets.csv) und [`data/datasets.json`](../data/datasets.json) enthalten **alle 34 beschriebenen Datensätze in einem einheitlichen Format**: die sechs Verzeichniskandidaten und 28 Quellenprofile aus den Fachthemen. Die CSV-Datei öffnet sich direkt in Excel, Google Sheets oder Airtable.

| Spalte | Bedeutung |
|---|---|
| `access` | `bulk_download`, `api`, `bulk_and_api`, `search_only`, `provider_feed`, `reference`, `software` |
| `license_id` | normalisierte Lizenzkennung (`CC0-1.0`, `CC-BY-4.0`, `Etalab-2.0`, `DL-DE-BY-2.0`, `OGL-3.0`, `ODbL-1.0`, …, `unknown`) |
| `commercial_use` | `yes`, `conditional` (je Objekt oder mit Auflagen), `unknown` |
| `attribution_required`, `share_alike` | Pflichten aus der Lizenz |
| `download_url` | direkter, getesteter Downloadlink (bisher für die sechs Kandidaten) |
| `count_*` | Menge laut Quelle, mit Einheit, Bezugsraum und Zählbasis |
| `measured_record_count`, `measured_unique_ids`, `measured_at` | selbst gemessene Zeilen und eindeutige IDs nach Download |
| `doc` | Fachanalyse mit Belegen und Grenzen |

Typische Filter:

```python
import json

datasets = json.load(open("data/datasets.json", encoding="utf-8"))["datasets"]
usable = [
    d for d in datasets
    if d["commercial_use"] == "yes"
    and d["access"] in ("bulk_download", "bulk_and_api", "api")
    and not d["share_alike"]
]
for d in usable:
    print(d["id"], d["license_id"], d["download_url"] or d["url"])
```

```js
const { datasets } = await (await fetch(
  "https://raw.githubusercontent.com/zoooul/open_data_gov/main/data/datasets.json"
)).json();
const bulk = datasets.filter(d => d.download_url && d.commercial_use === "yes");
```

Die Datei wird aus den Themendateien erzeugt (`python scripts/build_dataset_index.py`). Änderungen bitte in den Themendateien vornehmen.

Daneben gibt es [`data/portals.csv`](../data/portals.csv) mit 100 Open-Data-Portalen (Name, URL, Kategorie, Region).

## 2. Die sechs Kandidaten: gemessene Rohdaten

Am 28.10.2026 wurden alle sechs Quellen tatsächlich heruntergeladen und ausgewertet ([`scripts/probe_sources.py`](../scripts/probe_sources.py), Ergebnis in [`data/source_probes.json`](../data/source_probes.json) inklusive Füllgrad jedes Feldes).

| Projekt | Datei | Größe | Gemessene Datensätze | ID-Feld | Lizenz |
|---|---|---:|---:|---|---|
| Badegewässer DE | [XLSX (EEA, 1990–2025, EU-weit)](https://sdi.eea.europa.eu/datashare/s/sptXqwkQr5g7Bp5/download?path=/eea_t_bathing-water-status_p_1990-2025_v01_r00&files=bw_assessment_eea_datahub_1990_2025.xlsx) | 43 MB | 2.291 (DE, Saison 2025) | `bathingWaterIdentifier` | CC BY 4.0 |
| Museen FR | [CSV](https://ministere-culture.s3.sbg.io.cloud.ovh.net/POP/museofile.csv) | 3,4 MB | 1.216 | `Identifiant` | Licence Ouverte 2.0 |
| Schulen NRW | [CSV](https://www.schulministerium.nrw.de/BiPo/OpenData/Schuldaten/schuldaten.csv) | 1,8 MB | 5.645 | `Schulnummer` | DL-DE BY 2.0 |
| Lebensmittelbetriebe Westminster | [XML](https://ratings.food.gov.uk/api/open-data-files/FHRS533en-GB.xml) | 5,7 MB | 5.779 | `FHRSID` | OGL 3.0 |
| Forschungsorganisationen DE | [ROR-API](https://api.ror.org/v2/organizations?filter=country.country_code:DE) / [Dump](https://ror.readme.io/docs/data-dump) | – | 5.878 (API-Zählwert) | `id` | CC0 |
| Denkmäler FR | [CSV](https://ministere-culture.s3.sbg.io.cloud.ovh.net/POP/merimee.csv) | 100 MB | 46.761 | `Reference` | Licence Ouverte 2.0 |

In allen Dateien war die ID eindeutig (Datensätze = eindeutige IDs). Damit ist der Rohbestand bei allen sechs über 1.000 bestätigt. Das ist weiterhin kein fertiger Import: Status, Teilobjekte und Pflichtfelder sind noch zu filtern (siehe unten).

### Stolperfallen beim Einlesen

**Schulen NRW**
- Die erste Zeile ist `sep=;` (Excel-Hinweis), danach folgt der Header. Trennzeichen Semikolon, UTF-8, alle Werte in Anführungszeichen.
- Jede Zeile endet mit `;`, dadurch entsteht eine leere letzte Spalte.
- Koordinaten liegen als UTM (`EPSG`, `UTMRechtswert`, `UTMHochwert`) vor, nicht als Längen-/Breitengrad. Für Karten umrechnen (z. B. mit `pyproj`).
- `Schulbetriebsschluessel = 1` sind 5.606 Schulen im Betrieb; die übrigen 39 haben andere Statuswerte. Die amtliche Statistik nennt 5.418 Schulen, der Export enthält also mehr Einheiten. Vor der Veröffentlichung abgleichen.
- `Schulform` ist ein Code (`02` = Grundschule, 2.820 Einträge). Die Schlüsseltabelle liegt beim Schulministerium.

```python
import pandas as pd
df = pd.read_csv(URL, sep=";", skiprows=1, dtype=str).dropna(axis=1, how="all")
active = df[df["Schulbetriebsschluessel"] == "1"]
```

**Museen und Denkmäler Frankreich**
- Trennzeichen ist `|` (Pipe), UTF-8, Werte in Anführungszeichen.
- Museen: Beschreibende Felder sind gut gefüllt (`Histoire` 96 %, `Atout` 94 %, `Domaine_thematique` 96 %). Gute Grundlage für Profilseiten mit eigenem Text.
- Denkmäler: Die Datei enthält 46.761 Datensätze, mehr als die amtlichen 45.080 geschützten Objekte, weil laut Herausgeber auch ehemals geschützte Objekte enthalten sind. `Nature_de_la_protection` unterscheidet das nicht (fast alles ist `arrêté`); welches Feld aufgehobene Schutzakte markiert, ist beim Import noch zu klären, ein Ansatz ist `Date_et_typologie_de_la_protection`.
- Denkmäler: Inhaltsfelder sind dünn. `Historique` ist zu 53 % gefüllt, `Description_de_l_edifice` nur zu 2 %, `Datation_de_l_edifice` zu 24 %. Ein reichhaltiges Profil gibt es also nur für einen Teil des Bestands.

```python
df = pd.read_csv(URL, sep="|", dtype=str)
```

**Lebensmittelbetriebe Westminster (FSA)**
- XML mit `<EstablishmentDetail>`-Elementen; `Header/ItemCount` nennt die Gesamtzahl.
- `Scores.*` (89 %) und `Geocode.*` (92 %) fehlen bei einem Teil der Betriebe.
- `BusinessType` trennt Restaurants, Läden, Hotels usw. `Restaurant/Cafe/Canteen` sind 3.540 der 5.779 Betriebe.
- Andere Gebiete: Die Dateinummer (`FHRS533`) wechselt je Behörde, Übersicht auf der [FSA-Open-Data-Seite](https://ratings.food.gov.uk/open-data).

```python
df = pd.read_xml(URL, xpath="//EstablishmentDetail")
```

**Badegewässer (EEA)**
- Eine Excel-Datei für alle EU-Länder und alle Jahre ab 1990 (694.918 Zeilen). Für Deutschland filtern: `countryCode == "DE"` und `season == 2025`.
- `quality` ist ein Text wie `1 - Excellent`. Der Wert beschreibt die abgeschlossene Saison, nicht die heutige Badesicherheit.
- `lon`/`lat` sind vollständig gefüllt. `bwProfile` verlinkt das Badegewässerprofil der zuständigen Behörde.

```python
df = pd.read_excel(URL, sheet_name=0)  # benötigt openpyxl
de = df[(df["countryCode"] == "DE") & (df["season"] == 2025)]
```

**Forschungsorganisationen (ROR)**
- Die API liefert 20 Treffer pro Seite. Für einen vollständigen Länderbestand den [CC0-Datendump](https://ror.readme.io/docs/data-dump) nutzen, nicht die Filterpaginierung (ROR warnt vor Lücken und Dubletten).
- Organisationstypen sind gemischt (Hochschulen, Firmen, Kliniken, Archive …). Über `types` filtern.

## 3. Vom Rohbestand zum veröffentlichten Verzeichnis

Die Messung oben ersetzt nicht die Prüfungen vor einem Launch. Die [Prüfmethode](METHODIK.md) beschreibt sie im Detail. Kurz:

1. **Snapshot speichern** mit Abrufdatum, Prüfsumme und Quelle. Die [Integrationsarchitektur](integration/ARCHITECTURE.md) beschreibt ein Importmanifest.
2. **Bestand eingrenzen**: Betriebsstatus, Bezugsraum, Objektart.
3. **Pflichtfelder festlegen** und zählen, wie viele Einträge sie wirklich haben.
4. **Lizenzpflichten umsetzen**: Namensnennung, Lizenzlink, Änderungsvermerk. Bilder und Logos separat prüfen.
5. **Aktualität anzeigen**: Datum der Quelle sichtbar machen, Aktualisierung planen (die NRW-Schuldaten werden täglich erneuert).
6. Erst dann `qualified_entry_count` und `launch_ready` in [`verified_directory_projects.json`](../data/verified_directory_projects.json) setzen.

## 4. Lokale Werkzeuge

```bash
python -m pip install -r requirements-validation.txt
python scripts/build_dataset_index.py           # datasets.json/.csv und portals.csv neu erzeugen
python scripts/build_dataset_index.py --check   # prüfen, ob sie aktuell sind (läuft in CI)
python -m unittest discover -s tests -v         # alle Offline-Tests
python -m pip install openpyxl
python scripts/probe_sources.py                 # alle sechs Quellen neu herunterladen und messen (~150 MB)
```

`probe_sources.py` speichert Downloads in `~/.cache/open_data_gov`, nicht im Repository. Es läuft nicht in CI, weil es Netzwerk und größere Downloads braucht.
