# Container Build und Runtime-Vertrag

## Einordnung

Container sind eine mögliche Packaging-/Runtimeform, keine Pflichtarchitektur.

Der zentrale Skill heißt deshalb `container-build`, nicht `docker`.

## Build-Ziele

- reproduzierbares identifizierbares Image;
- klare Build-/Runtime-Trennung;
- nur notwendiger Runtime-Inhalt;
- bekannte Base-/Dependency-Versionen;
- keine Secrets im Image oder Buildkontext;
- explizite Runtime-Anforderungen.

## Multi-Stage und Runtime-Minimierung

Buildwerkzeuge müssen nicht automatisch Teil des Runtime-Images sein. Multi-Stage- oder vergleichbare Verfahren helfen, Build- und Laufzeitinhalt zu trennen.

## Base Images

Version/Digest-Pinning erhöht Reproduzierbarkeit, ersetzt aber keine Patchstrategie.

## Runtime-Vertrag

Mindestens sichtbar machen:

- Entrypoint/Command;
- Ports;
- benötigte Environment-/Config-Werte;
- Filesystem-/Write-Bedarf;
- User/UID und benötigte Privilegien;
- Signal-/Shutdown-Verhalten;
- Liveness/Readiness, falls die Plattform sie nutzt;
- Resource-Annahmen, soweit für den Runtimebetrieb relevant.

## Security-Grenze

`container-build` macht benötigte Privilegien und sensible Buildpfade sichtbar. Ob Privileged, Capabilities, Seccomp, Signing, Admission oder Supply-Chain-Vertrauen zulässig sind, entscheidet `Sicherheit/` beziehungsweise lokale Policy.

## Secrets

Secrets nicht in Layers, Build Args, Image Metadata oder unnötigen Buildkontext einbacken.

## Leitgedanke

> Ein Containerimage ist ein Runtime-Artefakt, kein kleiner virtueller Server mit allem drin.