# Deutsche Weiterbildungsangebote und AZAV: Quellen, Funktionen und Nutzung

[Zur Übersicht](../../README.md) · [Datenmodell](COURSE_DATA_MODEL.md) · [Maschinenlesbare Quellen](../../data/education_sources.json)

**Recherche- und Dokumentationsstand: 22.10.2026.** Dieses Dokument analysiert Datenquellen. Es enthält keinen bundesweiten Kursimport, keinen bestandenen API-Integrationstest und keine pauschale rechtliche Nutzungsfreigabe. Quellenbelege stehen bei den jeweiligen Aussagen; Produktvorschläge sind eigene konzeptionelle Bewertungen.

## 1. Ergebnis und Empfehlung

Für konkrete deutsche Weiterbildungsangebote existieren mehrere unterschiedliche Zugänge. Sie sollten nicht unter dem Etikett „Open Data“ vermischt werden:

| Zugang | Geeignete Quellen | Was damit zunächst möglich ist |
|---|---|---|
| Öffentlich dokumentierte, maschinenlesbare Angebotsdaten | Berliner VHS-Datensatz; Europass / European Learning Data | Ressourcen und Lizenzen prüfen, kleinen Import erproben, Abdeckung messen |
| Offene Lizenz für bestimmte Kursdatensätze, aber Exportweg ungeklärt | Hamburger Kursportal WISY | Lizenzumfang und Share-Alike prüfen; zulässigen technischen Bezug klären |
| Kostenlose Recherche, keine allgemeine Datenübernahme nachgewiesen | mein NOW, IWWB, WIS, hoch & weit | Angebote entdecken, vergleichen und zum Original verlinken |
| Schnittstelle für eigene Anbieterbestände | KURSNET / open-Qcat | Autorisiert bereitgestellte eigene Angebotsdaten normalisieren |
| Referenzen statt Kursdaten | BA-Zulassungsinformationen, DAkkS, ESCO | Zulassungslogik, Ausstellerprüfung und Kompetenzzuordnung unterstützen |

**Für ein erstes eigenes Produkt empfiehlt sich ein kleiner, belegbarer Datenbestand statt eines vermeintlich vollständigen AZAV-Registers.** Berlin eignet sich als technischer Kursdaten-Pilot, Europass als europäische Ergänzung, WISY als besonders interessanter Lizenzkandidat. mein NOW bleibt eine wichtige fachliche Recherchequelle. Die Belege und Grenzen dieser Einordnung werden unten erläutert.

In den geprüften Quellen wurde **kein vollständig offener, bundesweit vollständiger und aktuell verifizierter Gesamtdatensatz aller AZAV-Träger und Maßnahmen** nachgewiesen. Das ist ein Rechercheergebnis, keine Aussage, dass ein solcher Bestand grundsätzlich nicht existieren könne.

## 2. Quellenvergleich

| Quelle | Datenebene und Funktionen | Technischer Stand | AZAV-Bedeutung |
|---|---|---|---|
| mein NOW | Konkrete Weiterbildungen, Umschulungen, Orte und Lernformen | Öffentliche Suche; keine offene Gesamtabruf-API nachgewiesen | Recherchehinweis, kein eigenständiger Zertifikatsbeleg |
| KURSNET / open-Qcat | Eigene Angebote eines registrierten Anbieters | XML-Austausch im Anbieter-Kontext | Anbieterangaben nicht mit geprüfter Maßnahmezulassung gleichsetzen |
| IWWB | Suchübergreifende Entdeckung von Bildungsangeboten | Metasuche und Partneranbindungen | Förderinformationen quellenbezogen prüfen |
| Berliner VHS | Konkrete Kursangebote | JSON/XML dokumentiert; Nutzdatenabruf noch nicht getestet | Kein allgemeiner AZAV-Nachweis |
| Europass / QDR | Lernangebote und Qualifikationen | TTL, JSON-LD und SPARQL dokumentiert | Deutsche Abdeckung nur teilweise; kein AZAV-Vollregister |
| Hamburg WISY | Kurse, Anbieter, Bildungsgutschein-Suche | Öffentliche Suche; Bulk-Zugang ungeklärt | Förderhinweise als zu prüfende Angaben behandeln |
| WIS | IHK-nahe Weiterbildung und Seminare | Öffentliche Suche | IHK-Bezug ist kein AZAV-Nachweis |
| hoch & weit | Hochschulische Weiterbildung | Öffentliche Suche und Hochschulmeldungen | Hochschulstatus ist kein AZAV-Nachweis |
| ESCO | Berufe und Kompetenzen, keine Kursdurchführungen | Download und API dokumentiert | Keine Zulassungsfunktion |
| Bundesagentur für Arbeit | Zulassungsanforderungen | Informationsseiten | Referenz für Träger-/Maßnahmetrennung |
| DAkkS | Akkreditierte fachkundige Stellen | Referenzsuche | Aussteller prüfen, nicht alle Kurse finden |

