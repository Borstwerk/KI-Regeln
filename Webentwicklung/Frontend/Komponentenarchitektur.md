# Komponentenarchitektur

## Zweck

Dieses Dokument beschreibt allgemeine Regeln für wartbare Frontend-Komponenten.

Ziel ist nicht maximale Abstraktion. Ziel ist eine Struktur, die lokale Änderungen ermöglicht, Zuständigkeiten sichtbar hält und unnötige Konfigurationskomplexität vermeidet.

## Grundregel

> Komposition vor Konfigurationsexplosion.

## 1. Komponenten nach Verantwortung schneiden

Eine Komponente sollte einen nachvollziehbaren Zweck haben.

Warnsignale:

- sehr viele Boolean-Props;
- unverbundene Darstellungsmodi in einer Komponente;
- Datenzugriff, Fachlogik und Präsentation untrennbar vermischt;
- wiederkehrende `if`-Kaskaden für Sonderfälle;
- Props, deren Bedeutung nur im Zusammenspiel mit mehreren anderen Props klar wird.

## 2. Varianten explizit machen

Statt viele unabhängige Flags zu kombinieren, lieber klare Varianten oder Zusammensetzungen verwenden.

Schwach:

```text
isCompact
showHeader
showFooter
isEditing
showActions
isDark
```

Stärker kann sein:

- klar benannte Variante;
- Compound Components;
- Slots;
- Composition über Children;
- getrennte Komponenten für fachlich verschiedene Fälle.

Nicht jede Abweichung rechtfertigt eine neue Komponente. Entscheidend ist semantische Trennung.

## 3. UI und Zustand nicht unnötig koppeln

Wiederverwendbare Darstellung sollte nicht ohne Grund an einen bestimmten Datenzugriff oder globalen Store gebunden sein.

Prüfen:

- Kann Darstellung über Daten/Callbacks beschrieben werden?
- Muss diese Komponente wirklich den Fetch selbst besitzen?
- Ist der Zustand lokal, gemeinsam oder serverseitig?
- Ist State höher gezogen als nötig?

## 4. Fachbegriffe im Komponentenmodell respektieren

Komponenten sollen bestehende Domänenbegriffe nutzen, wenn sie tatsächlich Fachobjekte darstellen.

Keine neue UI-Terminologie erfinden, die die Fachlogik verschleiert.

## 5. Abstraktion aus Wiederholung oder stabiler Struktur ableiten

Nicht vorsorglich ein universelles Komponentenframework bauen.

Eine Abstraktion ist eher gerechtfertigt, wenn:

- Verhalten mehrfach vorkommt;
- Unterschiede klar beschreibbar sind;
- gemeinsame Invarianten stabil sind;
- spätere Änderung dadurch tatsächlich einfacher wird.

## 6. Designsystem-Komponenten sind keine Seitenarchitektur

Button, Input oder Surface sind Basiskomponenten.

Produktkomponenten dürfen darüber hinaus fachliche Bedeutung tragen.

Nicht jede Seite aus rein generischen Container/Card/Stack-Komponenten zusammensetzen, wenn dadurch Struktur und Fachbezug verschwinden.

## 7. Server- und Clientgrenzen bewusst wählen

Bei Frameworks mit Server-/Client-Komponenten oder vergleichbaren Laufzeitgrenzen:

- Clientcode nur dort, wo Interaktion oder Browserfähigkeit nötig ist;
- Daten möglichst dort laden, wo sie sinnvoll verfügbar sind;
- unnötige Serialisierung und Hydration vermeiden;
- Frameworkregeln lokal dokumentieren.

## 8. Abhängigkeiten begrenzen

Neue UI-Bibliotheken, State-Frameworks oder Utility-Pakete nicht nur wegen eines kleinen Features hinzufügen.

Prüfen:

- existiert bereits eine Lösung im Projekt?
- ist die neue Abhängigkeit langfristig gerechtfertigt?
- beeinflusst sie Bundle, Architektur oder Stylingmodell?

Breite Architekturentscheidungen benötigen das entsprechende Gate.

## 9. Testbarkeit als Strukturhinweis

Wenn Kernverhalten nur durch riesige End-to-End-Tests prüfbar ist, kann die Struktur zu stark gekoppelt sein.

Umgekehrt nicht jede reine Darstellungseinheit mit künstlicher Testlogik aufblasen.

## Qualitätscheck

1. Hat jede größere Komponente einen klaren Zweck?
2. Gibt es Boolean-Prop-Explosion?
3. Werden fachlich unterschiedliche Fälle künstlich zusammengehalten?
4. Sind State- und Datenzugriffsgrenzen nachvollziehbar?
5. Entstehen Abstraktionen aus echtem Bedarf?
6. Sind Client-/Servergrenzen bewusst?
7. Werden neue Abhängigkeiten begründet?
8. Bleibt die Struktur für spätere Agenten und Menschen lesbar?

## Leitgedanke

> Gute Komponentenarchitektur reduziert Entscheidungschaos. Sie versucht nicht, jede denkbare Zukunft vorab zu abstrahieren.