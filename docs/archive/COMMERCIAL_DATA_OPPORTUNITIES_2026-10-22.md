# Wirtschaftlich nutzbare Daten: Funktionen, Integration und Produktpotenzial

[Repository-Übersicht](../../README.md) · [Integrationsarchitektur](../integration/ARCHITECTURE.md) · [Weiterbildung und AZAV](../education/WEITERBILDUNG_DE_AZAV.md)

**Stand: 22.10.2026.** Quellenfakten sind verlinkt. Prioritäten, Produktideen und wirtschaftliche Bewertungen sind eigene Hypothesen, keine belegten Umsatzprognosen oder Investitionsempfehlungen. Eine offene Lizenz ist immer für den konkret verwendeten Bestand zu prüfen.

## 1. Wo der wirtschaftliche Mehrwert liegt

Ein frei zugänglicher Datensatz ist noch kein verkaufsfähiges Produkt. Zahlungsrelevant kann eine wiederkehrende, aufwendige Entscheidung sein: passende Weiterbildung auswählen, eine relevante Ausschreibung erkennen, Anlagenbestände vergleichen oder eine regionale Versorgungslage verstehen. Der Mehrwert entsteht dann durch Zuverlässigkeit, verständliche Aufbereitung, Suchqualität und Integration in einen Arbeitsablauf.

Die Gegenprobe ist wichtig: Wenn dieselbe Aufgabe in einem kostenlosen Originalportal bereits einfach gelöst wird, reicht eine neue Oberfläche allein als Geschäftsmodell oft nicht. Vor dem Bau sollten echte Suchaufgaben beobachtet und der Aufwand des bisherigen Vorgehens gemessen werden. Die folgende Priorisierung ist deshalb ein Vorschlag für Tests, keine Aussage über einen bewiesenen Markt.

## 2. Vergleich der aussichtsreichen Produktfelder

| Feld | Konkrete Funktion | Denkbare Nutzer | Integrationsaufwand | Kritische Grenze |
|---|---|---|---|---|
| Weiterbildung | Kursvergleich mit Terminen, Lernform und Nachweisen | Ratsuchende, Coaches, Beratungsstellen | Mittel bis hoch; heterogene Quellen | Rechte und AZAV-Nachweisabdeckung |
| Öffentliche Vergabe | Relevanzfilter, Fristen, Änderungen und Ausschreibungs-Matching | Kleine Unternehmen, spezialisierte Dienstleister | Mittel; versionierte Bekanntmachungen | Keine Vollständigkeit aller lokalen Aufträge versprechen |
| Energieanlagen | Bestands- und Veränderungsanalysen nach Region und Technik | Projektierer, Analysten, regionale Planung | Mittel bis hoch; große Exporte | Bestand ist keine Netzanschluss- oder Absatzgarantie |
| Patente/Forschung | Themenmonitor und belegte Zusammenfassungen | Forschung, Produktentwicklung, spezialisierte Beratung | Hoch; Identitäten und Fachsprache | Kein Ersatz für Rechts- oder Fachprüfung |
| Gesundheitsinfrastruktur | Standort- und Fachbereichsvergleich | Beratung, Versorgungsplanung, Angehörige | Mittel; Datenstände und Standorte | Keine Echtzeitkapazität oder Behandlungszusage |
| Gebäude/Umwelt | Standort- und Risikoindikatoren | Immobilien- und Energieprojekte | Hoch; Geodaten und Modellunsicherheit | Einzelobjekt-Wahrheit nicht aus Modellwerten behaupten |

„Mittel“ und „hoch“ beschreiben relative Umsetzungsrisiken für einen kleinen neuen Dienst. Sie sind keine gemessenen Projektbudgets. Ein enges Thema mit gutem Datenzugang ist meist ein sinnvollerer Pilot als ein gleichzeitiger Start in allen Bereichen.

## 3. Quellen mit aktuell geprüfter Dokumentation

### 3.1 Öffentliche Ausschreibungen: TED

