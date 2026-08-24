# Deployment-Strategien, Promotion und Rollback

## Deployment ≠ Release

```text
Build
→ Artefakt erzeugt

Deploy
→ Artefakt in Zielumgebung vorhanden

Release
→ Verhalten für Consumer/Nutzer wirksam
```

Feature Flags oder Traffic-Steuerung können Deploy und Release trennen.

## Strategiewahl

Mögliche Muster:

- recreate;
- rolling;
- blue-green;
- canary;
- shadow;
- feature-gated release.

Keine Strategie ist universell besser.

Entscheidung nach:

- Blast Radius;
- Reversibilität;
- Versionsüberlappung;
- Daten-/Contract-Kompatibilität;
- zusätzlicher Infrastrukturkomplexität;
- benötigter Health-Evidence;
- Kosten einer Fehlentscheidung.

## Promotion / Abort

Vor risikoreichen Rollouts möglichst definieren:

- Promotionkriterien;
- Pausekriterien;
- Abortkriterien;
- benötigte Signale;
- Beobachtungsfenster.

Die konkreten SLO-/Health-Schwellen kommen aus lokaler Reliability-/Produktpolicy, nicht aus diesem Bereich.

## Rollback

Rollback ist eine reale Zustandsänderung und kann eigene Risiken besitzen.

Ein Code-Rollback macht nicht automatisch rückgängig:

- Datenmigrationen;
- bereits geschriebene Daten;
- versendete Events/Nachrichten;
- externe Aktionen;
- Cache-/Indexänderungen.

## Versionsüberlappung

Rolling/Canary/Blue-Green können mehrere Versionen gleichzeitig aktiv machen. Schnittstellen, Datenmodelle und Migrationen müssen diesen Zwischenzustand tolerieren.

## Leitgedanke

> Eine Deploymentstrategie kauft kontrollierte Information, bevor der volle Blast Radius erreicht ist.