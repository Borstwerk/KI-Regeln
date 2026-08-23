# Technischer Schreibstil

## Zweck

Technische Dokumentation soll klar, scanbar, präzise und für ihre Zielgruppe verständlich sein.

## Klarheit vor Eindruck

Bevorzuge:

- konkrete Subjekte und Verben;
- aktive Formulierungen, wenn dadurch klarer wird, wer handelt;
- direkte Anweisungen;
- kurze bis mittlere Sätze;
- stabile Terminologie;
- konkrete Bedingungen und Ergebnisse.

Vermeide unnötig:

- Werbesprache;
- Bedeutungsrhetorik;
- Füllsätze;
- Meta-Ankündigungen;
- künstliche Förmlichkeit;
- wechselnde Synonyme für denselben technischen Begriff.

## Nutzer direkt ansprechen

Bei Anleitungen ist die direkte zweite Person oft klarer als unpersönliche Passivkonstruktionen.

Beispiel:

```text
Besser:
Öffne die Konfigurationsdatei und setze `timeout` auf `3000`.

Schwächer:
Die Konfigurationsdatei sollte geöffnet und der Timeout entsprechend angepasst werden.
```

## Bedingungen vor Aktionen

Wenn ein Schritt nur unter einer Bedingung gilt, nenne die Bedingung zuerst.

```text
Wenn du Version 3 oder neuer verwendest, führe ... aus.
```

statt die Einschränkung erst nach dem Schritt zu erklären.

## Terminologie stabil halten

- Produktbegriffe nicht aus stilistischen Gründen variieren;
- UI-Bezeichnungen exakt wiedergeben;
- Codebegriffe in Codeformat;
- projektlokales Glossar respektieren;
- Abkürzungen beim ersten relevanten Auftreten erklären, wenn die Zielgruppe sie nicht sicher kennt.

## Überschriften mit Informationswert

Überschriften sollen erkennen lassen, was der Abschnitt beantwortet oder ermöglicht.

Schwach:

- Allgemeines;
- Weitere Informationen;
- Sonstiges.

Besser:

- Konfiguration laden;
- Fehler beim Verbindungsaufbau beheben;
- Warum der Dienst zwei Datenbanken verwendet.

## Scanbarkeit

Nutze Struktur dort, wo sie Lesen erleichtert:

- nummerierte Listen für Sequenzen;
- Aufzählungen für gleichrangige Punkte;
- Tabellen für echte strukturierte Vergleiche;
- kurze Abschnitte;
- Codeblöcke für ausführbare oder kopierbare Beispiele.

Nicht jede Information in Tabellen oder Bullet-Listen pressen.

## Globale Verständlichkeit

Bei internationaler oder gemischter Zielgruppe:

- unnötige Idiome vermeiden;
- kulturelle Insiderreferenzen vermeiden;
- mehrdeutige Datumsangaben vermeiden;
- klare Einheiten und Bezeichnungen verwenden;
- Fachjargon nur dort einsetzen, wo er fachlich notwendig ist.

## Accessibility im Text

- beschreibende Linktexte statt „hier klicken“;
- Alt-Texte für informative Bilder;
- Bedeutung nicht ausschließlich über Farbe transportieren;
- Anweisungen nicht nur auf räumliche Positionen wie „rechts oben“ stützen, wenn ein eindeutiger Name verfügbar ist.

## Projektregeln haben Vorrang

Ein allgemeiner Style Guide ist Hilfsmittel, keine höhere Wahrheit.

Wenn lokale Terminologie oder Formatregeln verbindlich sind, gelten diese, solange sie nicht Sicherheit oder fachliche Korrektheit gefährden.

## Leitgedanke

> Technische Dokumentation soll dem Leser Arbeit ersparen, nicht dem Autor Gelegenheit geben, besonders technisch zu klingen.
