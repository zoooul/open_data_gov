# Zusammenhänge und Querbezüge

[README](../README.md) · [Prüfmethode](METHODIK.md)

Die Fachanalysen sind zu verschiedenen Zeitpunkten entstanden und stehen jede für sich. Diese Seite zeigt, was sie verbindet: welche Lizenzen immer wieder vorkommen, welche Quellen in mehreren Themen auftauchen, woher die aktuellen Projektkandidaten kommen und wie die Datendateien zusammenhängen.

## 1. Drei Ebenen, die sich durch alle Themen ziehen

| Ebene | Frage | Wo im Repository |
|---|---|---|
| Wo finde ich Daten? | Portale und Kataloge | [Portalverzeichnis](portals/OPEN_DATA_PORTALE.md), [`portals.json`](../data/portals.json) |
| Was ist in einer Quelle, und darf ich es nutzen? | Quellenprofile mit Menge, Lizenz, Grenzen | Fachanalysen unter `docs/<thema>/`, `data/*_sources.json` |
| Reicht das für ein Produkt? | Projektprofile mit Bestands- und Freigabestufe | [Projektanalyse](strategy/DIRECTORY_PROJECT_PRIORITIES.md), [`verified_directory_projects.json`](../data/verified_directory_projects.json) |

Der Weg von oben nach unten ist in der [Integrationsarchitektur](integration/ARCHITECTURE.md) als Datenfluss beschrieben: Quellenkatalog → Rohdaten → Fachmodell → Produktansicht. Das Repository deckt bisher nur die erste Ebene und Teile der zweiten ab.

## 2. Lizenzen im Vergleich

Alle in den Profilen belegten Lizenzen, sortiert von sehr offen bis eingeschränkt. Stand der Prüfung: Oktober 2026; vor der Nutzung an der Quelle erneut prüfen.

| Lizenz | Kommerziell | Namensnennung | Weitergabe unter gleicher Lizenz | Vorkommen |
|---|---|---|---|---|
| CC0 / Public Domain | ja | nein | nein | ROR, Wikidata, OpenNeuro ds004572, PsychArchives (nur Metadaten), e-rara (teilweise), Wikimedia-Tarotbilder (Einzelprüfung) |
| CC BY 4.0 | ja | ja | nein | EEA-Badegewässer, Berliner VHS-Kurse (Version unklar) |
| Licence Ouverte / Etalab 2.0 | ja | ja | nein | Muséofile, Mérimée-Denkmäler |
| Datenlizenz Deutschland – Namensnennung 2.0 | ja | ja | nein | NRW-Schuldaten |
| Open Government Licence 3.0 | ja | ja | nein | FSA-Hygienebewertungen (Logos mit Zusatzbedingungen) |
| ODC-By 1.0 | ja | ja | nein | Metapsy-Datenbanken |
| ODbL | ja | ja | ja, für abgeleitete Datenbanken | OpenStreetMap (Psychotherapiepraxen, Esoterikläden) |
| CC BY-SA 3.0 DE / 4.0 | ja | ja | ja | Hamburger Kursportal WISY, e-rara (teilweise) |
| AGPL oder kommerzielle Lizenz | nur mit Auflagen | ja | ja (AGPL) | Swiss Ephemeris |
| Je Objekt verschieden | teils | teils | teils | PMC Open Access Subset, Project Gutenberg |
| Nicht belegt | unklar | – | – | AACT, AnnoMI, mein NOW, IWWB, WIS, hoch & weit |

**Beobachtungen:**

- Die deutschen und französischen Verwaltungsdaten in den Beispielprojekten sind durchweg ohne Share-Alike nutzbar. Die einzigen Share-Alike-Quellen (OSM, WISY) sind genau die, auf denen frühere Nischenideen (Praxisfinder, Esoterikläden, Kursportal) aufgebaut hätten.
- Bei Weiterbildung fehlt für die meisten großen Suchportale eine belegte Datenlizenz. Das ist der Hauptgrund, warum das ursprünglich erstplatzierte Weiterbildungsprojekt nicht mehr empfohlen wird.
- „Metadaten offen, Inhalte nicht“ ist ein wiederkehrendes Muster (PsychArchives, PMC, e-rara, Wikidata gegenüber Commons-Medien).

## 3. Quellen, die in mehreren Themen vorkommen

| Quelle | Kommt vor in | Rolle |
|---|---|---|
| OpenStreetMap | Portalverzeichnis, Psychotherapie, Esoterik, frühere Strategie | Standorte von Praxen und Läden; nie Qualifikationsnachweis |
| Amtliches Krankenhausverzeichnis | Portalverzeichnis, Patente/Gesundheit, frühere Strategie, verworfene Kandidaten | Klinik-/Reha-Stammdaten, Bezugsstand 31.12.2024 |
| Wikidata | Esoterik | Strukturierte Wissensdaten unter CC0; auch für andere Themen nutzbar |
| GovData, data.europa.eu, data.gouv.fr | Portalverzeichnis, Projektanalyse | Einstieg; die Datensätze der Beispielprojekte liegen auf diesen Portalen |
| Google-Richtlinien zu hilfreichen Inhalten | Projektanalyse, frühere Strategie | Begründung, warum keine massenhaft generierten Seiten |

## 4. Datendateien

