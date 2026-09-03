# Repository-Standard: Ressourcenbezogene Berechtigungen

- `current_user.is_authenticated` beantwortet nur die Frage "angemeldet".
  Es ist **keine** Aussage ueber Zugriff auf eine konkrete Ressource.
- Fuer projektbezogene Endpunkte ist der vorhandene Helfer
  `assert_project_member(user, project_id)` zu verwenden. Er wirft `Forbidden`,
  wenn der Nutzer nicht Mitglied des Projekts ist.
- Query-Parameter werden vor der Verwendung validiert, nicht danach.
