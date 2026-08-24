# Conformance, Fitness Functions und Drift

## Zweck

Dokumentierte Architekturregeln sind Hypothesen über die gewünschte Struktur. Conformance-Evidence prüft, ob die tatsächliche Architektur diese Regeln weiterhin einhält.

## Conformance-Fragen

- stimmen Modul-/Servicegrenzen mit der implementierten Abhängigkeitsstruktur überein;
- existieren unerlaubte Dependency Directions oder Zyklen;
- greifen Consumer auf interne Oberflächen anderer Module zu;
- besitzt Zustand weiterhin die dokumentierte Ownership;
- widerspricht die aktuelle Implementierung akzeptierten ADRs;
- sind Cross-Cutting Concerns an den vorgesehenen Seams verankert;
- existieren parallele Alt- und Neupfade ohne klaren Retirement-Plan;
- sind dokumentierte Architekturviews stale.

## Fitness Functions

Eine Architecture Fitness Function ist ein automatisierter oder reproduzierbarer Check für eine konkrete Architekturregel oder ein relevantes Quality-Szenario.

Beispiele:

- Modul A darf nicht auf Interna von Modul B importieren;
- Dependency Graph muss einen definierten Layerflow einhalten;
- bestimmte Komponenten dürfen keinen direkten Datenbankzugriff besitzen;
- eine kritische Runtime-Eigenschaft wird in einem dafür geeigneten Test verifiziert.

## Regeln für Fitness Functions

1. Nur Regeln automatisieren, deren Verletzung einen realen Architektur- oder Betriebsnachteil erzeugt.
2. Die lokale Architekturentscheidung bestimmt die Regel; das Tool erfindet sie nicht.
3. Fehlermeldungen müssen Verletzung und Fundort verständlich machen.
4. Bestehende Legacyverletzungen können einen gestuften Enforcement-Pfad benötigen.
5. Ein konfigurierter Check ist erst Evidence, wenn gezeigt wurde, dass er relevante Verstöße erkennt.
6. Zu viele Fitness Functions können Architektur unnötig einfrieren.
7. Behavioral-, Reliability-, Security- oder Performancechecks bleiben fachlich bei den zuständigen Bereichen, auch wenn Architecture deren Ergebnis als Conformance-Evidence nutzt.

## Drift

Drift kann entstehen zwischen:

```text
Requirements / Drivers
↔ ADR / Soll-Architektur
↔ Dokumentation / Diagramme
↔ Code / Config
↔ Runtime-Verhalten
```

Ein Unterschied ist nicht automatisch ein Defekt. Er wird danach bewertet, ob er eine gültige Entscheidung, Invariante oder relevante Eigenschaft verletzt.

## Review vs. Fix

Architecture Conformance Review ist read-only, solange kein separater Implementierungsauftrag und kein gültiges Gate vorliegt. Findings werden nicht ungefragt repariert.

## Leitgedanke

> Eine Architekturregel wird belastbarer, wenn ihre Verletzung erkennbar ist – aber nicht jede architektonische Entscheidung muss zu einem Linter werden.