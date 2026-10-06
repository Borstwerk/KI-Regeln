# Architekturvarianten für Benachrichtigungen

## Ziel

Ein internes System soll nach abgeschlossener Verarbeitung Benachrichtigungen an nachgelagerte interne Consumer auslösen.

## Bestätigte Kriterien

Die Entscheidung soll diese Kriterien berücksichtigen:

- Betriebsaufwand;
- Fehlerisolation;
- Rückstau-/Retry-Fähigkeit;
- Kopplung zwischen Produzent und Consumer;
- Einführungskomplexität.

Es gibt **keine bestätigten numerischen Gewichtungen**. Keine Prozentwerte oder Scores erfinden.

## Option A – synchroner HTTP-Aufruf

- geringste Einführungskomplexität;
- Produzent wartet auf den Consumer;
- Consumer-Ausfall beeinflusst den Produzenten direkt;
- Retry muss im Produzenten behandelt werden;
- kein natürlicher Rückstaupuffer.

## Option B – bestehende Message Queue

- Queue-Infrastruktur existiert bereits und wird betrieben;
- Produzent und Consumer sind zeitlich entkoppelt;
- Rückstau ist sichtbar und kann abgearbeitet werden;
- Retry / Dead-Letter-Mechanik existiert;
- Consumer-Ausfall blockiert den Produzenten nicht direkt;
- zusätzliche Message-/Schema-Disziplin erforderlich.

## Option C – neue Event-Plattform

- stärkste langfristige Entkopplung und Erweiterbarkeit;
- aktuell keine Plattform vorhanden;
- höchste Einführungs- und Betriebsinvestition;
- zusätzliche Betriebs-, Governance- und Observability-Komponenten nötig;
- für den beschriebenen einzelnen Use Case ist der zusätzliche Umfang nicht als zwingend bestätigt.

## Bestätigte Randbedingung

Der aktuelle Auftrag betrifft genau diesen Benachrichtigungsfall. Eine organisationsweite Event-Strategie ist **nicht** Teil des Auftrags.
