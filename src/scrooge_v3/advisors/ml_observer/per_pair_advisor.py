"""per_pair_advisor.py — the new ML observer brain.

For every scan the bot emits, this advisor:
  1. Identifies the pair (from candidate.symbol)
  2. Looks up the candidate's regime via PairModule.assign_regime
  3. Matches the candidate against that regime's WIN and LOSE rules
  4. Logs (regime, matched rules, decision) to scans_per_pair.jsonl
  5. On trade close, updates per-rule live W/L stats

This is intentionally separate from observer.py's cluster_serial machinery
(which targets the legacy matrix). The new advisor talks only to the 28
self-contained per-pair modules.

Persistent state files (under data/ml-observer/):
  scans_per_pair.jsonl       — every advised scan, one line each
  outcomes_per_pair.jsonl    — every closed trade, one line each
  per_pair_live_stats.json   — accumulated per-rule live W/L counts
"""

from __future__ import annotations

import json
import logging
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

try:
    from . import per_pair_modules as ppm
except (ImportError, ValueError):
    # Flat-import style (matches observer.py's launch context)
    import per_pair_modules as ppm  # type: ignore

DATA_DIR = Path("/home/ubuntu/mr-scrooge-v3/data/ml-observer")
SCANS_FILE = DATA_DIR / "scans_per_pair.jsonl"
OUTCOMES_FILE = DATA_DIR / "outcomes_per_pair.jsonl"
STATS_FILE = DATA_DIR / "per_pair_live_stats.json"

log = logging.getLogger("scrooge_v3.ml_observer.per_pair_advisor")


# ---------------------------------------------------------------------------
# Persistent live-rule statistics
# ---------------------------------------------------------------------------
def _load_stats() -> dict:
    if STATS_FILE.exists():
        try:
            return json.loads(STATS_FILE.read_text())
        except Exception:
            log.exception("[PPA] failed to load live stats, starting fresh")
    return {}


def _save_stats(stats: dict) -> None:
    tmp = STATS_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(stats, indent=2, sort_keys=True))
    tmp.replace(STATS_FILE)


def _append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(row) + "\n")


