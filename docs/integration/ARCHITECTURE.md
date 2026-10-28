# Integrationsarchitektur: vom Quellenkatalog zum nutzbaren Datenprodukt

[Übersicht](../../README.md) · [Geschäftsmodelle](../strategy/COMMERCIAL_ASSESSMENT.md) · [Kursdatenmodell](../education/COURSE_DATA_MODEL.md)

**Stand: 22.10.2026. Status: Architekturvorschlag, nicht bereitgestellte Infrastruktur.** Dieses Repository liefert Recherche, Quellenprofile und eine lokale Katalogvalidierung. Es betreibt keine produktive API, keinen Crawler, kein Kundensystem und keine regelmäßigen Datenimporte.

## 1. Vier getrennte Ebenen

| Ebene | Inhalt | Warum die Trennung wichtig ist |
|---|---|---|
| Quellenkatalog | Portale, Zugänge, Rechtehinweise, Belege | Ein Link ist noch kein nutzbarer Datensatz |
| Rohdatenbereich | Autorisiert bezogene, versionierte Originaldaten | Herkunft und Änderungen bleiben nachvollziehbar |
| Fachmodell | Bereinigte Einheiten, Termine, Standorte, Nachweise | Unterschiedliche Quellschemata werden vergleichbar |
| Produktansicht | Suche, Vergleich, Berichte, Benachrichtigungen | Nutzwert entsteht durch eine konkrete Entscheidungshilfe |

Die bestehende `data/portals.json` gehört zur ersten Ebene. Die neue `data/education_sources.json` ergänzt fachlich geprüfte Quellenbeschreibungen, nicht importierte Kurse. Die übrigen Ebenen müssen erst implementiert und geprüft werden.

## 2. Empfohlener Datenfluss

```text
Offizielle Quelle / autorisierter Anbieterfeed
    -> Rechte- und Zugriffskontrolle
    -> quellspezifischer Adapter
    -> versionierter Rohdatenstand mit Herkunft
    -> Normalisierung und Dublettenprüfung
    -> fachliche Validierung und Freigabe
    -> Suchindex / strukturierte Produktdaten
    -> Benutzeroberfläche / kontrollierte KI-Werkzeuge
```

**Rechtekontrolle vor Abruf und Veröffentlichung:** Für jede konkrete Ressource sind Herausgeber, Lizenz, Lizenzbeleg, Nutzungszweck und Zugangsbedingungen zu erfassen. „Öffentlich sichtbar“, „kostenlos herunterladbar“ und „kommerziell weiterverwendbar“ bleiben unterschiedliche Zustände. Die [Bildungsanalyse](../education/WEITERBILDUNG_DE_AZAV.md) zeigt diese Unterschiede anhand realer Quellen.

## 3. Adapter statt eines universellen Scrapers

| Quelltyp | Adapteraufgabe | Wesentliche Fehlerquelle |
|---|---|---|
| JSON/XML-Kursfeed | Felder und Kennungen abbilden, Vollständigkeit prüfen | Teillieferung wird irrtümlich als Gesamtbestand behandelt |
| RDF/JSON-LD | Begriffs-URIs, Sprachfassungen und Modellversionen erhalten | Qualifikation und buchbarer Termin werden verwechselt |
| Große XML-Exporte | Speicherbegrenztes Lesen, Schema- und Versionskontrolle | Unvollständiges Archiv oder geänderte Feldbedeutung |
| CSV/XLSX | Spaltentypen, Einheiten und Berichtsstand prüfen | Führende Nullen, Datumsformate oder Geheimhaltungscodes gehen verloren |
| Öffentliche Suchseite | Beleg und Originalverlinkung, soweit zulässig | Sichtbare Frontend-Anfrage wird als freigegebene API behandelt |
| Zertifikat/Referenz | Nachweis erfassen und fachlich überprüfen | Allgemeines Anbieterlogo wird zur Kurszulassung hochgestuft |

Adapter erhalten explizite Grenzen: erlaubte Hosts, maximale Dateigröße, zulässige Formate und dokumentierten Zugriff. Keine Umgehung von Anmeldung, Captchas oder Sperren. Bei unklaren Rechten bleibt der Datensatz in einem nicht veröffentlichten Prüfzustand oder wird gar nicht übernommen.

## 4. Importvertrag und Herkunft

Jeder Importlauf sollte ein Manifest erzeugen:

```text
import_id, source_id, resource_url
requested_at, completed_at
source_published_at, observation_period
license_id, license_url, license_observed_at
format, schema_version, adapter_version
checksum, byte_count, record_count
is_complete_snapshot, validation_result
previous_successful_import_id
```

Ein Abrufdatum beweist nicht die Aktualität der Daten. Ein Krankenhausbestand mit Bezugsjahr 2024 bleibt ein Bestand von 2024, auch wenn er 2026 heruntergeladen wird. Ebenso besagt ein HTTP-200-Ergebnis nur, dass eine bestimmte Anfrage beantwortet wurde; es bestätigt weder Lizenz noch inhaltliche Qualität.

**Löschungen:** Nur ein als vollständig validierter Gesamtstand darf fehlende Datensätze als mögliche Löschung markieren. Eine leere Antwort, ein Zeitlimit oder eine Teillieferung darf niemals den produktiven Bestand leeren. Neue Stände zunächst getrennt laden, prüfen und danach atomar freigeben. Den letzten brauchbaren Stand mit sichtbarer Altersangabe behalten.

## 5. Qualität, Aktualisierung und Betrieb

Für jeden Bestand werden eigene Erwartungen definiert: ungefährer Umfang, Pflichtfelder, erlaubte Statuswerte, plausible Zeitbereiche und bekannte Sonderwerte. Abweichungen erzeugen eine Prüfaufgabe statt einer stillen Korrektur. Inhaltliche Nachweise benötigen eine andere Prüfung als die Erreichbarkeit einer URL.

