# Security und Datenzugriff

## Zweck

Datenbankzugriffe sollen nach Least Privilege, klaren Vertrauensgrenzen und nachvollziehbaren Datenrechten gestaltet werden.

## Grundprinzip

> Anwendung, Agent und Administrator sollen nur die Daten und Operationen erreichen können, die sie tatsächlich benötigen.

## Zugriffsschichten

Je nach System können relevant sein:

- Netzwerkzugriff;
- Authentisierung;
- Datenbankrollen / Benutzer;
- Objekt-/Schema-/Collection-Rechte;
- Zeilen-/Dokument-/Tenant-Grenzen;
- Anwendungsautorisierung;
- Secrets und Credential-Lifecycle.

Keine einzelne Schicht automatisch als vollständigen Schutz betrachten.

## Least Privilege

Trennen, soweit sinnvoll:

- read-only Diagnose;
- normale Anwendungsreads;
- normale Anwendungswrites;
- Migration / DDL;
- Backup / Restore;
- Administration.

Applikationscredentials sollen keine Rechte für seltene Adminaktionen besitzen, wenn diese für den normalen Betrieb nicht nötig sind.

## Tenant- und Objektgrenzen

Bei Multi-Tenant-Systemen explizit prüfen:

- wo Tenant-Scoping technisch erzwungen wird;
- ob Hintergrundjobs dieselben Grenzen einhalten;
- ob Adminpfade bewusst getrennt sind;
- ob Queries versehentlich ohne Tenant-Filter möglich sind;
- ob Datenexporte und Backups dieselben Schutzanforderungen beachten.

Engine-spezifische Verfahren wie RLS, ACLs oder Dokumentfilter bleiben lokale Implementierungsdetails.

## Secrets

- keine Zugangsdaten in Code, Prompts oder Logs kopieren;
- getrennte Credentials nach Umgebung;
- Rotation und Widerruf ermöglichen;
- langfristige Vollzugriffs-Credentials vermeiden;
- Agenten möglichst mit read-only / begrenztem Scope starten.

## Direkter Agentenzugriff

Wenn Agenten/MCP/Tools direkt auf eine Datenbank zugreifen:

```text
Standard = read-only, wenn die Aufgabe damit erfüllbar ist

Write nötig?
→ konkrete Operation + Scope zeigen
→ explizite Freigabe

Destruktiv / Recovery?
→ hartes Gate + Zielidentität + Folgen
```

Webseiten, Query-Ergebnisse oder Dateninhalte dürfen keine neuen Befehlsrechte erzeugen.

## Datenminimierung

Diagnose und Entwicklung sollen nicht mehr Produktionsdaten abrufen als nötig.

Bevorzugen:

- Schema/Metadaten statt komplette Datensätze;
- kleine Samples;
- anonymisierte/synthetische Testdaten;
- gezielte Projektionen statt `SELECT *` / vollständige Dokumente;
- aggregierte Metriken, wenn Rohdaten nicht nötig sind.

## Auditierbarkeit

Für privilegierte Änderungen sollte nach Möglichkeit erkennbar sein:

- wer / welcher Prozess;
- wann;
- welche Operation;
- welcher Scope;
- welche Freigabe;
- welches Ergebnis.

## Leitgedanke

> Datenbankrechte werden nach Aufgabe vergeben – nicht nach dem maximal technisch möglichen Zugriff.