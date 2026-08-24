# Environments, Konfiguration und Promotion

## Umgebungen

Dev, Test, Staging und Produktion können unterschiedliche Anforderungen besitzen. Ziel ist nicht künstliche Gleichheit, sondern kontrollierte, dokumentierte Unterschiede.

## Environment-Parität

Unterschiede sind riskant, wenn sie unabsichtlich oder für das getestete Verhalten wesentlich sind.

Deshalb dokumentieren:

- welche Unterschiede bewusst sind;
- welche identisch sein müssen;
- welche Provider-/Region-/Scale-Unterschiede Tests beeinflussen;
- welche Secrets/Identitäten pro Umgebung gelten.

Keine Universalregel „Umgebungen unterscheiden sich nur in Values“.

## Konfiguration

Trennen, soweit sinnvoll:

```text
Code / Artifact
≠
Environment Configuration
≠
Secret Material
```

Secrets nicht in normale Konfigurationsdateien kopieren, nur um Promotion einfacher zu machen.

## Promotion

Wenn die Architektur es zulässt, bevorzugt dasselbe identifizierbare Artefakt zwischen Umgebungen promoten statt für jede Umgebung neu zu bauen.

Ausnahmen können legitim sein, müssen aber bewusst sein.

## Environment Credentials

Nichtproduktionsjobs dürfen nicht stillschweigend Produktionscredentials verwenden.

Rechte pro Job und Zielumgebung minimal halten.

## Promotion Evidence

Je Stufe können verlangt werden:

- Artefaktidentität;
- Test-/Security-Evidence;
- Environment-spezifische Checks;
- Change Review;
- Gate;
- Deployment-/Health-Evidence.

## Leitgedanke

> Unterschiede zwischen Umgebungen sind nicht automatisch schlecht – unbekannte Unterschiede sind es.