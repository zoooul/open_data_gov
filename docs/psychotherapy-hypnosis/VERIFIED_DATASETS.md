# Psychotherapie und Hypnose: verifizierte Datenquellen und Projektansätze

[Repository](../../README.md) · [Quellenprofile](../../data/psychotherapy_sources.json) · [Vier neue Projektideen](../../data/psychotherapy_projects.json) · [Gesamtkatalog](../../data/project_catalog.json)

**Prüfstand: 23.10.2026.** Verifiziert werden jeweils konkrete Eigenschaften: Existenz, Beschreibung, Lizenzhinweis oder eine ausdrücklich genannte Menge. Das ist keine pauschale Freigabe sämtlicher Inhalte und kein medizinischer Wirksamkeitsnachweis. Hypnoseforschung wird hier als eigenständiges Forschungsgebiet behandelt, nicht als Unterkategorie der Esoterik.

## 1. Ergebnis für ein eigenes Datenprodukt

Für **Psychotherapiestudien, Forschungsmetadaten, bestimmte wissenschaftliche Volltexte und einzelne Hypnoseexperimente** gibt es nutzbare offene Quellen. Für ein aktuelles, vollständiges deutsches Register aller approbierten Psychotherapeuten, kassenzugelassenen Praxen oder qualifizierten Hypnosetherapeuten wurde dagegen in dieser Prüfung kein offen lizenzierter Gesamtbestand bestätigt.

Daher zwei unterschiedliche Vorhaben planen: Ein Praxisverzeichnis braucht belegte Standorte und Qualifikationen; ein Forschungsnavigator braucht Studien, Publikationen, Methoden und nachvollziehbare Quellen. Eine Studienliste ist keine Therapeutenliste. Versuchspersonen sind keine öffentlich zu profilierenden Klienten. Aus offenen Forschungsdaten entstehen nicht automatisch 1.000 sinnvolle lokale SEO-Seiten.

**Empfehlung als eigene Produktbewertung:** Zunächst einen eng gefassten deutschsprachigen Forschungs- und Evidenznavigator prüfen. Für ein Praxisverzeichnis können rechtmäßig nutzbare Praxisstandorte separat ergänzt werden. Kein automatisches Therapieempfehlungs- oder Heilungsversprechen daraus ableiten.

## 2. Übersicht: neun Profile mit unterschiedlichen Einheiten

| Profil | Datenart | Bestätigte Menge | Rechte-/Zugangsstatus |
|---|---|---|---|
| Metapsy Depression, Psychotherapie vs. Kontrolle | Studienmerkmale und aggregierte Effektdaten | **480 Studien** laut Metadatei des geprüften Git-Stands | ODC-By 1.0 dokumentiert; CSV, R und JSON-API |
| Metapsy stationäre Depression | Studienmerkmale und Effektdaten | **34 Studien** laut Metadatei | ODC-By 1.0; mögliche Überschneidung mit anderen Teilbeständen |
| Metapsy PTBS | Randomisierte Studien psychologischer Interventionen | Keine Zahl bestätigt | ODC-By 1.0 dokumentiert |
| OpenNeuro ds004572 | Experimentelle Hypnose-/EEG-Daten | **52 Teilnehmende in einem Experiment** | Datensatzbeschreibung nennt CC0 |
| PsychArchives | Forschungsobjekte, Tests, Materialien, Datensätze | Themenbezogene Zahl nicht erhoben | Metadaten CC0; Dateien mit eigenen Lizenzen und Sharing Levels |
| PMC Open Access Subset | Wissenschaftliche Volltexte | Themenbezogene Zahl nicht erhoben | Artikelbezogene Lizenzen; nicht alles kommerziell nutzbar |
| AACT / ClinicalTrials.gov | Studienregister, Protokoll- und Ergebnisangaben | Keine Hypnose-/Psychotherapie-Trefferzahl bestätigt | Öffentlicher Zugang dokumentiert; Nutzungsrechte hier nicht vollständig verifiziert |
| OpenStreetMap Psychotherapiepraxen | Praxisstandorte und teilweise Kontaktdaten | Deutschlandbestand nicht gezählt | ODbL; keine automatische Qualifikationsprüfung |
| AnnoMI | Annotierte MI-Demonstrationsgespräche | **133 Demonstrationen** laut Herausgeber | Öffentlich verfügbar; keine eigenständige Datensatzlizenz im geprüften Repository gefunden |

