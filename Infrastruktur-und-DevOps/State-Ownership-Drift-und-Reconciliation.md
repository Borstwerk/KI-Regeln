# State Ownership, Drift und Reconciliation

## State-Arten

Bei Infrastrukturarbeit mindestens unterscheiden:

- deklarierter Desired State;
- Tool-/Controller-State oder Mapping;
- tatsächlicher Provider-/Cluster-Zustand;
- externe oder unmanaged Ressourcen;
- temporäre Runtime-Zustände.

## Ownership

Vor einer Änderung klären:

- welches Tool besitzt welche Ressource;
- wer darf Desired State ändern;
- ob Ressourcen geteilt oder extern verwaltet sind;
- ob mehrere Automationen dieselbe Ressource kontrollieren;
- ob Imports, Moves oder Ownership-Wechsel nötig sind.

Zwei unabhängige Controller mit widersprüchlicher Autorität erzeugen keine Resilience, sondern Fight Loops.

## Drift

Drift kann entstehen durch:

- manuelle Änderungen;
- Providerdefaults;
- externe Controller;
- automatische Skalierung/Mutation;
- Import-/Statefehler;
- veraltete Konfiguration.

Drift vor Korrektur klassifizieren.

## Reconciliation

Ein einmaliges Apply und kontinuierliche Reconciliation sind unterschiedliche Autorisierungsmodelle.

```text
Apply
→ Aktion endet

Continuous Reconciliation
→ Controller erhält dauerhafte Änderungsautorität
```

Bei automatischer Reconciliation besonders prüfen:

- Prune/Delete;
- Self-Heal;
- Ownership;
- Drift-Ignorierregeln;
- Retry-/Loop-Verhalten;
- Rechte des Controllers.

## State-Artefakte

State, Plan- und Preview-Artefakte können sensible Daten enthalten. Schutzbedarf explizit prüfen; nicht automatisch als harmlose CI-Artefakte behandeln.

## Leitgedanke

> Drift ist eine Abweichung, keine automatische Anweisung, welche Seite gewinnen soll.