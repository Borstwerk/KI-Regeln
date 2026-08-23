# Backup, Restore und Recovery

## Zweck

Backups sind nur dann belastbar, wenn Wiederherstellung, Zielzustand und Datenverlustfenster verstanden und getestet sind.

## Grundprinzip

> Ein Backup ist erst dann eine Recovery-Strategie, wenn Restore und Verifikation tatsächlich funktionieren.

## Vor dem Design klären

- Welche Daten müssen wiederherstellbar sein?
- Welche RPO-/RTO-Ziele gelten lokal?
- Vollbackup, inkrementell, Log-/Point-in-Time-Recovery oder andere Mechanismen?
- Sind Schlüssel, Extensions, externe Objekte oder Konfiguration ebenfalls nötig?
- Wie werden Backups verschlüsselt und geschützt?
- Wie lange werden sie aufbewahrt?
- Wie wird Restore getestet?

Konkrete Mechanismen bleiben enginespezifisch.

## Backup ≠ Restore

Regelmäßig prüfen:

```text
Backup erzeugt
→ Integrität / Vollständigkeit prüfen
→ Restore in isolierte Umgebung
→ Schema + Daten + Anwendungspfad verifizieren
→ Recovery-Zeit messen
```

Ein grüner Backup-Job allein beweist keine Wiederherstellbarkeit.

## Restore ist eine riskante Aktion

Ein Restore kann:

- bestehende Daten überschreiben;
- neuere Daten verlieren;
- falsche Umgebung treffen;
- Schema-/Versionskonflikte erzeugen;
- externe Seiteneffekte beim Wiederanlauf auslösen.

Darum vor Restore:

1. Zielsystem eindeutig identifizieren;
2. Restore-Punkt und erwarteten Datenverlust klären;
3. bestehende Daten / aktuelles Backup sichern, falls sinnvoll;
4. Anwendung / Writes passend stoppen oder isolieren;
5. Restore durchführen;
6. technische und fachliche Verifikation;
7. kontrollierter Wiederanlauf.

Realer Restore über vorhandene Daten benötigt ein hartes Human Gate.

## Disaster vs. logische Fehler

Unterscheiden:

- Infrastruktur-/Datenträgerverlust;
- versehentliche Löschung;
- fehlerhafte Migration;
- Applikationsbug mit falschen Writes;
- Security Incident / Manipulation.

Nicht jede Recovery-Strategie hilft gegen jeden Fehler gleich gut.

## Recovery-Evidence

Nach einem Test oder echten Restore dokumentieren:

```text
Restore-Quelle / Point
Zielumgebung
Dauer
technische Checks
fachliche Stichproben
bekannte Lücken
RPO/RTO-Abweichungen
```

## Leitgedanke

> Backups beruhigen. Getestete Restores beweisen.