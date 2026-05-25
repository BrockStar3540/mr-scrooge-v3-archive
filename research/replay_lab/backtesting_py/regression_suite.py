"""Regression suite — assert per-cell behavior across commits."""
from __future__ import annotations
import json
import logging
from pathlib import Path

import pandas as pd

from .experiments import benchmark_cases, run_single_replay, RESULTS_ROOT

log = logging.getLogger("replay_lab.regression")


def run_regression_suite(output_dir: str | None = None,
                          family: str = "canonical_lien_dbb") -> pd.DataFrame:
    """Run all benchmark cases, save summary."""
    rd = Path(output_dir) if output_dir else (RESULTS_ROOT / "regression_latest")
    rd.mkdir(parents=True, exist_ok=True)

    rows = []
    for spec in benchmark_cases():
        try:
            r = run_single_replay(spec, family=family)
            if "error" in r:
                rows.append({"label": spec.label, "error": r["error"]})
                continue
            s = r["stats"]
            rows.append({
                "label": spec.label,
                "symbol": spec.symbol,
                "n_trades": s.get("# Trades", 0),
                "win_rate_pct": s.get("Win Rate [%]", 0),
                "expectancy_pct": s.get("Expectancy [%]", 0),
                "return_pct": s.get("Return [%]", 0),
            })
        except Exception as e:
            log.exception("regression case failed: %s", spec.label)
            rows.append({"label": spec.label, "error": str(e)})
    df = pd.DataFrame(rows)
    df.to_csv(rd / "regression_summary.csv", index=False)
    print(f"regression results -> {rd}")
    print(df.to_string(index=False))
    return df
