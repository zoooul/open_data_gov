# Directory-Projekte mit belegtem Ausgangsbestand

[README](../../README.md) · [Maschinenlesbare Auswahl](../../data/verified_directory_projects.json) · [Frühere Ideenanalyse: nur Archiv](../archive/DIRECTORY_PROJECT_PRIORITIES_2026-10-22.md)

**Prüfstand: 23.10.2026.** Diese Auswahl ersetzt die frühere allgemeine Rangfolge für den konkreten Auftrag: ein einfaches Directory, keine vorrangige SaaS-Anwendung, mit einem Ausgangsbestand von mindestens 1.000 passenden Einheiten. Die sechs Projekte besitzen belegte Quellenmengen, dokumentierte Inhalte über eine reine Adresse hinaus und einen ausgewiesenen offenen Lizenzweg. Daraus folgt noch keine Freigabe von 1.000 fertig aufbereiteten Profilseiten.

## 1. Ergebnis: sechs konkrete statt fünfzig spekulative Ideen

| Rang | Abgegrenztes Projekt | Belegte Menge | Was genau gezählt ist | Nachweisart |
|---|---|---:|---|---|
| 1 | Badegewässer Deutschland | 2.291 | Gemeldete Badegewässer, Saison 2025 | Amtliche Zahl zur konkret ausgewählten Datensatzperiode |
| 2 | Museen mit der Bezeichnung « Musée de France » | über 1.200 | Museen des Muséofile-Verzeichnisses | Herausgeberangabe zum Datensatz |
| 3 | Schulen in Nordrhein-Westfalen | 5.418 | Öffentliche und private Ersatzschulen, Schuljahr 2025/26 | Amtliche Population; laufender Export noch abzugleichen |
| 4 | Lebensmittelbetriebe in Westminster | 5.779 | Betriebe im angebotenen FSA-Gebietsexport | Herausgeberzahl am konkreten Download |
| 5 | Forschungsnahe Organisationen in Deutschland | 5.878 | Deutschland-Facette der aktiven ROR-API-Ergebnismenge | Tatsächlich gelesene JSON-Antwort |
| 6 | Historischer Denkmalatlas Frankreich | 45.080 | Geschützte unbewegliche Güter am 01.01.2024 | Amtlicher historischer Bezugsbestand; keine aktuelle CSV-Zeilenzahl |

Die Quellen und Rechtebelege stehen jeweils im folgenden Profil und zusätzlich im JSON. Frankreich und Westminster sind ausdrücklich keine deutschen Bestände. Die Zahlen sind nicht addierbar, um eine gemeinsame Websitegröße zu versprechen. Eine Zahl wie « über 1.200 » wird nicht in eine scheinbar exakt gezählte 1.200 umgewandelt.

**Meine redaktionelle Startauswahl:** Für ein deutsches Verbraucherprojekt Badegewässer; bei Offenheit für einen französischen Reisemarkt Museen; für ein regionales Bildungsverzeichnis NRW-Schulen. Die übrigen drei sind Alternativen mit schwächerer Passung zum Wunsch nach unkompliziertem Verbrauchertraffic oder höherem Pflegeaufwand. Diese Bewertung ist eine eigene Einschätzung, keine erhobene Nachfrageanalyse.

## 2. Was jetzt belegt ist und was nicht

Die **Bestandsstufe** verlangt eine konkrete Quelle, einen abgegrenzten Markt, mindestens 1.000 Einheiten in diesem Bezugsraum, dokumentierte fachliche Merkmale und einen passenden Lizenzbeleg. Eine bloße Vermutung aufgrund der Marktgröße genügt nicht. Quellenberichte und API-Zählwerte werden nicht als eigene Vollzählung ausgegeben.

Die strengere **Veröffentlichungsstufe** verlangt anschließend einen tatsächlichen Import, eindeutige Identitäten, Dublettenprüfung, ausreichende Pflichtfelder, passende Aktualität und eine wiederholbare Pflege. Dieser Mindeststandard wird nicht abgesenkt. Aktuell gilt bei allen sechs Projekten: `full_import_tested: false`, `qualified_entry_count: null`, `launch_ready: false`.

