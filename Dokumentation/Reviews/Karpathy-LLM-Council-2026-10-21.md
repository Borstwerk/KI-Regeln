# Kandidatensichtung: karpathy/llm-council

**Status:** `OBSERVED / UNVERIFIED / NOT ADMITTED / NOT RUN`
· 21.10.2026

## Quelle, Identität, Grenzen

- GitHub: [karpathy/llm-council](https://github.com/karpathy/llm-council)
- Bei Sichtung: Branch `master`, Commit
  `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131`.
- **Projektform:** Web-App mit Python/FastAPI-Backend und React/Vite-Frontend,
  **kein natives KI-Regeln-Skill-Bundle**.
- Statisch eingesehen: `README.md`, `CLAUDE.md`,
  `backend/config.py`, `backend/council.py`,
  `backend/openrouter.py`, `backend/main.py`,
  `backend/storage.py`, `pyproject.toml`, `start.sh`,
  Root-Dateiliste.
- Am beobachteten Rootstand ist **keine Lizenzdatei vorhanden**.
  Mangels verifizierter Lizenz **keine fremden Code-, Prompt- oder
  Textfragmente übernehmen oder weiterverteilen**. Allgemeines
  Methodenprinzip kann unabhängig neu beschrieben werden.
- Keine vollständige Security-/Dependency-Prüfung, keine
  Installation, keine laufende App, keine Tests, kein Traffic,
  keine Kostenmessung und keine Wiederholung des Verfahrens.

## Funktionsprinzip – anhand des Quellcodes

1. `stage1_collect_responses`: gleiche Nutzerfrage an mehrere
   konfigurierte Modelle unabhängig und parallel.
2. `stage2_collect_rankings`: Antworten als `Response A/B/...`
   anonymisiert; dieselben Modelle sehen alle Antworten und geben
   eine textuelle Bewertung plus Rangfolge ab.
3. `calculate_aggregate_rankings`: arithmetische mittlere
   Platzierung der erkannten Labels als Anzeige-/API-Metadaten.
4. `stage3_synthesize_final`: Chairman sieht Erstantworten
   **einschließlich Modellnamen** und Rohbewertungen; erzeugt
   freie Synthese. Er erhält **nicht** explizit die berechnete
   aggregierte Rangliste als gesonderte Eingabe.
5. Optional `generate_conversation_title`: separater Modellaufruf.
   Bei vier Standardmitgliedern normal **4 + 4 + 1 + 1 = 10**
   Modellaufrufe für eine neue Unterhaltung (ohne Retries).
   Parallelisierung begrenzt Latenz, aber nicht automatisch
   Token- oder API-Kosten.

## Positive Methodenimpulse

- Unabhängige Erstantworten vermeiden frühe gegenseitige Anpassung.
- Anonymisierte Peer-Reviews können Namens-/Marken-Bias reduzieren,
  ohne ihn vollständig auszuschließen.
- Einzelantworten und Rohbewertungen sind sichtbar statt
  durch nur eine Synthese verborgen.
- Unterschiedliche Standpunkte werden explizit vergleichbar.

## Kritische Grenzen (noch **keine** Admission)

| Thema | Beobachtung und Prüfung vor Anwendung |
| --- | --- |
| Faktentreue | Freitextranking nach Plausibilität/Insight ersetzt keine Primärquelle, Unit Tests oder echte Evidence. Mehrheitsirrtum möglich |
| Bewertungsbias | Labelreihenfolge ist deterministisch, Peer-Reviewer gehören zum Kandidatenkreis; Unabhängigkeit und Blindheit sind begrenzt |
| Parsing | `parse_ranking_from_text` benutzt Regex/Fallback und validiert nicht strikt vollständige, eindeutige Ränge |
| Chairman | Frei formulierte Synthese kann unbelegte Aussagen glätten oder Minderheitsbelege verdecken; Modelnamen werden sichtbar |
| Kosten | OpenRouter-Calls einschließlich Peer-Reviews sind zusätzliche Token-/Budgetlast; Nutzen bisher nicht gemessen |
| Privacy | Inhalte gehen an OpenRouter/Provider; lokal wirkende UI ist **nicht** lokale Inferenz |
| Credentials | `.env` und `OPENROUTER_API_KEY` werden erwartet; keine Daten/Schlüssel im KI-Regeln-Pilot übertragen |
| Persistenz | Conversations liegen als JSON lokal; Lösch-, Retention-, Rechte- und Sensitive-Data-Verhalten nicht vollständig geprüft |
| Runtime | Webserver bindet im Quelltext an `0.0.0.0:8001`; Authentifizierung/Deployment-Netzgrenze vor jeder Live-Nutzung separat prüfen |
| Lizenz | Keine Root-Lizenzdatei im betrachteten Stand; keine Codeübernahme ohne Rechteklärung |

**Sicherheitsentscheidung:** `DO NOT INSTALL / DO NOT CONNECT /
DO NOT REGISTER AS SKILL`. Das ist eine **vorläufige
Planungseinstufung**, kein negatives Endurteil über das Projekt.

## Mögliche KI-Regeln-Integration

**Separater Skill-Kandidat** `multi-model-deliberation`:
[Ideenkarte](../Multi-Model-Council-Optionen.md).

**Separater Methodenvergleich** `Council-01`:
[Pilotplan](../../Evals/Agentenarbeit/Council-01-Pilot/README.md).

Prüfkriterium ist eine **inhaltlich belegbare Verbesserung** bei
schwierigen Aufgaben, nicht Anzahl der Modelle oder die
Selbstbewertung des Councils.

**Nächster Prüfstand:** Quell-/Lizenz- und Risiko-Review nur,
wenn tatsächlich eine externe Runtime oder Codeübernahme
angestrebt wird. Für einen **eigenständig formulierten,
CLI-/manuell-basierten Methodenpilot** ist die Fremd-App
nicht erforderlich.
