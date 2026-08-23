# Testautomatisierung, CI und Evidence

## Grundsatz

> Automatisierung ist wertvoll, wenn sie schnell, reproduzierbar und vertrauenswürdig Evidence erzeugt.

## Automatisieren, wenn

- der Test häufig wiederholt wird;
- Regression relevant ist;
- Ergebnis objektiv prüfbar ist;
- manuelle Wiederholung teuer oder fehleranfällig wäre;
- Testdaten und Umgebung ausreichend kontrollierbar sind.

Nicht automatisieren nur, weil ein Tool es kann.

## CI-Schichten

Ein sinnvolles Portfolio kann unterschiedliche Feedbackzeiten besitzen:

```text
sehr schnell
→ statische Checks + fokussierte Tests

schnell
→ breitere Unit-/Integrationstests

langsamer
→ ausgewählte E2E-/Contract-/Systemtests

periodisch
→ besonders teure, reale oder umfangreiche Prüfungen
```

Die konkrete Aufteilung bleibt projektspezifisch.

## Fresh Evidence

Ein Qualitätsclaim soll sich auf einen aktuellen Lauf des relevanten Nachweises beziehen.

Nicht ausreichend:

- „lief gestern“;
- „CI war vor dem letzten Commit grün“;
- „der Agent sagt, die Tests seien bestanden“;
- „nur der schnelle Teil war grün“, wenn der Claim die gesamte Suite betrifft.

## Testartefakte

Für Diagnose und Review können gespeichert werden:

- Testreports;
- Exit Codes;
- Logs;
- Traces;
- Screenshots/Videos;
- Coverage-/Mutation-Reports;
- reproduzierbare Seeds;
- betroffener Commit/Build;
- verwendete Versionen und Umgebung.

Datenschutz und Secrets beachten. Vollständige Inhalte nicht automatisch dauerhaft speichern.

## Fehlgeschlagene Tests

Ein CI-Fehler soll möglichst unterscheiden können:

```text
Produktdefekt
Testdefekt / Flake
Umgebungsdefekt
Tool-/Infrastrukturdefekt
blockierter Nachweis
```

Nicht jeden roten Job pauschal als Produktfehler interpretieren.

## Teständerungen im Review

Besonders kritisch prüfen, wenn gleichzeitig Produktionscode und bestehende Assertions geändert werden.

Tests nicht lockern, löschen oder Baselines ungeprüft aktualisieren, nur damit CI grün wird.

## Verifikation vor Abschluss

Der ausführende Agent oder Entwickler soll vor Completion Claims:

1. relevanten Nachweis identifizieren;
2. ihn frisch ausführen;
3. vollständiges Ergebnis und Exit Status prüfen;
4. Claim auf genau die tatsächlich erzeugte Evidence begrenzen;
5. fehlende oder blockierte Prüfungen offen nennen.