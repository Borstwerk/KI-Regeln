# RPC, IDL und Protobuf-Verträge

## Einordnung

IDL-basierte RPC-Systeme erzeugen häufig Code und besitzen sowohl Wire- als auch Source-Verträge. Deshalb reicht ein reiner Schema-Diff nicht.

## Protobuf als wichtiges Beispiel

Für Protocol Buffers sind unter anderem contractrelevant:

- Package und Symbolnamen;
- Service-/Methodennamen;
- Request-/Response-Messages;
- Field Numbers;
- Field Types und Presence;
- Enums;
- oneof;
- reserved Numbers/Names;
- Streamingart;
- generierter Clientcode.

## Wichtige Evolutionsregel

Bereits verwendete Field Numbers nicht wiederverwenden. Gelöschte Nummern und bei Bedarf Namen reservieren.

Eine Änderung kann binär wire-kompatibel und trotzdem source-incompatible sein, zum Beispiel durch generierten Code oder Datei-/Importänderungen.

## Rollout-sensitive Änderungen

Manche Änderungen können technisch lesbar bleiben, aber nur mit kontrollierter Deploymentreihenfolge sicher sein. Diese gehören in `ROLLOUT-SENSITIVE`, nicht pauschal in `COMPATIBLE`.

## gRPC

Bei gRPC gehören zusätzlich zur Schnittstelle:

- unary vs. streaming;
- Deadline-/Cancellation-Erwartungen;
- Status-/Fehlermodell;
- Metadata;
- Retry nur nach lokal definierter Methodensemantik.

## Storage ≠ API Message

Protobuf-Dokumentation empfiehlt, API-Messages und Storage-Messages nicht zwangsläufig gleichzusetzen. Diese Trennung passt zum zentralen Grundsatz, öffentliche Contracts nicht aus internem Persistenzmodell abzuleiten.

## Leitgedanke

> IDL erzeugt Typen – aber Compatibility entsteht erst aus Wire, Source und Semantik zusammen.