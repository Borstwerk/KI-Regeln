# Testing und QA

Dieser Bereich bündelt allgemeine, technologie- und frameworkneutrale Regeln für Softwaretesting und Qualitätsevidence.

## Ziel

> Testen soll relevantes Risiko sichtbar reduzieren und belastbare Evidence liefern – nicht bloß möglichst viele grüne Checks produzieren.

Der Bereich beantwortet insbesondere:

- welche Risiken überhaupt getestet werden sollen;
- auf welcher Testebene ein Risiko am sinnvollsten geprüft wird;
- wie Testfälle aus Anforderungen, Invarianten und Failure Modes entstehen;
- wann Test Doubles sinnvoll sind und wann reales Verhalten geprüft werden muss;
- wie Testdaten, Isolation und Determinismus hergestellt werden;
- wie Integration, Contracts und End-to-End-Flows getrennt werden;
- wie flaky Tests diagnostiziert statt nur wiederholt werden;
- wie Failure-/Recovery-Pfade getestet werden;
- wie Coverage, Mutation und andere Wirksamkeitssignale einzuordnen sind;
- wie explorative Tests und Release-Evidence aussehen können;
- wie Automatisierung und CI verlässliche, aktuelle Evidence erzeugen.

## Abgrenzung

```text
Programmieren / TDD
→ testgetriebene Implementierung in kleinen Red-Green-Schnitten

Testing und QA
→ Teststrategie, Testdesign, Testportfolio und Qualitätsevidence

Agentenarbeit / verification-loop
→ definierte Nachweise tatsächlich frisch ausführen und Ergebnisse verifizieren

Webentwicklung / visual-verification
→ visuelle, responsive und interaktive Browserqualität

Sicherheit
→ tiefgehende Security-Testmethodik

Reliability und System-Observability
→ SLOs, Runtime-Health, Incidents, Capacity und systemische Resilience-Experimente unter kontrollierten Störungen
```

Für die Grenze zwischen reproduzierbarem Failure Testing und systemischem Experiment siehe `../Reliability-und-System-Observability/Chaos-Engineering-und-Game-Days.md`.

## Grundmodell

```text
Änderung / Produktziel
        ↓
Risiken und Failure Modes
        ↓
benötigte Confidence
        ↓
kleinste geeignete Testebene
        ↓
Testdesign + Daten + Umgebung
        ↓
Ausführung
        ↓
Evidence
        ↓
Restunsicherheit / offene Risiken
        ↓
lokales Release- oder Freigabe-Gate
```

## Wichtige Grundregeln

1. **Risiko vor Testmenge.** Testtiefe folgt Risiko und benötigter Aussagekraft.
2. **Kleinste belastbare Ebene.** Nutze die kleinste Testebene, die das relevante Risiko zuverlässig erkennen kann.
3. **Verhalten vor Implementierungsdetails.** Tests sollen zugesichertes Verhalten schützen, nicht unnötig private Struktur einfrieren.
4. **Reale Abhängigkeit, wenn reales Verhalten Teil des Risikos ist.** Test Doubles dienen Kontrolle und Isolation; sie dürfen reale Verträge nicht unbemerkt ersetzen.
5. **Tests müssen reproduzierbar sein.** Versteckter globaler Zustand, Reihenfolgenabhängigkeit und willkürliche Sleeps sind Warnsignale.
6. **Retry repariert keine Flakiness.** Ein erst nach Wiederholung grüner Test bleibt ein Qualitätssignal mit Defekt.
7. **Coverage ist kein Qualitätsbeweis.** Ausführung einer Zeile beweist nicht, dass ein Test relevantes Fehlverhalten erkennen würde.
8. **Test-Evidence ist keine automatische Release-Freigabe.** Testing berichtet Qualität, Risiken und Restunsicherheit; die Releaseentscheidung bleibt beim gültigen lokalen Gate.
9. **Fresh Evidence vor Completion Claims.** Ein alter oder nur behaupteter Testlauf gilt nicht als aktueller Nachweis.

## Skills

- `test-strategy`
- `test-design`
- `integration-testing`
- `contract-testing`
- `e2e-testing`
- `flaky-test-diagnosis`
- `failure-testing`
- `exploratory-testing`
- `test-suite-review`

## Quellen

Siehe `Quellen-und-Inspirationen.md`.

Mutable Skill- und Web-Upstreams werden zusätzlich in `../Dokumentation/upstream-sources.yml` gepflegt.