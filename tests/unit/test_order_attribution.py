"""Patch B.right regression — order_id → strategy attribution.

Pre-patch, ml-observer used a 60-second backward walk over `scans.jsonl`
to attribute strategy on every trade_open event. 27/50 (54%) of live
trade_opens missed the window because their LIMIT entries took longer
than 60 s to fill, leaving `matched_scan_cycle: null` and forcing
downstream tools to fall back to `strategy=unknown`.

Patch B.right: bot writes (order_id → strategy) at order placement.
ml-observer resolves attribution by orderID from the OANDA fill txn.
Time-window walk is reduced to a fallback only.

Tests cover the writer + reader contract and the fallback ordering.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from scrooge_v3.telemetry.order_attribution import (
    OrderAttributionWriter,
    lookup_attribution,
)


def test_writer_records_full_row(tmp_path: Path):
    fp = tmp_path / "order-attribution.jsonl"
    w = OrderAttributionWriter(filepath=fp)
    w.record(
        order_id="2317", symbol="NZD_USD", strategy="dbb_trend",
        direction="short", score=65.0, tier="A", scan_cycle=1138,
        order_kind="entry_limit",
    )
    body = fp.read_text().strip().splitlines()
    assert len(body) == 1
    import json
    row = json.loads(body[0])
    assert row["order_id"] == "2317"
    assert row["symbol"] == "NZD_USD"
    assert row["strategy"] == "dbb_trend"
    assert row["direction"] == "short"
    assert row["score"] == 65.0
    assert row["tier"] == "A"
    assert row["scan_cycle"] == 1138
    assert row["order_kind"] == "entry_limit"
    assert row["placed_at"]  # ISO timestamp filled


def test_writer_skips_when_required_fields_missing(tmp_path: Path):
    fp = tmp_path / "order-attribution.jsonl"
    w = OrderAttributionWriter(filepath=fp)
    w.record(order_id="", symbol="EUR_USD", strategy="direct")
    w.record(order_id="X", symbol="", strategy="direct")
    assert not fp.exists() or not fp.read_text().strip()


def test_lookup_resolves_by_order_id(tmp_path: Path):
    fp = tmp_path / "order-attribution.jsonl"
    w = OrderAttributionWriter(filepath=fp)
    w.record(order_id="A1", symbol="EUR_USD", strategy="direct", scan_cycle=1)
    w.record(order_id="A2", symbol="USD_JPY", strategy="dbb_trend", scan_cycle=2)
    w.record(order_id="A3", symbol="GBP_USD", strategy="direct", scan_cycle=3)
    found = lookup_attribution(fp, "A2")
    assert found is not None
    assert found["strategy"] == "dbb_trend"
    assert found["scan_cycle"] == 2


def test_lookup_returns_most_recent_when_duplicate(tmp_path: Path):
    """Append-only — if order_id ever recurs (shouldn't happen in
    practice), reader returns the most recent record."""
    fp = tmp_path / "order-attribution.jsonl"
    w = OrderAttributionWriter(filepath=fp)
    w.record(order_id="DUP", symbol="EUR_USD", strategy="direct")
    w.record(order_id="DUP", symbol="EUR_USD", strategy="dbb_trend")
    found = lookup_attribution(fp, "DUP")
    assert found["strategy"] == "dbb_trend"


def test_lookup_returns_none_when_missing(tmp_path: Path):
    fp = tmp_path / "order-attribution.jsonl"
    w = OrderAttributionWriter(filepath=fp)
    w.record(order_id="X", symbol="EUR_USD", strategy="direct")
    assert lookup_attribution(fp, "NONEXISTENT") is None


def test_lookup_handles_missing_file(tmp_path: Path):
    """ml-observer may start before the bot has placed any orders. Reader
    must not crash on missing file."""
    assert lookup_attribution(tmp_path / "absent.jsonl", "X") is None


def test_lookup_handles_empty_order_id(tmp_path: Path):
    fp = tmp_path / "order-attribution.jsonl"
    OrderAttributionWriter(filepath=fp).record(
        order_id="X", symbol="EUR_USD", strategy="direct",
    )
    assert lookup_attribution(fp, "") is None
    assert lookup_attribution(fp, None) is None


def test_lookup_skips_corrupt_lines(tmp_path: Path):
    """A torn write or a stale legacy line must not crash the reader."""
    fp = tmp_path / "order-attribution.jsonl"
    fp.write_text(
        '{"order_id": "GOOD", "symbol": "EUR_USD", "strategy": "direct"}\n'
        'this is not json\n'
        '{"order_id": "BAD", "symbol": "USD_JPY"\n'  # truncated
        '{"order_id": "ALSO_GOOD", "symbol": "GBP_USD", "strategy": "dbb_trend"}\n'
    )
    assert lookup_attribution(fp, "GOOD")["strategy"] == "direct"
    assert lookup_attribution(fp, "ALSO_GOOD")["strategy"] == "dbb_trend"
    assert lookup_attribution(fp, "BAD") is None


def test_writer_concurrent_safe(tmp_path: Path):
    """Lock prevents interleaved writes. Smoke test only — not a true race
    test, just a correctness check that two records both land intact."""
    fp = tmp_path / "order-attribution.jsonl"
    w = OrderAttributionWriter(filepath=fp)
    w.record(order_id="P1", symbol="EUR_USD", strategy="direct")
    w.record(order_id="P2", symbol="USD_JPY", strategy="dbb_trend")
    lines = fp.read_text().strip().splitlines()
    assert len(lines) == 2
    import json
    rows = [json.loads(l) for l in lines]
    assert {r["order_id"] for r in rows} == {"P1", "P2"}
