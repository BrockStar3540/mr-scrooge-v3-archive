"""Dashboard Flask app — real-time trading dashboard.

Serves the live trading state as a single JSON endpoint.
HTML renders it into proper cards, badges, and signal panels.
"""

from __future__ import annotations

import functools
import logging
import os
from typing import Any

from flask import Flask, Response, jsonify, render_template, request

from .live_state import LiveState

log = logging.getLogger("scrooge_v3.dashboard.app")

_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
_STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

# Global reference set by run_dashboard()
_live_state: LiveState | None = None


def create_app(
    live_state: LiveState | None = None,
    config: dict | None = None,
) -> Flask:
    global _live_state
    _live_state = live_state or LiveState()

    config = config or {}
    app = Flask(__name__, template_folder=_TEMPLATE_DIR, static_folder=_STATIC_DIR)

    auth_user = config.get("auth_user", os.environ.get("DASHBOARD_USER", "admin"))
    auth_pass = config.get("auth_pass", os.environ.get("DASHBOARD_PASS", "scrooge"))

    def check_auth(u: str, p: str) -> bool:
        return u == auth_user and p == auth_pass

    def requires_auth(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if auth and check_auth(auth.username, auth.password):
                resp = f(*args, **kwargs)
                if isinstance(resp, Response):
                    resp.set_cookie("sa", "1", httponly=True, samesite="Strict")
                return resp
            if request.cookies.get("sa") == "1":
                return f(*args, **kwargs)
            return Response("Auth required", 401, {"WWW-Authenticate": 'Basic realm="V3"'})
        return decorated

    @app.route("/")
    @requires_auth
    def index():
        return render_template("index.html")

    @app.route("/api/data")
    @requires_auth
    def api_data():
        return jsonify(_live_state.snapshot())

    return app


def run_dashboard(
    live_state: LiveState | None = None,
    config: dict | None = None,
) -> None:
    config = config or {}
    app = create_app(live_state, config)
    port = config.get("port", 8084)
    log.info("[DASHBOARD] Starting on 127.0.0.1:%d", port)
    app.run(host="127.0.0.1", port=port, debug=False)