| Datei | Inhalt | Anzahl | Schema / Validator | Status |
|---|---|---:|---|---|
| [`datasets.json`](../data/datasets.json) / [`.csv`](../data/datasets.csv) | Alle Datensätze einheitlich, mit normalisierter Lizenz (erzeugt) | 34 | `schemas/datasets.schema.json`, `build_dataset_index.py --check` | aktuell |
| [`source_probes.json`](../data/source_probes.json) | Gemessene Downloads der sechs Kandidaten | 6 | Tests | 28.10.2026 |
| [`project_catalog.json`](../data/project_catalog.json) | Manifest: verweist auf alle Projektdateien | – | – | aktuell |
| [`verified_directory_projects.json`](../data/verified_directory_projects.json) | Sechs Projektkandidaten mit Bestandsbeleg | 6 | `scripts/validate_verified_directories.py` | aktuell |
| [`portals.json`](../data/portals.json) | Portale aus dem Verzeichnis, Dubletten entfernt | 100 | `schemas/portals.schema.json` (kein Validator-Skript) | aktuell |
| [`education_sources.json`](../data/education_sources.json) | Weiterbildungsquellen | 11 | `schemas/education_sources.schema.json`, `scripts/validate_education.py` | aktuell |
| [`psychotherapy_sources.json`](../data/psychotherapy_sources.json) | Psychotherapie-/Hypnosequellen | 9 | keins | aktuell |
| [`esotericism_sources.json`](../data/esotericism_sources.json) | Esoterik-/Geschichtsquellen | 8 | keins | aktuell |
| [`project_priorities.json`](../data/project_priorities.json) | Zehn frühere Projektideen | 10 | keins | Archiv |
| [`psychotherapy_projects.json`](../data/psychotherapy_projects.json) | Vier frühere Projektideen | 4 | keins | Archiv |
| [`esotericism_projects.json`](../data/esotericism_projects.json) | Sechs frühere Projektideen | 6 | keins | Archiv |

**Unterschiede, die man beim Einlesen kennen sollte:**

- Das Lizenzfeld heißt je nach Datei unterschiedlich: `license.id` (Projekte), `license_label` (Bildung, Psychotherapie) und `license_summary` (Esoterik). Die erzeugte `datasets.json` vereinheitlicht das zu `license_id`, `commercial_use`, `attribution_required` und `share_alike`.
- `portals.json` enthält 100 Einträge, die Markdown-Tabellen zusammen etwas mehr, weil Berlin, Hamburg, EU-Portal und Data.gov dort mehrfach stehen. Die thematischen Fachportale (Abschnitt 7 des Verzeichnisses) sind nicht im JSON.
- Für die Portale sind Lizenz und API-Zugang durchweg `unverified` bzw. `unknown`; das Verzeichnis ist eine Linksammlung, keine Lizenzprüfung.
- Nutzdaten wurden für die sechs Kandidaten vollständig heruntergeladen und gemessen, außerdem für den US Naval Observatory. Die übrigen Quellenprofile beruhen auf Dokumentationsprüfung.

## 5. Woher die aktuellen Projektkandidaten kommen

Die Recherche ist in zwei Runden entstanden. Die erste Runde (22.10.2026) sammelte 20 breite Projektideen nach Nutzen und Geschäftsmodell. Die zweite Runde (23.10.2026) legte eine strengere Bedingung an: mindestens 1.000 belegte Einheiten in einem klar abgegrenzten Bezugsraum mit offener Lizenz.

| Frühere Idee | Ergebnis in der zweiten Runde |
|---|---|
| Schul- und Bildungsstandortnavigator | fortgeführt als **Schulverzeichnis NRW** (landesweite Schuldaten statt Einzelstadt) |
| Forschungs- und Innovationspartnerfinder | thematisch fortgeführt als **Forschungsnahe Organisationen (ROR)** |
| Weiterbildungsnavigator | verworfen: kein geklärter Bulkzugang zu Kursdaten |
| Klinik-/Reha-Wegweiser | verworfen: qualifizierte Startmenge nicht gezählt; Quellen bleiben in [Patente/Gesundheit](patents-health/SOURCES_AND_USE_CASES.md) |
| Entsorgungsnavigator | verworfen: Beispielbestand mit 12 Standorten |
| Ladepausenfinder | verworfen: Ladepunkte zählen Anschlüsse, nicht Standorte |
| Ausschreibungsradar, Barrierefreiheit, Energieanlagen, Wohnumfeld | in der zweiten Runde nicht erneut bewertet |
| Esoterikladen-Finder, Tarotatlas, Hermetik-Bibliothek | verworfen: keine belastbare Menge (78 Bilder, 289 Titel) |
| Psychotherapie-Evidenznavigator und weitere | verworfen als Verzeichnis; als Forschungswerkzeug weiter interessant |
| – (neu) | **Badegewässer DE, Museen FR, Lebensmittelbetriebe Westminster, Denkmäler FR** |

Vier der sechs aktuellen Kandidaten sind also neu hinzugekommen, und zwei davon liegen außerhalb Deutschlands. Das ist eine direkte Folge der strengeren Belegregel: In Frankreich und Großbritannien sind die Verwaltungsdaten für diese Kategorien häufiger mit gezählter Menge und klarer Lizenz veröffentlicht.

## 6. Offene Lücken

Aus dem Vergleich ergeben sich Arbeitspunkte, die in keiner Einzelanalyse stehen:

1. Für Psychotherapie-, Esoterik- und Portaldaten gibt es kein eigenes Validator-Skript; sie werden nur über die erzeugte Datensatztabelle geprüft.
2. Die Downloads sind gemessen, aber nicht bereinigt: Statusfilter, Dubletten über Teilobjekte und Pflichtfelder fehlen noch (siehe [Entwickler-Guide](ENTWICKLER.md)).
3. Für die 28 Quellenprofile gibt es noch keine direkten Downloadlinks im Index.
4. Die Links im Portalverzeichnis werden nicht automatisch auf Erreichbarkeit geprüft.