Die offizielle Dokumentation beschreibt `POST /v3/notices/search` für veröffentlichte Bekanntmachungen, Such- und Downloadfunktionen sowie den Zugang ohne Authentifizierung zur Search API. Kommerzielle Weiterverwender werden als Nutzergruppe angesprochen. [TED Search API](https://docs.ted.europa.eu/api/latest/search.html).

**Produktvorschlag:** Ein fachlich enger Suchdienst, der passende Aufträge nicht nur nach Schlagworten, sondern nach Leistungsart, Region, Fristen und konkreten Anforderungen vorsortiert. Berichtigungen, Verlängerungen und Aufhebungen müssen zu bereits bekannten Ausschreibungen zugeordnet werden. Ein Treffer erklärt, warum er passt und was noch unklar ist.

**Integration:** Bekanntmachungs- und Versionskennungen erhalten, Originale verlinken, Dokumente nur im zulässigen Umfang übernehmen. Datenstand und letzte Prüfung sichtbar machen. TED nicht ohne Prüfung als vollständigen Ersatz sämtlicher nationaler oder unterschwelliger Vergabequellen darstellen.

**Nachfragetest:** Reale Ausschreibungen einer kleinen Zielgruppe rückwirkend sortieren lassen. Entscheidend sind relevante zusätzliche Treffer, vermiedene Fehlalarme und gesparte Prüfzeit, nicht die bloße Anzahl versendeter Meldungen.

### 3.2 Energieinfrastruktur: Marktstammdatenregister

Das MaStR bietet den öffentlichen Datenbestand als XML-Gesamtexport an und dokumentiert einen regelmäßigen, typischerweise täglichen Export. Als Lizenz wird Datenlizenz Deutschland – Namensnennung 2.0 genannt. [Offizieller Download](https://www.marktstammdatenregister.de/MaStR/Datendownload).

**Produktvorschlag:** Regionale Bestandsberichte zu Erzeugungsanlagen, Speichern und Energieträgern oder nachvollziehbare Änderungsübersichten. Ein belastbarer Bericht trennt Leistung, Betriebsstatus, Ort und Beobachtungszeitraum.

**Integration:** Große Archive speicherbegrenzt verarbeiten, Schemaänderungen beachten und Kennungen erhalten. Einheiten nicht mit Standorten oder Betreibern gleichsetzen. Koordinatenqualität und fehlende Angaben transparent behandeln.

**Grenze:** Anlagenbestand bedeutet nicht, dass ein Anschluss verfügbar ist, ein Betreiber Kaufinteresse hat oder eine Kontaktaufnahme erlaubt ist. Der sinnvolle Mehrwert liegt zunächst in aggregierten Markt- und Standortinformationen, nicht in einer unkontrollierten personenbezogenen Lead-Liste.

### 3.3 Weiterbildung: evidenzbasierter Kursvergleich

Die [gesonderte Analyse](../education/WEITERBILDUNG_DE_AZAV.md) dokumentiert elf Quellen einschließlich tatsächlich beschriebenen Kursdatenzugängen. Besonders relevant sind Berliner VHS-Daten, Europass und die WISY-Lizenzbedingungen; mein NOW bietet eine wichtige öffentliche Fachsuche. Die Rechte und technischen Zugänge unterscheiden sich erheblich.

**Produktvorschlag:** Eine nachvollziehbare Auswahl weniger passender Angebote mit Terminen, Unterrichtsform, belegten Voraussetzungen, Quellenstand und offenen Fragen. Für Coaches kann ein exportierbares Rechercheblatt mehr Nutzen haben als eine weitere große Trefferliste. Für Ratsuchende kann ein enger, verständlicher Vergleich hilfreich sein.

**Integration:** Anbieter, Kurs, Durchführung und Nachweis getrennt modellieren. Kein allgemeines „AZAV“-Häkchen aus einem Anbieterlogo ableiten. Ein kuratierter Pilot mit echten Belegen ist wertvoller als ein großer unberechtigter Datenimport.

**Monetarisierungshypothesen:** Bezahlte Rechercheunterstützung, Teamzugang, individualisierte Vergleichsberichte oder autorisierte Anbieter-Datenpflege. Bezahlte Platzierungen müssten deutlich von der fachlichen Passung getrennt sein. Individuelle Förderentscheidungen bleiben außerhalb eines automatischen Vergleichsversprechens.

### 3.4 Patente und Forschung

OPS, PATSTAT/TIP und die aktuellen USPTO-/PatentsView-Zugänge werden in der [Fachanalyse](../patents-health/SOURCES_AND_USE_CASES.md) mit ihren Grenzen beschrieben. Für Forschung bietet OpenAlex dokumentierte öffentliche Snapshots; API-Authentifizierung und Nutzungsumfang sind gesondert geregelt. [OpenAlex-Snapshots](https://help.openalex.org/access/snapshot/), [API-Authentifizierung](https://help.openalex.org/api/authentication/).

**Produktvorschlag:** Ein enger Technologie-Monitor mit nachvollziehbarer Themenzuordnung und verständlicher Erklärung neuer Veröffentlichungen. Relevanzprüfung, Quellenqualität und Zusammenhang sind wichtiger als die Anzahl automatisch erzeugter Zusammenfassungen.

**Integration:** Metadaten und Volltexte getrennt behandeln. Rechte an einer Metadatenquelle erlauben nicht automatisch die Weiterveröffentlichung sämtlicher verlinkter Artikel. Statt einen sehr großen Bestand sofort vollständig zu spiegeln, zunächst einen zulässig bezogenen Ausschnitt und nachvollziehbare Abfragen verwenden.

**Grenze:** Eine Zusammenfassung ist keine Freedom-to-Operate-Prüfung. Ebenso ist ein Patent kein Nachweis für die Zulassung eines Medizinprodukts oder dessen tatsächliche Nutzung.

### 3.5 Gesundheitsinfrastruktur

Das amtliche Krankenhausverzeichnis und der Bundes-Klinik-Atlas liefern unterschiedliche Datenstände und Merkmale. Die [Fachanalyse](../patents-health/SOURCES_AND_USE_CASES.md) dokumentiert Download, Wiederverwendungshinweise und wichtige Sonderwerte.

**Produktvorschlag:** Ein gut gepflegter Klinik-/Reha-Wegweiser oder regionaler Versorgungsbericht. Der Bericht sollte konkrete Fragen beantworten: Welche Einrichtungen und Fachbereiche gibt es? Welche Quelle bestätigt das? Aus welchem Bezugsjahr stammen Kapazitäten?

**Integration:** Einrichtung, Träger, Standort und Fachabteilung trennen. Unterdrückte Fallzahlen nicht als null darstellen. Räumliche Auswertungen benötigen passende Gebietsstände und nachvollziehbare Bezugsgrößen.

**Grenze:** Keine aktuellen freien Therapieplätze, Wartezeiten oder Behandlungserfolge aus Bestandsdaten erfinden. Ein Verzeichnis ist kein medizinisches Beratungs- oder Qualitätsurteil.

## 4. Weitere Kandidaten aus der ursprünglichen Sammlung

Die folgenden Quellen bleiben als Recherchekandidaten erhalten. Ihre vollständigen aktuellen Lizenz-, API- und Produktbedingungen wurden in dieser Überarbeitung **nicht erneut abschließend verifiziert**. Frühere pauschale Kennzeichnungen als vollständig geprüft werden hierdurch ersetzt.

| Quelle | Ansatz für ein späteres Produkt | Noch zu prüfen |
|---|---|---|
| [ETHOS.BUILDA](https://ethos-builda.fz-juelich.de/api/v8_20240916/swagger/) | Gebäudemerkmale und energetische Struktur | Aktuelle Version, erreichbare API, Modellunsicherheit und Lizenzumfang |
| [EUBUCCO](https://eubucco.com/) | Europäische Gebäude- und Standortanalysen | Regionale Abdeckung, Quelllizenzen, aktualisierte Releases |
| [EU Building Stock Observatory](https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/eu-building-stock-observatory_en) | Gebäudestatistische Vergleiche | Aggregation, Bezugsjahre und konkrete Exportbedingungen |
| [Copernicus Data Space](https://dataspace.copernicus.eu/) | Flächen-, Vegetations- und Umweltmonitoring | Produkt, Auflösung, Quoten, Rechenaufwand und Rechte |
| [EIOPA Insurance Statistics](https://www.eiopa.europa.eu/tools-and-data/insurance-statistics_en) | Versicherungsmarkt-Dashboards | Aussageebene, Aktualisierung und Weiterverwendung |
| [Geofabrik](https://download.geofabrik.de/) | Einrichtungen und geografische Einzugsgebiete | ODbL-Anforderungen, Abdeckung und Aktualität konkreter Merkmale |
| [DWD Open Data](https://opendata.dwd.de/) | Wetterbezogene Entscheidungsunterstützung | Produktlizenz, Vorhersagegüte, räumliche Auflösung und Aktualisierung |

Für alle Kandidaten gilt: Modellierte oder aus verschiedenen Quellen kombinierte Daten müssen als solche sichtbar bleiben. Eine professionelle Oberfläche darf Unsicherheit nicht verdecken.

## 5. Geschäftsmodell zuerst als überprüfbare Hypothese formulieren

Ein nützlicher Hypothesensatz lautet: „Diese Zielgruppe erledigt diese wiederkehrende Aufgabe heute mit diesem Aufwand. Ein besser belegter Vergleich senkt den Aufwand oder vermeidet einen bestimmten Fehler. Dafür würde sie dieses konkrete Produkt testen.“ Ohne diese Präzisierung ist „wertvoller Datensatz“ noch keine Marktchance.

Mögliche Erlösformen sind ein Zugang für wiederkehrende Aufgaben, ein einzelner überprüfter Bericht, eine autorisierte Datenintegration oder ein gepflegter Export. Für Privatkunden sind Häufigkeit des Bedarfs und Zahlungsbereitschaft besonders zu prüfen; eine seltene Entscheidung trägt nicht automatisch ein dauerhaftes Abonnement. Für Unternehmen erhöhen verlässliche Prozesse und Support den Nutzen, aber auch den Betriebsaufwand.

Eine einfache Kalkulation sollte mindestens unterscheiden:

```text
monatliche Einnahmen = aktive zahlende Kunden x tatsächlich erzielter Preis
variable Kosten = Datenzugriff + Rechenaufwand + Kommunikation + Support
Fixkosten = Betrieb + Pflege + Qualitätssicherung + Administration
Deckungsbeitrag vor Fixkosten = Einnahmen - variable Kosten
```

Hier sind bewusst keine vermeintlich marktüblichen Preise oder Umsatzversprechen eingesetzt. Besonders oft unterschätzt werden manuelle Nachweisprüfung, Quelländerungen und die laufende Behandlung von Fehlern.

## 6. Entscheidungskriterien für einen Pilot

| Kriterium | Gute Ausgangslage | Warnsignal |
|---|---|---|
| Rechte | Konkreter Bestand und Nutzung sind nachvollziehbar | Nur „kostenlos im Browser“ |
| Problem | Eine klar beschriebene wiederkehrende Aufgabe | Sammlung ohne konkreten Nutzer |
| Datenqualität | Originalbelege, stabile Kennungen, sichtbarer Stand | Viele Einträge ohne Herkunft |
| Technik | Dokumentierter und erprobbarer Zugang | Undokumentierte interne API als einzige Grundlage |
| Differenzierung | Messbar bessere Entscheidung oder Zeitersparnis | Kopie einer bereits guten freien Suche |
| Betrieb | Pflege und Fehlerbehandlung sind einkalkuliert | „KI wird die Daten schon korrigieren“ |
| Vertrauen | Grenzen und bezahlte Einflüsse transparent | Unbelegte Gütesiegel oder Förderversprechen |

Die Freigabe eines Piloten sollte nicht aus einem einzigen Gesamtscore folgen. Ein schweres Rechte- oder Nachweisproblem kann ein Ausschlusskriterium sein, selbst wenn andere Faktoren attraktiv erscheinen.

## 7. Empfehlung für diese Sammlung

Für den bildungsbezogenen Anwendungsfall ist ein kleiner Kursvergleich mit Quellenbelegen der naheliegende erste Test. Für ein davon unabhängiges wirtschaftliches Experiment ist ein enges TED-Thema mit dokumentierter Schnittstelle ein prüfbarer Kandidat. Energie-, Patent- und umfangreiche Geodatenprodukte folgen erst, wenn Verarbeitung, Aktualisierung und fachliche Kontrolle tragfähig sind.

Das Repository legt dafür Grundlagen, betreibt aber noch keinen bezahlten Dienst. Der nächste fachliche Meilenstein ist ein erfolgreich geprüfter kleiner Nutzdatenimport mit nachvollziehbarer Lizenz und einem Test an realen Nutzeraufgaben – nicht die Behauptung einer sofort monetarisierbaren Vollständigkeit.
