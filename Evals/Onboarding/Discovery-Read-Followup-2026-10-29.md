# Discovery-Folgelauf: Lesezugriff zuerst

## Vorab festgelegter Scope

PR #107 ist mit `87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f` übernommen.
Der erste Kaltleseversuch bleibt unverändert `UNVERIFIED`. Dieser Folgelauf
untersucht zunächst den verfügbaren Leseweg, statt die blockierte Messung zu
wiederholen oder ein positives Ergebnis aus Bootstrap-Text abzuleiten.

Die vorhandene native Windows-Sandbox liest `PROJECT.md` modellfrei mit
`codex sandbox --include-managed-config --permission-profile :read-only`.
Eine separate synthetische Schreibprobe muss unter demselben Profil abgewiesen
werden. Das prüft nur diese Operationen, keine vollständige Isolation.

Danach höchstens zwei neue Codex-Abo-Sitzungen insgesamt:

1. **Lese-Canary**, höchstens 45 Sekunden, ein Versuch: eine lokal erzeugte Datei
   lesen. Der zufällige Inhalt steht weder im Prompt noch im Antwortschema.
   Nur eine bytegenau passende Antwort bestätigt den Zugriff. Bei Fehler/Blockade
   stoppen; die nachfolgende Kaltlese bleibt `NOT RUN`.
2. **Nur bei bestätigtem Zugriff:** eine frische read-only Kaltlese von D1/D3/D5
   aus dem [Pilotprotokoll](Agent-Discovery-Pilot-2026-10-29.md) am gemergten Stand.
   Derselbe Aufgabenprompt und derselbe kuratierte Snapshot-Umfang, keine Rubrik
   oder alten Antworten. Höchstens 180 Sekunden, keine Wiederholung.

Modell/Reasoning bleiben `gpt-6.1-sol` / `high`, CLI `0.165.0-alpha.1.2`.
Die lokale Prozesskonfiguration setzt `default_permissions=":read-only"` und
`windows.sandbox="elevated"` ausdrücklich, passend zur vorhandenen Installation.
Das Profil bleibt read-only; die verwalteten Anforderungen gelten weiterhin.
Keine globalen Konfigurationsänderungen, Sandbox-Bypässe, API-Schlüssel oder
direkten API-Aufrufe. Auth über den vorhandenen ChatGPT-Login.

Diese Konfiguration unterscheidet sich sichtbar vom ersten Lauf mit
`--ignore-user-config --sandbox read-only`. Die frühere Blockadeursache ist
damit nicht bereits bewiesen. Ein neuer Erfolg wäre ein Zugriffs-/Discovery-
Nachweis für diesen Stand, kein fairer Vorher-/Nachher-Lift und keine
nachgewiesene Tokenersparnis.

## Abnahme

- Modellfreie Read-/Write-Probe mit Status und tatsächlichem Dateizustand.
- Canary-Inhalt und -Hash lokal gebunden, kein Lösungswert im Aufgabenprompt.
- Native Tool-Evidence und Antwort unterscheiden; Behauptungen allein zählen
  nicht als erfolgreicher Fachquellen-Read.
- D1/D3/D5 nach den unveränderten Kriterien beurteilen. Fehlende Evidence bleibt
  `UNVERIFIED`, nicht ausgeführte Phasen `NOT RUN`.
- Alte Antworten und Bewertungen unverändert lassen; QMD, Mara-Oberfläche und
  tatsächlicher Index-Refresh weiterhin separat betrachten.

## Ergebnis

Vorabprotokoll; Ergebnis folgt separat.
