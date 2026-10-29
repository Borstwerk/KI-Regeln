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

Die Vorabkriterien wurden in `f255f2dd95f9d0fe4cc7ddc13f6c4ae19c16638e`
committed und veröffentlicht. [Getrennte Evidence](Discovery-Read-Followup-2026-10-29.json)
enthält Konfiguration, lokale Kontrollen, native Tool-Ereignisse, Antwortbindung
und die kriterienspezifische Bewertung. Die beiden früher blockierten Antworten
und ihre Bewertung bleiben unverändert.

### Was tatsächlich nachgewiesen ist

| Prüfung | Beobachtung | Begrenztes Urteil |
| --- | --- | --- |
| Modellfreies Lesen unter verwalteten Anforderungen | Canary-Datei gelesen, Exit 0, richtiger Prüfwert | PASS für diese Operation |
| Modellfreie Schreib-Gegenprobe | Exit 1 / Permission-Denied-Signal, keine Zieldatei angelegt | PASS für diese Gegenprobe, keine allgemeine Isolationszertifizierung |
| Modell liest zufälligen Canary-Wert | nativer `Get-Content`, Exit 0; richtiger unvorhersehbarer Wert | Inhaltszugriff beobachtet, strenges Bytekriterium dennoch nicht erfüllt |
| Kaltlese D1/D3/D5 | konkrete Fachquellen geöffnet; Antwort mit überprüfbaren Fundstellen | drei Produktkriterien erfüllt, vollständiger Bootstrap nur PARTIAL |

