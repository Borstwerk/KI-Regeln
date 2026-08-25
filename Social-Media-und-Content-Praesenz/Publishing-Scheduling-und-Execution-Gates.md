# Publishing, Scheduling und Execution Gates

## Zweck

Planung, Draft, Review, Scheduling und tatsächliche Veröffentlichung sind getrennte Zustände.

## Zustandsmodell

```text
IDEA
→ DRAFT
→ REVIEWED
→ APPROVED_FOR_LOCAL_PUBLISH_GATE
→ SCHEDULED / PUBLISHED
→ VERIFIED
```

Lokale Projekte dürfen andere Statusmodelle verwenden.

## Grundregeln

- ein fertiger Text autorisiert keine Veröffentlichung;
- ein Content-Kalender autorisiert kein Scheduling;
- ein Review-Verdict autorisiert keinen Post, Reply, DM oder Delete;
- Toolverfügbarkeit ist keine Account-Autorisierung;
- Account, Identität, Zielplattform und Zeitpunkt vor externer Aktion prüfen;
- Cross-Posting kann mehrere Außenaktionen bedeuten und braucht entsprechenden Scope;
- nach Veröffentlichung bei relevanten Posts reale Darstellung, Link, Medien und Disclosure prüfen.

## Externe Aktionen

Besonders klar lokal gaten:

- Publish / Schedule / Reschedule;
- Reply / Comment / Quote;
- DM;
- Delete / Hide;
- Block / Report;
- Account-/Profiledit;
- bezahlte Promotion.

> `READY_TO_PUBLISH` ist Evidence für ein lokales Gate, keine globale Ausführungsberechtigung.
