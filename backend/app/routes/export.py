"""Streaming CSV export for ticket reports."""
import csv, io
from flask import Blueprint, Response
export_bp = Blueprint("export", __name__)

@export_bp.route("/api/v1/tickets/export/csv")
def export_csv():
    def gen():
        out = io.StringIO()
        w = csv.writer(out)
        w.writerow(["id","title","status","priority","assigned_to","created_at"])
        yield out.getvalue()
    return Response(gen(), mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=tickets.csv"})
