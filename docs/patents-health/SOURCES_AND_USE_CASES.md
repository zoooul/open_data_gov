# Patente und Gesundheitsinfrastruktur: Quellen, Integration und Grenzen

[Übersicht](../../README.md) · [Monetarisierung](../strategy/COMMERCIAL_ASSESSMENT.md)

**Stand: 22.10.2026.** Ergänzende Fachanalyse mit offiziellen Belegen. Dokumentationsprüfung und technische Erprobung sind getrennt: Es wurde keine vollständige Patent- oder Krankenhausdatenbank importiert.

## 1. Patentdaten

### EPO Open Patent Services

OPS bietet Webservices für Patentinformationen, darunter bibliografische Angaben und weitere Inhalte je nach Abdeckung. Registrierung, Zugangsdaten und Fair-Use-Regeln gehören zum Zugang; die kostenlose Nutzungsstufe ist auf ein Datenvolumen begrenzt. Die aktuelle Produktseite nennt bis zu 4 GB pro Woche. [OPS](https://www.epo.org/en/searching-for-patents/data/web-services/ops), [Fair Use](https://www.epo.org/en/service-support/ordering/fair-use).

**Integration:** Mit einer kleinen dokumentierten Abfrage beginnen, Antwortschema und Abdeckung prüfen, Abfragen zwischenspeichern und Limits einhalten. Anmeldungen, Veröffentlichungen, Prioritäten und Patentfamilien sind im eigenen Modell zu unterscheiden. Familienbildung kann regionale Mehrfachveröffentlichungen zusammenführen; sie darf Unterschiede des Rechtsstands nicht verdecken.

**Nutzen:** Themenmonitoring, Technologie-Suche und belegte Zusammenfassungen. Eine Veröffentlichung ist kein Beleg für ein erteiltes oder weiterhin wirksames Schutzrecht. Ein Rechercheassistent ersetzt keine rechtliche Freedom-to-Operate-Prüfung.

### PATSTAT und Technology Intelligence Platform

Das EPA beschreibt den Zugang zu PATSTAT über die Technology Intelligence Platform. Die Möglichkeit zur kostenlosen Arbeit in einer Plattform ist jedoch nicht mit einer allgemeinen Freigabe eines beliebigen vollständigen Bulk-Downloads gleichzusetzen: Für PATSTAT-Bulk-Daten dokumentiert das EPA einen gesonderten Antrags- und Bewertungsprozess. [PATSTAT](https://www.epo.org/en/about-us/observatory-patents-and-technology/observatory-tools/patstat), [TIP](https://www.epo.org/en/searching-for-patents/data/technology-intelligence-platform), [Bulk-Antrag](https://www.epo.org/en/patstat-bulk-request).

**Korrektur einer früheren Verkürzung:** „PATSTAT-Bulk ist allgemein kostenlos verfügbar“ ist als pauschale Aussage nicht belastbar. Für ein Produkt müssen tatsächlich bewilligter Zugang, Exportmöglichkeiten und Bedingungen der vorgesehenen Nutzung dokumentiert werden.

### PatentsView und USPTO Open Data Portal

Die USPTO kündigte für den 20.03.2026 den Umzug von PatentsView in ihr Open Data Portal an; die Mitteilung nennt vorübergehende Unterbrechungen bestimmter Such- und API-Dienste. Neuere Meldungen beschreiben verfügbare Bulk- und jährliche Datensätze. [Migrationsmitteilung](https://www.uspto.gov/subscription-center/2026/patentsview-migrating-uspto-open-data-portal-march-20), [offizieller Einstieg](https://www.uspto.gov/ip-policy/economic-research/patentsview), [jährliche Datensätze](https://www.uspto.gov/subscription-center/2026/june-17-new-update-patentsview-annualized-datasets).

**Integration:** Aktuelle ODP-Dokumentation und konkrete Downloads verwenden. Alte PatentsView-API-Adressen nicht als funktionierend voraussetzen; eine Wiederaufnahme muss eigens geprüft werden. Auch frei zugängliche Daten können für programmatischen Bezug Registrierung oder Schlüssel erfordern. [ODP Bulk Data API](https://data.uspto.gov/apis/bulk-data/search).

**Nutzen:** Erfinder-, Anmelder- und Technologieanalysen. Bereinigte Entitätszuordnungen sind Analysehilfen, keine amtlich bestätigte wirtschaftliche Identität. Schreibweisen und Firmenzusammenschlüsse benötigen nachvollziehbare Zuordnungsregeln.

## 2. Gesundheitsinfrastruktur in Deutschland

### Amtliches Krankenhausverzeichnis

Das Statistikportal stellt das Krankenhausverzeichnis 2024 als Excel-Datei bereit; Bezugsstand ist der 31.12.2024, Veröffentlichung der 29.05.2026. Es enthält Krankenhäuser sowie Vorsorge- und Rehabilitationseinrichtungen mit Anschriften und weiteren Merkmalen. Die Seite gestattet Vervielfältigung und Verbreitung mit Quellenangabe. [Originalquelle](https://www.statistikportal.de/de/veroeffentlichungen/krankenhausverzeichnis).

**Integration:** Datei- und Berichtsstand speichern, Spalten prüfen und Einrichtung von Standort und Fachabteilung trennen. Kennungen nicht allein aus Namen ableiten. Herausgeber und Quellenangabe in jedem abgeleiteten Export erhalten.

**Nutzen:** Einrichtungsverzeichnis, regionale Erreichbarkeits- und Versorgungsanalysen. Aus dem Datenstand folgen keine aktuellen freien Betten, Wartezeiten oder konkreten Aufnahmezusagen. Das Verzeichnis ist außerdem kein vollständiges Register ambulanter Psychotherapiepraxen.

### Bundes-Klinik-Atlas: maschinenlesbare Exporte

Die Open-Data-Seite bietet einen Exportstand vom 29.09.2026 und beschreibt XML-Dateien samt Schema. Besonders wichtig: Bestimmte Fallzahlen unter vier werden als `-1` ausgegeben, um kleine Werte nicht offenzulegen. [Export und Erläuterungen](https://bundes-klinik-atlas.de/open-data/).

**Integration:** `-1` als unterdrückten Wert interpretieren, nicht als negative Fallzahl oder null Fälle. Schema und Codes mit dem jeweiligen Export versionieren. Vor öffentlicher Weiterverarbeitung den genauen Lizenz- und Nutzungsumfang des gewählten Exports dokumentieren; die technische Downloadmöglichkeit allein genügt nicht.

**Nutzen:** Erweiterung eines Standortverzeichnisses um nachvollziehbare Leistungsinformationen. Fallzahl, Bettenzahl, Fachabteilung und Versorgungsqualität sind unterschiedliche Größen. Eine eigene Qualitätsrangfolge braucht eine begründete Methodik und darf nicht allein aus Datenverfügbarkeit abgeleitet werden.

## 3. Gemeinsame Verknüpfungsregeln

Für Patent- und Gesundheitsdaten gleichermaßen empfiehlt sich ein Modell mit unabhängigen Entitäten und zeitlichen Beziehungen. Eine Organisation ist nicht dasselbe wie ein einzelner Standort. Ein Adresswechsel darf die Historie nicht auslöschen. Mehrere Namen oder Quellenkennungen können derselben Organisation entsprechen, müssen aber belegt zugeordnet werden.

Eine Verbindung „Medizintechnik-Patent + Klinikstandort“ ist zunächst eine analytische Hypothese. Sie beweist weder, dass die Klinik das patentierte Verfahren einsetzt, noch dass ein Medizinprodukt zugelassen ist oder eine Behandlung verfügbar wäre. Solche Aussagen benötigen separate Belege.

## 4. Produktansätze und Abnahmekriterien

| Produktidee | Entscheidungsnutzen | Erforderlicher Qualitätsnachweis |
|---|---|---|
| Technologie-Monitor | Relevante neue Veröffentlichungen schneller finden | Quellen, Familienlogik, nachvollziehbare thematische Treffer |
| Patentportfolio-Übersicht | Technologische Schwerpunkte vergleichen | Keine Gleichsetzung von Anmeldung, Erteilung und Wirksamkeit |
| Klinik- und Reha-Verzeichnis | Einrichtungen und Fachbereiche finden | Quellenstand, Standortabgleich, keine erfundenen Kapazitäten |
| Regionaler Versorgungsbericht | Geografische Unterschiede sichtbar machen | Bezugsjahre, Gebietsstände, Nenner und unterdrückte Werte korrekt |
| Innovationslandschaft | Forschung und Infrastruktur gemeinsam beschreiben | Verknüpfungen als Hypothesen kennzeichnen, keine Kausalität vortäuschen |

Die Attraktivität dieser Produkte ist eine Geschäftshypothese. Vor einer Umsetzung müssen reale Nutzeraufgaben, Zahlungsbereitschaft, Datenpflegeaufwand und Lizenzbedingungen geprüft werden. Die [kommerzielle Analyse](../strategy/COMMERCIAL_ASSESSMENT.md) liefert dafür ein Testgerüst.
