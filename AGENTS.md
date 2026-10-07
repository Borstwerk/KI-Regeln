# KI-Regeln – Agent Bootstrap

Diese Datei ist der kleinste Einstiegspunkt für einen frischen KI-Agenten. Lade nicht pauschal README, alle Skills oder das vollständige Handbuch in den Kontext.

## Pflicht vor nichttrivialer Arbeit

Bevor bei einer **nichttrivialen** Aufgabe ein erster Lösungsentwurf entsteht, müssen im aktuellen Lauf die zentralen Router tatsächlich benutzt werden:

1. `Dokumentation/Skill-Handbuch.md` öffnen;
2. `skill-catalog.yml` öffnen oder gezielt durchsuchen;
3. `routing-overlays.yml` öffnen;
4. bei einem plausiblen mehrphasigen Prozess zusätzlich `workflow-index.yml` und den passenden Workflow öffnen.

Erst danach Primärowner, mögliche Composition und `none` festlegen. Diese Pflicht gilt nicht für den unten definierten trivialen Direktpfad.

## Problem-first Routing

Der Nutzer muss keine Skill-Namen, Domänen oder Workflows kennen. Ein Auftrag darf vollständig in Alltagssprache formuliert sein.

Beispiele:

- „Ich muss diese Datenbanktabelle dokumentieren.“
- „Prüfe, ob diese Behauptung stimmt.“
- „Ich möchte ein Buch mit wiederkehrenden Figuren entwickeln.“
- „Hilf mir, meine Rücklagen und Geldanlage einzuordnen.“

Die Aufgabe des Routers ist es, aus dem **Problem** den kleinsten ausreichenden Werkzeug-Satz abzuleiten. Nicht möglichst viele Skills aktivieren und nicht vom Nutzer verlangen, den Katalog selbst zu durchsuchen.

```text
Problem / Ziel des Nutzers
→ lokale Wahrheit und verfügbare Evidence verstehen
→ Aufgabe fachlich einordnen
→ passenden Workflow prüfen
→ primären Skill-Satz wählen
→ Cross-Cutting-Kandidaten am passenden Checkpoint prüfen
→ Primärrouting bei Bedarf verfeinern statt Skills nur zu addieren
→ nur wirklich fehlende Informationen klären
→ ausführen
→ vor Completion/Output relevante Overlays erneut prüfen
→ verifizieren / reviewen / gaten
```

## Routing

### Verbindlicher Minimal-Discovery-Gate

Bei **nichttrivialen** Aufgaben sind die Routing-Schritte 3–5 echte Arbeitsphasen und kein optionaler Hintergrundhinweis. Eine bereits formulierbare Antwort aus Nutzertext oder Fixture ist **kein** Grund, Domänen-/Workflow-, Katalog- oder Cross-Cutting-Discovery zu überspringen.

Als nichttrivial gelten insbesondere Aufträge mit mehreren Kriterien oder Trade-offs, adressaten- oder voice-spezifischer Kommunikation, publikationsreifer Synthese, mehreren eigenständigen Arbeitsjobs, Security-/Admission-/Permission-Fragen, Toolnutzung, Mutation oder mehreren Arbeitsschritten.

Dafür gilt vor der eigentlichen Ausführung ein **verbindlicher Bootstrap-Read-Vertrag**:

1. `Dokumentation/Skill-Handbuch.md` tatsächlich öffnen und den passenden Routingraum bestimmen;
2. `workflow-index.yml` prüfen, wenn die Aufgabe mehrere Phasen verbindet oder ein vorhandener Workflow plausibel ist; einen passenden Workflow dann tatsächlich öffnen;
3. `skill-catalog.yml` tatsächlich öffnen oder gezielt darin suchen und die plausiblen fachlichen Owner gegen ihre Description prüfen;
4. `routing-overlays.yml` tatsächlich öffnen und die Kandidaten für den aktuellen Checkpoint bestimmen;
5. erst danach mit dem kleinsten ausreichenden Skill-Satz – einschließlich `none`, falls nach dieser Prüfung wirklich kein Skill nötig ist – ausführen.

Ein bloßer Verweis aus `AGENTS.md` auf diese Dateien zählt nicht als Discovery. Für nichttriviale Aufgaben müssen die relevanten Router-Artefakte im aktuellen Lauf wirklich gelesen oder gezielt durchsucht worden sein.

**Trivialer Direktpfad:** Eine kurze Faktenklärung, eine mechanische Kleintransformation oder eine eng begrenzte Ein-Satz-Zusammenfassung ohne Risiko, Außenwirkung oder Spezialanforderung darf nach Auftrag + lokaler Wahrheit direkt beantwortet werden. Dafür muss kein künstlicher Skill gesucht werden.

Kurz: `none` ist ein gültiges Routing-Ergebnis, aber bei nichttrivialen Aufgaben kein ungeprüfter Default-Bypass.

