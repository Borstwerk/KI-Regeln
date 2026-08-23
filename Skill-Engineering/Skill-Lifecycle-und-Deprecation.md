# Skill Lifecycle und Deprecation

## Zweck

Skills verändern sich. Deshalb braucht ein Skill neben Inhalt auch einen nachvollziehbaren Reife- und Ablöseprozess.

## Empfohlene Reifestufen

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

### experimental

Neue Idee oder neuer Workflow. Quellen plausibel, aber wenig Praxis und wenige Evals.

### candidate

Mehrfach geprüft oder praktisch eingesetzt. Noch nicht vollständig stabilisiert.

### stable

Wiederholt eingesetzt, relevante Evals vorhanden, keine bekannten schweren Verhaltensprobleme.

### deprecated

Soll nicht mehr für neue Nutzung gewählt werden. Ersatz oder Migrationsweg ist benannt.

### retired

Nicht mehr aktiv angeboten. Historie bleibt nachvollziehbar.

## Änderungen nach Risiko

### Redaktionell

- Tippfehler;
- bessere Formulierung ohne Verhaltensänderung;
- Links/Quellen aktualisieren.

Keine Maturity-Rückstufung nötig.

### Verhaltensändernd

- Trigger verändert;
- neue Pflichtgates;
- anderer Output;
- neue Toolrechte;
- neue Abhängigkeit.

Evals und Changelog prüfen.

### Brechend

- Skillverantwortung wesentlich geändert;
- bisherige Eingaben/Outputs inkompatibel;
- Rechte oder Sicherheitsmodell erheblich verändert.

Möglicherweise neuer Skill statt stiller Umdefinition.

## Deprecation

Ein deprecated Skill soll dokumentieren:

- warum er ersetzt wird;
- welchen Skill oder Workflow man stattdessen verwendet;
- ob lokale Projekte migriert werden müssen;
- ob es bekannte inkompatible Unterschiede gibt.

Nicht sofort löschen. Sonst verlieren Projekte Kontext darüber, warum eine ältere Skillreferenz nicht mehr empfohlen wird.

## Upstream ist nicht Lifecycle

Ein externer Upstream kann sich verändern, ohne dass der lokale Skill automatisch seine Reifestufe ändert.

Lokale Maturity bewertet **unser tatsächliches Skillverhalten**.

## Leitgedanke

> Reife ist eine Aussage über erprobtes Verhalten – nicht über Alter, Dateigröße oder Popularität.
