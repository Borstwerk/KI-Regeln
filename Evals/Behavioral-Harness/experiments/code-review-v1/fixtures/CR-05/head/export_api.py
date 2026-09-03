from framework import route, current_user, Unauthorized

from records import load_records


@route("GET", "/projects/<project_id>/export")
def export_project(project_id, limit=None):
    if not current_user.is_authenticated:
        raise Unauthorized()
    records = load_records(project_id)
    if limit is not None:
        records = records[: int(limit)]
    return {"project_id": project_id, "records": records}
