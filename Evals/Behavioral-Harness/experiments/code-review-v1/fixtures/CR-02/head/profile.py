from framework import require_auth, render, unauthorized


@require_auth
def profile_view(request, user):
    """Zeigt das Profil des angemeldeten Nutzers.

    Faellt auf 401 zurueck, falls kein Nutzer ermittelt werden konnte.
    """
    return render("profile.html", {"display_name": user.display_name})
