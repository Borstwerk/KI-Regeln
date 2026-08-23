# Skill: runbook

## Zweck

Einen bekannten Betriebs- oder Störungsfall so dokumentieren, dass eine berechtigte Person ihn unter Zeitdruck sicher diagnostizieren, mitigieren und verifizieren kann.

## Vorgehen

1. Definiere Symptome und Impact.
2. Nenne notwendige Zugriffe, Rollen und Tools.
3. Schreibe Diagnose in klarer Reihenfolge mit erwarteten Normalergebnissen.
4. Beschreibe die kleinste sichere Mitigation zuerst.
5. Kennzeichne riskante oder destruktive Schritte deutlich.
6. Dokumentiere Verifikation nach der Maßnahme.
7. Nenne Rollback/Recovery, wenn relevant.
8. Definiere Eskalationsbedingungen.
9. Verknüpfe Incident- und Folgeprozesse.
10. Erfasse letzten Test-/Reviewstand, wenn das Projekt dies unterstützt.

## Regeln

- Keine Credentials oder sensiblen Geheimnisse in die Doku schreiben.
- Keine produktiven Hostnamen, IPs oder Schwellenwerte erfinden.
- Kein destruktiver Befehl ohne Scope, Wirkung und Sicherheitskontext.
- Fehlende Betriebsinformationen als Lücke markieren.
- Runbook nach realen Incidents und relevanten Betriebsänderungen prüfen.

## Fertig, wenn

Der Ablauf mit den vorgesehenen Rechten und Tools nachvollziehbar ausführbar ist und ein klarer Verifikations- und Eskalationsweg existiert.