Die Mengen dürfen **nicht addiert** werden. Die drei Metapsy-Profile sind Teilbestände einer Infrastruktur. Eine Effektzeile ist nicht zwingend eine unabhängige Studie. Die 52 Versuchspersonen und 133 Demonstrationen sind weder Einrichtungen noch qualifizierte Verzeichnisprofile.

## 3. Metapsy: unmittelbar passende strukturierte Psychotherapiedaten

Die Depression-Dokumentation beschreibt Studieninformationen, Effektgrößen und Verzerrungsrisiken für Vergleiche von Psychotherapie mit Kontrollbedingungen. Sie nennt **ODC-By 1.0**. Diese Datenbanklizenz ist von der MIT-Lizenz des R-Zugriffspakets zu unterscheiden. Die Lizenzzusammenfassung erlaubt Nutzung, Weitergabe und Bearbeitung unter Namensnennungs- und Hinweispflichten. [S1, S2, S3]

Die gelesene Datei `metadata/number_studies.txt` des Depression-Repositorys nennt **480**. Der fixierte Commit ist `ceeabb718db4a8ed6d5c5e265262d6ed7a392b72`; dessen `metadata/last_search.txt` nennt **2024-01-01**. Das ist der dokumentierte Suchstand dieses Snapshots, nicht der Nachweis einer vollständig aktuellen Gesamtschau im Oktober 2026. Die Zahl wurde aus Herausgebermetadaten übernommen, nicht durch eigene CSV-Deduplizierung errechnet. [S4]

Der stationäre Teilbestand nennt **34 Studien**. Er enthält unterschiedliche Vergleichstypen und mehrere Berechnungsarten innerhalb von Studien; eine Zeilenzählung wäre daher besonders irreführend. Die Dokumentation weist auf möglicherweise neuere interne Versionen hin. [S5]

Für PTBS ist ein weiterer Teilbestand dokumentiert, der auf einer Datenbank des US National Center for PTSD beruht. Auch hier gilt laut Metapsy-Dokumentation ODC-By 1.0. Die Originaldatenbank und der Metapsy-Ausschnitt sind keine unabhängigen Mengen, die ungeprüft zusammengezählt werden dürfen. Eine aktuelle Zahl dieses Teilbestands wurde nicht bestätigt. [S6]

**Integration:** CSV und Metadaten versioniert beziehen; Studien-ID, DOI, Population, Intervention, Vergleich, Outcome, Zeitpunkt, Effektmaß und Unsicherheit getrennt halten. Die dokumentierte JSON-API verwendet `list_data` und `get_data`, benötigt keine Authentifizierung und bittet möglichst um höchstens eine Anfrage pro Minute. Der API-Nutzdatenabruf gelang in dieser Prüfung nicht; ein vollständiger Import wurde nicht durchgeführt. [S7]

**Eigene Anwendungsideen:** Ein recherchierbares Studienverzeichnis, ein Methodenvergleich mit fachlicher Einordnung oder Literaturberichte für Fortbildungsinstitute. Eine Rangliste „beste Therapie“ allein aus einzelnen Effektgrößen wäre keine sachgerechte Anwendung. Unterschiedliche Populationen, Kontrollen und Messzeitpunkte benötigen fachliche Bewertung. Der Betreiber empfiehlt für neue Forschungsprojekte die Kontaktaufnahme; diese Empfehlung nicht mit einer pauschalen zusätzlichen Lizenzpflicht gleichsetzen.

## 4. OpenNeuro: ein konkreter offener Hypnose-Datensatz

**Titel:** The effects of sham hypnosis techniques. **Kennung:** `ds004572`. Die Datensatzbeschreibung nennt BIDS 1.6.0, CC0 und den DOI `10.18112/openneuro.ds004572.v1.3.2`. Das README berichtet **52 Teilnehmende** und vier experimentelle Bedingungen aus konventioneller bzw. unkonventioneller Induktion und unterschiedlicher Beschreibung der Technik. [S8]

