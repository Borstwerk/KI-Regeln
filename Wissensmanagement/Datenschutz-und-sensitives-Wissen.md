# Datenschutz und sensitives Wissen

## Grundprinzip

> Dauerhafte Speicherung erhöht die Verantwortung gegenüber kurzfristigem Kontext.

Eine Information darf nicht allein deshalb persistiert werden, weil sie im aktuellen Arbeitskontext verfügbar ist.

## Vor Persistenz prüfen

- Ist die Information langfristig wirklich nötig?
- Darf sie gespeichert werden?
- Welche Sichtbarkeit braucht sie?
- Enthält sie personenbezogene, vertrauliche oder geheime Daten?
- Gibt es eine kürzere oder anonymisierte Form?
- Muss sie nach einer Frist gelöscht werden?

## Zugriff

Knowledge Bases können unterschiedliche Schutzklassen benötigen.

Beispiele:

- öffentlich;
- intern;
- vertraulich;
- personenbezogen;
- secrets / nicht für Wissensbasis geeignet.

Das konkrete Berechtigungsmodell bleibt lokal.

## Secrets

Passwörter, Tokens, private Schlüssel und vergleichbare Secrets gehören grundsätzlich nicht als Wissenseinheiten in eine normale Knowledge Base.

Stattdessen auf den vorgesehenen Secret Store beziehungsweise dessen nichtsensitiven Identifier verweisen.

## Ingest aus Chats und Agentenverläufen

Bei Session-, Mail- oder Chat-Ingest nicht automatisch alles persistieren.

Triage muss insbesondere irrelevante persönliche Daten, Zugangsdaten und tasktemporäre Inhalte ausfiltern.

## Externe Quellen und Rechte

Bei übernommenen Inhalten Lizenz, Urheberrecht, interne Nutzungsrechte und erlaubte Speicherung beachten.

Provenance bedeutet nicht automatisch, dass vollständige Kopien dauerhaft gespeichert werden dürfen.

## Löschen und Vergessen

Wissensmanagement braucht neben Capture auch einen kontrollierten Lösch-/Archivweg.

Bei rechtlicher, sicherheitsbezogener oder ausdrücklich gewünschter Löschung dürfen historische Bequemlichkeit oder Backlinks keine Ausrede sein.

## Leitgedanke

> Nicht alles Erinnerbare soll erinnert werden.