# ---------------------------------------------------------------------------
# Advisor — singleton
# ---------------------------------------------------------------------------
class PerPairAdvisor:
    def __init__(self):
        # Force module load + log inventory
        ppm.load_all()
        self.stats = _load_stats()
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        log.info("[PPA] advisor ready — %d pair modules, stats has %d pair entries",
                 len(ppm.pairs()), len(self.stats))

    # ----------------------------------------------------------------
    # Per-scan
    # ----------------------------------------------------------------
    def advise_scan(self, scan: dict) -> dict:
        """Evaluate one scan against its pair's module.

        scan must contain:
          symbol         — e.g. "EUR_USD"
          buckets        — dict {factor_code: bucket_code} for all 14 factors
          session_bucket — string
          strategy       — strategy_id
          direction      — "long" / "short"

        Returns dict with keys: pair, regime, win_rule_count, lose_rule_count,
        decision, top_win, top_lose, plain_english.
        """
        pair = (scan.get("symbol") or "").strip()
        buckets = scan.get("buckets") or {}
        session = scan.get("session_bucket") or ""
        strategy = scan.get("strategy") or ""
        direction = (scan.get("direction") or "").lower().replace("tradedirection.", "")

        module = ppm.get(pair, strategy)
        if module is None:
            verdict = {
                "pair": pair, "regime": None,
                "decision": "no_module",
                "win_rule_count": 0, "lose_rule_count": 0,
                "top_win": None, "top_lose": None,
                "plain_english": f"no per-pair module for {pair}",
            }
            self._record_scan(scan, verdict)
            return verdict

        regime = module.assign_regime(buckets)
        match = module.match_rules(regime, session, buckets, strategy, direction)
        wins = match["win_rules"]
        loses = match["lose_rules"]

        if loses:
            # ANY lose-rule match -> BLOCK
            top = max(loses, key=lambda r: (r["lab_n"], -r["lab_wr"]))
            decision = "BLOCK"
            plain = (f"loser veto: {top['raw_rule']} -> lab WR {top['lab_wr']:.0%} "
                     f"on n={top['lab_n']}")
        elif wins:
            # >=1 winner match -> PASS
            top = max(wins, key=lambda r: (r["lab_wr"], r["lab_n"]))
            decision = "PASS"
            plain = (f"winner allow: {top['raw_rule']} -> lab WR {top['lab_wr']:.0%} "
                     f"on n={top['lab_n']}")
        else:
            decision = "no_signal"
            top = None
            plain = "no matching rule"

        verdict = {
            "pair": pair, "regime": regime,
            "decision": decision,
            "win_rule_count": len(wins), "lose_rule_count": len(loses),
            "top_win": wins[0] if wins else None,
            "top_lose": loses[0] if loses else None,
            "plain_english": plain,
        }
        self._record_scan(scan, verdict)
        return verdict

    def _record_scan(self, scan: dict, verdict: dict) -> None:
        row = {
            "ts": scan.get("ts") or datetime.now(timezone.utc).isoformat(),
            "trade_id": scan.get("trade_id"),
            "scan_id": scan.get("scan_id"),
            "pair": verdict["pair"], "regime": verdict["regime"],
            "session": scan.get("session_bucket"),
            "strategy": scan.get("strategy"),
            "direction": scan.get("direction"),
            "buckets": scan.get("buckets"),
            "decision": verdict["decision"],
            "win_rule_count": verdict["win_rule_count"],
            "lose_rule_count": verdict["lose_rule_count"],
            "matched_win_rule": verdict["top_win"]["raw_rule"] if verdict["top_win"] else None,
            "matched_lose_rule": verdict["top_lose"]["raw_rule"] if verdict["top_lose"] else None,
            "plain_english": verdict["plain_english"],
        }
        _append_jsonl(SCANS_FILE, row)

    # ----------------------------------------------------------------
    # Per outcome
    # ----------------------------------------------------------------
    def record_outcome(self, outcome: dict) -> None:
        """Update per-rule live stats when a trade closes.

        outcome must contain:
          symbol, trade_id, pnl_pips OR realized_pnl_usd, win (bool)
        plus the matched rule info captured earlier in the scan log row
        (re-resolved by trade_id below).
        """
        pair = outcome.get("symbol") or outcome.get("pair") or ""
        tid = outcome.get("trade_id")
        won = bool(outcome.get("win"))
        if not pair or tid is None:
            return

        scan_row = self._find_scan_for_trade(pair, tid)
        if not scan_row:
            log.warning("[PPA] outcome for tid=%s pair=%s has no scan attribution",
                        tid, pair)
            return

        regime = scan_row.get("regime") or "Rxx"
        matched_win = scan_row.get("matched_win_rule") or ""
        matched_lose = scan_row.get("matched_lose_rule") or ""

        # Update stats per rule
        pair_stats = self.stats.setdefault(pair, {})
        regime_stats = pair_stats.setdefault(regime, {})

        for rule_key, rule_text in (("win", matched_win), ("lose", matched_lose)):
            if not rule_text:
                continue
            rs = regime_stats.setdefault(rule_text, {
                "rule_type": rule_key.upper(),
                "live_n": 0, "live_w": 0, "live_l": 0,
            })
            rs["live_n"] += 1
            if won:
                rs["live_w"] += 1
            else:
                rs["live_l"] += 1
            rs["live_wr"] = rs["live_w"] / rs["live_n"]

        _append_jsonl(OUTCOMES_FILE, {
            "ts": outcome.get("ts") or datetime.now(timezone.utc).isoformat(),
            "trade_id": tid, "pair": pair, "won": won,
            "pnl_pips": outcome.get("pnl_pips"),
            "regime": regime,
            "matched_win_rule": matched_win,
            "matched_lose_rule": matched_lose,
        })
        _save_stats(self.stats)

    def _find_scan_for_trade(self, pair: str, trade_id) -> Optional[dict]:
        if not SCANS_FILE.exists():
            return None
        # Walk backward — most recent scan for this pair+trade_id wins
        candidate = None
        with SCANS_FILE.open() as f:
            for line in f:
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if r.get("pair") == pair and str(r.get("trade_id")) == str(trade_id):
                    candidate = r
        return candidate


# ---------------------------------------------------------------------------
# Singleton helper
# ---------------------------------------------------------------------------
_INSTANCE: Optional[PerPairAdvisor] = None


def get_advisor() -> PerPairAdvisor:
    global _INSTANCE
    if _INSTANCE is None:
        _INSTANCE = PerPairAdvisor()
    return _INSTANCE
