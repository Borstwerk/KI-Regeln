# Teststrategie und risikobasiertes Testen

## Grundsatz

> Eine Teststrategie beginnt bei Risiken, nicht bei Frameworks oder Coverage-Zahlen.

## Ausgangspunkt

Vor der Auswahl von Tests möglichst klären:

- welches Verhalten zugesichert werden soll;
- welche Nutzer-, Geschäfts-, Daten- oder Betriebsrisiken bestehen;
- welche Failure Modes plausibel und relevant sind;
- welche Auswirkungen ein unentdeckter Fehler hätte;
- wie häufig oder wahrscheinlich das Risiko ist;
- welche Confidence für die konkrete Änderung benötigt wird;
- welche Evidence bereits existiert und welche fehlt.

## Risikoorientierung

Ein einfaches qualitatives Modell reicht oft:

```text
Risiko
≈ Auswirkung × Wahrscheinlichkeit × Entdeckungsunsicherheit
```

Das ist keine mathematische Wahrheit, sondern eine Entscheidungshilfe.

Hohes Risiko rechtfertigt typischerweise:

- mehr unabhängige Prüfperspektiven;
- realistischere Integration;
- stärkere Negativ- und Failure-Cases;
- explizite Regressionstests;
- engere Release-Evidence.

Niedriges Risiko rechtfertigt dagegen nicht automatisch eine große Testarchitektur.

## Testportfolio statt Testreligion

Nicht pauschal festlegen:

- „alles braucht Unit Tests“;
- „E2E gibt die höchste Sicherheit und ist deshalb immer besser“;
- „80 % Coverage ist ausreichend“;
- „jede Dependency muss gemockt werden“.

Stattdessen:

```text
Risiko
→ kleinste geeignete Testebene
→ zusätzliche Ebene nur wenn sie neue Evidence liefert
```

## Testziele

Für jede wichtige Prüfachse möglichst benennen:

- welches Risiko der Test adressiert;
- welches Verhalten oder welche Invariante geschützt wird;
- warum diese Testebene geeignet ist;
- welches Ergebnis als bestanden gilt;
- welche relevante Unsicherheit danach noch verbleibt.

## Regression

Ein bestätigter Defekt sollte möglichst einen reproduzierbaren Nachweis erzeugen, wenn dies wirtschaftlich und technisch sinnvoll ist.

Der Regressionstest soll den Fehlergrund oder das zugesicherte Verhalten schützen – nicht zufällige Implementierungsdetails des konkreten Fixes.

## Nicht-Ziel

Die Teststrategie entscheidet nicht automatisch über Produkt-, Architektur- oder Releasefreigaben.

Sie liefert dafür Evidence und Restunsicherheit.