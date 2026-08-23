# Skill-Handbuch – Dokumentationserstellung

Dieses Ergänzungsblatt erklärt die Skills aus `Dokumentationserstellung/` für Menschen.

## Schnellauswahl

| Ich möchte ... | Skill |
|---|---|
| vorab klären, welche Doku überhaupt gebraucht wird | `docs-plan` |
| technische Doku klar schreiben oder überarbeiten | `technical-writing` |
| einen Projekteinstieg erstellen | `readme` |
| jemanden lernend durch einen Ablauf führen | `tutorial` |
| eine konkrete Aufgabe dokumentieren | `how-to` |
| scanbare Nachschlagedoku erstellen | `reference-docs` |
| Hintergründe und Trade-offs erklären | `explanation-docs` |
| eine Architekturentscheidung dokumentieren | `adr` |
| einen Betriebs-/Störungsfall dokumentieren | `runbook` |
| vorhandene Doku kritisch prüfen | `docs-review` |

## `docs-plan`

**Was ist das?**  
Der Planungs-Skill vor dem eigentlichen Schreiben.

**Wann sinnvoll?**

- neue Doku oder größerer Doku-Umbau;
- Zielgruppe oder Dokumenttyp ist unklar;
- mehrere Sources of Truth müssen zusammengeführt werden.

**Mini-Beispiel**

> „Plane die Dokumentation für dieses Tool: Wer liest sie, welche Docs-Typen brauchen wir und welche Dateien sind Source of Truth?“

---

## `technical-writing`

**Was ist das?**  
Der allgemeine Schreib-Skill für klare technische Dokumentation.

**Wann sinnvoll?**

- bestehende technische Texte überarbeiten;
- neue Docs-Seite schreiben;
- Terminologie und Klarheit stabilisieren.

**Wichtig:** Der Skill darf fehlende technische Fakten nicht erfinden.

---

## `readme`

**Was ist das?**  
Ein Skill für den Einstiegspunkt eines Projekts.

**Fokus:**

- Was ist das?
- Warum ist es relevant?
- Wie bekomme ich schnell ein erstes Ergebnis?
- Wo finde ich weitere Doku?

Ein README soll nicht das komplette Handbuch verschlucken.

---

## `tutorial`

**Was ist das?**  
Lernorientierte Dokumentation: Der Leser lernt durch einen geführten praktischen Ablauf.

**Kennzeichen:**

- definierte Zielgruppe;
- kleine End-to-End-Strecke;
- überprüfbare Ergebnisse nach wichtigen Schritten;
- wenig Ablenkung durch tiefe Reference oder Theorie.

---

## `how-to`

**Was ist das?**  
Arbeitsorientierte Dokumentation für eine konkrete Aufgabe.

**Kennzeichen:**

- klares Ziel;
- Voraussetzungen;
- notwendige Schritte;
- Ergebnisprüfung;
- Hintergrund nur verlinken, wenn er den Arbeitsfluss stören würde.

---

## `reference-docs`

**Was ist das?**  
Nachschlagedokumentation für Fakten.

**Typische Inhalte:**

- Parameter;
- Optionen;
- Commands;
- API-Felder;
- Defaults;
- Statuswerte;
- Schemas.

Reference sollte möglichst eng an einer kanonischen Source of Truth hängen.

---

## `explanation-docs`

**Was ist das?**  
Dokumentation zum Verstehen von Zusammenhängen und Gründen.

**Typische Fragen:**

- Warum ist das so gebaut?
- Wie hängen A und B zusammen?
- Welche Trade-offs gibt es?

Nicht mit Schritt-für-Schritt-How-tos vermischen.

---

## `adr`

**Was ist das?**  
Ein Architecture Decision Record dokumentiert eine relevante Entscheidung mit Kontext, Alternativen und Konsequenzen.

**Wann sinnvoll?**

- mehrere ernsthafte Optionen;
- größere Architektur- oder Technologieentscheidung;
- spätere Maintainer werden wahrscheinlich fragen „Warum haben wir das so gemacht?“.

Abgelöste ADRs werden üblicherweise als superseded markiert statt still gelöscht oder historisch umgeschrieben.

---

## `runbook`

**Was ist das?**  
Operative Dokumentation für bekannte Betriebs- und Störungsfälle.

**Besonders wichtig:**

- Symptome;
- Rechte und Voraussetzungen;
- erwartete Normalergebnisse;
- sichere Mitigation;
- Verifikation;
- Rollback/Recovery;
- Eskalation.

Ein Runbook muss unter Zeitdruck funktionieren, nicht nur am Schreibtisch gut aussehen.

---

## `docs-review`

**Was ist das?**  
Ein unabhängiger Qualitäts- und Driftcheck für Dokumentation.

**Reihenfolge:**

```text
fachliche Korrektheit
→ richtige Zielgruppe / Dokumenttyp
→ Vollständigkeit
→ Beispiele / Links / Befehle
→ Informationsarchitektur
→ Klarheit / Terminologie
→ Stilpolitur
```

Der Review ist nicht automatisch ein Rewrite.

## Typische Kombinationen

```text
neue technische Doku:
docs-plan
→ passender Dokumenttyp-Skill
→ technical-writing
→ docs-review
```

```text
README:
docs-plan, falls Zweck unklar
→ readme
→ Befehle / Links verifizieren
→ docs-review
```

```text
Betriebsdoku:
docs-plan
→ runbook
→ reale technische Verifikation
→ docs-review
```

```text
Doku-Audit:
docs-review
→ gezielte Korrektur
→ betroffene Prüfungen erneut ausführen
```

## Leitgedanke

> Nicht jeden Doku-Skill gleichzeitig laden. Erst Dokumentzweck bestimmen, dann den kleinsten passenden Satz wählen.
