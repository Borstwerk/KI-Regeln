# Aktualität, Staleness und Lifecycle

## Grundprinzip

> Wissen ist nicht dauerhaft aktuell, nur weil es einmal korrekt war.

## Zeitinformationen

Je nach Wissensart relevant:

- erstellt am;
- zuletzt geprüft;
- gültig ab / bis;
- beobachtet am;
- aus Quelle abgerufen am;
- ersetzt durch.

Nicht jede Wissenseinheit braucht alle Felder.

## Staleness

Stale bedeutet nicht automatisch falsch. Es bedeutet, dass Aktualität nicht mehr ausreichend belegt ist.

Typische Trigger:

- veränderliche externe Quelle wurde aktualisiert;
- Software-/Produktversion änderte sich;
- abhängige Wissenseinheit änderte sich;
- definierte Reviewfrist ist überschritten;
- reale Nutzung widerspricht dem gespeicherten Wissen.

## Review nach Risiko

Reviewfrequenz richtet sich nach Veränderlichkeit und Auswirkung.

```text
schnell veränderlich + hohe Wirkung
→ häufiger prüfen

stabile Grundlagen
→ ereignis- oder risikobasiert prüfen
```

Keine universelle Monatsfrist für alles.

## Statusmodell

Mögliche allgemeine Zustände:

```text
WIP
→ noch unvollständig

unverified
→ plausibel, aber noch nicht ausreichend geprüft

validated
→ aktuell ausreichend gestützt

stale-candidate
→ erneute Prüfung erforderlich

archived
→ nicht mehr für aktuelle Nutzung empfohlen
```

Projekte dürfen ein einfacheres Modell verwenden.

## Archivieren statt löschen

Wenn Geschichte, Provenance oder eingehende Links relevant sind, lieber archivieren beziehungsweise ersetzen markieren als hart löschen.

Löschung ist sinnvoll bei echten Dubletten, sensiblen Daten oder bewusst nicht aufbewahrbaren Inhalten – mit passenden Gates.

## Leitgedanke

> Lifecycle macht sichtbar, wie viel Vertrauen ein Wissensstand heute noch verdient.