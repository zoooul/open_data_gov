# Prüfmethode: wann eine offene Quelle als belegt gilt

[README](../README.md) · [Zusammenhänge](ZUSAMMENHAENGE.md) · [Beispielprojekte](strategy/DIRECTORY_PROJECT_PRIORITIES.md)

Diese Regeln gelten für alle Themen in diesem Repository. Sie fassen zusammen, was in den Fachanalysen jeweils im Detail angewendet wird.

## 1. Eine Zahl braucht fünf Angaben

| Angabe | Beispiel |
|---|---|
| Einheit | Badegewässer, nicht „Einträge“ |
| Bezugsraum | Deutschland, nicht „EU“ |
| Zeitraum | Saison 2025 |
| Zählbasis | amtliche Statistik, Herausgeberangabe oder selbst gelesene API-Antwort |
| Primärbeleg | Link auf das Dokument, in dem die Zahl steht |

In den JSON-Dateien heißt die Zählbasis `source_count.basis`:

- `official_scope_statistic`: amtliche Bezugszahl, nicht die Zeilenzahl einer Datei
- `publisher_dataset_count`: Angabe des Herausgebers zum Datensatz
- `api_country_facet`: selbst abgefragter Zählwert einer API

`relation: gt` bedeutet „mehr als“. Eine Untergrenze wird nie in eine exakte Zahl umgeschrieben. Unbekannt heißt unbekannt, nicht null.

## 2. Zahlen verschiedener Einheiten nicht addieren

Studien, Effektzeilen, Versuchspersonen, Bilder, Buchtitel, Ladeanschlüsse und Einrichtungen sind verschiedene Dinge. 52 Versuchspersonen sind keine 52 Verzeichnisprofile, zehn Ladepunkte an einem Ort keine zehn Standorte. Teilbestände (etwa Grundschulen innerhalb aller Schulen) werden nicht zusätzlich gezählt.

## 3. Lizenz am Datensatz belegen

Maßgeblich ist die Lizenz des konkreten Datensatzes, nicht die des Portals. „Öffentlich sichtbar“, „kostenlos herunterladbar“ und „kommerziell weiterverwendbar“ sind drei verschiedene Zustände. Bilder, Logos, verlinkte Volltexte und personenbezogene Angaben haben oft eigene Rechte. Eine [Übersicht aller vorkommenden Lizenzen](ZUSAMMENHAENGE.md#2-lizenzen-im-vergleich) steht in den Zusammenhängen.

## 4. Zwei Freigabestufen

| Stufe | Feld im JSON | Bedeutung |
|---|---|---|
| Quellenbestand belegt | `source_stock_supported` | Menge, Inhalte und offener Lizenzweg sind an der Quelle belegt |
| Veröffentlichungsfähig | `full_import_tested`, `qualified_entry_count`, `launch_ready` | Vollständiger Import, Dublettenprüfung, Pflichtfelder und Aktualität sind gemessen |

Die erste Stufe sagt nichts über die zweite. Aktuell hat kein Projekt die zweite Stufe erreicht. Wer einen Import durchführt, setzt diese Felder erst nach der Messung.

## 5. Dokumentiert ist nicht getestet

`documented_content` und `documentation_checked_at` beschreiben, was eine Quelle über sich sagt. `payload_checked_at` ist nur gesetzt, wenn tatsächlich Nutzdaten gelesen wurden. Für die sechs Kandidaten stehen gemessene Zeilen- und ID-Zahlen getrennt in `data/source_probes.json` und als `measured_*` in `data/datasets.json`. Ein erreichbarer Link, ein HTTP-200 oder ein bestandener Metadatentest ist kein Integrationstest.

## 6. Hypothesen kennzeichnen

Suchvolumen, Wettbewerb und Erlöse wurden in keinem Fall gemessen. Geschäftsideen, SEO-Beispiele und Ranglisten sind redaktionelle Einschätzungen und stehen als solche im Text. Mehr Datensätze rechtfertigen nicht automatisch mehr indexierbare Seiten; künstlich kombinierte Ort-Keyword-Seiten werden nicht empfohlen.

## 7. Fachliche Grenzen

- Trägerzulassung, Maßnahmezulassung und persönliche Förderung (AZAV) sind verschieden.
- Ein OpenStreetMap-Tag bestätigt keine Approbation oder Qualifikation.
- Studien und Registereinträge sind keine Behandlungsempfehlung.
- Historische Badequalität ist keine heutige Sicherheitsfreigabe; eine Hygienebewertung ist keine Geschmackswertung.
- Ein Baudenkmal ist nicht automatisch öffentlich zugänglich.
- Eine Patentveröffentlichung ist kein erteiltes oder wirksames Schutzrecht.
