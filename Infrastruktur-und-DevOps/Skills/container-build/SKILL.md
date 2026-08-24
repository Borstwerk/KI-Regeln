---
name: container-build
description: Entwirft oder prüft reproduzierbare Container-Builds und den Runtime-Vertrag eines Images einschließlich Build-/Runtime-Trennung, Base Image, Dependencies, Secrets, User, Signals, Health und Konfiguration. Verwenden bei Dockerfile, BuildKit, Podman, Buildah, Buildpacks oder OCI-Images. Nicht als vollständigen Container-Security-Review verwenden.
---

# Container Build

## Ziel

Ein identifizierbares, reproduzierbares und für die Zielruntime verständliches Containerartefakt erzeugen.

## Arbeitsweise

1. Build Context und benötigte Inputs bestimmen.
2. Build- und Runtime-Inhalte trennen.
3. Dependencies/Base Image kontrolliert versionieren.
4. unnötige Runtime-Tools und Buildartefakte entfernen.
5. Secrets aus Layers, Metadata und Buildkontext halten.
6. Runtime Contract definieren: Entrypoint, Config, Ports, User, Filesystem, Signals, Health.
7. Artifact Identity/Digest und Rebuild-/Patchstrategie benennen.
8. Security-spezifische Privilegien/Policies an `Sicherheit/` übergeben.

## Nicht tun

- Containerisierung als Pflichtarchitektur darstellen;
- `latest` oder andere floating Inputs ungeprüft als reproduzierbar bezeichnen;
- Secrets einbacken und später nur löschen;
- root/privileged automatisch erlauben oder verbieten ohne lokalen Contract/Policy;
- grüne Image-Builds als Deploymentfreigabe behandeln.

## Ausgabe

```text
Build Inputs
Build / Runtime Stages
Base / Dependencies
Artifact Identity
Runtime Contract
Secret Handling
Security Handoff
Verification
```

## Related

- `ci-pipeline-design`
- `deployment-strategy`
- `tool-permission-review`
- `skill-security-review`