Die zugehörige Publikation beschreibt gesunde Erwachsene und eine explorative Untersuchung EEG-bezogener Merkmale subjektiver Hypnosetiefe. Das ist **kein klinischer Wirksamkeitsdatensatz für eine konkrete psychische Erkrankung** und keine fertige Diagnosefunktion. [S9]

**Prüftiefe:** README und JSON-Datensatzbeschreibung wurden tatsächlich gelesen. Roh-EEG und individuelle Teilnehmerdaten wurden nicht heruntergeladen oder in dieses Repository kopiert. Publikation und README unterscheiden sich in technischen Angaben zu Haube bzw. Kanalzahl; vor einer Reanalyse die tatsächlichen BIDS-Aufzeichnungsmetadaten prüfen und hier keine ungesicherte Montage behaupten.

**Eigene Anwendungsideen:** Forschungsdatenfinder, nachvollziehbare Lehrbeispiele oder Reproduzierbarkeitsarbeit. Für ein großes Branchenverzeichnis ist dies ein Quellenprofil mit 52 Versuchspersonen, nicht 52 Hypnoseangebote. Eine offene Urheberrechtslizenz ersetzt weder die Prüfung eines konkreten Forschungszwecks noch die Verantwortung für personenbezogene Daten. Keine Re-Identifizierung versuchen.

## 5. PsychArchives: besonders relevant für deutschsprachige Psychologie

PsychArchives ist ein disziplinäres Forschungsrepositorium mit unter anderem Artikeln, Forschungsdaten, Code, Tests und Materialien. Laut eigener Richtlinie stehen die **Objektmetadaten unter CC0**. Für Dateien gelten hingegen die konkret zugewiesenen Lizenzen und Zugangsmodelle. Selbst innerhalb eines Objekts können Daten und Codebuch unterschiedliche Rechte haben. [S10]

Public Use Files der Levels 0/0+ sind von Scientific Use Files zu trennen. Letztere sind kein automatisch freigegebener kommerzieller Trainingskorpus. Auch ein öffentlich sichtbarer Titel belegt noch keinen offenen Rohdatendownload. Die Website weist zudem auf Überlastung durch automatisierte Zugriffe hin; es wurde kein Massencrawl durchgeführt.

**Eigener Integrationsvorschlag:** Zunächst DOI, Titel, Sprache, Objekttyp, Themenbezug, Rechtehinweis und Zugangslevel indexieren. Ein Rechtefilter kann Nutzern helfen, tatsächlich verwendbare Materialien zu finden. Erst danach und nur im belegten Umfang Dateien übernehmen. Keine Zahl aller Hypnose- oder Psychotherapiedatensätze bestätigt.

## 6. PMC Open Access Subset: Volltexte mit Lizenzfilter

PMC stellt einen offenen Teilbestand wissenschaftlicher Volltexte bereit, aber **nicht alle PMC-Artikel sind zur Wiederverwendung freigegeben**. Rechte unterscheiden sich artikelweise; kommerziell nutzbare Lizenzen, nichtkommerzielle Bedingungen und Sonderbedingungen sind getrennt zu behandeln. Eine ND-Lizenz kann trotz erlaubter kommerzieller Verbreitung gerade für veröffentlichte Übersetzungen oder Bearbeitungen ungeeignet sein. [S11]

**Aktueller technischer Hinweis:** Der alte PMC OA Web Service ist seit **25.08.2026** nicht mehr verfügbar. Die aktuelle Dokumentation verweist auf Cloud Service, OAI-PMH, E-Utilities und BioC. Alte Anleitungen für `oa.fcgi` oder frühere Bulk-Verteilungen nicht ungeprüft übernehmen. [S12]

**Eigener Integrationsvorschlag:** Thematische Suchstrategie festlegen, PMCID/PMID/DOI abgleichen, Lizenz und Version speichern, danach zulässige Volltexte beziehen. Retractions, Korrekturen und Expressions of Concern müssen sichtbar werden. Ein Studienregistereintrag, ein Preprint und ein systematischer Review sind verschiedene Evidenztypen.

**Nutzen:** Fachlich geprüfte, quellengestützte Recherche und Zusammenfassungen. Keine aktuelle Zahl lizenzgeeigneter Hypnose-/Psychotherapievolltexte ermittelt; globale Millionenbestände sind dafür keine Ersatzangabe. Es wurde kein Volltextkorpus importiert.

