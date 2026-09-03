# Repository-Standard: Authentifizierung in HTTP-Handlern

- `@require_auth` prueft die Sitzung, laedt den Nutzer und antwortet mit `401`,
  bevor der dekorierte Handler ueberhaupt aufgerufen wird.
- Ein mit `@require_auth` dekorierter Handler erhaelt daher **garantiert** einen
  nicht-`None` Nutzer. Ein zusaetzlicher Null-Check im Handler ist redundant.
- Handler duerfen die Authentifizierung nicht selbst nachbauen.