1. **Nutzerauftrag lesen.** Problem, gewünschtes Ergebnis, Scope, Grenzen und explizite Autorisierung festhalten. Fehlende Skill-Namen sind kein fehlender Input.
2. **Lokale Wahrheit zuerst.** Projektregeln, lokale Sources of Truth, vorhandene Artefakte und Nutzerangaben schlagen allgemeine Repository-Regeln. Allgemeine Arbeitsweise ist zentral; konkrete Wahrheit bleibt lokal.
3. **Aufgabe einordnen.** Aus dem realen Problem geeignete Domäne(n) und vorhandene Workflows ableiten. Nutze `Dokumentation/Skill-Handbuch.md` als Master-Router und `workflow-index.yml` für vorhandene Workflows. Bei nichttrivialen Aufgaben den Master-Router im aktuellen Lauf tatsächlich öffnen; wenn ein Workflow plausibel ist, den Index und anschließend den Workflow öffnen.
4. **Primären Skill-Satz wählen.** Nutze `skill-catalog.yml`; lade nur die fachlich tatsächlich benötigten `SKILL.md`-Dateien und deren zwingende Abhängigkeiten. `related` ist ein Routinghinweis, kein Ladebefehl. Bei nichttrivialen Aufgaben den Katalog im aktuellen Lauf tatsächlich öffnen oder gezielt durchsuchen und mindestens die plausiblen Owner gegen ihre Description prüfen, bevor `none` gewählt wird. Nennt ein geladener Workflow einen Skill ausdrücklich als **Kern**, **Primary Owner** oder zwingenden Schritt, muss dessen `SKILL.md` vor einem generischeren Ersatzkandidaten gelesen werden. Ein Ersatz ist nur zulässig, wenn die kanonische Description oder Near-Miss-Grenze den Kernskill für den konkreten Auftrag ausschließt.
5. **Cross-Cutting-Checkpoints anwenden.** `routing-overlays.yml` ist bei nichttrivialen Aufgaben im aktuellen Lauf tatsächlich zu öffnen. Prüfe an den dort genannten Checkpoints ausschließlich die kanonische Description der registrierten Kandidaten. Ein Cross-Cutting-Check darf nicht allein deshalb entfallen, weil der fachliche Inhalt schon formulierbar wäre. Für `pre-completion` und `pre-output` die Registry erneut konsultieren; wenn seit dem ersten Pass kein relevanter Overlay-Kandidat gelesen wurde, die Datei erneut öffnen statt sich auf eine implizite Erinnerung zu verlassen.
6. **Primary verfeinern statt aufblasen.** Wenn ein Overlay-Kandidat laut eigener Description der spezifischere Primärowner für den Auftrag ist, darf er einen vorläufig gewählten generischen Skill ersetzen. Beide bleiben nur aktiv, wenn jeder einen eigenen notwendigen Job besitzt. Vor dem Zusammenfallen auf genau einen Skill die expliziten Teiljobs des Auftrags kurz trennen: besitzt ein zweiter Kandidat einen eigenständigen, im Auftrag tatsächlich vorhandenen Job, muss auch dessen Description geprüft werden. Das gilt besonders, wenn fachliche Wirkung und Form/Voice, Synthese und Assurance oder Inhalt und Darstellung getrennte Anforderungen sind.
7. **Nur notwendige Lücken klären.** Frage nach Informationen, die für eine belastbare Bearbeitung wirklich fehlen. Wenn eine Nutzerantwort, ein Toolergebnis, eine gefundene Datei, eine Scope-Änderung oder ein Fehlschlag einen für eine bereits geprüfte Skill-Description relevanten Sachverhalt materiell ändert, prüfe genau diesen Kandidaten erneut. Dieses ereignisgesteuerte Re-Entry ist kein zusätzlicher globaler Checkpoint und kein Anlass für einen vollständigen Katalogscan.
8. **Vor Ausführung prüfen.** `maturity`, `eval_coverage`, `capabilities` und `related` im Katalog sowie die Skill-Frontmatter beachten. Toolverfügbarkeit ist keine Autorisierung.
9. **Capability-Runtime wählen.** Wenn eine externe App, ein Account oder ein Dienst materiell helfen würde, zuerst native Capabilities und bereits verbundene Plugins/Apps prüfen. READ, WRITE und extern sichtbare ACTIONS getrennt behandeln.
10. **Pre-Execution-Security nach Objekt und Job schneiden.** `skill-security-review` ist Owner für Admission eines externen oder mächtigen **Skill-Bundles** und umfasst dessen Berechtigungsrisiken. `tool-permission-review` zusätzlich nur laden, wenn das Berechtigungsdesign selbst einen eigenständigen Prüfauftrag bildet. Für eigenständige MCP-Server, Plugins, Connectors oder Hooks gilt die Baseline aus `Sicherheit/MCP-und-externe-Tools.md`; dort `tool-permission-review` für den Capability-/Rechte-Scope und `prompt-injection-review` nur bei tatsächlich instruktionshaltigem oder verdächtigem untrusted Input verwenden. Ein Nicht-Skill wird nicht allein wegen seiner Externalität zu `skill-security-review` geroutet. Liefert ein Plugin oder Paket Skills mit, ist es als Ganzes ein Skill-Bundle.
11. **Ausführen.** Fachliche Wahrheit nicht aus allgemeinen Regeln erfinden. Riskante oder externe Aktionen nur innerhalb der ausdrücklich vorhandenen Rechte/Gates.
12. **Vor Completion und Output erneut prüfen.** Späte Trigger dürfen nicht verloren gehen: Prüfe an den Checkpoints `pre-completion` und `pre-output` die in `routing-overlays.yml` dafür registrierten Kandidaten gegen ihre kanonische Description. Beispiele: Ein Citation-Audit kann erst nach Entstehung einer weitgehend fertigen Synthese sinnvoll werden; eine visuelle Antwort kann durch die tatsächlich entstandene Informationsdichte erst am Ende relevant werden.
13. **Verifizieren.** Ergebnis gegen Auftrag, lokale Sources of Truth, relevante Evals/Checks und Skill-Grenzen prüfen.
14. **Review/Gate.** Offene Annahmen, Blocker, nicht ausgeführte Prüfungen und notwendige menschliche Freigaben sichtbar machen.

