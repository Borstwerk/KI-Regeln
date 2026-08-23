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

## Rechte begrenzen

Agenten sollten nur die Rechte erhalten, die für den aktuellen Arbeitsschritt nötig sind.

Beispiele:

- Lesen ohne Schreiben während Analyse und Review;
- Repository-Schreibzugriff erst in der freigegebenen Umsetzungsphase;
- kein automatischer Push oder Release, wenn dafür ein Human-Gate vorgesehen ist;
- Produktionszugriff nur bei ausdrücklichem Bedarf und klarer Freigabe.

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
5. Kann eine fehlgeschlagene Prüfung versehentlich als Erfolg interpretiert werden?
6. Erzwingt der Harness die wichtigen Invarianten, ohne unnötig konkrete Implementierungen vorzuschreiben?

## Leitgedanke

> Gute Agenten brauchen nicht nur gute Prompts, sondern eine gute Arbeitsumgebung.