# Context Compaction

## Zweck

Compaction verdichtet einen gewachsenen Arbeitskontext so, dass ein Agent mit weniger aktivem Kontext möglichst ohne relevanten Informationsverlust weiterarbeiten kann.

> Gute Compaction ist keine hübsche Zusammenfassung. Sie erhält den Zustand, der für korrekte Fortsetzung notwendig ist.

## Wann Compaction sinnvoll ist

- aktiver Kontext wächst stark;
- alte Toolergebnisse dominieren den Verlauf;
- eine Phase ist abgeschlossen und kann verdichtet werden;
- eine Runtime signalisiert Context Pressure;
- wiederkehrende Historie kann durch stabile Referenzen ersetzt werden;
- ein langer Lauf soll in einen frischen Kontext überführt werden.

Nicht automatisch kompaktieren, nur weil ein Kontext „lang aussieht“.

## Was bevorzugt erhalten bleibt

Je nach Aufgabe insbesondere:

- aktuelles Ziel und Scope;
- verbindliche Anforderungen und Constraints;
- Source-of-Truth-Referenzen;
- bestätigte Entscheidungen und deren relevante Konsequenzen;
- aktueller Artefakt- oder Implementierungszustand;
- offene Fehler, Risiken und Blocker;
- relevante Evidence und Teststatus;
- Gate-/Freigabestatus;
- bekannte fehlgeschlagene Ansätze, wenn ihre Wiederholung wahrscheinlich oder teuer wäre;
- nächster prüfbarer Schritt.

## Was bevorzugt reduziert oder ausgelagert wird

- redundante Gesprächswiederholungen;
- alte Tooloutputs, wenn das relevante Ergebnis bereits extrahiert ist;
- temporäre Hypothesen, die widerlegt wurden;
- irrelevante historische Details;
- Rohdaten, die über ein persistentes Artefakt oder eine Source of Truth wieder abrufbar sind.

## Fidelity vor Aggressivität

Zu starke Verdichtung kann subtile, später entscheidende Details verlieren.

Deshalb:

```text
zuerst hohe Recall-Fidelity
→ Verlustfälle beobachten
→ erst danach unnötige Details weiter entfernen
```

Eine hohe Kompressionsrate ist kein Qualitätsziel an sich.

## Verifizierbare Compaction

Compaction möglichst gegen die Fortsetzungsaufgabe prüfen.

Starker Test:

```text
gleicher Ausgangszustand
├─ Lauf A mit unkompaktiertem relevanten Kontext
└─ Lauf B mit kompaktertem Kontext

→ nächste Entscheidung / Aktion / Outcome vergleichen
```

Wo ein solcher Paartest nicht praktikabel ist, mindestens prüfen:

- sind harte Constraints erhalten?
- sind offene Probleme erhalten?
- sind Source-of-Truth-Referenzen erhalten?
- ist der nächste Schritt korrekt ableitbar?
- wurden bestätigte Fakten nicht in Vermutungen verwandelt?

## Reversibilität und Rohzustand

Wenn technisch und datenschutzrechtlich sinnvoll, Compaction nicht mit sofortiger Vernichtung des Rohverlaufs gleichsetzen.

Ein ausgelagerter Rohzustand kann für Audit, Fehleranalyse oder erneute Verdichtung nützlich sein. Aufbewahrung und Zugriff bleiben projektspezifisch und müssen Datenschutz- sowie Sicherheitsregeln beachten.

## Leitgedanke

> Komprimiere den Verlauf, nicht die Wahrheit.