## 7. AACT / ClinicalTrials.gov: Studienmonitor statt Anbieterregister

AACT beschreibt eine täglich aktualisierte relationale Aufbereitung des ClinicalTrials.gov-Registers mit Protokoll- und Ergebnisdaten. Die aktuelle Einstiegsseite sieht ein Konto für Cloud-Zugang und Downloads vor und beschreibt SQL sowie historische Snapshots. [S13]

**Verifikationsgrenze:** Eine Themenabfrage der ClinicalTrials.gov-API lieferte hier keinen erfolgreich auswertbaren Payload. Die Nutzungsbedingungen waren in der verfügbaren Ansicht nicht vollständig lesbar. Deshalb werden weder eine aktuelle Trefferzahl noch eine pauschale kommerzielle Wiederverwendungsfreigabe behauptet. Der Datensatz wird als **verifizierter öffentlicher Recherchezugang mit noch zu prüfenden Nutzungsbedingungen** geführt, nicht als uneingeschränkt freigegebener Korpus. [S14]

**Eigene Anwendungsidee:** Ein Hypnose-Studienradar mit Registrierungsdatum, Design, Rekrutierungsstatus, Land und Publikationsverknüpfung. Suchwörter wie `hypnosis`, `hypnotherapy` und `psychotherapy` wären Ausgangspunkte, aber keine validierten systematischen Suchstrategien. Deutschlandbezug erfordert eine geeignete Standortfilterung; Freitext allein reicht nicht.

Registrierung bedeutet weder positive Wirksamkeit noch freie Therapieplätze. Ein rekrutierendes Forschungszentrum ist keine ohne Weiteres übernehmbare Praxisempfehlung. Kontakte aus dem Register nicht als Werbeadressliste nutzen.

## 8. OpenStreetMap: der passendere Baustein für Praxisstandorte

Die OSM-Dokumentation beschreibt `healthcare=psychotherapist` für entsprechende Praxisstandorte und nennt ergänzende Kontakt- und Adressfelder. Psychiatrie, Beratung und Psychotherapie haben unterschiedliche Kennzeichnungen; die Kategorien nicht automatisch gleichsetzen. Die Datenbank steht unter ODbL, nicht unter der Lizenz des Wiki-Textes. [S15]

**Grenzen:** Keine bestätigte Deutschlandzahl, keine flächendeckende Hypnosekennzeichnung und keine aus dem Tag ableitbare Approbation, Kassenzulassung, Zusatzqualifikation oder aktuelle Behandlungskapazität. Dafür wären eigene, passende Nachweise nötig. Die offene Datenlizenz umfasst keine unbegrenzte kostenlose Nutzung gehosteter Karten-, Geokodierungs- oder API-Dienste.

Eine mögliche, noch nicht ausgeführte Zählabfrage lautet:

```overpass
[out:json][timeout:180];
area["ISO3166-1"="DE"]["admin_level"="2"]->.de;
nwr["healthcare"="psychotherapist"](area.de);
out count;
```

Das Ergebnis würde OSM-Objekte zählen, nicht deduplizierte approbierte Personen. Vor Veröffentlichung Quelle und Abrufzeit erhalten, Dubletten prüfen und die Nutzung beruflicher personenbezogener Kontaktdaten gesondert bewerten.

**Projektbezug:** Als Ergänzung des bereits vorhandenen Gesundheits-/Praxisprojekts verwenden, nicht als zusätzliches künstliches Duplikat im Projektkatalog zählen.

## 9. AnnoMI: interessanter Dialogdatensatz, aber Rechte offen

Das Herausgeber-README nennt **133 transkribierte und fachlich annotierte Demonstrationen von Motivational Interviewing** sowie eine einfache und eine ausführliche CSV-Version. Die Annotationen unterscheiden unter anderem Fragen, Reflexionen und Gesprächsbeiträge. [S16]

