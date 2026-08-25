# Bestätigte Projektanforderung

- `GET /orders/{id}` ist tenant-isoliert.
- Jeder Datenbankzugriff dieses Endpoints muss sowohl `order_id` als auch den authentifizierten `tenant_id` einschränken.
- Ein Order-Datensatz eines anderen Tenants darf weder gelesen noch durch seine Existenz bestätigt werden.
- Dieser Golden Task ist ein **Reviewauftrag**. Codeänderungen sind nicht autorisiert.
