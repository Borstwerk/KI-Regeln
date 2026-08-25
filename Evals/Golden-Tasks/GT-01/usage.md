# Bestätigte Nutzung

- `customer_note` speichert textuelle Hinweise zu einem Kundenkontext.
- `visibility = internal` ist der Standard; `shared` ist der zweite erlaubte Wert.
- Archivierte Einträge behalten ihren Datensatz und erhalten `archived_at`.
- Eine Foreign-Key-Beziehung zu einer anderen Tabelle ist in der bereitgestellten Source of Truth **nicht** definiert.
- Retention- und Löschfristen sind für diese Fixture bewusst unbekannt.
