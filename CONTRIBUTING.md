# Mitmachen

Danke, dass du helfen willst. Willkommen sind vor allem:

- **Tote oder umgezogene Links** im Portalverzeichnis oder in den Fachanalysen
- **Neue offene Quellen** mit belegter Lizenz
- **Aktualisierte Zahlen** mit neuem Primärbeleg
- **Korrekturen**, wenn eine Lizenz oder Menge falsch wiedergegeben ist

## Was ein guter Beitrag enthält

Jede neue oder geänderte Angabe braucht einen Beleg. Konkret heißt das (Details in der [Prüfmethode](docs/METHODIK.md)):

1. Link auf die Primärquelle, nicht auf einen Blogartikel darüber
2. Bei Mengen: Einheit, Bezugsraum, Zeitraum und Zählbasis
3. Bei Lizenzen: Link auf die Stelle, an der die Lizenz des konkreten Datensatzes steht
4. Prüfdatum
5. Was **nicht** geprüft wurde (zum Beispiel: nur Dokumentation gelesen, keine Daten heruntergeladen)

Bitte keine Zahlen schätzen, Untergrenzen nicht als exakte Werte eintragen und keine Fremddaten in das Repository kopieren. Beschreibungen und Links genügen.

## Ablauf

1. Für kleine Korrekturen direkt einen Pull Request öffnen, für größere Ergänzungen zuerst ein Issue.
2. Wenn du JSON-Dateien änderst, lokal prüfen:

   ```bash
   python -m pip install -r requirements-validation.txt
   python scripts/validate_verified_directories.py
   python scripts/validate_education.py
   python scripts/build_dataset_index.py
   python -m unittest discover -s tests -v
   ```

3. `data/datasets.*` und `data/portals.csv` werden erzeugt, nicht von Hand bearbeiten. Neue Quellen in `scripts/build_dataset_index.py` unter `SOURCES` klassifizieren.
4. Bestehende IDs in den JSON-Dateien nicht umbenennen; andere Projekte können darauf verweisen.
5. Änderungen kurz im [CHANGELOG](CHANGELOG.md) vermerken.

Dateien unter `docs/archive/` sind historische Stände und werden nicht mehr aktualisiert.

## Lizenz deiner Beiträge

Mit einem Beitrag stimmst du zu, dass Texte und Daten unter [CC BY 4.0](LICENSE) und Code unter [MIT](LICENSE-CODE) veröffentlicht werden.
