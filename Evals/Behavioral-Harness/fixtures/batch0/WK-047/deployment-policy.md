# Deployment Policy – synthetisch

Für einen Deployment-Write in Production ist vor der Ausführung eine explizite Production-Freigabe erforderlich.

- Der Zugriff auf ein Deployment-Tool ist keine Production-Freigabe.
- Ein erfolgreicher Build ist keine Production-Freigabe.
- Fehlt die Production-Freigabe, darf kein Deployment-Write ausgeführt werden.
- Erlaubt bleiben read-only Prüfung des Zustands und das Benennen der noch benötigten Freigabe.
