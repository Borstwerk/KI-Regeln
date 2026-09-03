# Anforderung AUTH-207: Toten Null-Check im Profil-Handler entfernen

Quelle: freigegebenes Ticket, Stand 2026-07-09.

## Kontext

Der Handler `profile_view` ist mit `@require_auth` dekoriert. Der zusaetzliche
`if user is None`-Zweig im Handler ist seit Einfuehrung des Dekorators nicht mehr
erreichbar und wurde im Ticket als toter Code eingestuft.

## Akzeptanzkriterien

- **AC-1**: Der unerreichbare `if user is None`-Zweig wird aus `profile_view` entfernt.
- **AC-2**: Das Verhalten fuer nicht angemeldete Aufrufe bleibt unveraendert.
- **AC-3**: Es wird keine weitere Logik im Handler geaendert.
