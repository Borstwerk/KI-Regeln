# Cross-Cutting Skill Discovery und Routing Overlays

## Problem

Problem-first Routing beantwortet zuerst:

> Welcher fachliche Skill bearbeitet den eigentlichen Auftrag?

Bei einem größeren Skillbestand entsteht zusätzlich:

> Gibt es einen domänenübergreifenden Skill, den der Nutzer nicht kennen muss, der das Ergebnis materiell verbessert, absichert oder das vorläufige Routing präzisiert?

Diese zweite Entdeckung ist Systemarbeit. Sie darf weder dem Nutzer zugeschoben werden noch den aktiven Skill-Satz aufblasen.

## Grundprinzip

> Der Werkzeugschrank darf groß sein. Der aktive Werkzeuggürtel soll klein bleiben.

Cross-Cutting Discovery besteht deshalb aus **wenigen Kandidaten** und **mehreren kleinen Checkpoints** statt aus einem vollständigen zweiten Katalogscan.

## Warum ein einmaliger Overlay-Pass nicht genügt

Einige Trigger sind schon am Anfang sichtbar:

- konkrete Empfänger-/Hierarchiesituation;
- externer oder mächtiger Skill;
- neue Schreib-/Execute-/Produktionsrechte;
- iterativer Implementierungsauftrag mit reproduzierbaren Checks.

Andere Trigger entstehen erst während der Arbeit:

- `citation-audit` braucht eine fertige oder weitgehend fertige Research-Synthese;
- `visual-answer` kann erst anhand der tatsächlich entstandenen Informationsdichte sicher sinnvoll werden.

Darum gilt:

~~~text
PRIMARY
→ POST-PRIMARY
→ PRE-EXECUTION
→ EXECUTION
→ PRE-COMPLETION
→ PRE-OUTPUT
→ COMPLETION
~~~

Nicht jeder Auftrag nutzt jeden Checkpoint. Geprüft werden nur die wenigen Kandidaten, die in `routing-overlays.yml` für diesen Checkpoint eingetragen sind.

## routing-overlays.yml

Die Datei ist **Discovery-Metadaten**, keine Triggerwahrheit.

Sie enthält:

- `skill` – kanonische Skill-ID;
- `phase` – Cross-Cutting-Rolle;
- `checkpoints` – Zeitpunkte, an denen die Description erneut geprüft werden soll.

Beispiel:

~~~yaml
- skill: citation-audit
  phase: assurance
  checkpoints: [pre-completion]
~~~

Das bedeutet ausschließlich:

> Wenn ein Auftrag den Pre-Completion-Zustand erreicht, prüfe kurz die kanonische Description von `citation-audit` gegen das jetzt vorhandene Ergebnis.

Es bedeutet nicht, den Skill automatisch zu aktivieren, Triggertexte zu duplizieren oder fehlende Capability zu simulieren.

## Checkpoints

### post-primary

Direkt nach dem vorläufigen fachlichen Routing. Hier kann ein domänenübergreifender Zusatznutzen sichtbar werden oder ein **spezifischerer Primärowner** entdeckt werden.

Beispiel:

~~~text
"Schreib meinem Chef, dass ich A oder B schaffen kann,
aber nicht beides. Er soll priorisieren."

vorläufig:
→ natuerliches-schreiben

post-primary:
→ adressatengerechte-kommunikation ist der spezifischere Owner

Ergebnis:
→ adressatengerechte-kommunikation
→ natuerliches-schreiben nur zusätzlich bei eigenem Voice-/Rewrite-Job
~~~

### pre-execution

Vor Toolnutzung, Änderungen, externer Aktivierung oder iterativer Ausführung.

Typische Kandidaten:

- `verification-loop`;
- `skill-security-review`;
- `tool-permission-review`.

Hier müssen Rechte und Gates stehen, bevor der erste riskante Schritt passiert.

### pre-completion

Wenn ein Ergebnis weitgehend vorliegt, aber noch kein Fertig-/Pass-/Publikationsclaim abgegeben wurde.

Typischer Kandidat: `citation-audit`.

~~~text
research-synthesis erzeugt Draft
→ pre-completion
→ citation-audit prüft wichtige Claims gegen tatsächliche Evidence
→ erst danach Completion/Publication-Readiness behaupten
~~~

### pre-output

Unmittelbar vor der finalen Darstellung.

Typischer Kandidat: `visual-answer`.

Der Skill darf bereits `post-primary` ausgewählt worden sein. `pre-output` ist die zweite Chance, wenn erst das entstandene Ergebnis zeigt, dass Vergleich, Hierarchie, Timeline, Findings oder Abhängigkeiten visuell wesentlich schneller erfassbar wären.

## Ereignisgesteuertes Re-Entry

Checkpoints werden nicht bei jedem Zwischenschritt wiederholt. Ein bereits geprüfter oder verworfener Kandidat wird nur dann erneut bewertet, wenn **neue Evidence einen für seine Description relevanten Sachverhalt materiell verändert**.

Typische Re-Entry-Ereignisse:

- eine Nutzerantwort klärt Empfänger, Hierarchie, Ziel oder Scope;
- ein Toolergebnis zeigt neue Rechte, neue Datenquellen oder einen anderen Zielzustand;
- eine gefundene Datei verändert die lokale Wahrheit;
- ein Fehlschlag erzwingt echtes Re-Planning;
- Output-Typ oder Evidence-Anforderung ändert sich materiell.

Nicht ausreichend sind bloß mehr Text, ein weiterer interner Gedankenschritt oder die Hoffnung, dass ein zusätzlicher Skill helfen könnte.

Re-Entry ist **kein fünfter globaler Checkpoint** und kein vollständiger Katalogscan. Neu geprüft werden nur Kandidaten, deren kanonische Description durch den neuen Fakt plausibel anders beantwortet werden könnte.