Der Quellenzugriff gelingt mit dem ausdrücklich gewählten Read-only-Profil und
der bereits vorhandenen Windows-Implementierung. Welche der Konfigurationsdetails
die frühere Blockade verursacht hat, wurde nicht isoliert gemessen. Die offiziellen
Beschreibungen von [Permission-Profilen](https://learn.chatgpt.com/docs/permissions)
und [Windows-Sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox) stützen
die verwendeten Parameter; die lokale Evidence trägt nur die beobachteten Operationen.

### Abweichung: Canary-Gate war zu schwach implementiert

Die Datei hat 45 UTF-8-Bytes. Die [aufgezeichnete Canary-Antwort](Discovery-Read-Followup-2026-10-29.json)
hat 47 Bytes: Der richtige Prüfwert wird von zusätzlichen Zeilenumbrüchen begleitet.
Der Controller verglich vor dem Kaltlesestart mit `.strip()` und meldete deshalb
Erfolg. Das widerspricht dem vorher festgelegten **bytegenauen** Kriterium.
Der strenge Nachvergleich lautet `answer.encode("utf-8") == source_bytes` und
liefert für die tatsächlich gespeicherte Antwort **FAIL**. Die Kontrolle mit den
unveränderten Quelldateibytes liefert dagegen `True`.

Damit wurde die Kaltlese auf Grundlage eines schwächeren Gates gestartet.
Das ist eine Abweichung des Prüfablaufs, keine erfolgreiche Erfüllung des
Vorabprotokolls. Sie wird nicht nachträglich durch ein neues Whitespace-Kriterium
repariert. Der richtige zufällige Wert und der native Read bleiben tatsächliche
Zugriffsevidence; ein vollständiger Protokoll-PASS wird ausdrücklich nicht vergeben.

### Kaltlese und Snapshot-Grenzen

Die [veröffentlichte Antwort-Lesefassung](Discovery-Read-Followup-2026-10-29-cold-read.md)
findet den Beitragsweg über `CONTRIBUTING.md`, Skill-Engineering und die
Authoring-/Review-Skills. Sie trennt MCP-Rechteprüfung und Skill-Bundle-Admission
und verweigert den unbelegten Prüfclaim bei einem nicht ausgeführten Test.
Fundstellen wurden gegen den eingefrorenen Stand geprüft.

Die native Telemetrie enthält 24 abgeschlossene Befehle: 23 mit Exit 0, einen mit
Exit 1. Darunter sind direkte Reads auf `AGENTS.md`, Master-Router, Workflow-Index,
Overlays, relevante Skill-Dateien und die lokale Verifikationsdokumentation sowie
gezielte Katalogsuche. Gruppierte Befehle sind kein einzelner Read-Nachweis für
jeden Teilschritt und beweisen keine internen Checkpoints.

Der begrenzte Export enthält zwei registrierte Overlay-Dateien nicht:
`Recherche/Skills/citation-audit/SKILL.md` und
`Schreiben/Skills/adressatengerechte-kommunikation/SKILL.md`.
Der Agent versucht den Zugriff beziehungsweise sucht gezielt und benennt die
Lücke. Im vollständigen Repository existieren beide Dateien. Das ist ein
Snapshot-/Packaging-Problem; die Repository-Regeln werden deshalb nicht erweitert.
Die vollständige Bootstrap-Discovery bleibt **PARTIAL**.

CLI-Laufzeiten: Canary 10,03 s, Kaltlese 63,95 s; insgesamt 73,98 s.
Usage-Felder: 246.599 Input-, 178.688 Cached-Input-, 3.150 Output- und
450 Reasoning-Output-Tokens. Keine Aussage zu Abrechnung oder Einsparung.
Modellidentität nur als angeforderte Konfiguration gebunden.

Die Originalantworten bleiben lokal unverändert. Für die Veröffentlichung wurden
in der Kaltlese ausschließlich temporäre absolute Linkziele durch an denselben
Git-Commit gebundene Quellenlinks ersetzt; die Prosa ist unverändert. Runtime-
Kommandopräfixe sind anonymisiert. Raw- und Publikationshashes stehen in JSON.
Bewertung durch die koordinierende Instanz mit Kenntnis des Versuchs, nicht blind.

**Gesamturteil: PARTIAL.** Quellenzugriff und begrenzte Produktqualität sind nun
beobachtet; strenges Canary-Gate und vollständiger Bootstrap sind nicht bestanden.
Kein Vorher-/Nachher-Lift, kein Maturity- oder Gate-Upgrade, keine weiteren
Modellversuche in diesem Folgelauf. QMD, Mara-Oberfläche und lokaler Index-Refresh
bleiben `NOT RUN`.

Vor einem späteren Discovery-Lauf den Bytevergleich ohne Whitespace-Normalisierung
ausführen und die beiden fehlenden kanonischen Overlay-Descriptions bereitstellen.
Das ist ein begrenzter Reparaturschnitt am Prüfweg, kein Anlass für eine zusätzliche
Testplattform.

Diese Reparaturvorbereitung wurde anschließend **modellfrei** geprüft: Der strenge
Vergleich akzeptiert die 45 Quelldateibytes und weist die aufgezeichneten 47 Bytes
zurück. Ein neu vorbereiteter Export desselben Git-Stands enthält mit den zwei
zusätzlichen Dateien 242 statt 240 Dateien; alle sechs aktuell registrierten
Overlay-Descriptions sind darin vorhanden und per Hash gebunden. Dieser korrigierte
Export wurde nicht erneut einem Modell gegeben. Der historische 240-Datei-Lauf und
sein `PARTIAL`-Urteil bleiben unverändert.

Die Windows-Archive wurden mit lokalem `core.autocrlf=true` erzeugt. Die Descriptor-
Hashes binden die tatsächlich exportierten CRLF-Bytes; kanonische Git-Blob-Hashes
sind separat erfasst. Zur Reproduktion dieselbe Option nur am Archive-Aufruf setzen
(`git -c core.autocrlf=true archive`), keine globale Git-Konfiguration ändern.

Der [separat ausgeführte korrigierte Fall](Discovery-Corrected-2026-10-29.md)
liefert später begrenzte PASS-Evidence. Das hier dokumentierte `PARTIAL` und die
alte Canary-Antwort werden dadurch nicht umbewertet.
