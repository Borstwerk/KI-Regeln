# Testing und QA

Dieser Bereich bündelt allgemeine, technologie- und frameworkneutrale Regeln für Softwaretesting und Qualitätsevidence.

## Einstieg nach Arbeitsfrage

| Typische Frage | Passender Einstieg | Abgrenzung |
| --- | --- | --- |
| „Wie sollen wir diese Änderung testen, und welche Testebenen brauchen wir?“ | [Risikobasierte Teststrategie](Skills/test-strategy/SKILL.md) | Plant Risiken, Testportfolio und benötigte Evidence; entwirft nicht den einzelnen konkreten Testfall. |
| „Welche konkreten Fälle, Grenzwerte und Fehlerzustände muss ich prüfen?“ | [Konkrete Testfälle entwerfen](Skills/test-design/SKILL.md) | Benötigt zugesichertes Verhalten und ein belastbares erwartetes Ergebnis; ersetzt weder Strategie noch Testausführung. |
| „Wie komme ich von der Testplanung zu belastbarer Qualitätsevidence?“ | [Workflow: Teststrategie und QA](../Workflows/Teststrategie-und-QA.md) | Verbindet die Phasen bedarfsgerecht; Test-Evidence ersetzt keine Releasefreigabe. |
| „Wie führe ich die vorgesehenen Nachweise im tatsächlichen Projekt aus?“ | [Native Verifikation und Reports](Umgebungsabhaengige-Verifikation-und-Reports.md); bei iterativer Umsetzung [Verification Loop](../Agentenarbeit/Skills/verification-loop/SKILL.md) | Testentwurf und alte grüne Läufe sind keine frischen Nachweise. Ein einzelner Prüflauf erfordert nicht automatisch einen iterativen Loop. |

Diese Verweise sind Orientierung. Projektlokale Anforderungen, Testumgebung und Gates bleiben maßgeblich; nicht ausgeführte Prüfungen bleiben als solche sichtbar.

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
Requirements und Spezifikations-Engineering
→ definiert, welches Verhalten beziehungsweise welche Eigenschaft gelten soll, plus Acceptance Criteria und Verification Intent

Programmieren / TDD
→ testgetriebene Implementierung in kleinen Red-Green-Schnitten

Testing und QA
→ Teststrategie, konkrete Testfälle, Testdaten, Testportfolio, Ausführung und Qualitätsevidence

Data Engineering
→ datenfachliche Invarianten, Freshness, Completeness, Reconciliation und Publish-Evidence für Datasets und Datenflüsse

Agentenarbeit / verification-loop
→ definierte Nachweise tatsächlich frisch ausführen und Ergebnisse verifizieren

Webentwicklung / visual-verification
→ visuelle, responsive und interaktive Browserqualität

Sicherheit
→ tiefgehende Security-Testmethodik

Reliability und System-Observability
→ SLOs, Runtime-Health, Incidents, Capacity und systemische Resilience-Experimente unter kontrollierten Störungen
```

Requirements und Spezifikations-Engineering definiert in `../Requirements-und-Spezifikations-Engineering/` **welche beobachtbare Bedingung** als Erfüllungsabsicht gilt. Testing und QA entscheidet anschließend über konkrete Testebene, Testdesign, Daten, Environment und Automation. `Acceptance Criterion ≠ Test Case`.

Data Engineering definiert in `../Data-Engineering/` **welche datenfachlichen Zustände** für ein Dataset relevant sind und wie Reconciliation/Freshness verstanden werden. Testing und QA bleibt zuständig für allgemeines Testdesign, Testebenen und die Wirksamkeit der Teststrategie.

Für die Grenze zwischen reproduzierbarem Failure Testing und systemischem Experiment siehe `../Reliability-und-System-Observability/Chaos-Engineering-und-Game-Days.md`.

## Grundmodell

```text
bestätigte Anforderungen / Änderung / Produktziel
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

## Projektabhängige Ausführung und Reporting

`Umgebungsabhaengige-Verifikation-und-Reports.md` konkretisiert, wie ein Agent die native Projekt-Testumgebung erkennt, welche Rechte er vor der Ausführung prüfen muss und wie Ergebnisse optional technologieunabhängig nach `../Schemas/verification-run.schema.json` dokumentiert werden. Kein zusätzlicher Test-Runner und keine pauschale Python-Pflicht.

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
