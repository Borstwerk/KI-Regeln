# Delegation und Evidence

## Zweck

Agentenarbeit wird zuverlässiger, wenn vor der Ausführung klar ist, **was delegiert wird**, **welche Grenzen gelten** und **welcher Nachweis am Ende erwartet wird**.

Ein Delegation Contract beschreibt den Arbeitsauftrag. Ein Evidence Bundle beschreibt anschließend, wodurch das Ergebnis überprüfbar wird.

## Grundprinzip

> Delegation ohne Abnahmekontext ist nur Arbeitsverteilung. Gute Delegation macht das Ergebnis prüfbar.

Nicht jede Kleinigkeit braucht einen formalen Vertrag. Je größer Scope, Risiko, Parallelität oder Übergabeaufwand, desto sinnvoller wird eine explizite Delegation.

## Delegation Contract

Vor einem relevanten Agentenlauf sollten mindestens folgende Punkte geklärt sein:

### Ziel

Welcher beobachtbare Zustand soll erreicht werden?

Nicht nur:

> Verbessere den Import.

Sondern beispielsweise:

> Fehlerhafte Datensätze werden abgewiesen, gültige Datensätze bleiben unverändert importierbar und der bestehende Dateivertrag bleibt kompatibel.

### Scope

Was gehört ausdrücklich zum Auftrag und was nicht?

- betroffene Bereiche oder Komponenten;
- erlaubte Änderungen;
- ausgeschlossene Bereiche;
- unveränderliche Verträge oder Invarianten.

### Quellen der Wahrheit

Welche Dokumente, Anforderungen, Entscheidungen, Tests oder Schnittstellen sind verbindlich?

Der Contract kopiert diese Quellen nicht unnötig, sondern verweist auf sie.

### Befugnisse und Werkzeuge

Welche Aktionen sind erlaubt?

Beispiele:

- nur lesen;
- Dateien lokal ändern;
- Tests ausführen;
- neue Abhängigkeiten nur nach Freigabe;
- kein Push, Merge, Release oder Produktionszugriff.

### Erwartetes Ergebnis

Welches Artefakt soll zurückkommen?

Beispiele:

- Analyse;
- Plan;
- Codeänderung;
- Test;
- Review-Bericht;
- Entscheidungsvorlage;
- reproduzierbarer Fehlernachweis.

### Akzeptanzbedingungen

Woran ist erkennbar, dass der delegierte Schritt wirklich erfüllt ist?

Akzeptanzbedingungen sollten beobachtbar und möglichst überprüfbar sein.

### Geforderte Evidence

Schon vor Beginn festlegen, welche Nachweise später benötigt werden.

Beispiele:

- ausgeführte Tests;
- Diff;
- Validatorergebnis;
- Messwerte;
- Screenshot oder manueller Prüfschritt, wenn sachlich nötig;
- Zuordnung von Akzeptanzkriterium zu Nachweis.

### Stop- und Eskalationsbedingungen

Wann darf der Agent nicht selbstständig weiterarbeiten?

Beispiele:

- neue Architekturentscheidung erforderlich;
- Scope reicht nicht aus;
- Spezifikation widersprüchlich;
- notwendiger Zugriff fehlt;
- wiederholter Loop ohne Fortschritt;
- Risiko liegt außerhalb der Freigabe.

### Abnahmekontext

Wer oder was bewertet das Ergebnis anschließend?

Ein Agent muss wissen, ob sein Ergebnis beispielsweise:

- von einem Menschen reviewed wird;
- in einen nachfolgenden Graphknoten eingeht;
- ein automatisiertes Gate passieren muss;
- nur als Analyse dient und noch keine Umsetzung erlaubt.

## Evidence Bundle

Nach der Arbeit soll der Agent keinen bloßen Fertig-Status liefern, sondern ein kompaktes Nachweispaket.

Ein Evidence Bundle kann enthalten:

1. **Ergebnis** – was wurde erreicht?
2. **Scope** – welche Dateien, Komponenten oder Artefakte wurden verändert?
3. **Nachweise** – welche Tests, Checks, Messungen oder manuellen Prüfungen wurden ausgeführt und mit welchem Ergebnis?
4. **Akzeptanzmatrix** – welches Kriterium wird wodurch belegt?
5. **Abweichungen** – wo wurde vom Plan oder Contract abgewichen?
6. **Offene Punkte** – welche Prüfungen oder Entscheidungen stehen noch aus?
7. **Risiken und Unsicherheiten** – was ist nicht sicher oder nur teilweise verifiziert?

## Kein Evidence-Theater

Mehr Text bedeutet nicht mehr Nachweis.

Schwache Evidence:

> Alle Tests wurden erfolgreich durchgeführt und die Implementierung ist robust.

Stärkere Evidence:

```text
ImportRejectsMalformedRows          PASS
ExistingImportFormatRoundtrip       PASS
Full test suite                     214 PASS, 0 FAIL
Manueller Upgrade-Test              offen
```

Evidence soll auf prüfbare Beobachtungen zeigen, nicht Erfolg nur sprachlich behaupten.

## Übergaben zwischen Agenten

Bei Multi-Agent- oder Graph-Arbeit ist das Evidence Bundle zugleich Übergabepunkt.

Der nächste Knoten soll nicht die komplette Denkgeschichte des vorherigen Agenten übernehmen müssen. Er benötigt:

- den bestätigten Ausgangszustand;
- relevante Artefakte;
- offene Unsicherheiten;
- die für seinen Schritt nötigen Quellen.

## Qualitätscheck

Vor einer Delegation prüfen:

1. Ist das Ziel beobachtbar statt nur allgemein formuliert?
2. Sind Scope und Nicht-Scope erkennbar?
3. Sind Quellen der Wahrheit genannt?
4. Sind Rechte und verbotene Aktionen klar?
5. Ist definiert, welcher Nachweis zurückkommen soll?
6. Gibt es Stop- und Eskalationsbedingungen?
7. Ist klar, wer oder was das Ergebnis anschließend abnimmt?

Nach der Delegation prüfen:

1. Belegt das Evidence Bundle tatsächlich die Akzeptanzbedingungen?
2. Sind offene Prüfungen sichtbar statt stillschweigend grün?
3. Ist der tatsächliche Scope nachvollziehbar?
4. Kann ein Reviewer das Ergebnis prüfen, ohne die gesamte Session rekonstruieren zu müssen?

## Leitgedanke

> Gute Agentenautonomie beginnt mit einem klaren Auftrag und endet mit überprüfbarer Evidence.