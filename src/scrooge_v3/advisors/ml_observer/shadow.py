#!/usr/bin/env python3
# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
Current-corpus shadow observer.

Builds a bank strictly from the current V3 observer corpus:
    scans.jsonl + outcomes.jsonl

The bank is hierarchical:
    1. exact bucket   — symbol + strategy + direction + regime + session + match kind
    2. strategy bucket
    3. family bucket

It then emits shadow decisions and maintains a simple parallel tradebook
without touching the broker.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from config import (
    SHADOW_MIN_AVG_PNL_USD,
    SHADOW_MIN_TRADES_EXACT,
    SHADOW_MIN_TRADES_FAMILY,
    SHADOW_MIN_TRADES_STRATEGY,
    SHADOW_MIN_WIN_RATE,
)


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    try:
        with open(path) as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except OSError:
        return []
    return rows


def _identity_from_scan(row: dict[str, Any]) -> dict[str, Any]:
    identity = dict(row.get("identity") or {})
    candidate = dict(row.get("candidate") or {})
    identity.setdefault("strategy", candidate.get("strategy") or "")
    identity.setdefault("family", candidate.get("family") or "")
    identity.setdefault("direction", candidate.get("direction") or "")
    identity.setdefault("routing_cell_strategy", candidate.get("routing_cell_strategy") or "")
    identity.setdefault("routing_cell_family", candidate.get("routing_cell_family") or "")
    identity.setdefault("routing_cell_tier", candidate.get("routing_cell_tier") or "")
    identity.setdefault("routing_match_kind", candidate.get("routing_match_kind") or "")
    identity["symbol"] = str(row.get("symbol") or "")
    identity["verdict"] = str(row.get("verdict") or "")
    return identity


def _exact_key(identity: dict[str, Any]) -> str:
    parts = [
        identity.get("symbol", ""),
        identity.get("strategy", ""),
        identity.get("direction", ""),
        identity.get("regime53", ""),
        identity.get("sub_regime", ""),
        identity.get("session_bucket", ""),
        identity.get("routing_cell_strategy", ""),
        identity.get("routing_match_kind", ""),
    ]
    return "|".join(str(p or "") for p in parts)


def _strategy_key(identity: dict[str, Any]) -> str:
    parts = [
        identity.get("symbol", ""),
        identity.get("strategy", ""),
        identity.get("direction", ""),
        identity.get("regime53", ""),
        identity.get("session_bucket", ""),
    ]
    return "|".join(str(p or "") for p in parts)


def _family_key(identity: dict[str, Any]) -> str:
    parts = [
        identity.get("symbol", ""),
        identity.get("family", ""),
        identity.get("direction", ""),
        identity.get("regime53", ""),
        identity.get("session_bucket", ""),
    ]
    return "|".join(str(p or "") for p in parts)


def _bank_entry(identity: dict[str, Any]) -> dict[str, Any]:
    return {
        "identity": identity,
        "n": 0,
        "wins": 0,
        "losses": 0,
        "scratches": 0,
        "sum_pnl_usd": 0.0,
        "avg_pnl_usd": 0.0,
        "win_rate": 0.0,
        "last_close_ts": None,
    }


def _apply_outcome(bucket: dict[str, Any], pnl: float, ts: str, label: str) -> None:
    bucket["n"] += 1
    bucket["sum_pnl_usd"] += float(pnl)
    bucket["avg_pnl_usd"] = bucket["sum_pnl_usd"] / max(bucket["n"], 1)
    if label == "win":
        bucket["wins"] += 1
    elif label == "loss":
        bucket["losses"] += 1
    else:
        bucket["scratches"] += 1
    decisive = bucket["wins"] + bucket["losses"]
    bucket["win_rate"] = bucket["wins"] / decisive if decisive else 0.0
    bucket["last_close_ts"] = ts


def _extract_market_price(scan_row: dict[str, Any]) -> float:
    features = scan_row.get("features") or {}
    scorer = scan_row.get("scorer") or {}
    candidate = scan_row.get("candidate") or {}
    price = 0.0
    try:
        price = float((((features.get("bollinger") or {}).get("current_close")) or 0.0))
    except (TypeError, ValueError):
        price = 0.0
    if price > 0:
        return price
    try:
        price = float((((scorer.get("context") or {}).get("px")) or 0.0))
    except (TypeError, ValueError):
        price = 0.0
    if price > 0:
        return price
    try:
        return float(candidate.get("entry_price") or 0.0)
    except (TypeError, ValueError):
        return 0.0


