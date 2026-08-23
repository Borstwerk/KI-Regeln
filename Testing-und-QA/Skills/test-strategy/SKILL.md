---
name: test-strategy
description: Entwickelt für ein Feature, System oder eine Änderung eine risikobasierte Teststrategie und ein sinnvolles Testportfolio. Verwenden bei Fragen wie „Wie sollen wir das testen?“, „Welche Tests brauchen wir?“ oder wenn Testebenen und Qualitätsevidence geplant werden müssen. Nicht für das Schreiben eines einzelnen konkreten Testfalls verwenden.
---

# Test Strategy

## Ziel

Aus Risiken und benötigter Confidence ein begründetes Testportfolio ableiten.

## Eingaben

Möglichst:

- Anforderung / Scope;
- relevante Invarianten und Nutzerflows;
- Architektur- und Systemgrenzen;
- bekannte Risiken / Failure Modes;
- bestehende Tests und verfügbare Testumgebungen;
- lokale Release-/Qualitätsanforderungen.

Fehlende Fakten nicht erfinden.

## Arbeitsweise

1. Zu prüfenden Scope klar begrenzen.
2. Kritische Verhaltensweisen, Invarianten und Failure Modes identifizieren.
3. Risiken qualitativ priorisieren.
4. Für jedes relevante Risiko die kleinste Testebene wählen, die es zuverlässig erkennen kann.
5. Prüfen, ob zusätzliche Integration-/Contract-/E2E-Evidence einen echten Mehrwert liefert.
6. Testdaten-, Isolation-, Capability- und Umgebungsbedarf benennen.
7. Manuelle/explorative Prüfung ergänzen, wenn Automatisierung nicht ausreichend ist.
8. Abschluss- und Evidence-Kriterien definieren.
9. Restunsicherheit sichtbar lassen.

## Ausgabe

```text
Scope
Risiken / Failure Modes
Testziele
Testportfolio nach Ebene
Testdaten / Umgebung
Automatisierung
manuelle / explorative Prüfungen
Evidence-Kriterien
Restunsicherheit
```

## Regeln

- keine starren Prozentquoten für Testebenen;
- Coverage-Ziel nicht ohne fachlichen Grund als Qualitätsziel setzen;
- E2E nicht verwenden, wenn eine kleinere Ebene dasselbe Risiko zuverlässiger prüft;
- Teststrategie autorisiert keine Releaseentscheidung;
- Security-/Performance-/Chaos-Spezialprüfungen nur einplanen, nicht ohne passenden Skill vertiefen.

## Related

- `test-design`
- `integration-testing`
- `contract-testing`
- `e2e-testing`
- `failure-testing`
- `exploratory-testing`
- `test-suite-review`