Ein vorgeschlagenes Betriebsprotokoll sollte erfassen: fehlgeschlagene Abrufe, Schemaänderungen, ungewöhnliche Bestandsrückgänge, Dublettenrate, fehlende Belege und veraltete Angaben. Wiederholungen nach Fehlern begrenzen; bei Rate-Limits die Anbieterhinweise respektieren. Geplante Aktualisierungsintervalle orientieren sich am tatsächlichen Veröffentlichungsrhythmus und nicht am Wunsch, jede Quelle täglich vollständig neu einzulesen.

Für den Start reicht häufig ein kleiner freigegebener Ausschnitt und eine einfache lokale Datenhaltung. Eine größere Serverdatenbank, Suchinfrastruktur oder Vektorsuche sollte erst aus gemessenen Anforderungen folgen. Große freie Downloads können trotzdem erhebliche Speicher-, Rechen- und Wartungskosten verursachen; das illustrieren beispielsweise die [OpenAlex-Snapshots](https://help.openalex.org/access/snapshot/).

## 6. Vorgeschlagene Produktfunktionen

Diese Funktionen sind ein Entwurf, keine bereits erreichbaren API-Endpunkte.

| Funktion | Eingaben | Ergebnis | Schutzregel |
|---|---|---|---|
| `search_sources` | Thema, Region, Zugangsart, Rechtebedarf | Quellenprofile mit Evidenz | Unbekannte Lizenz nicht als offen filtern |
| `search_offers` | Ziel, Termin, Lernform, Region | Passende freigegebene Kursdurchführungen | Nur tatsächliche Kursdaten, keine Portaltreffer als Kurse |
| `get_offer_evidence` | Kurs-ID, zu prüfendes Feld | Beleg und Prüfstatus | Kein Zertifikatsstatus ohne Nachweis |
| `compare_offers` | Auswahl von Kurs-IDs | Vergleich und offene Fragen | Unbekannte Werte sichtbar lassen |
| `get_dataset_changes` | Zwei freigegebene Versionen | Hinzugefügte, geänderte und entfallene Einträge | Teillieferungen nicht als vollständige Differenz werten |

Externe Kennungen und Beleglinks sollten in Ausgaben erhalten bleiben. Die fachliche Berechtigung zur Verwendung einer Quelle muss vor der Suche feststehen; sie ist nicht etwas, das ein Sprachmodell nachträglich erraten soll.

## 7. KI-Integration und Retrieval

Ein Sprachmodell sollte als Erklärungs- und Rechercheoberfläche dienen, nicht als Wahrheitsquelle für Datenbankfelder. Empfohlen ist eine Kombination aus strukturierten Filtern und beleggestützter Textsuche. Harte Kriterien werden deterministisch geprüft; erst danach kann die KI Ergebnisse erläutern oder thematisch ordnen.

Eine Antwort enthält: Ergebnis, verwendete Quellen, Beobachtungsstand, geprüfte Eigenschaften und offene Punkte. Bei widersprüchlichen Angaben nennt sie den Widerspruch. Für jede Aussage über Förderung, Zulassung, Kosten oder Termin muss ein zugänglicher Beleg existieren. Fehlende Nachweise werden nicht aus ähnlichen Kursen oder allgemeinen Anbieterbeschreibungen ergänzt.

**Schutz vor fremden Anweisungen:** Webseiten, Beschreibungen und heruntergeladene Dateien sind Daten, keine Arbeitsanweisungen. Sie dürfen keine Geheimnisse abfragen, Rechte ändern oder neue Netzaufrufe außerhalb der freigegebenen Hosts auslösen. Ausgaben und URLs vor Verwendung in Tools validieren; interne Netzwerkziele und unerwartete Weiterleitungen blockieren.

## 8. Datenschutz und Zugang

Dieses Repository enthält keine Teilnehmerprofile, Beratungsakten oder Zugangsdaten. Personenspezifische Informationen müssten in einer späteren Anwendung getrennt, zweckgebunden und mit eigenen Berechtigungen behandelt werden. Ein Kursvergleich benötigt nicht automatisch Diagnosen; freiwillig genannte funktionale Anforderungen lassen sich oft getrennt verarbeiten.

`AGENTS.md` beschreibt Arbeitsregeln; `llms.txt` ist lediglich eine zusätzliche Navigationshilfe. Keine der Dateien räumt Rechte an den beschriebenen Fremdquellen ein oder garantiert eine automatische Indexierung. Die Lizenz dieses Repositorys ist in [LICENSE](../../LICENSE) beschrieben.

## 9. Pilot und Abnahmekriterien

Ein sinnvoller erster Pilot umfasst einen kleinen lizenzierten Bestand, dokumentierte Feldzuordnung, überprüfbare Originalbelege und eine einfache Vergleichsansicht. Er wird mit realen Suchaufgaben getestet, ohne bereits eine vollständige bundesweite Abdeckung zu behaupten.

Vor einer Erweiterung sind mindestens folgende Fragen zu beantworten: Stimmen die Ergebnisse mit den Originalquellen überein? Werden Unbekanntes und Widersprüche sichtbar? Bleibt ein unvollständiger Import ohne Datenverlust? Lassen sich Aussagen auf einen konkreten Datenstand zurückführen? Ist die Quellenlizenz mit der vorgesehenen Veröffentlichung vereinbar?

Die mitgelieferte lokale Validierung prüft ausschließlich das Format und grundlegende Konsistenzregeln der Bildungsquellen. Ein erfolgreicher Test bestätigt keine Erreichbarkeit externer Portale, keine rechtliche Freigabe und keine AZAV-Zulassung.