def build_shadow_bank(scans_path: Path, outcomes_path: Path) -> dict[str, Any]:
    scans = _load_jsonl(scans_path)
    outcomes = _load_jsonl(outcomes_path)

    scan_by_ts_symbol: dict[tuple[str, str], dict[str, Any]] = {}
    for row in scans:
        ts = str(row.get("ts") or "")
        symbol = str(row.get("symbol") or "")
        if ts and symbol:
            scan_by_ts_symbol[(ts, symbol)] = row

    opens_by_trade: dict[str, dict[str, Any]] = {}
    closes_by_trade: dict[str, dict[str, Any]] = {}

    for row in outcomes:
        trade_id = str(row.get("trade_id") or "")
        kind = str(row.get("kind") or "")
        if not trade_id or not kind:
            continue
        if kind == "trade_open":
            opens_by_trade[trade_id] = row
            continue
        if kind != "trade_close":
            continue
        agg = closes_by_trade.setdefault(trade_id, {
            "trade_id": trade_id,
            "symbol": row.get("symbol"),
            "sum_pnl_usd": 0.0,
            "last_ts": row.get("ts"),
            "close_events": 0,
        })
        agg["sum_pnl_usd"] += float(row.get("realized_pnl_usd", 0.0) or 0.0)
        agg["close_events"] += 1
        if row.get("ts"):
            agg["last_ts"] = row["ts"]

    exact: dict[str, dict[str, Any]] = {}
    strategy: dict[str, dict[str, Any]] = {}
    family: dict[str, dict[str, Any]] = {}
    labeled_examples = 0

    for trade_id, close in closes_by_trade.items():
        open_row = opens_by_trade.get(trade_id)
        if not open_row:
            continue
        matched_ts = str(open_row.get("matched_scan_ts") or "")
        symbol = str(open_row.get("symbol") or close.get("symbol") or "")
        scan_row = scan_by_ts_symbol.get((matched_ts, symbol))
        if not scan_row:
            continue
        identity = _identity_from_scan(scan_row)
        if not identity.get("strategy") or not identity.get("direction"):
            continue
        labeled_examples += 1
        pnl = float(close.get("sum_pnl_usd", 0.0) or 0.0)
        if pnl > 0:
            label = "win"
        elif pnl < 0:
            label = "loss"
        else:
            label = "scratch"

        ex_key = _exact_key(identity)
        st_key = _strategy_key(identity)
        fam_key = _family_key(identity)

        exact.setdefault(ex_key, _bank_entry(identity))
        strategy.setdefault(st_key, _bank_entry(identity))
        family.setdefault(fam_key, _bank_entry(identity))

        _apply_outcome(exact[ex_key], pnl, str(close.get("last_ts") or ""), label)
        _apply_outcome(strategy[st_key], pnl, str(close.get("last_ts") or ""), label)
        _apply_outcome(family[fam_key], pnl, str(close.get("last_ts") or ""), label)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_counts": {
            "scans": len(scans),
            "outcome_rows": len(outcomes),
            "trade_opens": len(opens_by_trade),
            "closed_trade_ids": len(closes_by_trade),
            "labeled_examples": labeled_examples,
        },
        "thresholds": {
            "exact_min_trades": SHADOW_MIN_TRADES_EXACT,
            "strategy_min_trades": SHADOW_MIN_TRADES_STRATEGY,
            "family_min_trades": SHADOW_MIN_TRADES_FAMILY,
            "min_win_rate": SHADOW_MIN_WIN_RATE,
            "min_avg_pnl_usd": SHADOW_MIN_AVG_PNL_USD,
        },
        "summaries": {
            "exact_buckets": len(exact),
            "strategy_buckets": len(strategy),
            "family_buckets": len(family),
        },
        "exact": exact,
        "strategy": strategy,
        "family": family,
    }


def save_shadow_bank(bank: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(bank, indent=2, default=str))


