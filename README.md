# Open Data Gov

**Quellengeprüfte Recherche zu offenen Verwaltungs- und Forschungsdaten: Portalverzeichnis, Datensatzprofile mit Lizenzbelegen und eine Prüfmethode, die Quellenzahlen nicht mit fertigen Datenbeständen verwechselt.**

> **English summary:** A German-language research repository about open government and research data. It contains a directory of ~100 open-data portals (DE/EU/world), 28 source profiles with license evidence across education, psychotherapy research, esotericism/history, patents and health infrastructure, and six directory-project candidates whose source files were actually downloaded and measured (rows, unique IDs, field fill rates). **For developers:** one normalized table of all 34 datasets with license, commercial-use flag and download link: [`data/datasets.csv`](data/datasets.csv) / [`.json`](data/datasets.json), plus a [developer guide](docs/ENTWICKLER.md). Every number carries its unit, scope, period and evidence. Nothing here is a finished import, a legal opinion or a traffic forecast. Machine-readable files live in [`data/`](data/); validation runs offline with Python.

Stand der Recherche: Oktober 2026 · Sprache: Deutsch · Lizenz: [CC BY 4.0 für Texte und Daten, MIT für Code](#lizenz)

## Wofür ist das nützlich?

| Du willst … | Starte hier |
|---|---|
| als Entwickler direkt mit Daten loslegen | [**Entwickler-Guide**](docs/ENTWICKLER.md) · [alle Datensätze als CSV](data/datasets.csv) / [JSON](data/datasets.json) |
| ein offenes Datenportal für ein Land, Bundesland oder eine Stadt finden | [Portalverzeichnis](docs/portals/OPEN_DATA_PORTALE.md) · [CSV](data/portals.csv) · [JSON](data/portals.json) |
| wissen, ob ein bestimmter Datensatz wiederverwendet werden darf | [Lizenzübersicht über alle Themen](docs/ZUSAMMENHAENGE.md#2-lizenzen-im-vergleich) |
| ein Verzeichnis oder Datenprodukt auf offenen Daten aufbauen | [Prüfmethode](docs/METHODIK.md) → [sechs Beispielprojekte](docs/strategy/DIRECTORY_PROJECT_PRIORITIES.md) |
| Quellen zu einem Fachthema recherchieren | [Themenübersicht](#themen) |
| einen Datenimport technisch planen | [Integrationsarchitektur](docs/integration/ARCHITECTURE.md) |
| verstehen, wie alles zusammenhängt | [Zusammenhänge und Querbezüge](docs/ZUSAMMENHAENGE.md) |

## Was macht dieses Repository anders?

Viele Open-Data-Listen sammeln Links. Hier wird zusätzlich festgehalten, **was genau belegt ist und was nicht**:

- Jede Mengenangabe hat Einheit, Bezugsraum, Zeitraum, Zählmethode und Primärbeleg. „2.291 Badegewässer, Deutschland, Saison 2025, EEA-Länderblatt“ statt „über 2.000 Einträge“.
- Quellenbestand und nutzbarer Bestand sind getrennt. Dass eine Quelle 5.000 Datensätze nennt, heißt nicht, dass 5.000 brauchbare Profile daraus werden.
- Lizenzen werden am konkreten Datensatz belegt, nicht am Portal.
- Zahlen verschiedener Einheiten (Studien, Versuchspersonen, Bilder, Einrichtungen) werden nie addiert.

Die Regeln dazu stehen kompakt in der [Prüfmethode](docs/METHODIK.md).

## Inhalt auf einen Blick

### Portalverzeichnis

Rund 100 Einstiegspunkte: zentrale Kataloge, alle 16 Bundesländer, 24 deutsche Städte, 27 europäische und 20 weitere nationale Portale, internationale Statistikplattformen und thematische Fachportale. Dazu eine Lizenzübersicht und eine Checkliste vor dem Datenimport. → [Verzeichnis](docs/portals/OPEN_DATA_PORTALE.md)

### Themen

| Thema | Inhalt | Quellenprofile |
|---|---|---|
| [Weiterbildung und AZAV](docs/education/WEITERBILDUNG_DE_AZAV.md) | Kursdatenquellen in Deutschland, Unterschied zwischen Träger- und Maßnahmezulassung, [Datenmodell für Kurse](docs/education/COURSE_DATA_MODEL.md) | [11 Profile](data/education_sources.json) |
| [Psychotherapie und Hypnose](docs/psychotherapy-hypnosis/VERIFIED_DATASETS.md) | Metaanalyse-Datenbanken (Metapsy), Studienregister, offene Volltexte, ein Hypnose-EEG-Datensatz | [9 Profile](data/psychotherapy_sources.json) |
| [Esoterik, historische Quellen, Astronomie](docs/esotericism/VERIFIED_SOURCES.md) | Digitalisierte historische Sammlungen, Wikidata, Mondphasen-API, Ephemeriden | [8 Profile](data/esotericism_sources.json) |
| [Patente und Gesundheitsinfrastruktur](docs/patents-health/SOURCES_AND_USE_CASES.md) | EPO OPS, PATSTAT, USPTO Open Data, Krankenhausverzeichnis, Bundes-Klinik-Atlas | im Text |

### Sechs Verzeichnisprojekte mit belegtem Ausgangsbestand

Offene Quellen, aus denen sich ein Verzeichnis mit mindestens 1.000 Einträgen bauen lässt. Alle sechs Dateien wurden am 28.10.2026 heruntergeladen und ausgewertet:

| Projekt | Laut Quelle | Selbst gemessen | Format | Lizenz |
|---|---:|---:|---|---|
| Badegewässer Deutschland, Saison 2025 | 2.291 | 2.291 | XLSX | CC BY 4.0 |
| Museen Frankreich (« Musée de France ») | über 1.200 | 1.216 | CSV | Licence Ouverte 2.0 |
| Schulen NRW | 5.418 (Statistik 2025/26) | 5.645 (Tagesexport) | CSV | DL-DE BY 2.0 |
| Lebensmittelbetriebe mit Hygienebewertung, Westminster | 5.779 | 5.779 | XML | OGL 3.0 |
| Forschungsnahe Organisationen Deutschland (ROR) | 5.878 | 5.878 (API) | JSON | CC0 |
| Baudenkmäler Frankreich | 45.080 (Stand 01.01.2024) | 46.761 (inkl. ehemaliger) | CSV | Licence Ouverte 2.0 |

Direkte Downloadlinks, Feldlisten, Füllgrade und Stolperfallen beim Einlesen: [Entwickler-Guide](docs/ENTWICKLER.md). Ein bereinigter, veröffentlichungsfertiger Bestand ist das noch nicht (`launch_ready: false`). Details, Grenzen und verworfene Kandidaten: [Projektanalyse](docs/strategy/DIRECTORY_PROJECT_PRIORITIES.md) · [JSON](data/verified_directory_projects.json) · [Geschäftsmodell-Hypothesen](docs/strategy/COMMERCIAL_ASSESSMENT.md)

## Aufbau des Repositorys

```text
README.md                 Einstieg (diese Datei)
docs/
  ENTWICKLER.md           Daten laden: Downloadlinks, Formate, Stolperfallen, Code
  METHODIK.md             Prüfregeln: Einheiten, Zählbasis, Lizenz, Freigabestufen
  ZUSAMMENHAENGE.md       Querbezüge: Lizenzen, wiederkehrende Quellen, Ideen-Herkunft
  portals/                Portalverzeichnis Deutschland, Europa, weltweit
  education/              Weiterbildung, AZAV, Kursdatenmodell
  psychotherapy-hypnosis/ Psychotherapie- und Hypnoseforschung
  esotericism/            Esoterik, historische Quellen, Astronomie
  patents-health/         Patente und Gesundheitsinfrastruktur
  strategy/               Sechs Verzeichnisprojekte und Erlöshypothesen
  integration/            Architekturvorschlag für Importe
  archive/                Ältere Recherchestände (nicht mehr aktuell)
data/                     Maschinenlesbare Kataloge (JSON, CSV)
  datasets.csv / .json    Alle 34 Datensätze in einer einheitlichen Tabelle
  source_probes.json      Messung der sechs Downloads
schemas/                  JSON-Schemas
scripts/                  Validatoren, Index-Generator, Download-Probe
tests/                    Unit-Tests für die Validatoren
```

Was jede JSON-Datei enthält und wie sie zusammenhängt, steht in [docs/ZUSAMMENHAENGE.md](docs/ZUSAMMENHAENGE.md#4-datendateien). Der einfachste Einstieg für Programme ist [`data/datasets.json`](data/datasets.json).

## Daten prüfen

Python 3.10 oder neuer:

```bash
python -m pip install -r requirements-validation.txt
python scripts/validate_verified_directories.py
python scripts/validate_education.py
python scripts/build_dataset_index.py --check
python -m unittest discover -s tests -v
```

Die Prüfungen laufen offline. Sie kontrollieren Struktur, Kennungen, Mengenangaben, verbotene Freigabezustände und ob die erzeugte Datensatztabelle aktuell ist, nicht die Erreichbarkeit externer Links oder die rechtliche Zulässigkeit einer Nutzung. Bei jedem Push laufen sie zusätzlich über [GitHub Actions](.github/workflows/validate.yml).

## Grenzen

- **Kein Rechtsrat.** Lizenzangaben beschreiben, was zum Prüfzeitpunkt an der Quelle stand. Vor einer Veröffentlichung selbst prüfen; Fotos, Logos und personenbezogene Daten haben oft eigene Regeln.
- **Kein medizinischer Rat.** Studien- und Registerdaten sind keine Behandlungsempfehlung.
- **Momentaufnahme.** Links und Zahlen stammen aus Oktober 2026 und werden nicht automatisch aktualisiert.
- **Hypothesen bleiben Hypothesen.** Suchvolumen, Umsatz und Wettbewerb wurden nicht gemessen.

## Mitmachen

Fehler, tote Links, neue Quellen oder veraltete Zahlen bitte als Issue oder Pull Request melden. Was ein guter Beitrag braucht, steht in [CONTRIBUTING.md](CONTRIBUTING.md). Für KI-Assistenten gibt es [AGENTS.md](AGENTS.md) und [llms.txt](llms.txt).

## Lizenz

- **Texte, Tabellen und JSON-Daten** dieses Repositorys: [Creative Commons Namensnennung 4.0 (CC BY 4.0)](LICENSE). Nutzung, auch kommerziell, mit Namensnennung „Open Data Gov (github.com/zoooul/open_data_gov)“.
- **Skripte und Tests** (`scripts/`, `tests/`, `.github/`): [MIT](LICENSE-CODE).
- **Die beschriebenen Fremddatensätze** unterliegen ausschließlich ihren eigenen Lizenzen. Dieses Repository enthält keine Kopien davon, nur Beschreibungen und Links.

Änderungsverlauf: [CHANGELOG.md](CHANGELOG.md)
