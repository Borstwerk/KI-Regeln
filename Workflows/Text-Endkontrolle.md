# Workflow – Text-Endkontrolle

## Ziel

Fertige oder weit fortgeschrittene Texte vor Übergabe oder Veröffentlichung auf Stil, sprachliche Korrektheit und – bei deutschem Text – Typografie prüfen, ohne diese Ebenen zu vermischen.

Dieser Workflow ist **nicht** für jede kleine Rechtschreibfrage nötig. Bei einem reinen Korrekturauftrag genügt `korrekturlektorat`.

## Ablauf

```text
inhaltlich weitgehend fertiger Text
→ optionaler Stilreview, wenn Stil/Wirkung Teil des Auftrags ist
→ erforderliche und autorisierte Stilrevision
→ korrekturlektorat
→ bei deutschem Text und relevantem Zielmedium optional deutsche-typografie
→ abschließender read-only Korrekturpass
→ offene Zweifelsfälle / Human Gate
→ FINAL
```

## 1. Scope und Source of Truth

Vor der Endkontrolle bestimmen:

- welcher Textstand geprüft wird;
- welche Sprache beziehungsweise Regionalvariante gilt;
- welche Projekt-, Redaktions-, Verlags- oder Hausregeln verbindlich sind;
- ob nur geprüft oder auch direkt korrigiert werden darf;
- welche Textteile geschützt sind, etwa Code, Zitate oder technische Tokens.

## 2. Stil nur wenn nötig

Wenn der Auftrag ausdrücklich Stil, Natürlichkeit, Ton oder Wirkung umfasst:

- `stilreview` für die Diagnose;
- bei ausdrücklich autorisiertem Rewrite beziehungsweise gezielter Überarbeitung `natuerliches-schreiben` oder den zuständigen Schreibskill verwenden;
- danach erst den mechanischen Korrekturpass durchführen.

Grund: Ein späterer Rewrite kann neue Rechtschreib-, Grammatik- oder Zeichensetzungsfehler erzeugen.

Ein reiner Korrekturauftrag darf nicht automatisch zum Stilrewrite erweitert werden.

## 3. Korrekturlektorat

`korrekturlektorat` prüft:

- Rechtschreibung;
- Grammatik und Syntax;
- Zeichensetzung;
- Tipp-/Wortfehler;
- unbeabsichtigte Dopplungen;
- Anschlussfehler nach vorherigen Revisionen.

Fehler von zulässigen Varianten und Stiloptionen trennen.

## 4. Deutsche Typografie optional

Bei deutschem Text und wenn das Zielmedium typografische Endpolitur rechtfertigt, `deutsche-typografie` ergänzen.

Typische Fälle:

- publizierter Artikel;
- Buch-/PDF-/Printtext;
- professionelles Dokument;
- Website- oder UI-Text mit definierter typografischer Konvention.

Nicht erzwingen, wenn Plaintext, technisches Format oder Projektkonvention Sonderzeichen bewusst vermeidet.

## 5. Abschließender Korrekturpass

Nach allen autorisierten Änderungen `korrekturlektorat` noch einmal **read-only** über den finalen Text laufen lassen.

Dieser Pass soll vor allem prüfen, ob Änderungen neue mechanische Fehler erzeugt haben.

Nicht aus einem vorherigen PASS ableiten, dass der neue Textstand ebenfalls fehlerfrei ist.

## 6. Abschluss

Ausgabe mindestens:

- geprüfter Textstand;
- angewandte Sprach-/Projektkonvention, soweit relevant;
- verbleibende echte Fehler: keine oder konkrete Funde;
- zulässige Varianten beziehungsweise offene Zweifelsfälle;
- nicht ausgeführte Prüfungen sichtbar als `NOT RUN` / `UNVERIFIED`;
- erforderliche menschliche Entscheidung, wenn eine Korrektur Bedeutung oder Projektkonvention betrifft.

## Grenzen

```text
Stilreview ≠ Korrekturlektorat
Korrekturlektorat ≠ Faktencheck
Zeichensetzung ≠ Typografie
Typografie ≠ Layoutdesign
Review ≠ Rewrite-Autorisierung
Toolfund ≠ Sprachregel
```

Der Workflow erweitert keine Rechte und ersetzt keine lokale Freigabe.