def build_comparison_summary(outcomes_path: Path, shadow_trades_path: Path) -> dict[str, Any]:
    outcomes = _load_jsonl(outcomes_path)
    shadow_trades = _load_jsonl(shadow_trades_path)

    v3_closes = [row for row in outcomes if row.get("kind") == "trade_close"]
    shadow_closes = [row for row in shadow_trades if row.get("kind") == "shadow_trade_close"]

    def _wr(rows: list[dict[str, Any]], win_pred) -> float:
        if not rows:
            return 0.0
        wins = sum(1 for row in rows if win_pred(row))
        return wins / len(rows)

    def _group(rows: list[dict[str, Any]], field: str, pnl_field: str, win_pred) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for row in rows:
            key = str(row.get(field) or "unknown")
            bucket = out.setdefault(key, {"n": 0, "wins": 0, "sum_pnl": 0.0})
            bucket["n"] += 1
            bucket["sum_pnl"] += float(row.get(pnl_field, 0.0) or 0.0)
            if win_pred(row):
                bucket["wins"] += 1
        for bucket in out.values():
            bucket["win_rate"] = bucket["wins"] / bucket["n"] if bucket["n"] else 0.0
        return out

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "v3": {
            "closed_trades": len(v3_closes),
            "win_rate": _wr(v3_closes, lambda row: float(row.get("realized_pnl_usd", 0.0) or 0.0) > 0),
            "realized_pnl_usd": sum(float(row.get("realized_pnl_usd", 0.0) or 0.0) for row in v3_closes),
            "by_symbol": _group(v3_closes, "symbol", "realized_pnl_usd",
                                lambda row: float(row.get("realized_pnl_usd", 0.0) or 0.0) > 0),
        },
        "shadow": {
            "closed_trades": len(shadow_closes),
            "win_rate": _wr(shadow_closes, lambda row: float(row.get("pnl_r", 0.0) or 0.0) > 0),
            "sum_pnl_r": sum(float(row.get("pnl_r", 0.0) or 0.0) for row in shadow_closes),
            "sum_pnl_price": sum(float(row.get("pnl_price", 0.0) or 0.0) for row in shadow_closes),
            "by_symbol": _group(shadow_closes, "symbol", "pnl_r",
                                lambda row: float(row.get("pnl_r", 0.0) or 0.0) > 0),
        },
    }


def save_comparison_summary(summary: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, default=str))


def decide_shadow(scan_row: dict[str, Any], bank: dict[str, Any]) -> dict[str, Any]:
    identity = _identity_from_scan(scan_row)
    candidate = scan_row.get("candidate") or {}
    verdict = str(scan_row.get("verdict") or "")
    eligible = bool(
        identity.get("strategy")
        and identity.get("direction")
        and float(candidate.get("entry_price") or 0.0) > 0
        and float(candidate.get("stop_price") or 0.0) > 0
    )

    if not eligible:
        return {
            "decision": "ABSTAIN",
            "reason": "no_tradeable_candidate",
            "bank_level": None,
            "bank_stats": None,
            "identity": identity,
            "v3_verdict": verdict,
        }

    lookup_order = [
        ("exact", _exact_key(identity), SHADOW_MIN_TRADES_EXACT),
        ("strategy", _strategy_key(identity), SHADOW_MIN_TRADES_STRATEGY),
        ("family", _family_key(identity), SHADOW_MIN_TRADES_FAMILY),
    ]

    for level, key, min_trades in lookup_order:
        bucket = ((bank.get(level) or {}).get(key))
        if not bucket:
            continue
        if int(bucket.get("n", 0)) < min_trades:
            continue
        win_rate = float(bucket.get("win_rate", 0.0) or 0.0)
        avg_pnl = float(bucket.get("avg_pnl_usd", 0.0) or 0.0)
        take = win_rate >= SHADOW_MIN_WIN_RATE and avg_pnl >= SHADOW_MIN_AVG_PNL_USD
        return {
            "decision": "TAKE" if take else "SKIP",
            "reason": "bank_threshold_pass" if take else "bank_threshold_fail",
            "bank_level": level,
            "bank_key": key,
            "bank_stats": bucket,
            "identity": identity,
            "v3_verdict": verdict,
        }

    return {
        "decision": "ABSTAIN",
        "reason": "insufficient_current_corpus",
        "bank_level": None,
        "bank_stats": None,
        "identity": identity,
        "v3_verdict": verdict,
    }


def shadow_decision_record(scan_row: dict[str, Any], decision: dict[str, Any]) -> dict[str, Any]:
    candidate = scan_row.get("candidate") or {}
    bank_stats = decision.get("bank_stats") or {}
    return {
        "ts": scan_row.get("ts"),
        "cycle": scan_row.get("cycle"),
        "symbol": scan_row.get("symbol"),
        "v3_verdict": scan_row.get("verdict"),
        "shadow_decision": decision.get("decision"),
        "shadow_reason": decision.get("reason"),
        "bank_level": decision.get("bank_level"),
        "bank_key": decision.get("bank_key"),
        "bank_n": bank_stats.get("n"),
        "bank_win_rate": bank_stats.get("win_rate"),
        "bank_avg_pnl_usd": bank_stats.get("avg_pnl_usd"),
        "identity": decision.get("identity"),
        "candidate": {
            "entry_price": candidate.get("entry_price"),
            "stop_price": candidate.get("stop_price"),
            "take_profit": candidate.get("take_profit"),
            "score": candidate.get("score"),
        },
    }