Im geprüften Repository-Stand `42936645ec3857a9c84ab296a36a3c34b779ef49` liegen die zwei CSV-Dateien und das README; eine eigenständige Lizenzdatei wurde dort nicht gefunden. Das belegt keinen endgültigen Ausschluss jeder Nutzung, aber ebenso wenig eine allgemeine kommerzielle Freigabe. Eine Lizenz des Forschungsartikels darf nicht ohne Prüfung auf Transkripte und Quellvideos übertragen werden.

**Folge:** Nur als Recherchekandidat aufnehmen. Kommerzielles Modelltraining und Wiederveröffentlichung bleiben bis zur Rechteklärung zurückgestellt. Es wurden keine Dialoge heruntergeladen. Demonstrationen sind außerdem kein repräsentativer Bestand realer deutscher Psychotherapieverläufe. Kein automatisches Therapeuten- oder Patientenscoring daraus ableiten.

## 10. Vier ergänzende Projekte: nur redaktionelle Hypothesen

| Nischenrang | Idee | Modelle | Denkbarer zahlungsrelevanter Nutzen | Startbedingung |
|---|---|---|---|---|
| 1 | Psychotherapie-Evidenznavigator | B2C / B2B / B2B2C | Fachlich geprüfte deutsche Erklärungen, Studienvergleich, Teamexport | Lizenzkompatibilität, Deduplizierung und qualifizierte Redaktion |
| 2 | Hypnose-Forschungs- und Studienradar | B2C / B2B / B2B2C | Themenbezogene Literaturberichte für Aus- und Fortbildung | Rechte und Themenabdeckung vor Import belegen |
| 3 | Forschungsdaten- und Materialfinder | B2B / B2B2C | Recherche nach Sprache, Datentyp, Lizenz und Zugang | Genügend fachlich passende, tatsächlich nutzbare Objekte |
| 4 | MI-Gesprächsführungs-Lernlabor | B2B / B2B2C | Strukturierte Lernrückmeldung anhand lizenzierter Demonstrationen | **Zurückgestellt bis Rechte geklärt sind** |

Bestehende Forschungsportale und Metaanalyse-Werkzeuge sind der Red-Ocean-Ausgangspunkt. Eine deutschsprachige, in Ausbildung oder Beratung integrierte Arbeitsweise ist eine zu prüfende Differenzierung, kein nachgewiesener Blue Ocean. B2B2C bedeutet hier beispielsweise: Ein Institut finanziert Informationen oder Lernwerkzeuge für seine Nutzer. Bloße Werbung eines Unternehmens ist damit nicht automatisch gleichzusetzen.

Suchintentionen wie „Hypnose Studien“, „Psychotherapie Forschungsdaten“ oder „Motivational Interviewing Lernmaterial“ sind lediglich Recherchekandidaten. Keine Suchvolumina, organischen Schwierigkeitswerte oder Einnahmen gemessen. Keine 1.000 qualifizierten Projekte, Praxen oder Studienseiten zugesichert.

## 11. Datenvertrag und KI-Nutzung

Empfohlene getrennte Objekte: `provider`, `site`, `study`, `publication`, `dataset`, `outcome`, `license_record` und `verification`. Verknüpfungen möglichst über DOI, PMCID, NCT-ID oder Datensatzversion; keine Titelähnlichkeit als alleinigen Identitätsbeweis verwenden.

Die neue JSON-Datei speichert pro Quellenprofil Datenart, Zugangsweg, Rechtebeleg, Quellen-URLs, dokumentierte Menge und Einheit. `payload_checked_at: null` heißt ausdrücklich: kein bestätigter Rohdaten-/API-Integrationstest. Das Lesen einer Metadatei ist nicht das erfolgreiche Einlesen der gesamten Studie. Unbekannte Mengen bleiben `null`, nicht null Einträge.

Für ein kommerzielles Produkt: nur zulässigen Umfang beziehen; Attribution und Lizenzstand halten; Evidenztyp und Aktualität sichtbar machen; sensible Informationen minimieren. Keine individuellen Rohdaten, Sitzungsprotokolle oder persönlichen Gesundheitsangaben in dieses Repository oder einen öffentlichen Suchindex übernehmen. Keine Re-Identifizierung.

