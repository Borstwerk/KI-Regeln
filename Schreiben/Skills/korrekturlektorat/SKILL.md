---
name: korrekturlektorat
description: Mechanisches Korrekturlektorat für fertige oder weit fortgeschrittene Texte: Rechtschreibung, Grammatik, Syntax, Zeichensetzung, Tipp-/Wortfehler und unbeabsichtigte Dopplungen prüfen oder minimal korrigieren, ohne Inhalt, Stimme oder Stil unnötig umzuschreiben. Verwenden bei Korrekturlesen, Rechtschreibprüfung, Grammatikprüfung, Komma-/Zeichensetzungsprüfung oder einem letzten sprachlichen Fehlerpass. Nicht für Stilrewrite, fachliche Faktenprüfung, Übersetzung oder Typografie als Hauptziel.
---

# Korrekturlektorat

Dieser Skill nutzt `../../Sprachrichtigkeit-und-Typografie.md`.

Leitgedanke:

> Fehler korrigieren, nicht den Text neu erfinden.

## Trigger

Typische Aufträge:

- „Lies Korrektur.“
- „Prüfe Rechtschreibung und Grammatik.“
- „Sind die Kommas korrekt?“
- „Korrigiere Tippfehler und Zeichensetzung, aber ändere meinen Stil nicht.“
- „Mach einen letzten sprachlichen Fehlerpass vor Veröffentlichung.“

## Nicht verwenden

Nicht primär verwenden für:

- stilistische oder rhetorische Qualität → `stilreview`;
- gewünschten natürlichen Rewrite → `natuerliches-schreiben`;
- Empfängerwirkung, Hierarchie oder Konfliktkommunikation → `adressatengerechte-kommunikation`;
- deutsche Anführungszeichen, Gedanken-/Bis-Striche, typografische Abstände oder Sonderzeichen als Hauptauftrag → `deutsche-typografie`;
- fachliche Richtigkeit oder Quellenprüfung → passende Fach-/Recherche-Skills;
- Übersetzung → kein stiller Ersatz durch Korrekturlektorat.

## Ablauf

1. **Scope bestimmen.** Prüfen, ob nur diagnostiziert oder auch korrigiert werden soll. Review ist keine automatische Rewrite-Freigabe.
2. **Sprachvariante und lokale Regeln bestimmen.** Nur soweit für konkrete Funde relevant; keine unnötige Rückfrage.
3. **Schutzbereiche erkennen.** Eigennamen, Fachbegriffe, Code, URLs, Pfade, Zitate, Markup und absichtliche nichtstandardsprachliche Formen schützen.
4. **Gesamttext lesen.** Nicht nur bekannte Fehlerstellen oder einzelne Sätze isoliert prüfen.
5. **Mechanischen Pass durchführen.** Orthografie, Grammatik/Syntax, Zeichensetzung, Wort-/Tippfehler und unbeabsichtigte Dopplungen prüfen.
6. **Funde klassifizieren.** Zwischen Fehler, zulässiger Variante, Projektkonvention, unklarem/bedeutungsabhängigem Fall und Stiloption unterscheiden.
7. **Nur im autorisierten Scope ändern.** Objektive Fehler minimal korrigieren; bei Bedeutungsrisiko nicht raten.
8. **Zweiten Pass durchführen.** Den geänderten Gesamttext erneut lesen und neue Anschluss-, Grammatik- oder Zeichensetzungsfehler ausschließen.
9. **Ergebnis knapp ausgeben.** Keine Probleme erfinden, nur um Kategorien zu füllen.

## Prüffelder

### Rechtschreibung

- Tipp- und Buchstabendreher;
- Groß- und Kleinschreibung;
- Getrennt- und Zusammenschreibung;
- Bindestrichschreibung;
- kontextuell falsche, aber formal plausible Wörter;
- versehentliche Wortdopplungen.

### Grammatik und Syntax

- Subjekt-Prädikat-Kongruenz;
- Kasus, Numerus und Genus;
- Verbformen und Tempuskonsistenz;
- Pronomen- und Bezugsfehler;
- Artikel und Präpositionen;
- fehlende Satzglieder oder Wörter;
- unvollständige oder syntaktisch gebrochene Konstruktionen;
- Parallelität koordinierter Strukturen, sofern grammatisch erforderlich.

### Zeichensetzung

- notwendige beziehungsweise falsche Kommas;
- Satzgrenzen;
- Doppelpunkt und Semikolon im konkreten Satzbau;
- Klammern und eingeschobene Strukturen;
- Zeichensetzung bei direkter Rede und Zitaten, soweit der Text selbst redigiert werden darf;
- Leerraumfehler direkt an Satzzeichen.

## Varianten und Zweifelsfälle

Nicht jede Abweichung vom eigenen Sprachgefühl ist ein Fehler.

Insbesondere:

- zulässige Varianten nicht zwangsvereinheitlichen;
- optionale Zeichensetzung nicht als Pflicht verkaufen;
- regionale Varianten nicht in eine andere Sprachvariante umschreiben;
- bei semantischer Mehrdeutigkeit die Stelle markieren statt eine Bedeutung zu erfinden;
- etablierte Projektterminologie nicht aufgrund eines generischen Sprachmodells „verbessern“.

Für standardsprachliches Deutsch bei strittigen Fällen das aktuelle amtliche Regelwerk beziehungsweise IDS/grammis heranziehen, wenn entsprechende Quellen verfügbar sind.

## Toolhinweise

Ein Rechtschreib- oder Grammatikchecker darf als zusätzlicher Finder dienen. Jeder Toolfund wird dennoch im Kontext geprüft.

Nicht zulässig:

- alle Vorschläge eines Checkers blind übernehmen;
- ein nicht beanstandeter Text automatisch als fehlerfrei behaupten;
- Toolkonfidenz als Sprachregel behandeln.

## Ausgabe

### Bei Review-only

Funde möglichst kompakt nach Kategorie:

- **Fehler** – objektiv beziehungsweise nach maßgeblicher Regel zu korrigieren;
- **Variante / optional** – korrekt, aber vereinheitlichbar;
- **unklar** – Bedeutung oder lokale Regel fehlt;
- **außerhalb Scope** – etwa Stil-, Fakten- oder Typografiefrage.

Bei jedem relevanten Fund kurze Fundstelle und Korrekturrichtung nennen.

### Bei autorisierter Korrektur

1. korrigierte Fassung beziehungsweise gezielte Dateiänderung;
2. auf Wunsch oder bei nichttrivialen Änderungen kurzer Änderungsnachweis;
3. verbleibende Zweifelsfälle separat;
4. zweiten Pass als tatsächlich durchgeführt benennen, nicht nur behaupten.

## Qualitätsgrenze

Ein Text kann orthografisch und grammatisch korrekt und trotzdem stilistisch schlecht, fachlich falsch oder unverständlich sein. Dieses Korrekturlektorat darf aus einem mechanischen PASS keine Gesamtfreigabe des Inhalts ableiten.
