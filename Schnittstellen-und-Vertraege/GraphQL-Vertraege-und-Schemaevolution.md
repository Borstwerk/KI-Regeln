# GraphQL-Verträge und Schemaevolution

## Einordnung

GraphQL besitzt ein typisiertes, introspektierbares Schema mit eigener Evolutionslogik. Es wird deshalb fachlich separat behandelt, aber zunächst nicht als eigener zentraler Skill.

## Contract-Oberfläche

Relevant sind insbesondere:

- Types und Interfaces;
- Fields;
- Arguments;
- Input Objects;
- Nullability;
- Enums;
- Queries, Mutations und Subscriptions;
- Directives;
- Deprecation;
- Introspection;
- dokumentierte Semantik und Authorization.

## Evolution

Die GraphQL Specification betrachtet Änderungen als breaking, wenn eine zuvor gültige Anfrage dadurch ungültig werden kann.

Additive Schemaentwicklung und `@deprecated` erlauben häufig Evolution ohne klassische parallele `/v1`-/`/v2`-Oberflächen. Das ist ein Paradigmenmerkmal, keine universelle Versionierungsregel für andere APIs.

## Vorsicht bei Additionen

Auch scheinbar additive Änderungen können Consumerannahmen betreffen, etwa neue Enum-Werte oder veränderte Resolver-/Null-Semantik. Deshalb weiterhin semantische Compatibility prüfen.

## Deprecation

Deprecated Fields, Arguments, Input Fields oder Enum Values bleiben zunächst nutzbar. Gute Governance benötigt zusätzlich:

- Grund / Replacement;
- Consumer-Nutzung, wenn messbar;
- Migrationspfad;
- Removal-Gate.

## Nicht hier

- Resolver-Performance im Detail;
- Federation-Architektur;
- konkrete Gatewayprodukte;
- Frameworksyntax.

Diese Aspekte bleiben lokal beziehungsweise späteren Architektur-/Reliability-Bereichen vorbehalten.

## Leitgedanke

> GraphQL-Evolution nutzt das Schema als lebenden Vertrag – nicht als Freibrief für stille Bedeutungsänderungen.