Eine KI kann auf zulässig bezogenen Quellen suchen und mit Nachweisen zusammenfassen. Sie darf fehlende Ergebnisse, Praxisqualifikationen oder Behandlungskapazitäten nicht ergänzen. Offene Daten und eine fachlich ansprechende Oberfläche ersetzen keine validierte medizinische Anwendung. Hypnoseskripte, Audioaufnahmen und Fragebögen benötigen eigene Rechteprüfungen.

## 12. Offene Arbeit und Mengenfazit

Bestätigt sind **480 Studien**, **34 Studien eines möglicherweise überschneidenden Teilbestands**, **52 Versuchspersonen in einem Hypnoseexperiment** und **133 Demonstrationsgespräche**. Kein unabhängig gezählter deutscher Anbieterbestand und kein deduplizierter Gesamtbestand von 1.000 nutzbaren thematischen Objekten wurde erstellt.

Ein erster Pilot sollte daher Rechte, fachliche Relevanz und tatsächliche Zahl verwendbarer Objekte prüfen, bevor er eine große Website plant. Für Hypnose ist ein seriöser Forschungs- und Informationsdienst aus diesen Quellen besser begründbar als ein vermeintlich vollständiges kostenloses Anbieterregister.

## Primärquellen

- **S1:** [Metapsy Depression: Beschreibung und Datenlizenz](https://docs.metapsy.org/databases/depression-psyctr/)
- **S2:** [metapsyData: R-Zugriff und Softwarelizenz](https://data.metapsy.org/)
- **S3:** [ODC-By: offizielle Zusammenfassung](https://opendatacommons.org/licenses/by/summary/)
- **S4:** [480 Studien, fixierter Stand](https://github.com/metapsy-project/data-depression-psyctr/blob/ceeabb718db4a8ed6d5c5e265262d6ed7a392b72/metadata/number_studies.txt), [Suchstand 2024-01-01](https://github.com/metapsy-project/data-depression-psyctr/blob/ceeabb718db4a8ed6d5c5e265262d6ed7a392b72/metadata/last_search.txt)
- **S5:** [Stationäre Depression: Dokumentation](https://docs.metapsy.org/databases/depression-inpatients/), [34 Studien](https://github.com/metapsy-project/data-depression-inpatients/blob/main/metadata/number_studies.txt)
- **S6:** [Metapsy PTBS](https://docs.metapsy.org/databases/ptsd-psyctr/)
- **S7:** [Metapsy API](https://www.metapsy.org/api)
- **S8:** [OpenNeuro-Datensatz](https://openneuro.org/datasets/ds004572/versions/1.3.2), [CC0/DOI-Metadaten](https://github.com/OpenNeuroDatasets/ds004572/blob/main/dataset_description.json), [README und Stichprobe](https://github.com/OpenNeuroDatasets/ds004572/blob/main/README)
- **S9:** [Farahzadi et al., Scientific Reports 2024](https://www.nature.com/articles/s41598-024-56633-x)
- **S10:** [PsychArchives: Richtlinien, Rechte und Sharing Levels](https://www.psycharchives.org/en/about)
- **S11:** [PMC OA Subset](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/), [aktuelle Artikeldatensätze und Lizenzgruppen](https://pmc.ncbi.nlm.nih.gov/tools/textmining/)
- **S12:** [PMC: Abschaltung des OA Web Service](https://pmc.ncbi.nlm.nih.gov/tools/oa-service/)
- **S13:** [AACT: offizieller Zugang und Aktualisierung](https://aact.ctti-clinicaltrials.org/landing)
- **S14:** [ClinicalTrials.gov API-Dokumentation](https://clinicaltrials.gov/data-api/about-api), [Nutzungsbedingungen, in dieser Prüfung nicht vollständig auslesbar](https://clinicaltrials.gov/about-site/terms-conditions)
- **S15:** [OSM: healthcare=psychotherapist](https://wiki.openstreetmap.org/wiki/Tag:healthcare=psychotherapist), [Datenlizenz](https://www.openstreetmap.org/copyright)
- **S16:** [AnnoMI README, fixierter Stand](https://github.com/uccollab/AnnoMI/blob/42936645ec3857a9c84ab296a36a3c34b779ef49/README.md), [vollständige Dateiliste des geprüften Stands](https://api.github.com/repos/uccollab/AnnoMI/git/trees/42936645ec3857a9c84ab296a36a3c34b779ef49?recursive=1)
