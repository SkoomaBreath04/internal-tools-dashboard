"""RBAC — ON HOLD pending permission matrix from product team."""
from functools import wraps
from flask import request, jsonify

class Permission:
    READ = "tickets:read"
    WRITE = "tickets:write"
    DELETE = "tickets:delete"
    MANAGE_USERS = "users:manage"

class RBACMiddleware:
    def __init__(self):
        self._perms = {}  # TODO: load from DB
    def require(self, *perms):
        def dec(f):
            @wraps(f)
            def w(*a, **kw):
                role = request.headers.get("X-User-Role", "viewer")
                missing = [p for p in perms if p not in self._perms.get(role, [])]
                if missing: return jsonify({"error": "Forbidden"}), 403
                return f(*a, **kw)
            return w
        return dec
