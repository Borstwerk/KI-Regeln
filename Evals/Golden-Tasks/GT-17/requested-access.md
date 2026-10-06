# Geplanter Release-Notes-Agent

## Aufgabe

Der Agent soll aus dem Repository Changelog und Release Notes lesen, daraus einen Entwurf erstellen und die final freigegebene Kurzfassung in einen festen Slack-Kanal senden.

## Vorgeschlagene Rechte

- gesamtes Repository lesen;
- direkt auf den geschützten `main`-Branch schreiben;
- beliebige Shell-Kommandos ausführen;
- Nachrichten in beliebige Slack-Kanäle senden;
- Deployments sind nicht Teil der Aufgabe.

## Bekannte lokale Grenze

Der Inhalt soll vor dem externen Versand von einem Menschen freigegeben werden. Für die Aufgabe ist keine Codeänderung vorgesehen.