def update_shadow_positions(
    state: Any,
    scan_rows: list[dict[str, Any]],
    decisions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    by_symbol = {str(row.get("symbol") or ""): row for row in scan_rows}

    still_open: list[dict[str, Any]] = []
    for pos in list(getattr(state, "shadow_positions", [])):
        row = by_symbol.get(str(pos.get("symbol") or ""))
        if not row:
            still_open.append(pos)
            continue
        current_price = _extract_market_price(row)
        if current_price <= 0:
            still_open.append(pos)
            continue

        direction = str(pos.get("direction") or "")
        stop_price = float(pos.get("stop_price") or 0.0)
        take_profit = float(pos.get("take_profit") or 0.0)
        hit_stop = direction == "long" and current_price <= stop_price
        hit_stop = hit_stop or (direction == "short" and current_price >= stop_price)
        hit_tp = direction == "long" and current_price >= take_profit > 0
        hit_tp = hit_tp or (direction == "short" and current_price <= take_profit < stop_price)

        if not (hit_stop or hit_tp):
            pos["last_price"] = current_price
            pos["last_seen_ts"] = row.get("ts")
            still_open.append(pos)
            continue

        entry = float(pos.get("entry_price") or 0.0)
        risk = abs(entry - stop_price) if stop_price else 0.0
        if direction == "long":
            pnl_price = current_price - entry
        else:
            pnl_price = entry - current_price
        pnl_r = pnl_price / risk if risk > 0 else 0.0
        close_reason = "tp_hit" if hit_tp else "sl_hit"
        events.append({
            "kind": "shadow_trade_close",
            "ts": row.get("ts"),
            "shadow_trade_id": pos.get("shadow_trade_id"),
            "symbol": pos.get("symbol"),
            "strategy": pos.get("strategy"),
            "family": pos.get("family"),
            "direction": direction,
            "entry_price": entry,
            "exit_price": current_price,
            "stop_price": stop_price,
            "take_profit": take_profit,
            "pnl_price": pnl_price,
            "pnl_r": pnl_r,
            "close_reason": close_reason,
            "opened_ts": pos.get("opened_ts"),
            "bank_level": pos.get("bank_level"),
            "bank_n": pos.get("bank_n"),
            "bank_win_rate": pos.get("bank_win_rate"),
            "v3_verdict": pos.get("v3_verdict"),
        })

    state.shadow_positions = still_open

    open_signatures = {
        (
            str(pos.get("symbol") or ""),
            str(pos.get("strategy") or ""),
            str(pos.get("direction") or ""),
        )
        for pos in state.shadow_positions
    }

    for row, decision in zip(scan_rows, decisions):
        if decision.get("decision") != "TAKE":
            continue
        candidate = row.get("candidate") or {}
        identity = decision.get("identity") or {}
        signature = (
            str(row.get("symbol") or ""),
            str(identity.get("strategy") or ""),
            str(identity.get("direction") or ""),
        )
        if signature in open_signatures:
            continue
        entry_price = float(candidate.get("entry_price") or 0.0)
        stop_price = float(candidate.get("stop_price") or 0.0)
        take_profit = float(candidate.get("take_profit") or 0.0)
        if entry_price <= 0 or stop_price <= 0:
            continue
        shadow_trade_id = f"SHADOW-{getattr(state, 'shadow_next_id', 1)}"
        state.shadow_next_id = getattr(state, "shadow_next_id", 1) + 1
        bank_stats = decision.get("bank_stats") or {}
        pos = {
            "shadow_trade_id": shadow_trade_id,
            "opened_ts": row.get("ts"),
            "symbol": row.get("symbol"),
            "strategy": identity.get("strategy"),
            "family": identity.get("family"),
            "direction": identity.get("direction"),
            "entry_price": entry_price,
            "stop_price": stop_price,
            "take_profit": take_profit,
            "tp1_price": float(((candidate.get("metadata") or {}).get("tp1")) or 0.0),
            "regime53": identity.get("regime53"),
            "sub_regime": identity.get("sub_regime"),
            "session_bucket": identity.get("session_bucket"),
            "routing_match_kind": identity.get("routing_match_kind"),
            "routing_cell_strategy": identity.get("routing_cell_strategy"),
            "v3_verdict": row.get("verdict"),
            "bank_level": decision.get("bank_level"),
            "bank_n": bank_stats.get("n"),
            "bank_win_rate": bank_stats.get("win_rate"),
            "bank_avg_pnl_usd": bank_stats.get("avg_pnl_usd"),
            "source_scan_ts": row.get("ts"),
            "source_cycle": row.get("cycle"),
            "last_price": _extract_market_price(row),
            "last_seen_ts": row.get("ts"),
        }
        state.shadow_positions.append(pos)
        open_signatures.add(signature)
        events.append({
            "kind": "shadow_trade_open",
            **pos,
        })

    return events
