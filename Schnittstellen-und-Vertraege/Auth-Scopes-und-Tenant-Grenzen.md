# Auth, Scopes und Tenant-Grenzen

## Contract-Sicht

Eine Schnittstelle muss beschreiben, welche Identität und Autorisierung für beobachtbares Verhalten relevant sind.

Mindestens klären:

- wer sich authentisiert;
- welche Operationen/Scopes benötigt werden;
- welche Tenant-/Organisation-/Objektgrenze gilt;
- welche Felder abhängig von Rechten sichtbar oder änderbar sind;
- ob Nichtberechtigung als 403, verborgenes 404 oder anderes lokales Verhalten erscheint;
- welche Machine-to-Machine- bzw. User-Delegation gilt.

## AuthN ≠ AuthZ

Authentisierung etabliert Identität. Autorisierung entscheidet, was diese Identität innerhalb der Domäne darf.

Framework- oder Gatewaymechanik darf diese fachliche Grenze nicht stillschweigend definieren.

## Least Exposure

Request- und Response-Schemas sollen nur Felder enthalten, die der jeweilige Consumer wirklich senden beziehungsweise sehen darf.

Interne Felder oder Adminattribute nicht allein deshalb veröffentlichen, weil das interne Modell sie besitzt.

## Security-Grenze

Hier wird der Contract beschrieben. Detaillierte Themen wie OAuth Threat Models, Token-Härtung, Secrets, BOLA/BFLA, Angriffssimulation oder Pentesting bleiben in `Sicherheit/`.

## Leitgedanke

> Berechtigung ist Teil der API-Bedeutung – nicht nur Middleware.