## Kommunikation der Skill-Auswahl

Die interne Werkzeugauswahl soll dem Nutzer helfen, nicht zusätzliche Bedienlast erzeugen.

- Bei einfachen Aufträgen genügt eine knappe Begründung der gewählten Arbeitsweise.
- Bei größeren oder risikoreicheren Aufträgen den verwendeten Workflow beziehungsweise die wichtigsten Skills transparent nennen.
- Keine lange Skill-Liste als Selbstzweck ausgeben.
- Wenn kein Skill erforderlich ist, die Aufgabe direkt und innerhalb der allgemeinen Regeln bearbeiten.

## Minimaler Kontext

Typischer Startkontext:

- `AGENTS.md`;
- relevante lokale Projektregeln / Sources of Truth;
- bei **nichttrivialen** Aufgaben als kleiner obligatorischer Router-Satz: `Dokumentation/Skill-Handbuch.md`, passende Nutzung von `workflow-index.yml`, `skill-catalog.yml` und `routing-overlays.yml`;
- danach nur die tatsächlich ausgewählten Skills bzw. Workflows.

Der obligatorische Router-Satz bedeutet **nicht**, alle Skills zu laden. Er soll gerade verhindern, dass ein Agent ohne Discovery direkt aus der Fixture antwortet oder zufällig einen benachbarten Owner auswählt.

Nicht erforderlich: komplettes Repository, alle katalogisierten Skills, vollständige Nutzungsdokumentation oder alle Fachhandbücher.

## Repository-Validierung

Bei Änderungen am Repository den vorhandenen lokalen Validation Harness bevorzugen. Keine systemweit installierte Python-Runtime voraussetzen.

Unter Windows:

```powershell
.\Validate-KI-Regeln.ps1 -Quick
```

Für breitere Prüfungen je nach Scope `-Full` oder `-Release` verwenden. Details stehen in `Dokumentation/Local-Validation-Harness.md`.

Die vorhandenen Python-Validatoren bleiben kanonische Prüflogik hinter dem Harness. Wenn die vorgesehene Prüfung in der aktuellen Laufzeit nicht ausgeführt werden kann, den Status als `NOT RUN` beziehungsweise `UNVERIFIED` sichtbar machen statt einen Pass zu behaupten.

## Harte Grenzen

- Keine Maturity-Hochstufung aus Plausibilität oder wenigen Beispielen ableiten.
- Keine Evals als bestanden darstellen, die nicht ausgeführt wurden.
- Einen Fertig-, PASS- oder Erfolgsclaim nur so weit abgeben, wie **frische Evidence für genau den behaupteten Zustand** trägt. Ist ein relevanter Check nicht ausführbar, den Status als `NOT RUN`, `UNVERIFIED`, `BLOCKED` oder lokal gleichwertig sichtbar machen. Dafür ist kein `verification-loop` nötig, wenn keine iterative Arbeiten-Prüfen-Korrigieren-Schleife vorliegt.
- Keine externen Quellen automatisch synchronisieren.
- Keine produktiven Writes, Deployments, Veröffentlichungen oder sonstigen Außenaktionen aus bloßer Tool-, Plugin- oder App-Verfügbarkeit ableiten.
- Eine vorhandene Plugin-/App-Verbindung erweitert Capability, nicht automatisch Autorisierung.
- Bei nichttrivialen Aufgaben Routing-Schritte 3–5 nicht nur deshalb überspringen, weil ohne weitere Discovery bereits eine plausible Antwort formulierbar ist; Master-Router, Katalog und Overlay-Registry müssen im aktuellen Lauf tatsächlich gelesen oder gezielt durchsucht werden.
- Externe Skills nur entsprechend dokumentierter Provenance und Lizenzlage übernehmen oder weiterverteilen.
