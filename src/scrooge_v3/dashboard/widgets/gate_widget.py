"""Gate widget — pass/fail counts and rejection reasons."""

from __future__ import annotations

from collections import Counter
from typing import Any


class GateWidget:
    """Shows gate pipeline results: which gates pass/fail and why."""

    widget_name = "gates"
    widget_category = "gates"

    def __init__(self):
        self._pass_counts: Counter = Counter()
        self._fail_counts: Counter = Counter()
        self._rejection_reasons: list[dict[str, str]] = []

    def record_result(self, gate_name: str, passed: bool, reason: str = "",
                      symbol: str = "") -> None:
        if passed:
            self._pass_counts[gate_name] += 1
        else:
            self._fail_counts[gate_name] += 1
            self._rejection_reasons.append({
                "gate": gate_name, "symbol": symbol, "reason": reason,
            })
            if len(self._rejection_reasons) > 100:
                self._rejection_reasons = self._rejection_reasons[-100:]

    def render_data(self) -> dict[str, Any]:
        gates = sorted(set(list(self._pass_counts.keys()) + list(self._fail_counts.keys())))
        gate_stats = []
        for g in gates:
            p = self._pass_counts[g]
            f = self._fail_counts[g]
            total = p + f
            gate_stats.append({
                "name": g, "passed": p, "failed": f, "total": total,
                "pass_rate": round(p / total * 100, 1) if total > 0 else 0.0,
            })
        return {
            "gate_stats": gate_stats,
            "recent_rejections": self._rejection_reasons[-10:],
            "total_evaluated": sum(self._pass_counts.values()) + sum(self._fail_counts.values()),
        }
