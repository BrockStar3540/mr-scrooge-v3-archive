"""Phase 3 — replay of live trade 1445 AUD/USD with R-relative BE + pip floor.

Setup: AUD/USD long, entry 0.71546, SL 0.71510, R = 3.6 pips.

Old behavior: be_trigger_pips=5 never fired (needs 1.4R) -> full stop taken.
New behavior: be_trigger_min_pips=2.0 floor fires at +2 pips, BE+1-pip
offset locks the trade at 0.71556 (1 pip above entry, +0.28R).

Expected outcome: a subsequent retrace to the original stop closes the
trade at +1-pip lock instead of -3.6-pip loss.
"""

from __future__ import annotations

import pytest

from scrooge_v3.core.types import TradeDirection
from scrooge_v3.management.be_manager import BreakEvenManager


def test_trade_1445_replay_r_relative_be_saves_the_trade():
    entry = 0.71546
    sl = 0.71510  # -3.6 pips
    R = entry - sl  # 0.00036

    be = BreakEvenManager({
        "be_trigger_r": 0.5,
        "be_trigger_min_pips": 2.0,
        "be_offset_r": 0.1,
        "be_offset_min_pips": 1.0,
    })

    # Phase 1: price moves up 2.5 pips (below 0.5R = 1.8 pips AND above
    # the 2-pip floor). BE must fire via the floor.
    current = entry + 2.5 * 0.0001
    plan = be.should_move_to_be(
        TradeDirection.LONG, entry, current, sl, pip_size=0.0001,
        initial_risk_distance=R,
    )
    assert plan is not None, (
        "BE must fire at +2.5 pips (above 2-pip floor) — old code would miss it "
        "because 2.5 pips < 0.5R (1.8 pips) AND 2.5 pips < old 5-pip trigger."
    )
    # Offset: max(0.1 * 0.00036, 1 * 0.0001) = max(0.000036, 0.0001) = 0.0001
    # BE = 0.71556 (entry + 1 pip)
    assert plan.new_stop == pytest.approx(0.71556, abs=1e-6)

    # Phase 2: retrace to original stop level. Because SL is now 0.71556
    # (BE + 1 pip), the retrace closes the trade in small profit, not
    # at the -3.6-pip loss of the original setup.
    new_sl = plan.new_stop
    realized = new_sl - entry  # +1 pip
    assert realized > 0, "BE should lock profit, not a loss"
    # Saved distance compared to original loss.
    saved = (entry - sl) + realized  # old loss + new profit
    assert saved == pytest.approx(0.00046, abs=1e-6)  # 4.6-pip swing
