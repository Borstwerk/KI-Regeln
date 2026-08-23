# Harness Engineering für KI-Agenten

## Zweck

Harness Engineering beschreibt die Umgebung, in der ein Agent arbeitet: Regeln, Werkzeuge, Tests, Berechtigungen, Schemas, Linter, Prüfungen und andere technische Grenzen.

Ein guter Harness macht korrektes Verhalten leichter und riskantes Verhalten schwerer.

## Grundprinzip

> Wenn eine Regel automatisch überprüfbar ist, sollte sie möglichst nicht nur als Textanweisung existieren.

Textregeln bleiben wichtig. Sie sind aber schwächer als eine technische Grenze, die einen Verstoß zuverlässig erkennt oder verhindert.

## Von weich nach hart

Mögliche Formen einer Regel:

```text
Hinweis im Prompt
→ Repository-Regel
→ automatisierter Check
→ Linter / Schema / Test
→ Berechtigungsgrenze
→ technisch unmöglicher Verstoß
```

Nicht jede Regel lässt sich vollständig technisch erzwingen. Wo es möglich und sinnvoll ist, sollte die robustere Form bevorzugt werden.

## Beispiele

Statt nur zu schreiben:

> Ändere keine öffentlichen Schnittstellen ohne Freigabe.

können zusätzlich helfen:

- API-Snapshot-Tests;
- Kompatibilitätstests;
- Schema-Checks;
- Review-Gates.

Statt nur zu schreiben:

> Tests dürfen nicht abgeschwächt werden.

können zusätzlich helfen:

- Diff-Review der Testdateien;
- Mutation- oder Break-Tests bei kritischen Regeln;
- Coverage- oder Qualitätsgrenzen, sofern sie sinnvoll gewählt sind.

## Der Harness soll beobachtbar sein

Ein Agent braucht Rückmeldung darüber, ob seine Aktion erfolgreich war.

Dazu gehören je nach Aufgabe:

- Testausgaben;
- Linter- und Build-Ergebnisse;
- strukturierte Fehlermeldungen;
- Diff und Status der geänderten Dateien;
- reproduzierbare Messwerte;
- Validatoren oder Schemaprüfungen.

Eine Prüfung, deren Ergebnis der Agent nicht sehen oder interpretieren kann, hilft dem Loop nur eingeschränkt.

Für größere Workflows siehe zusätzlich `Observability-und-Traceability.md`.

## Rechte begrenzen

Agenten sollten nur die Rechte erhalten, die für den aktuellen Arbeitsschritt nötig sind.

Beispiele:

- Lesen ohne Schreiben während Analyse und Review;
- Repository-Schreibzugriff erst in der freigegebenen Umsetzungsphase;
- kein automatischer Push oder Release, wenn dafür ein Human-Gate vorgesehen ist;
- Produktionszugriff nur bei ausdrücklichem Bedarf und klarer Freigabe.

## Isolation und Blast Radius

Nicht nur Rechte, sondern auch der **Wirkungsbereich eines Fehlers** soll begrenzt werden.

Mögliche Isolationsformen:

- eigener Branch;
- eigener Git-Worktree;
- eigener temporärer Workspace;
- Container oder Sandbox;
- getrennte Testdaten;
- eingeschränkter Netzwerkzugriff;
- kurzlebige Zugangsdaten mit kleinem Berechtigungsumfang.

Ein Agent soll möglichst nur den Bereich beschädigen können, den sein Auftrag tatsächlich umfasst.

### Parallelität benötigt Isolation

Parallel arbeitende Agenten sollen nicht unkoordiniert dieselbe Working Copy, dieselben temporären Dateien oder denselben veränderlichen Zustand benutzen.

Bevor parallele Agenten gestartet werden, prüfen:

- besitzt jeder Knoten einen klar zugeordneten Workspace?
- können beide Agenten dieselben Dateien verändern?
- teilen sie veränderliche Test- oder Entwicklungsdaten?
- können Prozesse, Ports, Caches oder Artefakte kollidieren?
- ist die spätere Integration der Ergebnisse definiert?

Wenn keine ausreichende Isolation möglich ist, Arbeit lieber sequenziell ausführen.

## Least Privilege pro Arbeitsschritt

Berechtigungen können sich zwischen Phasen unterscheiden.

Beispiel:

```text
Analyse
→ lesen

Planung
→ lesen

Umsetzung
→ freigegebenen Workspace schreiben + Tests ausführen

Review
→ lesen + Diff / Checks

Release
→ nur über eigenes Gate
```

Nicht jeder Agent benötigt von Beginn an alle technisch verfügbaren Rechte.

## Externe Seiteneffekte begrenzen

Besondere Vorsicht bei Aktionen, die außerhalb des lokalen Workspaces wirken:

- Netzwerkzugriffe;
- API-Schreiboperationen;
- E-Mail oder externe Kommunikation;
- Änderungen an Cloud- oder Produktionssystemen;
- Veröffentlichung;
- Paket- oder Release-Publishing.

Solche Aktionen sollten ausdrücklich Teil des Delegation Contracts oder eines Gates sein und nicht als beiläufiges Werkzeug verfügbar werden.

## Fail closed bei wichtigen Grenzen

Wenn eine notwendige Prüfung nicht ausgeführt werden kann, darf ihr Ergebnis nicht als bestanden gelten.

Beispiele:

- externer Validator nicht erreichbar → Status offen, nicht grün;
- manueller Test noch nicht erfolgt → Freigabe offen;
- Diff-Basis unklar → Review nicht abgeschlossen.

## Harness und Agentenfreiheit

Ein guter Harness muss den Agenten nicht in jedem Detail steuern.

Er definiert Invarianten und überprüfbare Grenzen. Innerhalb dieser Grenzen darf der Agent selbstständig den einfachsten funktionierenden Weg finden.

Das reduziert Mikromanagement, ohne Kontrolle aufzugeben.

## Qualitätscheck

Bei einer wiederkehrenden Agentenaufgabe prüfen:

1. Welche Regeln existieren nur als Text, obwohl sie automatisch prüfbar wären?
2. Welche Fehler könnten technisch früh erkannt werden?
3. Sieht der Agent die Ergebnisse seiner Prüfungen?
4. Sind Schreib-, Push-, Release- und Produktionsrechte passend begrenzt?
5. Ist der Blast Radius eines fehlerhaften Agentenlaufs begrenzt?
6. Sind parallele Agenten durch Workspaces, Branches oder andere Grenzen ausreichend isoliert?
7. Sind externe Seiteneffekte ausdrücklich freigegeben statt beiläufig möglich?
8. Kann eine fehlgeschlagene Prüfung versehentlich als Erfolg interpretiert werden?
9. Erzwingt der Harness die wichtigen Invarianten, ohne unnötig konkrete Implementierungen vorzuschreiben?

## Leitgedanke

> Gute Agenten brauchen nicht nur gute Prompts, sondern eine gute Arbeitsumgebung.