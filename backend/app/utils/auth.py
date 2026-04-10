"""Basic role check. Proper RBAC planned (issue #3)."""
from functools import wraps
from flask import request, jsonify
ROLES = {"admin": ["read","write","delete","manage_users"], "support": ["read","write"], "viewer": ["read"]}

def require_role(role):
    def dec(f):
        @wraps(f)
        def w(*a, **kw):
            ur = request.headers.get("X-User-Role", "viewer")
            if ur not in ROLES: return jsonify({"error": "Invalid role"}), 403
            return f(*a, **kw)
        return w
    return dec
