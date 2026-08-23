# Source of Truth und Fachkorrektheit

## Zweck

Dokumentation darf keine plausible Parallelwirklichkeit zum tatsächlichen System erzeugen.

## Grundsatz

> Dokumentation beschreibt nur, was ihre Quellen der Wahrheit tatsächlich tragen.

## Typische Sources of Truth

Je nach Dokumenttyp können dies sein:

- tatsächlicher Code;
- API-Spezifikation oder Schema;
- Konfigurationsschema;
- freigegebene Architekturentscheidung;
- Produktanforderung;
- Release- oder Versionsstand;
- betrieblicher Prozess;
- getesteter Installationsweg;
- Benutzeroberfläche;
- freigegebene Terminologie.

## Beispiele

### API-Dokumentation

Bevorzugt aus einer kanonischen API-Beschreibung oder dem tatsächlichen Schema ableiten.

Prosa soll keine zweite, unabhängig gepflegte API-Wahrheit erzeugen.

### README

Installations- und Startbefehle müssen zum aktuellen Repository passen.

Nicht aus historischen Erinnerungen oder alten Blogposts rekonstruieren.

### ADR

Eine ADR dokumentiert eine tatsächliche Entscheidung oder einen echten Vorschlag im angegebenen Status.

Sie darf keine nachträglich erfundene Begründung als historischen Fakt darstellen.

### Runbook

Befehle, Rechte, Dashboards, Schwellenwerte und Eskalationswege müssen real und freigegeben sein.

Fehlende Betriebsinformationen werden als Lücke markiert, nicht erfunden.

## Quellenhierarchie

Wenn mehrere Dokumente widersprechen, gilt die projektspezifische Vorranglogik.

Allgemein sinnvoll:

```text
verbindliche Spezifikation / kanonisches Schema
→ gültige Entscheidung / Architektur
→ tatsächliche Implementierung und Tests
→ aktuelle Betriebs- oder Produktdokumentation
→ ältere Zusammenfassungen und Sekundärtexte
```

Die konkrete Reihenfolge kann projektabhängig abweichen und muss lokal definiert werden.

## „Nicht gefunden“ ist kein Gegenbeweis

Wenn eine Information nicht auffindbar ist:

- nicht behaupten, sie existiere nicht;
- nicht durch plausible Details ergänzen;
- fehlende Quelle oder Unsicherheit nennen;
- gegebenenfalls gezielt recherchieren oder nachfragen.

## Dokumentationsdrift erkennen

Warnsignale:

- Befehle existieren nicht mehr;
- Parameter wurden umbenannt;
- UI-Bezeichnungen stimmen nicht mehr;
- Architektur wurde geändert;
- Links führen zu veralteten Versionen;
- Screenshots zeigen alte Oberflächen;
- Runbook-Schritte passen nicht zum aktuellen Betrieb;
- Beispielausgaben entsprechen nicht mehr dem System.

## Versionen sichtbar machen

Wenn Verhalten versionsabhängig ist:

- Version oder Geltungsbereich nennen;
- keine zeitlosen Formulierungen verwenden, wenn sie nicht zeitlos sind;
- alte und neue Wege sauber trennen.

## Leitgedanke

> Fachliche Wahrheit kommt aus dem System und seinen kanonischen Quellen – nicht aus der Formulierungssicherheit der KI.
