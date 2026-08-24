# Build-Artefakte, Provenance und Reproduzierbarkeit

## Build als eigene Phase

```text
Source
→ Build
→ identifizierbares Artifact
→ Tests / Attestations / Evidence
→ Promotion
→ Deployment
```

Build, Deploy und Release nicht vermischen.

## Artefaktidentität

Ein deploytes Artefakt soll möglichst eindeutig auf seinen Build zurückgeführt werden können, zum Beispiel über Digest, Version, Commit oder eine andere unveränderliche Identität.

## Reproduzierbarkeit

Reproduzierbarkeit verbessern durch:

- lockbare Dependencies;
- bekannte Toolchain;
- kontrollierte Inputs;
- deterministische Schritte soweit realistisch;
- dokumentierte externe Einflüsse;
- Build-Metadaten.

Nicht behaupten, ein Build sei bit-identisch reproduzierbar, wenn nur „gleicher Source Commit“ bekannt ist.

## Provenance

SLSA dient als wichtige Referenz für Build Provenance: Informationen darüber, woher ein Artefakt stammt und wie es erzeugt wurde.

Infrastructure/DevOps erzeugt und transportiert passende Metadaten; `Sicherheit/` definiert die erforderliche Vertrauens- und Verifikationsstärke.

## Promotion statt Rebuild

Wenn möglich dasselbe geprüfte Artefakt promoten. Environment-spezifischer Rebuild kann die Beziehung zwischen Test-Evidence und Produktionsartefakt schwächen.

## Staleness

Gepinnte Dependencies oder Base Images erhöhen Reproduzierbarkeit, können aber veralten. Patch-/Rebuild-Strategie separat planen.

## Leitgedanke

> Gute Delivery kann beantworten: Was wurde gebaut, womit, woraus und genau welches Artefakt wurde ausgeliefert?