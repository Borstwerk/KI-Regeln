# CI-Pipelines und Automation

## Abgrenzung zu Testing

```text
Testing und QA
→ Was muss geprüft werden und welche Evidence zählt?

CI / DevOps
→ Wann, wo, mit welchen Abhängigkeiten, Rechten und Artefakten laufen diese Checks?
```

## Pipeline-Modell

Eine Pipeline definiert mindestens:

- Trigger;
- Jobs/Stages;
- Abhängigkeiten;
- Parallelität;
- Inputs/Outputs;
- Caches;
- Artefakte;
- Credentials;
- Environment-Grenzen;
- Blocking vs. informational Checks;
- Promotion-/Deployment-Gates;
- Fehler-/Retryverhalten.

## Reproduzierbarkeit

Wo sinnvoll pinnen oder locken:

- Actions/Tasks;
- Runtime/Toolchains;
- Dependencies;
- Images;
- Module/Provider.

Pinning und Patchbarkeit müssen gemeinsam geplant werden; reproduzierbar darf nicht „für immer ungepatcht“ bedeuten.

## Caching

Cache ist Optimierung, keine Source of Truth. Caches dürfen keine falschen Greens erzeugen.

Cache-Keys und Invalidierung an die tatsächlichen Korrektheitsabhängigkeiten koppeln.

## Flakiness

Flaky Tests gehören fachlich zu Testing/QA. Die Pipeline soll Flakiness sichtbar machen und nicht durch blinde Retries normalisieren.

## Secrets und Forks

Untrusted Contributions, Forks und externe Trigger dürfen keine mächtigen Credentials erhalten, nur weil der Job technisch Zugriff hätte.

## Fehlerdiagnose

Pipelines sollen relevante Evidence wie Logs, Reports oder Artefakte so bereitstellen, dass Fehler reproduzierbar eingeordnet werden können, ohne Secrets unnötig offenzulegen.

## Leitgedanke

> Eine Pipeline orchestriert Evidence und Übergänge; sie entscheidet nicht allein, was Qualität bedeutet.