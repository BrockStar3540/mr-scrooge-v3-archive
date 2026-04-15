"""Dashboard Flask app — modular widget-based trading dashboard.

Binds to 127.0.0.1 only, HTTP Basic Auth, HTTPS via Tailscale Serve.
REST API serves widget data as JSON. HTML templates render the UI.

Historical lessons applied:
  - Every widget returns data regardless of pass/fail (no 0/0 blanks)
  - Filter to active data, not dump everything
  - Live state, not boot-time snapshots
  - "Signals evaluated this cycle" counter (zero = red)
  - Broker-reconciled P/L only
  - 127.0.0.1 + Basic Auth + Tailscale
"""

from __future__ import annotations

import functools
import logging
import os
from typing import Any

from flask import Flask, Response, jsonify, render_template, request

from .widget_registry import WidgetRegistry

log = logging.getLogger("scrooge_v3.dashboard.app")

_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
_STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")


def create_app(
    widget_registry: WidgetRegistry,
    runtime_state: Any = None,
    config: dict | None = None,
) -> Flask:
    """Create and configure the dashboard Flask app."""
    config = config or {}
    app = Flask(
        __name__,
        template_folder=_TEMPLATE_DIR,
        static_folder=_STATIC_DIR,
    )

    auth_user = config.get("auth_user", os.environ.get("DASHBOARD_USER", "admin"))
    auth_pass = config.get("auth_pass", os.environ.get("DASHBOARD_PASS", "scrooge"))

    def check_auth(username: str, password: str) -> bool:
        return username == auth_user and password == auth_pass

    def requires_auth(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not check_auth(auth.username, auth.password):
                return Response(
                    "Authentication required", 401,
                    {"WWW-Authenticate": 'Basic realm="Scrooge V3"'},
                )
            return f(*args, **kwargs)
        return decorated

    @app.after_request
    def set_auth_cookie(response):
        """Once authenticated via Basic Auth, set a session cookie so
        JS fetch() calls from the same page work without re-sending
        credentials in the URL (which browsers block)."""
        if request.authorization and check_auth(
            request.authorization.username, request.authorization.password
        ):
            response.set_cookie("scrooge_auth", "1", httponly=True, samesite="Strict")
        return response

    def requires_auth_or_cookie(f):
        """Allow access via Basic Auth OR valid session cookie."""
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            if request.cookies.get("scrooge_auth") == "1":
                return f(*args, **kwargs)
            auth = request.authorization
            if auth and check_auth(auth.username, auth.password):
                return f(*args, **kwargs)
            return Response(
                "Authentication required", 401,
                {"WWW-Authenticate": 'Basic realm="Scrooge V3"'},
            )
        return decorated

    # --- HTML routes ---

    @app.route("/")
    @requires_auth
    def index():
        categories = widget_registry.categories()
        return render_template("index.html", categories=categories)

    # --- REST API ---

    @app.route("/api/status")
    @requires_auth_or_cookie
    def api_status():
        return jsonify({
            "status": "ok",
            "widgets": len(widget_registry.get_all()),
            "categories": widget_registry.categories(),
        })

    @app.route("/api/widgets")
    @requires_auth_or_cookie
    def api_widgets():
        return jsonify(widget_registry.render_all())

    @app.route("/api/widgets/<category>")
    @requires_auth_or_cookie
    def api_widgets_category(category: str):
        entries = widget_registry.get_by_category(category)
        if not entries:
            return jsonify({"error": f"No widgets in category '{category}'"}), 404
        result = []
        for entry in entries:
            try:
                data = entry.instance.render_data()
                result.append({"name": entry.name, "data": data})
            except Exception as e:
                result.append({"name": entry.name, "data": {"error": str(e)}})
        return jsonify(result)

    return app


def run_dashboard(
    widget_registry: WidgetRegistry,
    runtime_state: Any = None,
    config: dict | None = None,
) -> None:
    """Start the dashboard server (blocking)."""
    config = config or {}
    app = create_app(widget_registry, runtime_state, config)
    port = config.get("port", 8084)
    log.info("[DASHBOARD] Starting on 127.0.0.1:%d", port)
    app.run(host="127.0.0.1", port=port, debug=False)
