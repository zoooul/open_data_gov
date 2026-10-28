# Datenmodell für Kurse, Durchführungen und AZAV-Nachweise

[Quellenanalyse](WEITERBILDUNG_DE_AZAV.md) · [Architektur](../integration/ARCHITECTURE.md)

**Status:** Entwurf für eine spätere Implementierung, Stand 22.10.2026. Die Beispiele sind synthetisch und enthalten keine realen Zulassungsbehauptungen. Die fachliche Ausgangsbasis zur Trennung von Träger- und Maßnahmezulassung ist die [BA-Dokumentation](https://www.arbeitsagentur.de/institutionen/bildungstraeger/akkreditierung-zulassung).

## 1. Nicht alles in eine Kurstabelle schreiben

| Entität | Bedeutung | Wichtige Felder |
|---|---|---|
| `provider` | Rechtlicher Bildungsanbieter | interne ID, Name, Quellkennungen, Kontaktquelle |
| `site` | Konkreter Lern- oder Verwaltungsstandort | Anbieter-ID, Adresse, Koordinatenquelle, Art des Standorts |
| `course` | Inhaltlich beschriebenes Angebot | Titel, Lernziele, Voraussetzungen, Abschlussart, Kompetenzzuordnungen |
| `course_run` | Einzelne geplante Durchführung | Kurs-ID, Start, Ende, Unterrichtszeiten, Lernform, Ort, Preis, Status |
| `approval` | Einzelner Zulassungsnachweis | Typ, Aussteller, Bezugsobjekt, Gültigkeit, räumlicher und sachlicher Umfang |
| `funding_statement` | Quellenbezogene Förderangabe | Förderweg, Wortlautklasse, Bezugsobjekt, Beleg, Prüfstatus |
| `evidence` | Nachweis einer einzelnen Aussage | Quelle, Beobachtungsdatum, Dokumentversion, Fundstelle, Prüfverfahren |
| `source_record` | Ursprüngliche Datenmeldung | Quelle, externe ID, Lizenz, Abrufzeit, Prüfsumme, Transformationsversion |

Ein Kurs kann mehrere Termine haben. Ein Anbieter kann mehrere Standorte betreiben. Ein Kurs kann in mehreren Portalen auftauchen. Keine dieser Beziehungen sollte durch blindes Zusammenführen anhand des Namens verloren gehen.

## 2. Identität und Dubletten

Die Primäridentität eines importierten Datensatzes ist zunächst `(source_id, external_id)`. Eigene kanonische IDs dürfen erst nach einem dokumentierten Abgleich zugeordnet werden. Titelähnlichkeit allein reicht nicht aus: Unterschiedliche Abschlüsse, Dauer, Unterrichtssprache oder Lernformen können trotz ähnlichem Titel verschiedene Angebote bedeuten.

Mehrere Online-Listungen an unterschiedlichen Ortsseiten sind nicht automatisch mehrere Durchführungen. Umgekehrt dürfen zwei Kurse mit gleichem Titel und verschiedenen Startterminen nicht zu einem Termin verschmelzen. Speichere Zusammenführungen als nachvollziehbare Zuordnungen mit Methode, Konfidenz und manueller Entscheidung; lösche die ursprünglichen IDs nicht.

## 3. Minimalfelder für eine brauchbare Durchführung

| Feld | Vorgeschlagene Behandlung |
|---|---|
| `title` | Originaltitel separat von redaktioneller Kurzbezeichnung |
| `start_date`, `end_date` | ISO-Datum oder `null`; „laufender Einstieg“ als eigener Modus |
| `timezone` | Bei Uhrzeiten ausdrücklich, beispielsweise `Europe/Berlin` |
| `duration_value`, `duration_unit` | Tage, Wochen, Zeitstunden und Unterrichtseinheiten unterscheiden |
| `weekly_schedule` | Belegte Zeiten; keine automatische Annahme über Betreuungskompatibilität |
| `delivery_mode` | Präsenz, remote von zu Hause, virtuell am Lernstandort, hybrid, unbekannt |
| `site_id` | Nur bei belegtem Teilnahmeort; Verwaltungssitz nicht als Unterrichtsort verwenden |
| `fee_amount`, `fee_currency` | Unbekannt bleibt `null`, nicht 0 |
| `prerequisites` | Quelle und Prüfdatum erhalten; Interpretation von Originalanforderung trennen |
| `award_type` | Teilnahmebescheinigung, Herstellerzertifikat, IHK-Abschluss, Hochschulzertifikat etc. |
| `availability_status` | Angekündigt, buchbar laut Quelle, ausgebucht, abgesagt, abgelaufen, unbekannt |
| `source_url`, `observed_at` | Originalbeleg und Zeitpunkt der Beobachtung |

Die Einheitenumrechnung darf nur erfolgen, wenn die Länge einer Unterrichtseinheit belegt ist. Für einen Preisvergleich muss außerdem erkennbar sein, ob Prüfungsgebühren, Materialien und Umsatzsteuer enthalten sind. Aus fehlenden Angaben folgt keine Gebührenfreiheit.

## 4. Nachweiszustände statt eines einzigen AZAV-Häkchens

Empfohlene Zustände für einen einzelnen Nachweis:

- `unknown`: Kein ausreichender Beleg vorhanden.
- `claimed`: Aussage des Anbieters oder Portals, noch nicht unabhängig geprüft.
- `document_checked`: Dokument, Aussteller, Geltungsbereich und Gültigkeit wurden geprüft.
- `expired`: Der dokumentierte Gültigkeitszeitraum ist abgelaufen.
- `revoked`: Ein belastbarer Widerrufsbeleg liegt vor.
- `not_applicable`: Der betrachtete Nachweistyp passt nicht zum Angebot.

Dies ist eine interne Klassifikation, kein amtlicher Statusstandard. `document_checked` benötigt mindestens eine Nachweisreferenz, Prüfdatum und Prüferrolle. Ein automatischer Textklassifikator darf diesen Status nicht allein vergeben. Die aktuelle Wirksamkeit kann trotz eines geprüften Dokuments weitere Klärung erfordern.

Ein `approval` sollte ausdrücklich speichern:

```text
approval_id
approval_type = provider | measure
subject_id
issuer_name
issuer_reference_url
certificate_number
valid_from
valid_until
scope_sites[]
scope_delivery_modes[]
scope_description
verification_status
evidence_ids[]
checked_at
checked_by_role
```

Die [DAkkS](https://www.dakks.de/de/azav.html) ist eine Referenz zur Akkreditierung fachkundiger Stellen. Ein Treffer zur ausstellenden Stelle ist noch kein Beleg, dass die konkrete Maßnahme und der konkrete Termin abgedeckt sind.

## 5. Finanzierung unabhängig modellieren

Eine Förderangabe besteht aus Förderweg, Bezugsobjekt, Beleg und Wortlautklasse. Beispielhafte Förderwege sind Bildungsgutschein, AVGS, Arbeitgeberfinanzierung oder Selbstzahlung. Diese Kategorien dürfen nicht austauschbar verwendet werden.

Eine Anbieterangabe „mit Bildungsgutschein möglich“ wird als `claimed` und mit Quellenbeleg gespeichert. Sie ist weder eine individuelle Bewilligung noch ein Nachweis, dass für einen bestimmten Menschen sämtliche Voraussetzungen erfüllt sind. Personenspezifische Bescheide gehören nicht in den allgemeinen Kurskatalog dieses Repositorys.

## 6. Synthetisches Beispiel

Das folgende Objekt demonstriert ausschließlich die Struktur. Es ist kein realer Kurs und darf weder angezeigt noch als Trainingsexempel für tatsächlich zugelassene Maßnahmen behandelt werden.

```json
{
  "is_synthetic": true,
  "course_run_id": "example-run-001",
  "course_id": "example-course-001",
  "provider_id": "example-provider-001",
  "title": "Beispiel: Digitale Kompetenzen im Büro",
  "start_date": null,
  "end_date": null,
  "delivery_mode": "unknown",
  "fee_amount": null,
  "fee_currency": "EUR",
  "provider_approval_status": "unknown",
  "measure_approval_status": "unknown",
  "funding_statements": [],
  "evidence_ids": [],
  "publishable": false
}
```

## 7. Herkunft auf Feldebene

Ein Datensatz kann mehrere Quellen haben. Deshalb sollte nicht nur ein pauschaler Quellenlink am Gesamtprofil stehen. Für relevante Angaben sind getrennte Belege sinnvoll: Termin aus einem Kursfeed, Preis von der Kursseite, Zulassung aus einem Zertifikat. Bei widersprüchlichen Quellen werden beide Versionen und ihre Beobachtungsdaten erhalten.

Empfohlenes Evidenzobjekt: `evidence_id`, `source_url`, `publisher`, `source_record_id`, `observed_at`, `source_updated_at`, `valid_from`, `valid_until`, `field_paths`, `rights_reference`, `content_hash`, `verification_method`. Eine Prüfsumme belegt die Identität einer gespeicherten Datei, nicht die Wahrheit ihres Inhalts.

Belegdokumente werden nur gespeichert oder weiterveröffentlicht, wenn dafür ausreichende Rechte bestehen. Andernfalls können URL, Fundstelle und eigene Prüfnotiz genügen. Personenbezogene Kontaktdaten werden minimiert; Gesundheits- oder Beratungsakten gehören nicht in dieses Modell.

## 8. Vergleich und KI-Ranking

Zuerst harte Kriterien prüfen: tatsächlicher Termin, Lernform, nachweisbare Voraussetzungen, Kostenrahmen und gegebenenfalls benötigter Zulassungsstatus. Unbekannte Angaben sind keine erfüllten Kriterien. Erst danach können thematische Nähe und Kompetenzen ein Ranking unterstützen.

Eine vorgeschlagene ESCO-Zuordnung erhält `mapping_method`, `esco_version`, `confidence` und gegebenenfalls einen manuellen Prüfstatus. Das Sprachmodell darf aus einem ähnlichen Kursnamen keine bestandene Eignungsprüfung oder Zulassung ableiten. Die [ESCO-Downloads](https://esco.ec.europa.eu/de/use-esco/download) liefern das Vokabular, nicht diese fachlichen Entscheidungen.

## 9. Abnahmekriterien für eine spätere Implementierung

Ein Pilot ist erst brauchbar, wenn gleiche Kursmeldungen nicht doppelt gezählt werden, neue Termine alte nicht überschreiben, abgelaufene Nachweise sichtbar bleiben und unbekannte Preise nicht als kostenlos erscheinen. Zusätzlich muss jede Zulassungsbehauptung zu einem konkreten Nachweis führen.

Tests sollten mindestens einen unvollständigen Feed, zwei widersprüchliche Termine, einen Anbieter mit zugelassenen und nicht nachgewiesenen Angeboten, einen abgelaufenen Nachweis und einen Online-Kurs mit mehreren Ortslistungen abdecken. Die hier mitgelieferte JSON-Schema-Prüfung validiert dagegen nur den **Quellenkatalog**; sie ersetzt diese künftigen Fachtests nicht.
