from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import os
tickets_bp = Blueprint("tickets", __name__)
engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///dev.db"))

@tickets_bp.route("/api/v1/tickets")
def search_tickets():
    page = request.args.get("page", 1, type=int)
    query = "SELECT * FROM tickets WHERE 1=1"
    params = {}
    if q := request.args.get("q"):
        query += " AND (title LIKE :q OR description LIKE :q)"; params["q"] = f"%{q}%"
    if df := request.args.get("date_from"):
        query += " AND created_at >= :df"; params["df"] = df
    if dt := request.args.get("date_to"):
        query += " AND created_at <= :dt"; params["dt"] = dt
    query += f" ORDER BY created_at DESC LIMIT 25 OFFSET {(page-1)*25}"
    with Session(engine) as s:
        return jsonify({"tickets": [dict(r._mapping) for r in s.execute(text(query), params)]})
