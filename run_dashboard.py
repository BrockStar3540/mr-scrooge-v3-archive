#!/usr/bin/env python3
"""Quick-start script for the V3 dashboard in demo mode."""

from scrooge_v3.dashboard import create_app, WidgetRegistry
from scrooge_v3.dashboard.widgets import (
    HealthWidget, SystemWidget, ScoringWidget, GateWidget, ExecutionWidget,
)

reg = WidgetRegistry()
reg.register(HealthWidget())
reg.register(SystemWidget())
scoring = ScoringWidget()
scoring.record_result("EUR_USD", 82, "A", {"hr": 13, "age": 13, "vol": 9}, 42)
scoring.record_result("USD_JPY", 35, "REJECT", {"hr": -8, "age": -12}, -24)
scoring.record_result("GBP_USD", 0, "BLOCKED", {}, 0)
reg.register(scoring)
gates = GateWidget()
gates.record_result("spread", True, symbol="EUR_USD")
gates.record_result("overhead_ratio", True, symbol="EUR_USD")
gates.record_result("spread", False, "Spread 3.2 > 2.0", "GBP_JPY")
gates.record_result("regime_floor", False, "Regime BLOCKED", "USD_MXN")
reg.register(gates)
execution = ExecutionWidget()
execution.record_entry("EUR_USD", "short", 5000, 1.08450, 1.08650, 82.0)
reg.register(execution)

app = create_app(reg)
app.run(host="127.0.0.1", port=8084, debug=False)
