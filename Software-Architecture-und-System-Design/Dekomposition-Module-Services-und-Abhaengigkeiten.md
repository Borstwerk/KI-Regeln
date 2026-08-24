# Dekomposition, Module, Services und Abhängigkeiten

## Zweck

Dekomposition verteilt Verantwortung so, dass Änderungen, Fehler und Wissen möglichst lokal bleiben, ohne unnötige Betriebs- oder Koordinationskosten zu erzeugen.

## Dekompositionsachsen

Mögliche Grenzen entstehen unter anderem aus:

- fachlich eigenständiger Verantwortung;
- unterschiedlichen Invarianten oder Sources of Truth;
- unabhängiger Änderungsrate;
- Security-/Trust-Grenzen;
- Failure-Isolation;
- stark unterschiedlichen Last- oder Skalierungsprofilen;
- regulatorischer oder organisatorischer Ownership;
- notwendiger unabhängiger Deployment- oder Lifecycle-Steuerung.

Keine dieser Achsen erzwingt allein einen eigenen Service.

## Modul oder Service?

Ein Modul ist zunächst eine Verantwortungs- und Abhängigkeitsgrenze. Ein Service fügt zusätzlich verteilte Betriebs-, Netzwerk-, Deployment-, Compatibility- und Failure-Kosten hinzu.

Deshalb:

> Erst logische Grenze begründen, dann entscheiden, ob sie ein eigenes Deployable sein muss.

## Dependency Direction

Für jede relevante Grenze festlegen:

- wer wen kennen darf;
- welche öffentliche Oberfläche benutzt wird;
- welche internen Details verborgen bleiben;
- wo Zustands- und Entscheidungsautorität liegt;
- wie Zyklen vermieden oder bewusst erklärt werden.

Ein Dependency Cycle ist nicht automatisch ein Produktionsfehler, aber immer ein Signal für gegenseitige Kopplung, das begründet werden muss.

## Shared Components

`common`, `shared`, `utils` oder ein Shared Kernel sind keine neutralen Ablageorte. Gemeinsame Bausteine brauchen einen begrenzten Zweck, Ownership und eine kontrollierte öffentliche Oberfläche.

## Decomposition Smells

- ein Modul besitzt keinen klaren Grund zu existieren;
- mehrere Module schreiben denselben fachlichen Zustand ohne Autorität;
- Consumer greifen in interne Pfade eines Nachbarmoduls;
- gemeinsame Modelle koppeln fachlich unterschiedliche Kontexte;
- technische Layer sind so dominant, dass ein fachlicher Change quer durch das gesamte System schneiden muss;
- Services existieren primär, weil Microservices als Ziel angenommen wurden.

## Anti-Regeln

Nicht global fordern:

- no cycles um jeden Preis;
- ein Repository pro Service;
- eine Datenbank pro Service;
- ein Bounded Context pro Deployable;
- Domain-orientierte Struktur für jedes kleine System;
- technische Layer seien grundsätzlich schlecht.

## Leitgedanke

> Die richtige Dekomposition minimiert die Kosten relevanter Änderungen und Fehler – nicht die Anzahl von Dateien pro Ordner.