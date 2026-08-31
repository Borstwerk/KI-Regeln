# Quellen und Inspirationen – Schreiben

## Zweck

Diese Datei dokumentiert externe Beobachtungs-, Norm- und Inspirationsquellen für die allgemeinen Schreib-, Korrektur- und Stilreview-Regeln dieses Repositories.

Externe Quellen werden nicht automatisch übernommen. Normative Quellen, methodische Referenzen und bloße Musterkataloge haben unterschiedliche Rollen.

## Amtliches Regelwerk der deutschen Rechtschreibung

Quelle:

`https://grammis.ids-mannheim.de/orthos/`

Rolle:

- normative Referenz für standardsprachliche deutsche Rechtschreibung und Zeichensetzung;
- Regelteil und Wörterverzeichnis;
- Grundlage des Ratsbeschlusses vom 15.12.2023, 2024 von den zuständigen staatlichen Stellen beschlossen.

Lokale Verwendung:

- `Sprachrichtigkeit-und-Typografie.md`;
- `Skills/korrekturlektorat/SKILL.md`.

Bewusste Grenze:

Das Regelwerk wird nicht in dieses Repository kopiert. Bei strittigen oder zeitkritischen Detailfragen wird der aktuelle Stand der Primärquelle geprüft. Projekt- und Regionalvarianten bleiben sichtbar.

## grammis – Leibniz-Institut für Deutsche Sprache

Quelle:

`https://grammis.ids-mannheim.de/`

Rolle:

- fachliche Referenz für deutsche Grammatik, Syntax und sprachliche Zweifelsfälle;
- systematische Grammatik, korpusgestützte Informationen und grammatische Nachschlagewerke.

Lokale Verwendung:

- `Sprachrichtigkeit-und-Typografie.md`;
- `Skills/korrekturlektorat/SKILL.md`.

Bewusste Grenze:

Korpusbelege oder beschriebene Sprachvariation werden nicht automatisch als normative Pflicht interpretiert.

## Olshansk/agent-skills – cmd-write-proofread

Quelle:

`https://github.com/Olshansk/agent-skills/blob/main/skills/cmd-write-proofread/SKILL.md`

Lizenzraum:

- Repository: MIT.

Nützliche methodische Impulse:

- vollständigen Text vor der Korrektur lesen;
- bewusster mechanischer Pass statt bloß einzelne bekannte Fehler zu reparieren;
- nach Änderungen einen zweiten vollständigen Korrekturpass durchführen;
- mechanische Fehler von inhaltlichen beziehungsweise stilistischen Verbesserungsvorschlägen trennen.

Bewusste Abweichung:

KI-Regeln übernimmt nicht den breiten Publishing-/Link-/Argumentations-Scope dieses Skills und keine optionalen Vibe-/Audience-Pässe. `korrekturlektorat` bleibt enger auf Sprachrichtigkeit begrenzt.

## brendanbank/fix-my-text-skill

Quelle:

`https://github.com/brendanbank/fix-my-text-skill`

Lizenzraum:

- BSD-2-Clause.

Nützliche methodische Impulse:

- Stimme und Wortwahl bei mechanischer Korrektur möglichst erhalten;
- keine unnötige Formalisierung;
- Mehrdeutigkeit markieren statt eine Bedeutung zu erraten;
- korrigierten Text und auf Wunsch einen kompakten Änderungsnachweis trennen.

Bewusste Abweichung:

Keine source-spezifischen Stilverbote wie ein pauschales Verbot bestimmter Gedankenstriche übernehmen. Ob ein Zeichen passt, entscheidet Funktion, Sprachraum, Projektkonvention und Zielmedium.

## Red Pencil Editor – editor-mode

Quelle:

`https://github.com/justinneuman-coder/red-pencil-editor-skills`

Lizenzraum:

- MIT.

Nützlicher methodischer Impuls:

- objektive mechanische Fehler wie Rechtschreibung, Grammatik, Zeichensetzung und Tippfehler klar von Stil-/Argumentationsreview trennen.

Bewusste Abweichung:

KI-Regeln erzwingt kein grundsätzliches „nur markieren, nie korrigieren“. Review und Änderung werden stattdessen über den konkreten Auftrag und die vorhandene Autorisierung getrennt.

## Sebastian Software – Effective German Typography Skill

Quelle:

`https://github.com/sebastian-software/effective-german-typography-skill`

Status und Lizenzraum:

- MIT;
- Repository seit 2026-08-03 archiviert und deshalb keine lebende normative Quelle.

Nützliche methodische Impulse:

- deutsche Typografie als eigenen Scope von Grammatik und Rechtschreibung trennen;
- Anführungszeichen, Striche, Abstände und Sonderzeichen funktional unterscheiden;
- regionale DE-/AT-/CH-Konventionen berücksichtigen;
- Markdown, HTML, JSX und andere technische Formate vor blinden Ersetzungen schützen.

Bewusste Abweichung:

Die dort beschriebenen typografischen Detailregeln werden nicht als universelle Norm übernommen. Für verbindliche Sprach-, DIN-, Verlags- oder Hausregeln bleibt die aktuelle Primär- beziehungsweise Projektquelle maßgeblich.

## LanguageTool

Quelle:

`https://github.com/languagetool-org/languagetool`

Rolle:

- optionaler technischer Referenzraum für automatisierte Rechtschreib-, Grammatik- und Stilprüfung in mehreren Sprachen.

Lizenzhinweis:

- LanguageTool Core: LGPL-2.1, soweit upstream nicht anders gekennzeichnet.

Bewusste Grenze:

KI-Regeln übernimmt oder vendort keinen LanguageTool-Code und hat keine Runtime-Abhängigkeit davon. Toolvorschläge gelten als zusätzliche Fundstellen, nicht als normative Sprachentscheidung.

## Wikipedia – Signs of AI writing

Quelle:

`https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing`

Nützliche Funktion:

- Beobachtung wiederkehrender sprachlicher und struktureller Muster in KI-generierten beziehungsweise KI-verdächtigen Wikipedia-Texten;
- Radar für neue Muster, die bei einem Stilreview als Fundstellen dienen können;
- Erinnerung daran, dass Muster im Kontext geprüft werden müssen.

Bewusste Abweichung:

Die lokale Regel lautet ausdrücklich nicht, dass ein beobachtetes Muster automatisch ein Fehler oder ein Nachweis für KI-Autorenschaft ist.

Aus dem Katalog werden keine Wort-Blacklists oder mechanischen Ersetzungsregeln abgeleitet.

Lokale Auswirkungen vor allem auf:

- `Stilreview.md`;
- `Skills/stilreview/SKILL.md`;
- teilweise `Schreibstil.md` und `Skills/natuerliches-schreiben/SKILL.md`.

## Mutable Quelle

Die Wikipedia-Seite ist eine laufend veränderliche Community-Seite. Sie wird deshalb im zentralen Upstream-Register als semantisch zu prüfende Quelle geführt.

Ein Update der Seite ist nur ein Hinweis, neue oder geänderte Beobachtungsmuster zu prüfen. Es ändert lokale Regeln nicht automatisch.

## Leitgedanke

> Externe Quellen helfen bei Norm, Methode oder Beobachtung. Welche Rolle eine Quelle hat, muss vor ihrer Anwendung klar sein.