# GT-01 – armverblindete Zweitbewertung vorbereiten

**Status: vorbereitet, unabhängige Bewertung NOT RUN.** Der bisherige Autor/Auswerter kennt die beiden Bedingungen. Eine Zweitmeinung aus demselben Kontext ist keine unabhängige blinde Bewertung. Das Skript erzeugt eine lokale Prüferübergabe **ohne** Modellaufruf.

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Golden-Tasks/GT-01/prepare_blind_review.py
```

Voraussetzung: gespeicherte Originalantworten samt JSON-Evidence. Das Skript prüft Quell-/Antwort-SHA256, verweigert Veränderungen und Überschreiben. Es erzeugt zwei getrennte Verzeichnisse im gitignorierten `.validation/`:

- `.validation/gt01-blind-reviewer/`: nur neutrale Dateien `A.md`/`B.md`, DDL/Usage, die originalen neun Kriterien sowie ein leeres Scorecard-Template.
- `.validation/gt01-blind-operator/`: **PRIVATE** Zufallszuordnung A/B zu Baseline bzw. Skill samt Checksummen. Nie dem Judge geben, nie committen.

**Vorgehen:** Einen wirklich frischen Reviewer einsetzen. Nur den Reviewer-Ordner weitergeben; keinen Zugriff auf Repo, PR #88, alte Bewertungen oder Operator-Ordner. Beide Antworten anhand aller Kriterien mit Zitaten bewerten, Ergebnis festhalten, **danach** Mapping auflösen und die Abweichungen von der vorherigen nichtblinden Bewertung erklären.

Eine neue Sitzung desselben Modells ist armverblindet, aber nicht automatisch ein unabhängiger Human-Review oder ein verblindeter Generalisierungsbenchmark. Die Originalantworten sind öffentlich; ein Judge mit Repositoryzugriff könnte die Labels auflösen. Ohne tatsächlichen Review bleibt der Status **NOT RUN**. Kein neuer Skill-/Maturity-/B2-Claim.
