---
name: domain-modeling
description: Fachmodellierungs-Disziplin für KI-gestützte Softwarearbeit. Verwenden, wenn Begriffe, wiederholbare Fachobjekte, Zuständigkeiten oder Modulgrenzen geklärt werden müssen.
---

# Domain Modeling

Dieser Skill dient der Analyse und Planung. Während dieser Phase wird nicht implementiert.

## 1. Quellen zuerst

Vor Modellentscheidungen lesen:

- konkrete Anforderung und Akzeptanzkriterien;
- relevante Fachplanung und Quellen;
- Architektur- und Entscheidungsdokumentation;
- bestehenden Domaincode und Persistenzmodell;
- passende Tests und Szenarien.

Alte Planung ist ein Hinweis, keine automatisch gültige Architekturentscheidung.

## 2. Begriffe schärfen

Jeden wichtigen Begriff gegen Dokumentation und Code prüfen.

Wenn dasselbe Wort zwei Dinge meint oder zwei Wörter denselben Sachverhalt beschreiben, Widerspruch offenlegen und einen kanonischen Begriff vorschlagen.

Typische Fragen:

- Ist das eine grobe Scope-Antwort oder ein echtes Fachobjekt?
- Ist der Wert aktuelle Wahrheit oder nur historische Information?
- Ist etwas eine Verantwortung, Kontrolle, Eigenschaft oder ein Datenfluss?
- Ist ein Objekt wiederholbar oder existiert es fachlich genau einmal?

## 3. Konkrete Szenarien statt abstrakter Kästen

Das geplante Modell an realistischen Fällen stressen, beispielsweise:

- einfachster zulässiger Fall;
- mehrere reale Objekte nebeneinander;
- externer Dienstleister oder Fremdsystem;
- Unknown/Open;
- historischer Altbestand;
- Objekt wird gelöscht oder ersetzt;
- veröffentlichter oder eingefrorener Zustand wird später weiterverarbeitet.

Das Modell muss diese Fälle erklären können, ohne unnötige Enterprise-Struktur zu erfinden.

## 4. Antworten versus Fachobjekte

Leitregel:

> Eine beantwortete Frage ist kein Ersatz für ein Fachobjekt, wenn derselbe reale Sachverhalt wiederholbar, referenzierbar, historisierbar oder mit anderen Objekten verknüpft werden muss.

Umgekehrt gilt:

> Nicht jede Antwort braucht einen neuen Record oder eine neue Tabelle.

Ein neues persistiertes Fachobjekt nur vorschlagen, wenn mindestens ein echter fachlicher Grund besteht, zum Beispiel:

- mehrere Instanzen müssen parallel beschrieben werden;
- andere Fachobjekte müssen stabil darauf verweisen;
- eigener Lebenszyklus oder Löschschutz;
- Snapshot- oder Historienbedeutung;
- eine einzelne Antwort würde mehrere reale Sachverhalte vermischen.

## 5. Keine zweite Wahrheit

Vor jedem neuen Feld oder Objekt prüfen, ob derselbe Sachverhalt bereits verbindlich an anderer Stelle existiert.

Wenn ja: wiederverwenden oder die Abgrenzung ausdrücklich formulieren.

Keine parallele Freitext-, Tabellen- oder Objektwahrheit aufbauen, nur weil sie lokal bequemer wäre.

## 6. Grenzen des Slices

Explizit festhalten:

- was dieser Slice übernimmt;
- was bewusst bei einer anderen Anforderung bleibt;
- was nicht Teil des aktuellen Umfangs ist;
- welche vorhandenen Objekte nur referenziert werden;
- welche Legacyfelder oder Altpfade weiter existieren und warum.

Keine Nachbarmodule vorsorglich mitbauen.

## 7. Persistenzentscheidung

Falls ein neues Fachobjekt vorgeschlagen wird, die Planung muss beantworten:

- braucht es wirklich eine Schemaänderung;
- wie verhalten sich bestehende Daten;
- ist eine deterministische Migration möglich;
- welche Heuristiken sind verboten;
- wie verhalten sich Snapshots oder historische Zustände;
- welche Ableitungs-, Backup- oder Restore-Pfade sind betroffen;
- welche Fremdschlüssel- oder Löschregeln gelten.

Keine Schemaänderung nur, weil ein neuer Begriff schöner aussieht.

## 8. Ergebnisformat

Die Analyse sollte mindestens enthalten:

1. Bestandsmatrix: Was existiert bereits?
2. zentrale Modellentscheidung mit Begründung;
3. finalen Scope und Abgrenzungen;
4. Domain- und Persistenzvorschlag nur soweit nötig;
5. Auswirkungen auf bestehendes Verhalten;
6. positive und negative Szenarien;
7. Testplan;
8. harte Diff-Grenze.

Wenn eine Entscheidung langfristig, überraschend oder schwer umkehrbar ist, eine dauerhafte Architekturentscheidung im Projekt vorschlagen.

Nach der Analyse stoppen. Umsetzung beginnt erst entsprechend dem gültigen Projektprozess.