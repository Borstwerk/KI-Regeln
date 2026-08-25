# Bestätigte Requirements – Export API

- RQ-01: Ein authentifizierter Nutzer darf einen Export ausschließlich für seinen eigenen Tenant starten.
- RQ-02: Das Starten eines Exports ist asynchron und liefert eine stabile Export-ID zurück.
- RQ-03: Der Client muss einen `request_key` mitsenden; derselbe Key innerhalb desselben Tenants darf nicht zwei Exporte erzeugen.
- RQ-04: Ein Export hat genau die Zustände `queued`, `running`, `succeeded` oder `failed`.
- RQ-05: Der Client kann den aktuellen Zustand über die Export-ID abfragen.
- RQ-06: Bei `failed` muss eine maschinenlesbare Fehlerkategorie vorhanden sein; interne Stacktraces dürfen nicht Teil des öffentlichen Contracts sein.
- RQ-07: Ein Client darf keine Exportressource eines anderen Tenants lesen.

Nicht spezifiziert: konkrete Latenz, Durchsatz, SLA/Availability, Retentiondauer, Queue- oder Worker-Technologie.
