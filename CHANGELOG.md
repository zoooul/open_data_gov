# Änderungen

## 2026-10-28 – Entwicklerfreundliche Daten

- Alle sechs Kandidaten tatsächlich heruntergeladen und gemessen (`scripts/probe_sources.py`, `data/source_probes.json`): Datensätze, eindeutige IDs, Füllgrad je Feld. Rohbestand bei allen sechs über 1.000 bestätigt; `launch_ready` bleibt false.
- Direkter Downloadlink für die EEA-Badegewässerdatei ergänzt.
- Neu: `data/datasets.json` und `data/datasets.csv` mit allen 34 Datensätzen in einheitlichen Spalten (normalisierte Lizenz, kommerzielle Nutzbarkeit, Zugangsart, Mengen, Messwerte), dazu `data/portals.csv`. Erzeugt durch `scripts/build_dataset_index.py`, geprüft per Schema, Tests und CI.
- Neu: `docs/ENTWICKLER.md` mit Downloadlinks, Formaten, gemessenen Stolperfallen und getesteten Codebeispielen.
- Einen JSON-Schlüssel in `data/project_priorities.json` neutral benannt (`operator_expertise_fit`).

## 2026-10-28 – Vorbereitung für die Veröffentlichung

- README für öffentliche Leser neu geschrieben: Einstieg nach Anwendungsfall, englische Kurzfassung, Inhaltsübersicht, Grenzen.
- Neu: `docs/METHODIK.md` (Prüfregeln kompakt) und `docs/ZUSAMMENHAENGE.md` (Lizenzvergleich über alle Themen, mehrfach genutzte Quellen, Karte der Datendateien, Herkunft der aktuellen Kandidaten, offene Lücken).
- Lizenz: Texte und Daten CC BY 4.0 (`LICENSE`), Code MIT (`LICENSE-CODE`). Fremddatensätze ausgenommen.
- `CONTRIBUTING.md`, `.gitignore` und GitHub-Actions-Workflow für alle Validatoren und Tests ergänzt.
- Struktur: Portalverzeichnis nach `docs/portals/OPEN_DATA_PORTALE.md`, kommerzielle Einordnung nach `docs/strategy/COMMERCIAL_ASSESSMENT.md`, beide früheren Analysen nach `docs/archive/`. Alle relativen Links angepasst.
- Korrektur: `source_document` in `data/project_priorities.json` zeigte auf die aktuelle statt auf die archivierte Strategie.
- Hinweise auf private Sichtbarkeit und auf das persönliche Profil des Betreibers neutral formuliert. Keine Zahlen, Quellen oder IDs inhaltlich verändert.

## 2026-10-23 – Quellenbestand vor Projektversprechen

Die frühere allgemeine Empfehlungsliste wird für den aktuellen Directory-Auftrag ersetzt: sechs konkret abgegrenzte Projekte mit belegten Ausgangsmengen, dokumentiertem fachlichem Inhalt und Lizenzbelegen. Die 20 früheren Projektideen bleiben unverändert als historische Recherche erhalten; sie sind nicht mehr der aktive Auswahlkatalog.

### Neue Belege

- 2.291 deutsche Badegewässer, Saison 2025; konkrete EEA-Veröffentlichung mit CC BY 4.0.
- Über 1.200 Muséofile-Museen in Frankreich; aktuelle Katalogmetadaten, CSV-Zugang und Licence Ouverte 2.0.
- 5.418 Schulen in NRW, Schuljahr 2025/26; amtliche Statistik und separat dokumentierter täglicher Export.
- 5.779 Lebensmittelbetriebe im konkreten Westminster-Export der FSA; OGL und Aktualitätspflichten.
- 5.878 Deutschland-Einträge aus der tatsächlich gelesenen ROR-API-Länderfacette; CC0-Gesamtdump dokumentiert.
- 45.080 geschützte unbewegliche Güter Frankreichs am 01.01.2024; ausdrücklich historischer Bezugsbestand, kein aktueller CSV-Count.

### Struktur und Prüfung

- `data/verified_directory_projects.json` als aktuelle Auswahl ergänzt.
- Manifest auf Version 2 mit getrenntem `research_archive` umgestellt. Alte IDs nicht umnummeriert oder gelöscht.
- README, Strategie, kommerzielle Einordnung, AGENTS und llms.txt auf die neue Auswahl ausgerichtet.
- Frühere Strategie und kommerzielle Analyse als Archive erhalten.
- 14 neue Offline-Tests und neuer Metadatenvalidator erfolgreich lokal ausgeführt. Unveränderte Bildungstests in diesem Schritt nicht erneut ausgeführt.
- Keine Vollimports, keine gemessenen Feldfüllquoten, keine 1000 fertig qualifizierten Profilseiten je Projekt. Alle `launch_ready`-Werte bleiben false.
- Ungeklärte oder zu kleine Bestände nicht zum Erreichen einer Wunschzahl ergänzt. Keine künstliche Ausweitung auf 50 Projekte.
- Keine Änderung von Sichtbarkeit oder allgemeiner Repository-Lizenz; keine automatische Abrufplanung.

### Noch zu erledigen

Für jedes ausgewählte Projekt: vollständigen Snapshot beziehen, Bezugsraum abgleichen, Datensätze normalisieren und deduplizieren, Mindestfelder und Aktualität zählen. Danach tatsächliche Suchintentionen und einen konkreten Erlösweg prüfen. Quellenzahlen dürfen nicht vorab als fertig importierte Bestände ausgegeben werden.

## Frühere Änderungen

Das bisherige Protokoll einschließlich Bildungs-, Esoterik- und Psychotherapie-Erweiterung ist unverändert in [CHANGELOG_PRE_STOCK_GATE.md](docs/archive/CHANGELOG_PRE_STOCK_GATE.md) erhalten.
