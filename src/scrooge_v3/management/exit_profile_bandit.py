"""exit_profile_bandit.py — Thompson-sampling bandit for exit profile selection.

Per Brock 2026-05-31 pip-eater architecture. Phase 2 of RL exits.

Background
----------
Exit Quality Audit 2026-05-31 showed overall exit efficiency 25.46% —
we leave 74% of available pips on the table. Avg gap 7.85 pips/trade.

This bandit chooses an exit PROFILE per position (AGGRESSIVE/BALANCED/
CONSERVATIVE/PATIENT) based on which profile has historically yielded
best pnl_pips for that (pair, strategy, regime) cell.

SHADOW MODE
-----------
Bandit picks profile + logs choice. Live managers still use global config.
After collecting outcomes, verify the chosen profile would have done better.
Stage B (later): apply chosen profile to live position management.

Math
----
Per cell x profile, track running stats: n, sum_pips, sum_sq_pips.
Posterior on expected pip yield: Normal(mean, var/n).
Thompson sampling: sample one value from each profile posterior,
pick the profile with highest sample.

Cold start: first MIN_TRADES_EXPLORE per cell x profile = uniform random.
"""
from __future__ import annotations

import json
import logging
import math
import random
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

log = logging.getLogger("scrooge_v3.management.exit_profile_bandit")

STATE_PATH = Path("/home/ubuntu/mr-scrooge-v3/data/exit_profile_bandit_state.json")
SHADOW_LOG = Path("/home/ubuntu/mr-scrooge-v3/data/exit_profile_shadow.jsonl")

MIN_TRADES_EXPLORE = 20
PRIOR_MEAN = 0.0
PRIOR_VAR = 100.0


@dataclass
class ExitProfile:
    name: str
    trail_atr_mult: float
    be_trigger_pips: float
    be_offset_pips: float
    ratchet_trigger_r: float
    ratchet_lock_pct: float
    harvest_tp1_fraction: float
    favorable_exit_enabled: bool
    favorable_exit_min_peak_r: float
    favorable_exit_retrace_pct: float


PROFILES: dict[str, ExitProfile] = {
    "AGGRESSIVE": ExitProfile(
        name="AGGRESSIVE",
        trail_atr_mult=0.3, be_trigger_pips=3.0, be_offset_pips=2.0,
        ratchet_trigger_r=0.7, ratchet_lock_pct=0.7,
        harvest_tp1_fraction=0.5,
        favorable_exit_enabled=True, favorable_exit_min_peak_r=0.7, favorable_exit_retrace_pct=0.7,
    ),
    "BALANCED": ExitProfile(
        name="BALANCED",
        trail_atr_mult=0.5, be_trigger_pips=5.5, be_offset_pips=5.0,
        ratchet_trigger_r=1.0, ratchet_lock_pct=0.5,
        harvest_tp1_fraction=0.0,
        favorable_exit_enabled=True, favorable_exit_min_peak_r=1.0, favorable_exit_retrace_pct=0.5,
    ),
    "CONSERVATIVE": ExitProfile(
        name="CONSERVATIVE",
        trail_atr_mult=0.8, be_trigger_pips=10.0, be_offset_pips=8.0,
        ratchet_trigger_r=1.5, ratchet_lock_pct=0.4,
        harvest_tp1_fraction=0.0,
        favorable_exit_enabled=True, favorable_exit_min_peak_r=1.5, favorable_exit_retrace_pct=0.3,
    ),
    "PATIENT": ExitProfile(
        name="PATIENT",
        trail_atr_mult=999.0, be_trigger_pips=999.0, be_offset_pips=0.0,
        ratchet_trigger_r=999.0, ratchet_lock_pct=0.0,
        harvest_tp1_fraction=0.0,
        favorable_exit_enabled=False,
        favorable_exit_min_peak_r=999.0, favorable_exit_retrace_pct=0.0,
    ),
}

PROFILE_NAMES = list(PROFILES.keys())


def cell_key(pair: str, strategy: str, regime: str) -> str:
    return f"{pair}|{strategy}|{regime}"