## Addieren oder Primärrouting verfeinern?

Overlay bedeutet nicht automatisch `Primary + Overlay`.

**Add:** Der Overlay-Skill besitzt einen eigenen zusätzlichen Job, etwa `architecture-tradeoff-analysis + visual-answer`.

**Refine / Replace:** Der Overlay-Kandidat ist für den konkreten Auftrag der spezifischere Owner als ein vorläufig gewählter generischer Skill. Dann wird der redundante generische Skill entfernt, solange kein eigener Job übrig bleibt.

Regel:

> Zwei Skills bleiben nur aktiv, wenn jeder einen eigenständigen notwendigen Beitrag liefert.

## Security-Deduplizierung

`skill-security-review` und `tool-permission-review` überschneiden sich absichtlich an der Permission-Grenze, haben aber unterschiedliche Ownership.

`skill-security-review` ist Owner, wenn ein externer oder mächtiger **Skill** aufgenommen/aktiviert werden soll. Bundle, Provenance, Scripts, Remote Dependencies, Prompt Injection, Datenfluss, Rechte und Admission gehören zusammen.

`tool-permission-review` wird **zusätzlich** nur benötigt, wenn das Berechtigungsmodell selbst einen eigenständigen Design-/Reviewgegenstand bildet, etwa mehrere Tools/Rechte unabhängig vom Skill-Bundle gegeneinander abgewogen werden.

Eigenständige MCP-Server, Plugins, Connectors oder Hooks sind keine Skill-Bundles. Ihre allgemeine Admission-Baseline steht in `Sicherheit/MCP-und-externe-Tools.md`. Für deren Capability-/Rechte-Scope ist `tool-permission-review` der passende Spezialskill; `prompt-injection-review` kommt nur hinzu, wenn konkrete externe Inhalte oder Toolmetadaten eine eigene Trust-Boundary-/Injection-Prüfung rechtfertigen.

Nicht:

~~~text
externer Skill fordert Shell + Netzwerk
→ automatisch beide Security-Skills
~~~

Sondern:

~~~text
Admission eines externen Skills
→ skill-security-review

separater Permission-Architecture-Job?
→ ja: zusätzlich tool-permission-review
→ nein: kein Duplikat
~~~

## No-Skill ist ein gültiges Routing-Ergebnis

Ein guter Router muss nicht nur den richtigen Skill finden, sondern unnötige Skills vermeiden.

~~~text
"Was bedeutet HTTP 404?"

PRIMARY
→ none

OVERLAYS
→ none

ERGEBNIS
→ direkte kurze Antwort
~~~

Golden Tasks dürfen deshalb `required_skills: []` und `expected_domain: none` verwenden, wenn genau diese Zurückhaltung geprüft werden soll. Fixtures oder lokale Sources of Truth dürfen trotzdem vorhanden sein, wenn die Aufgabe sie direkt lesen kann, ohne dass daraus automatisch ein spezieller Skillbedarf entsteht.

## Algorithmus für einen frischen Agenten

1. Nutzerproblem und lokale Wahrheit bestimmen.
2. Primärdomäne/Workflow problem-first wählen.
3. Kleinsten fachlich ausreichenden Primärskill-Satz wählen – einschließlich `none`.
4. Am `post-primary`-Checkpoint nur dafür registrierte Overlay-Kandidaten gegen ihre Description prüfen.
5. Falls ein Kandidat spezifischerer Owner ist, Primärrouting verfeinern und redundanten generischen Skill entfernen.
6. Nur materiell fehlende Informationen klären. Ändert eine Antwort einen Description-relevanten Sachverhalt, genau dafür Re-Entry auslösen.
7. Am `pre-execution`-Checkpoint Verification-/Security-Kandidaten prüfen und Rechte/Gates klären.
8. Aufgabe ausführen. Bei materieller Scope-, Capability-, Evidence- oder Planänderung ereignisgesteuert re-routen statt alle Overlays erneut zu scannen.
9. Am `pre-completion`-Checkpoint späte Assurance-Trigger gegen das jetzt vorhandene Ergebnis prüfen.
10. Am `pre-output`-Checkpoint Presentation-Kandidaten gegen die tatsächliche Informationsform prüfen.
11. Completion Claim nur auf frische Evidence für genau den behaupteten Zustand begrenzen; dafür nicht automatisch einen Verification Loop erfinden.

## Anti-Bloat-Regel

Typischer Auftrag:

~~~text
0–1 fachlicher Primärowner
+ nur notwendige zusätzliche Fachskills
+ 0–1 Presentation/Communication-Overlay
+ nur eigenständig begründete Assurance-/Security-Overlays
~~~

Die Zahlen sind kein hartes Limit. Sie sind ein Warnsignal gegen „mehr Skills = bessere Antwort“.

## Evalstrategie

Cross-Cutting Routing braucht systemische Fälle, nicht nur isolierte Skill-Evals. Mindestens testen:

- Positive Discovery ohne genannten Skillnamen;
- Near-Miss: Overlay muss schweigen;
- Primary Refinement statt Add-Bloat;
- späten Pre-Completion-Trigger;
- Security-Deduplizierung;
- No-Skill Control;
- fehlende Capability ohne vorgetäuschte Ausführung.

Die Golden Tasks `GT-09` bis `GT-17` decken diese Routingklasse als Startset ab. Definition ist kein Behavioral-Pass-Nachweis.

## Leitgedanke

> Ein Skill ist gut entdeckt, wenn er bei seiner Aufgabe zuverlässig erscheint, bei der Nachbaraufgabe zuverlässig schweigt und keinen redundanten Kollegen mitbringt.
