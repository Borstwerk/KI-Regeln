---
name: database-operations
description: Plant oder prüft Datenbankbetrieb rund um Connections, Pooling, Ressourcen, Backup, Restore, Recovery und kontrollierte Maintenance. Verwenden bei Connection Exhaustion, Backup-/Restore-Planung, Betriebsproblemen oder administrativen Datenbankaktionen. Nicht für reine Query-Optimierung verwenden.
compatibility: Für reale Betriebsaktionen sind Engine-/Plattformversion, Zielumgebung und lokale Berechtigungen/Runbooks erforderlich. Standardmäßig read-only diagnostizieren.
---

# Database Operations

## Ziel

Datenbankbetrieb sicher und evidenzbasiert analysieren oder planen, ohne Diagnose automatisch in privilegierte Aktionen eskalieren zu lassen.

## Workflow

1. Zielumgebung eindeutig bestimmen.
2. Problem-/Betriebsziel und Risikoklasse bestimmen.
3. Read-only Evidence bevorzugen.
4. Connections, Pooling, Timeouts und Ressourcen systemweit betrachten.
5. Bei Backup/Restore RPO/RTO und Restore-Teststatus prüfen.
6. Bei Maintenance Auswirkungen auf Writes, Locks und Verfügbarkeit prüfen.
7. Write-/Admin-/Recovery-Aktion exakt previewen.
8. Passendes Human Gate einholen.
9. Aktion ausführen, falls autorisiert.
10. Ergebnis technisch und fachlich verifizieren.

## Risikoklassen

```text
READ
→ Diagnose / Metadaten

WRITE / ADMIN
→ konkrete Änderung, vorher Freigabe

RECOVERY / DESTRUCTIVE
→ hartes Gate + Ziel + Restore-Punkt + Folgen
```

## Regeln

- Poolgröße nicht isoliert pro App-Instanz betrachten.
- Timeout-Erhöhung nicht als Ersatz für Diagnose.
- Backup-Existenz nicht mit Restore-Fähigkeit gleichsetzen.
- Restore über bestehende Daten niemals implizit durchführen.
- Credentials/Secrets nicht in Logs oder Antworten reproduzieren.
- Fehlende Betriebs-Capability nicht simulieren.

## Output

```text
Umgebung
Symptom / Ziel
Evidence
Risiko
empfohlene Aktion
Gate
Verifikation
Recovery-/Restrisiko
```

## Leitgedanke

> Betrieb ist kontrollierte Zustandsänderung mit Rückweg – nicht nur ein Adminbefehl.