class ExitProfileBandit:
    def __init__(self,
                 state_path: Path = STATE_PATH,
                 shadow_log: Path = SHADOW_LOG,
                 min_explore: int = MIN_TRADES_EXPLORE) -> None:
        self.state_path = state_path
        self.shadow_log = shadow_log
        self.min_explore = min_explore
        self.state: dict = {}
        self._lock = threading.Lock()
        self._load()

    def _load(self) -> None:
        if not self.state_path.exists():
            log.info("[BANDIT] no prior state — starting fresh")
            return
        try:
            self.state = json.loads(self.state_path.read_text())
            n_cells = len(self.state)
            n_obs = sum(int(p.get("n", 0)) for c in self.state.values() for p in c.values())
            log.info("[BANDIT] loaded prior state: %d cells, %d observations", n_cells, n_obs)
        except Exception as e:
            log.warning("[BANDIT] state load failed (%s)", e)
            self.state = {}

    def _save(self) -> None:
        try:
            self.state_path.write_text(json.dumps(self.state, indent=2))
        except Exception as e:
            log.warning("[BANDIT] state save failed: %s", e)

    def _cell(self, key: str) -> dict:
        if key not in self.state:
            self.state[key] = {p: {"n": 0, "sum_pips": 0.0, "sum_sq_pips": 0.0} for p in PROFILE_NAMES}
        return self.state[key]

    def _posterior_sample(self, stats: dict) -> float:
        n = stats["n"]
        if n == 0:
            return random.gauss(PRIOR_MEAN, math.sqrt(PRIOR_VAR))
        mean = stats["sum_pips"] / n
        if n == 1:
            var = PRIOR_VAR
        else:
            var = (stats["sum_sq_pips"] - n * mean ** 2) / (n - 1)
            var = max(var, 0.01)
        post_var = var / n
        return random.gauss(mean, math.sqrt(post_var))

    def choose_profile(self, pair: str, strategy: str, regime: str):
        with self._lock:
            key = cell_key(pair, strategy, regime)
            cell = self._cell(key)
            under_explored = [p for p in PROFILE_NAMES if cell[p]["n"] < self.min_explore]
            if under_explored:
                chosen = random.choice(under_explored)
                reason = "explore"
            else:
                samples = {p: self._posterior_sample(cell[p]) for p in PROFILE_NAMES}
                chosen = max(samples, key=samples.get)
                reason = "thompson"
            debug = {
                "cell": key, "chosen": chosen, "reason": reason,
                "stats": {p: {"n": int(cell[p]["n"]),
                              "mean_pip": (cell[p]["sum_pips"] / cell[p]["n"]) if cell[p]["n"] else None,
                              } for p in PROFILE_NAMES},
            }
            return PROFILES[chosen], debug

    def observe(self, profile_name: str, pair: str, strategy: str, regime: str,
                pnl_pips: float, extra: dict | None = None) -> None:
        with self._lock:
            key = cell_key(pair, strategy, regime)
            cell = self._cell(key)
            if profile_name not in cell:
                return
            stats = cell[profile_name]
            stats["n"] = int(stats["n"]) + 1
            stats["sum_pips"] = float(stats["sum_pips"]) + float(pnl_pips)
            stats["sum_sq_pips"] = float(stats["sum_sq_pips"]) + float(pnl_pips) ** 2
            self._save()
            try:
                entry = {
                    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "cell": key, "profile": profile_name,
                    "pnl_pips": round(float(pnl_pips), 2),
                    "n_after": int(stats["n"]),
                    "mean_after": round(stats["sum_pips"] / stats["n"], 2) if stats["n"] else None,
                    **(extra or {}),
                }
                with self.shadow_log.open("a") as f:
                    f.write(json.dumps(entry) + "\n")
            except Exception as e:
                log.debug("[BANDIT] log write failed: %s", e)


_BANDIT: Optional[ExitProfileBandit] = None
_BANDIT_LOCK = threading.Lock()


def get_bandit() -> ExitProfileBandit:
    global _BANDIT
    with _BANDIT_LOCK:
        if _BANDIT is None:
            _BANDIT = ExitProfileBandit()
        return _BANDIT
