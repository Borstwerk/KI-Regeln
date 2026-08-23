# Inputs, Outputs und Verträge

## Zweck

Ein Skill soll nicht nur beschreiben, welche Schritte ein Agent ausführt. Er soll auch klar machen, **welche Eingaben er benötigt und woran ein brauchbares Ergebnis erkennbar ist**.

## Eingaben

Unterscheiden:

- **required** – ohne diese Information kann die Aufgabe nicht korrekt ausgeführt werden;
- **preferred** – verbessert Qualität, ist aber nicht zwingend;
- **discoverable** – kann der Agent selbst aus Projekt oder Quellen ermitteln;
- **unknown-safe** – darf fehlen, wenn die Unsicherheit transparent behandelt wird.

Fehlende Pflichtinformation darf nicht durch plausible Erfindung ersetzt werden.

## Output-Vertrag

Ein Skill sollte definieren, was er produziert, beispielsweise:

- Reviewbericht;
- freigegebenen Plan;
- Codeänderung;
- Evidence Ledger;
- Diagnose;
- Designbrief;
- Dokumentationsentwurf.

Der Output-Vertrag soll inhaltliche Mindestanforderungen beschreiben, nicht unnötig starres Layout erzwingen.

## Evidence

Wo Qualität überprüfbar ist, gehören Nachweise zum Vertrag.

Beispiele:

- ausgeführter Test;
- konkreter Diff;
- Quellenpassage;
- Screenshot;
- Messwert;
- reproduzierbarer Befehl;
- Browserzustand.

## Status statt Scheinsicherheit

Ein Skill soll unvollständige Ergebnisse markieren können:

```text
complete
partial
blocked
unverified
conflicting
```

Die genauen Namen dürfen fachlich variieren.

## Akzeptanzbedingungen

Vor allem bei agentischer Ausführung sollen Akzeptanzbedingungen möglichst vor der Arbeit feststehen.

Beispiel:

```text
Ziel:
Fehlerursache bestimmen und kleinsten Fix validieren.

Akzeptanz:
- Bug reproduzierbar;
- Ursache durch Evidence gestützt;
- Fix beseitigt ursprüngliches Symptom;
- Regressionstest vorhanden oder fehlende Testnaht dokumentiert.
```

## Kein versteckter Scope

Der Output-Vertrag darf nicht stillschweigend zusätzliche Ziele einführen.

Ein Reviewskill darf beispielsweise Verbesserungsvorschläge liefern, aber nicht automatisch alle Funde selbst implementieren, wenn dies nicht Teil des Auftrags ist.

## Leitgedanke

> Ein Skill ist erst operationalisiert, wenn klar ist, was er braucht, was er liefert und wie das Ergebnis geprüft werden kann.