Eine Ausnahme in der Prüftiefe ist ROR: Dort wurden JSON-Beispielobjekte und die Länderfacette gelesen, aber nicht sämtliche deutschen Datensätze importiert. Die anderen Mengen stammen aus Herausgeberangaben oder amtlichen Statistiken. Die in dieser Laufzeit nicht gelungenen Dateiabrufe beweisen keinen Ausfall beim Anbieter. Weder die Existenz eines CSV-Links noch ein bestandener Metadatentest ist ein Integrationstest.

## 3. Badegewässer Deutschland

**Beleg:** Das [EEA-Länderblatt Deutschland 2025](https://www.eea.europa.eu/en/topics/in-depth/bathing-water/state-of-bathing-water/bathing-water-country-factsheets-2025/de-bathing-water-country-factsheet-2025.pdf/@@download/file) nennt 2.291 gemeldete Badegewässer. Die [konkrete Datenveröffentlichung 2025 v1.0](https://sdi.eea.europa.eu/catalogue/datahub/api/records/070d9baa-448d-4168-8514-7dadb3ad876d) dokumentiert Excel, den Zeitraum bis 2025, Veröffentlichung am 02.06.2026 und CC BY 4.0. Die [offizielle Karte](https://www.eea.europa.eu/en/analysis/maps-and-charts/state-of-bathing-waters-in-2025) dient der gewässerbezogenen Qualitätsinformation.

**Schlanker Entwurf:** Ein Profil pro Badegewässer, verständliche historische Qualitätskategorie, Jahresverlauf soweit im Export vorhanden, Originalquelle und regionale Navigation. Eine Suchseite soll beispielsweise beantworten, welches gemeldete Gewässer gemeint ist und aus welcher Saison die Information stammt.

**Nicht im MVP versprechen:** heutige Badetauglichkeit, aktuelle Blaualgenlage, erlaubte Hunde, Parkplätze, Toiletten oder Rettungsdienst. Diese Angaben benötigen weitere Quellen. Historische Qualität wird nicht zu einer aktuellen Sicherheitszusage.

**Eigene Geschäftsmodellhypothese:** Kennzeichnete Reise-/Unterkunftsverweise und passende Outdoor-Angebote. Saisonabhängigkeit ist ein Risiko: ein Start im Oktober bedeutet keinen unmittelbaren Sommertraffic. Ein regionales Partnerwidget wäre eine spätere B2B2C-Option, nicht Teil des einfachen ersten Directorys.

## 4. Museen in Frankreich

Die [aktuelle Muséofile-Datensatzseite](https://www.data.gouv.fr/datasets/musees-de-france-base-museofile) nennt über 1.200 Museen und beschreibt unter anderem Kennung, Namen, Kontakt, Ort, Sammlungsthemen, Geschichte, besondere Künstler und Aktualisierungsdatum. Sie weist Licence Ouverte 2.0 aus. Die [offizielle Katalog-API](https://www.data.gouv.fr/api/1/datasets/musees-de-france-base-museofile/) verweist auf den [CSV-Export](https://ministere-culture.s3.sbg.io.cloud.ovh.net/POP/museofile.csv). Die ältere Liste mit einem anderen Datensatztitel ist archiviert und nicht der hier bevorzugte Einstieg.

**Schlanker Entwurf:** Museen nach Ort und tatsächlich angegebenem Sammlungsthema, Detailseiten mit eigenständig formulierter Zusammenfassung und direktem Link zur Institution. Kein Buchungssystem, keine Nutzerkonten und keine erfundenen Bewertungen.

**Stärke meiner Einschätzung:** Die dokumentierten beschreibenden Merkmale ermöglichen mehr eigenständigen Nutzen als eine Liste mit Name und Anschrift. Französischsprachige Seiten oder sorgfältig redigierte deutsche Reiseseiten sind denkbar; unkontrollierte KI-Übersetzung ist kein Qualitätskonzept.

**Grenzen:** Nicht alle Museen müssen aktuell besuchbar sein. Eintrittspreise, Öffnungszeiten und Bildrechte sind nicht pauschal bestätigt. Ticket- und Unterkunftsprovisionen sind mögliche, noch nicht vertraglich belegte Erlöswege.

## 5. Schulverzeichnis Nordrhein-Westfalen

Die [amtliche Schulstatistik 2025/26](https://www.schulministerium.nrw/system/files/media/document/file/statistiktelegramm-2025_0.pdf), Tabelle auf PDF-Seite 7, weist 5.418 Schulen aus, davon 2.817 Grundschulen. Die Population umfasst öffentliche Schulen und private Ersatzschulen, nicht alle denkbaren Bildungseinrichtungen.

Das [Schulministerium dokumentiert offene Schuldaten](https://www.schulministerium.nrw/open-data) mit täglichem CSV/XML-Export unter Datenlizenz Deutschland – Namensnennung 2.0. Enthalten sind unter anderem Schulnummer, Schulform, Anschrift, Kontakte, Website, Träger, Rechtsform, Koordinaten und Betriebsstatus. [CSV](https://www.schulministerium.nrw.de/BiPo/OpenData/Schuldaten/schuldaten.csv) · [XML](https://www.schulministerium.nrw.de/BiPo/OpenData/Schuldaten/schuldaten.xml).

**Schlanker Entwurf:** Öffentliche Profile mit Schulform, Ort und Kontakt; eine verständliche Orientierung zwischen Schulformen. Die Statistik ist nicht die Zählung des tagesaktuellen Exports. Betriebsstatus und Erfassungsumfang beim Import abgleichen. Die Grundschulen sind ein Teilbestand desselben Projekts, keine zusätzlich gezählten 2.817 unabhängigen Einträge.

**Geschäftshypothese:** Deutlich getrennte Nachhilfe-/Lernangebote oder regionale Sponsoren. Ein Arbeitgeber-/Relocation-Partner wäre eine spätere Option. Keine gekaufte Schulrangliste, keine Aufnahmeprognosen und keine Schülerdaten. Die Monetarisierung halte ich für weniger unmittelbar als den bloßen lokalen Suchnutzen.

## 6. Lebensmittelbetriebe Westminster

Die [FSA-Downloadseite](https://ratings.food.gov.uk/open-data) weist für Westminster am 23.10.2026 um 12:37 **5.779 Betriebe** aus und verlinkt deren [XML-Datei](https://ratings.food.gov.uk/api/open-data-files/FHRS533en-GB.xml). Die dokumentierte API liefert XML/JSON ohne erforderliche Registrierung. Angaben umfassen Betriebsart, Name, amtliche Kennung, Adresse soweit öffentlich, Inspektionsbewertung und Datum. Die [Nutzungsbedingungen](https://ratings.food.gov.uk/terms-and-conditions) verweisen auf die Open Government Licence.

**Schlanker Entwurf:** Ein englischsprachiges lokales Verzeichnis mit verständlich erklärter, datierter amtlicher Bewertung. Restaurants, Geschäfte, Hotels und andere Betriebsarten sind getrennte Filter; 5.779 ist nicht die Anzahl reiner Restaurantprofile.

**Pflegegrenze:** Der Anbieter verlangt die Verwendung aktueller Bewertungen oder die Angabe des Aktualisierungsdatums. Logo und Bewertungsbilder haben zusätzliche Bedingungen. Manche privaten Anschriften sind unterdrückt. Weder Qualität des Essens noch heutige Betriebssicherheit aus einer vergangenen Kontrolle ableiten.

**Geschäftshypothese:** Passende Buchungs-/Serviceverweise und erkennbare lokale Sponsoren. Das kostenlose amtliche Suchangebot ist ein starker Vergleichsmaßstab. Keine Manipulation offizieller Bewertungen durch Bezahlung. Als schneller Start ist eine einzelne eindeutig gezählte Behörde sinnvoller als ein sofortiger UK-Vollimport.

## 7. Forschungsnahe Organisationen Deutschland

Die tatsächlich gelesene [ROR-API-Antwort](https://api.ror.org/v2/organizations) enthält unter `meta.countries` für `id=de` den Wert **5878**. Die Standardabfrage bezieht sich auf aktive Registereinträge. Namen, Organisationstypen, Orte, Webseiten, Beziehungen und externe Kennungen sind in den Beispielobjekten vorhanden. Die [Dump-Dokumentation](https://ror.readme.io/docs/data-dump) bestätigt CC0 sowie JSON/CSV-Gesamtveröffentlichungen.

**Schlanker Entwurf:** Organisationsprofile mit Ort, Typ, offiziellen Links und transparenten Beziehungen. Für eine vollständige Länderwahl einen fixierten Dump nutzen: Die [Filterdokumentation](https://ror.readme.io/docs/api-filtering) warnt vor fehlenden oder doppelten Ergebnissen bei reiner Filterpaginierung.

**Grenzen:** Keine 5.878 Universitäten oder bereits qualifizierten Labordienstleister behaupten. ROR enthält gemischte Organisationstypen. Registerstatus ist kein eigener Vor-Ort-Betriebsnachweis; GeoNames-Koordinaten können Stadtmittelpunkte sein. Leistungsangebot und Kooperationsbereitschaft stehen nicht automatisch fest.

**Meine Priorisierung:** Technisch gut strukturierter Ausgangsbestand, jedoch eher B2B-Spezialverzeichnis als schnelle Verbraucherreichweite. Vermittlungs- und Sponsoringideen erst nach Prüfung einer konkreten Zielgruppe verfolgen.

## 8. Historischer Denkmalatlas Frankreich

Das [Kulturministerium](https://www.culture.gouv.fr/thematiques/monuments-sites/interventions-demarches/proteger-un-objet-un-immeuble-un-espace/proteger-des-immeubles-au-titre-des-monuments-historiques) nennt **45.080 geschützte unbewegliche Güter zum 01.01.2024**. Die [Mérimée-Veröffentlichung](https://www.data.gouv.fr/datasets/immeubles-proteges-au-titre-des-monuments-historiques-2) umfasst aktuelle und ehemalige Schutzobjekte; CSV/GeoJSON, Licence Ouverte 2.0, historische Beschreibungen, Datierungen, Typen, Schutzangaben, Orte und teils Koordinaten sind dokumentiert. [CSV](https://ministere-culture.s3.sbg.io.cloud.ovh.net/POP/merimee.csv).

**Schlanker Entwurf:** Ein historisch-architektonischer Atlas nach Ort und Epoche. Die Zahl ist ausdrücklich ein historischer Bezugsbestand und nicht die heutige CSV-Zeilenzahl. Schutzakten, Teilobjekte und Ensembles müssen sauber verknüpft werden.

**Kein zulässiger Kurzschluss:** 45.080 bedeutet weder 45.080 heute offene Sehenswürdigkeiten noch 45.080 Burgen. Öffentliche Zugänglichkeit, Eintritt und Bildrechte sind eigene Fragen. Als dritte Reisekategorie neben allen Orten beliebig skalieren würde den Nutzen nicht automatisch erhöhen.

**Geschäftshypothese:** Reise-/Unterkunftsverweise und kulturelle Partnerschaften. Ich würde dieses Projekt wegen größerem Import und höherem redaktionellem Aufwand hinter das Museumsverzeichnis stellen.

## 9. Aus der aktuellen Empfehlung ausgeschieden

| Alter oder zusätzlich geprüfter Ansatz | Warum aktuell nicht als bestandsgeprüfter Schnellstart empfohlen |
|---|---|
| Entsorgungsfinder aus dem Münchner Beispiel | Nur 12 Standorte im früher gelesenen Auszug, generischer Name, keine strukturierten Annahmebedingungen. Kein Beleg für 1.000 ausreichend beschriebene Profile. |
| Deutsche Esoterikläden oder Hypnosetherapeuten | Keine belastbare deutsche Menge und Feldabdeckung ermittelt. |
| Tarot, Hermetik, einzelne Hypnoseexperimente | 78 Bilder, 289 Titel oder 52 Versuchspersonen sind keine 1.000 Verzeichnisobjekte. |
| AZAV-/Weiterbildungsportal | Große Suchportale ersetzen keinen geklärten Bulkzugang und keine Maßnahmebelege. |
| Ladepausen mit Restaurant oder barrierefreiem WC | Ladepunktzahlen zählen technische Anschlüsse, nicht die gewünschte qualifizierte Standortnische. |
| Allgemeine Tourismusplattform aus DATAtourisme | Sehr großer offener Gesamtbestand, aber gemischte Orte, Angebote und Ereignisse; keine gezählte enge Startnische in dieser Prüfung. |
| Bäderleben | Angezeigte große Menge, aber die gelesenen Bedingungen belegen keine pauschale offene Lizenz am vollständigen Datenbestand. |
| Bibliotheksverzeichnis aus lobid-organisations | Die gelesenen [Herausgebermetadaten](https://github.com/hbz/lobid-organisations/blob/cd31fa40882165bad06754fc7b57db08865fcae5/conf/dataset.jsonld) nennen ausdrücklich nicht vollständig offen lizenzierte Quelldaten. CC0 anderer Bibliotheksstatistiken darf nicht übertragen werden. |
| CQC, Atout-France-Unterkünfte, OpenPlaques | Interessante Zugänge, aber kein passender belastbarer Teilbestandszählwert in dieser Prüfung. Nicht aufgrund von Dateigröße oder Downloadzählern aufnehmen. |
| Breites Krankenhaus-/Rehaverzeichnis | Weiterhin Forschungsquelle; die konkrete importierte, aktuelle und feldqualifizierte Startmenge ist nicht gezählt. Nicht als Psychosomatik-/Begleitkind-Nische ausgeben. |

Ausscheiden bedeutet hier **fehlender Nachweis für diesen konkreten Startauftrag**, nicht ein allgemeines Urteil über Wert oder Rechtmäßigkeit der Quelle. Die früheren 20 Ideen bleiben im Recherchearchiv; ihre alten Prioritäten sind keine aktuelle Empfehlung.

## 10. Umsetzung und wirtschaftliche Prüfung

Als eigene Umfangsentscheidung für ein kleines Projekt: Importskript, einfache Volltext-/Filtersuche, ein Profiltemplate, ausgewählte regionale Übersichten, Quellen-/Datumsanzeige und Korrekturkontakt. Karten, Nutzerkonten, Bewertungscommunity, Liveauskünfte, automatische Beratung und aufwendige Partnerintegrationen zunächst weglassen. Die gewünschte Drei-Wochen-Grenze bleibt ein Planungsziel, keine überprüfte Lieferzusage.

Vor Veröffentlichung eine Stichprobe und dann den ganzen gewählten Bestand messen: stabile IDs, Dubletten, Mindestfelder, veraltete Datensätze und tatsächlich publishbare Profile. Wenn nach Prüfung weniger als 1.000 geeignete Objekte bleiben, nicht mit Keywordkombinationen auffüllen. Ein kleineres ehrliches Projekt oder eine andere Quelle ist dann die bessere Entscheidung.

SEO-Fragen und monetäre Ideen im JSON sind Hypothesen. Es wurden keine Suchvolumina erhoben, keine Affiliate-Verträge geprüft und keine kurzfristigen Erträge zugesichert. Bestehende amtliche Angebote sind Wettbewerb; Quellenkopien allein sind kein Unterschied. Mehr als 1.000 Datensätze rechtfertigen nicht automatisch mehr als 1.000 indexierte Seiten. [Google: hilfreiche Inhalte](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [Spamrichtlinien](https://developers.google.com/search/docs/essentials/spam-policies).

## 11. Technische Kontrolle des Katalogs

```bash
python scripts/validate_verified_directories.py
python -m unittest discover -s tests -p 'test_verified_directories.py' -v
```

Die neuen 14 Offline-Tests prüfen unter anderem Menge, Einheiten, Quellen-/Lizenzverweise und unzulässige Behauptungen eines fertigen Imports. Sie sind keine Prüfung von Webseiten, Lizenzwirksamkeit, Feldfüllung oder medizinischer Eignung. Die vorhandenen Bildungstests wurden in diesem Schritt nicht erneut ausgeführt und bleiben unverändert.
