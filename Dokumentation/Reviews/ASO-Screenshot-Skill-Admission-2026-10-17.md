# Externer Kandidat: ASO App Store Screenshots – Vorprüfung

**Entscheidung:** `WATCH / DO NOT ADMIT`. Nur statisch gelesen;
nicht installiert, nicht ausgeführt, kein echter Sicherheits-PASS.

## Identität und geprüfter Scope

- Quelle: [adamlyttleapps/claude-skill-aso-appstore-screenshots](https://github.com/adamlyttleapps/claude-skill-aso-appstore-screenshots).
- MIT laut `LICENSE` (Copyright 2026 Adam Lyttle).
- Quellprüfung 17.10.2026: `README.md`, `SKILL.md`,
  `CLAUDE.md` sowie `compose.py`, `generate_frame.py` und
  `showcase.py`. Es wurde **kein** vollständiger rekursiver
  Bundle-Hash oder unabhängiger Security-Test erstellt.
- Methodenimpuls: echte Simulator-Screenshots zuerst deterministisch
  komponieren; **KI-Enhancement optional** als eigener Schritt, der
  separat genehmigt und verifiziert werden muss.

## Relevanter Unterschied zu KI-Regeln

Kein allgemeiner UI-/Frontend-Skill, sondern ein Spezialworkflow für
Store-Screenshot-Assets und ASO-Botschaften. Kann später als
**optionale Capability** zum Mobile-App-Workflow passen. Vorher
bestehende Bild-, Design-, Screenshot- und Reviewfähigkeiten
auf Überschneidung prüfen und einen echten Ergebnisvergleich verlangen.

## Security-/Admission-Befund

| Bereich | Vorläufige Bewertung |
| --- | --- |
| Lokale Skripte | Python/Pillow-Skripte vorhanden; nur gelesen, nicht ausgeführt |
| Externe Datenübertragung | Gemini-MCP für generatives Enhancement vorgesehen; Screenshots oder Kontext können extern übertragen werden |
| Credentials | Gemini-Schlüssel und MCP-Konfiguration benötigt, **nicht** automatisch aktivieren |
| Installationsrisiko | Dokumentation nennt `pip install Pillow` und globale MCP-Installation, ungeprüfte transitive Pakete |
| Rechte an Assets | Store-Screenshots müssen echte Funktionen zeigen; keine KI-Features oder Zertifikate vortäuschen |
| Datensparsamkeit | Vor Upload Nutzer-/Gesundheits-/Kundendaten und geheime Bildinhalte bereinigen |
| Code-Scope | Gesehene Skripte behandeln lokale Bilddateien; nicht vollständig auf alle Dateipfade, Abhängigkeiten oder Laufzeitverhalten auditiert |
| Ergebnis-Evidence | „High converting“ ist ein Projektslogan, kein durch uns belegter Conversion-Uplift |

**Admission bleibt offen** bis Snapshot-Pinning, Dependency-/Script-/MCP-Review,
Scope-/Datenfluss- und Permission-Review, isoliertem Test mit
synthetischen Screenshots und unabhängigem Ergebnisreview.

Kein Download oder automatisches Installationsrezept im
Mobile-App-Workflow. Quellen sind untrusted Inputs und dürfen
weder AGENTS.md noch lokale Projektrechte überschreiben.
