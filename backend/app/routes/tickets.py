"""WARNING: N+1 query on comments. See issue #4."""
from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import os
tickets_bp = Blueprint("tickets", __name__)
engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///dev.db"))

@tickets_bp.route("/api/v1/tickets")
def search_tickets():
    page = request.args.get("page", 1, type=int)
    # TODO: date_from / date_to not implemented
    with Session(engine) as s:
        result = s.execute(text(f"SELECT * FROM tickets ORDER BY created_at DESC LIMIT 25 OFFSET {(page-1)*25}"))
        return jsonify({"tickets": [dict(r._mapping) for r in result]})
