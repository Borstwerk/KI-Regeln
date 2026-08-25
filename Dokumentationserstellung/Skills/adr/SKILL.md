---
name: adr
description: Dokumentiert eine Architektur- oder technische Grundsatzentscheidung nachvollziehbar als Architecture Decision Record mit Kontext, Alternativen und Konsequenzen. Verwenden bei tatsächlich getroffenen oder klar als Proposal markierten Entscheidungen, deren Begründung und Trade-offs dauerhaft nachvollziehbar bleiben sollen.
---

# Skill: adr

## Zweck

Eine Architektur- oder technische Grundsatzentscheidung nachvollziehbar als Architecture Decision Record dokumentieren.

## Voraussetzungen

- tatsächlicher Entscheidungskontext oder klarer Proposal-Status;
- bekannte Alternativen und Constraints, soweit verfügbar.

## Vorgehen

1. Erfasse Status und Entscheidungstitel.
2. Beschreibe den Kontext, der die Entscheidung erforderlich macht.
3. Formuliere die Entscheidung präzise.
4. Dokumentiere ernsthaft betrachtete Alternativen.
5. Benenne positive und negative Konsequenzen sowie Trade-offs.
6. Verlinke Requirements, PoCs, Benchmarks oder Issues als Evidence.
7. Bei späterer Ablösung: neue ADR erstellen und alte als superseded markieren.

## Regeln

- Keine historische Begründung erfinden.
- Rejected oder superseded Entscheidungen nicht löschen, wenn sie Teil der Entscheidungshistorie sind.
- ADR ist kein allgemeines Architekturhandbuch.
- Nicht jede kleine Implementierungsentscheidung braucht eine ADR.
- Status muss klar erkennbar sein.

## Ergebnis

Ein knapper, dauerhafter Entscheidungsnachweis, der später erklärt, was entschieden wurde, warum und mit welchen Konsequenzen.