Die nachfolgenden Profile sind die Beleggrundlage dieser Tabelle. Der JSON-Katalog bildet dieselben elf Quellen ab; „dokumentiert“ bedeutet ausdrücklich nicht „erfolgreich integriert“.

## 3. Die einzelnen Quellen

### 3.1 mein NOW: bundesweite Suche nach tatsächlichen Angeboten

Die Weiterbildungsrecherche der BA bietet Filter unter anderem für Region, Lernform und Weiterbildungsart. Sie ist fachlich relevant, wenn ein konkreter Kurs gesucht wird und nicht lediglich eine Bildungsstatistik. Das übergeordnete Portal verbindet Weiterbildung mit Orientierung, Förderung und Beratung. [Quelle: mein NOW](https://mein-now.de/privatpersonen/weiterbildungen), [BA-Portalbeschreibung](https://www.arbeitsagentur.de/karriere-und-weiterbildung/nationales-onlineportal-berufliche-weiterbildung-mein-now).

**Integrationsbewertung:** Zunächst Originalverlinkung und nachvollziehbare Recherche verwenden. In dieser Prüfung ist keine dokumentierte, allgemein freigegebene öffentliche Lese-API für den gesamten Kursbestand belegt. Eine technisch sichtbare Anfrage des Web-Frontends ist weder eine zugesicherte API noch eine Nutzungslizenz.

**Beispiel eines konkreten Angebots:** [mein-NOW-Termin 271537450](https://mein-now.de/weiterbildungssuche/termin/271537450), „Mobile App Entwicklung …“, zeigt, wie ein Angebot mit Anbieter, Termin, Voraussetzungen und Lernform präsentiert wird. Der Link dient als Feld- und Quellenbeispiel, nicht als Empfehlung oder als unabhängig geprüfter AZAV-Nachweis. Die vollständige Beschreibung wurde nicht in dieses Repository übernommen.

### 3.2 KURSNET / open-Qcat: wichtig, aber keine offene Gesamtdatenbank

Die BA dokumentiert einen XML-Upload für Bildungsanbieter. Anbieter können eigene registrierte Angebotsdaten exportieren und ihre Daten strukturiert übertragen. Der beschriebene Zugriff ist an Anbieterprozesse gebunden. [Quelle: BA, XML-Upload](https://www.arbeitsagentur.de/institutionen/kurse-anbieten/xml-upload).

**Integration:** Ein autorisiert bereitgestellter Anbieterfeed kann ein verlässlicher Ausgangspunkt sein. XML-Schema, Anbieterkennung, Angebotskennung und Importprotokoll sollten erhalten bleiben. Ein Uploadformat ist jedoch keine öffentliche API zum Auslesen fremder Bestände. Auch der Name „open-Qcat“ belegt keine offene Lizenz an sämtlichen darin transportierten Kursen.

**Nutzen:** Weniger manuelle Mehrfachpflege, konsistente Angebotsinformationen und sauber dokumentierte Herkunft. Die Beschreibung eines Formats darf nicht mit einer von der BA erteilten Erlaubnis zum Betrieb eines vollständigen Spiegelportals verwechselt werden.

### 3.3 InfoWeb Weiterbildung: Entdeckung und Abdeckungsvergleich

IWWB beschreibt eine Metasuche über kooperierende Weiterbildungsdatenbanken. Die technische Zusammenarbeit mit Partnern und die Zwischenspeicherung von Suchinformationen sind dokumentiert. [Quelle: Über das IWWB](https://www.iwwb.de/information/UEber-das-IWWB-weiterbildung-20.html).

**Integration und Nutzen:** Geeignet, um weitere regionale oder thematische Quellen zu identifizieren. Für einen eigenen Datenimport müssen Rechte und Zugang der konkreten Ursprungssammlung geprüft werden. Partneranbindungen sind kein Nachweis einer offenen API für beliebige Dritte. Beim Vergleich sind Mehrfachmeldungen desselben Kurses zu erwarten; Trefferzahlen verschiedener Portale dürfen nicht einfach addiert werden.

### 3.4 Berliner Volkshochschulen: besonders konkreter Open-Data-Kandidat

Das Berliner Datenportal beschreibt Kursdaten mit JSON- und XML-Ressourcen und nennt CC BY. Die genaue Lizenzversion ist in der betrachteten Metadatenansicht nicht eindeutig. Zudem widersprechen sich Aktualisierungsangaben: Die Beschreibung nennt stündliche Aktualisierung, Ressourcenbeschreibungen nennen Montag. [Quelle: Berliner Kursdatensatz](https://daten.berlin.de/datensaetze/kurse).

**Integration:** Die aktuellen Ressourcenlinks aus dem Katalog auflösen, eine kleine Datei abrufen, Felder und Lizenzversion prüfen und erst danach einen Import freigeben. Der Nutzdatenabruf wurde in dieser Recherche nicht erfolgreich getestet. Eine garantierte stündliche Versorgung wird daher nicht behauptet.

**Nutzen:** Praktischer Pilot für Suche, Kostenvergleich, Termine und regionale Weiterbildung. Für den Anwendungsfall AZAV muss zusätzlich nachgewiesen werden, ob die jeweilige Maßnahme tatsächlich zugelassen ist; die bloße Aufnahme in einen VHS-Katalog genügt dafür nicht.

### 3.5 Europass / European Learning Data: strukturierte Lernangebote

Europass kündigte am 23.01.2026 die Bereitstellung von Qualifikations- und Lernangebotsdaten über das europäische Open-Data-Portal an. Dokumentiert werden TTL, JSON-LD und SPARQL auf Grundlage des European Learning Model. [Europass-Mitteilung](https://europass.europa.eu/en/news/data-qualifications-and-learning-opportunities-now-available-open-data-portal), [Datensatzkatalog](https://data.europa.eu/data/datasets/european-learning-data?locale=en).

**Wichtige Grenze für Deutschland:** Die veröffentlichte KURSNET-Einwilligung zur Europass-Übertragung bezieht sich auf ausgewählte Kategorien und die Zustimmung des Anbieters. Sie nennt unter anderem bestimmte Schulabschlüsse, Sprachangebote, berufliche Ausbildung ohne Umschulung, Aufstiegsweiterbildung und Anerkennungsqualifizierungen. Daraus folgt keine vollständige Abdeckung aller deutschen Weiterbildungen oder AZAV-Maßnahmen. [BA-Einwilligung](https://www.kursnet-online.arbeitsagentur.de/onlinekurs/printEinwilligungEuropass.do).

**Integration:** Zuerst tatsächlich verfügbare deutsche Distribution, Lizenz, ELM-Version und Feldabdeckung prüfen. Keine unbekannte SPARQL-Adresse erfinden. Die Einwilligung zur Datenlieferung an Europass ist keine allgemeine Lizenz zum unabhängigen Scraping des gesamten KURSNET-Bestands.

### 3.6 Hamburger Kursportal WISY: bemerkenswerte offene Lizenz

Die Anbieterbedingungen nennen in den Abschnitten 2.6 und 4.1 CC-BY-SA für eingestellte Kursdatensätze; der verlinkte Lizenztext ist **CC BY-SA 3.0 DE**. Dieser erlaubt auch kommerzielle Nutzung unter seinen Bedingungen, insbesondere Namensnennung und Weitergabe unter gleichen Bedingungen bei entsprechenden Bearbeitungen. [WISY-Bedingungen](https://hamburg.kursportal.info/g679), [Lizenztext](https://creativecommons.org/licenses/by-sa/3.0/de/).

Das [Hamburger Kursportal](https://hamburg.kursportal.info/) und das [Bildungsgutschein-Kursportal](https://bildungsgutschein.kursportal.info/) sind daher besonders relevante Recherchequellen. **Offen bleibt der technische Bezug eines vollständigen Bestands:** Eine öffentlich dokumentierte freie Bulk-API wurde nicht nachgewiesen.

**Integration:** Lizenzumfang für den jeweiligen Datensatz prüfen, insbesondere bei übernommenen Drittbeständen. Attribution und Änderungsvermerke speichern; Share-Alike-Kompatibilität vor Zusammenführung klären. Die Lizenz nicht pauschal auf Bilder, das komplette Webdesign oder beliebige externe Daten ausdehnen. Eine offene Lizenz löst außerdem keine Serverkapazitäts- oder Zugriffsbeschränkungen auf.

### 3.7 WIS: Weiterbildung im IHK-Umfeld

Das Weiterbildungs-Informations-System bietet eine bundesweite Suche nach Seminaren und Weiterbildung. [WIS](https://wis.ihk.de/), [Beschreibung der IHK Hagen](https://www.ihk.de/hagen/bildung/weiterbildung/weiterbildungs-informations-system-3174488).

**Nutzen:** Ergänzung für berufliche Qualifizierungen und Fortbildungen. Für die eigene Integration wurden keine allgemeine offene Weiterverwendungslizenz und keine freigegebene Drittnutzer-Lese-API nachgewiesen. IHK-Abschluss, Teilnahmezertifikat und AZAV-Maßnahmezulassung sollten im Datenmodell unterschiedliche Felder sein.

### 3.8 hoch & weit: wissenschaftliche Weiterbildung

Das Hochschulportal bündelt Weiterbildungsangebote von Hochschulen. Die FAQ erläutern die Eintragung durch Hochschulen und die Suchmöglichkeiten. [Portal](https://hoch-und-weit.de/), [FAQ](https://hoch-und-weit.de/faq/).

**Nutzen:** Berufsbegleitende Studienangebote, Zertifikate und wissenschaftliche Weiterbildung ergänzen den Blick über klassische Maßnahmen hinaus. Eine Anbindung für Hochschulen ist keine automatisch verfügbare Lese-API für Dritte. ECTS, Hochschulstatus oder wissenschaftliche Qualität dürfen nicht als Aussage über Bildungsgutschein-Förderung interpretiert werden.

### 3.9 ESCO: verbindendes Vokabular statt Angebotsdaten

ESCO stellt mehrsprachige Berufs- und Kompetenzbegriffe als Downloads und über API-Angebote bereit. CSV, ODS und RDF/TTL sind dokumentierte Formate. [Downloads](https://esco.ec.europa.eu/de/use-esco/download), [lokale API](https://esco.ec.europa.eu/en/use-esco/use-esco-services-api/esco-local-api).

**Integration:** Stabile Begriffs-URIs mit versionierten Zuordnungen verwenden. Kursinhalte können auf Kompetenzen abgebildet werden, wobei maschinelle Zuordnungen als solche erkennbar bleiben müssen. ESCO enthält keine buchbaren Kursdurchführungen und keine AZAV-Prüfung. Datenlizenz, API-Bedingungen und Lizenz einer lokal eingesetzten Software sind getrennt zu dokumentieren.

### 3.10 BA und DAkkS: Nachweislogik statt Kursliste

Die BA erläutert die Zulassung von Trägern und Maßnahmen. Bei Gutscheinmaßnahmen reicht die Zulassung des Anbieters allein nicht aus. Zulassungen erfolgen durch fachkundige Stellen; deren Akkreditierung ist Aufgabe der DAkkS. [BA-Zulassungsinformationen](https://www.arbeitsagentur.de/institutionen/bildungstraeger/akkreditierung-zulassung), [DAkkS zu AZAV](https://www.dakks.de/de/azav.html).

**Integration:** Aussteller, Geltungsbereich und Gültigkeit eines konkreten Nachweises prüfen. Die DAkkS-Suche nach akkreditierten Stellen ist kein Register sämtlicher Bildungsträger und Kursangebote. Eine persönliche Förderentscheidung darf nicht aus einer Kurslistung abgeleitet werden.

## 4. Fachliche Regeln für AZAV-Daten

Die folgenden Regeln sind ein konservativer Entwurf für ein Rechercheprodukt auf Grundlage der oben genannten BA-/DAkkS-Referenzen:

1. **Träger, Maßnahme und Durchführung trennen.** Ein Anbieter kann sowohl zugelassene als auch andere Angebote haben. Standort, Lernform und Gültigkeitszeitraum müssen zur vorliegenden Zulassung passen.
2. **Behauptung und Prüfung unterscheiden.** „Laut Anbieter förderbar“ ist etwas anderes als „Zertifikat geprüft“. Ohne ausreichenden Beleg lautet der Status „unbekannt“, nicht automatisch „nein“ und niemals automatisch „zugelassen“.
3. **Kennungen nicht verwechseln.** Veranstaltungs-ID, Maßnahmennummer und Zertifikatsnummer sind unterschiedliche Felder. Eine ID aus einer Suchseite ist kein Zulassungsnachweis.
4. **Förderung getrennt behandeln.** Bildungsgutschein, AVGS und andere Finanzierungswege erhalten eigene Angaben. Die individuelle Bewilligung ist eine zusätzliche Entscheidung und gehört nicht in einen öffentlichen allgemeinen Kursstatus.
5. **Zeitliche Gültigkeit erhalten.** Prüfdatum, Beobachtungsdatum und Gültigkeitsende getrennt speichern. Abgelaufene oder widerrufene Belege nicht einfach durch einen älteren positiven Status überdecken.

Das [Datenmodell](COURSE_DATA_MODEL.md) übersetzt diese Regeln in getrennte Entitäten und Nachweisfelder.

## 5. Funktionen mit konkretem Nutzen

### Für Ratsuchende

Ein sinnvoller Kursvergleich kombiniert Zielberuf, Inhalte, Dauer, Lernform, Termin und Erreichbarkeit. Unbekannte Gebühren dürfen nicht als kostenlos erscheinen. „Online“ sollte unterscheiden, ob Teilnahme von zu Hause oder nur an einem Lernstandort möglich ist. Ein Vergleich zeigt offene Fragen und verlinkt zum Original, statt eine unbelegte Eignungs- oder Fördergarantie zu geben.

### Für Coaches und Beratungsstellen

Eine belegte Auswahlliste kann drei bis fünf passende Angebote mit Quellenstand, nachvollziehbaren Ausschlussgründen und noch zu klärenden Punkten zusammenstellen. Der Mehrwert liegt in weniger Sucharbeit und besserer Dokumentation. Gesundheitsdaten von Teilnehmenden werden dafür nicht in einem öffentlichen oder allgemeinen Quellenrepository benötigt. Funktionale Anforderungen wie gewünschte Unterrichtszeiten lassen sich getrennt und datensparsam erfassen.

### Für Bildungsanbieter und Marktbeobachtung

Auf rechtmäßig nutzbaren Daten lassen sich regionale Angebotslücken, Kursstarts und Themenabdeckung analysieren. Dabei sind Angebotsanzahl, tatsächlich gestartete Gruppen und verfügbare Plätze verschiedene Größen. Aus mehrfach gemeldeten Online-Angeboten darf keine künstlich hohe regionale Kapazität berechnet werden.

## 6. Empfohlene Integrationsreihenfolge

**Stufe 1 – Machbarkeit:** Einen offenen Kursdatensatz mit belegter Lizenz und erreichbarer Ressource testen. Dokumentieren, welche Felder tatsächlich vorhanden sind. Fehlende Felder nicht aus allgemeinen Anbietertexten auffüllen.

**Stufe 2 – Vergleich:** Anbieter, Kurs und einzelne Durchführung normalisieren. Dubletten prüfen. Suchfilter und eine Quellenansicht bauen, bevor ein Sprachmodell eingesetzt wird.

**Stufe 3 – Nachweise:** AZAV nur für konkrete Angebote mit ausreichenden Belegen ausweisen. Für alles andere einen sichtbaren Prüfstatus verwenden. Belege regelmäßig gegen Gültigkeitsdaten prüfen; eine solche Routine ist hier noch nicht implementiert.

**Stufe 4 – KI-Unterstützung:** Zusammenfassungen aus freigegebenen Daten erzeugen, jede wesentliche Aussage mit Beleg verknüpfen und Unsicherheit anzeigen. Keine Förderentscheidung automatisieren. Die vorgeschlagene [Integrationsarchitektur](../integration/ARCHITECTURE.md) beschreibt technische und organisatorische Kontrollen.

## 7. Offene Punkte vor einem produktiven Betrieb

Noch ausstehend sind insbesondere Nutzdaten- und Schema-Tests der Downloadquellen, präzise Lizenzversionen und Lizenzumfänge, die deutsche Europass-Abdeckung, ein dokumentierter WISY-Exportweg sowie eine belastbare Aktualisierungs- und Nachweisstrategie. Es wurden weder Kursbestände massenhaft übernommen noch Zugangsbegrenzungen umgangen. Der aktuelle Stand ist eine fundierte Quellen- und Integrationsanalyse, keine betriebsbereite Kursdatenplattform.
