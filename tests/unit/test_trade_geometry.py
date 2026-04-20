"""Phase 3 — Bug F: trade_geometry canonical helpers."""

from __future__ import annotations

import pytest

from scrooge_v3.core.trade_geometry import (
    PairFamily,
    classify_pair,
    compute_tp1,
    initial_risk,
    pip_size,
    price_distance_to_r,
    r_to_price,
    r_to_price_distance,
)


class TestPipSize:
    def test_jpy_base_is_big_pip(self):
        assert pip_size("USD_JPY") == 0.01
        assert pip_size("JPY_USD") == 0.01

    def test_jpy_cross_is_big_pip(self):
        assert pip_size("AUD_JPY") == 0.01
        assert pip_size("EUR_JPY") == 0.01
        assert pip_size("NZD_JPY") == 0.01

    def test_non_jpy_is_small_pip(self):
        assert pip_size("EUR_USD") == 0.0001
        assert pip_size("AUD_USD") == 0.0001
        assert pip_size("GBP_CHF") == 0.0001

    def test_empty_symbol_defaults_non_jpy(self):
        assert pip_size("") == 0.0001


class TestClassify:
    def test_usd_base(self):
        assert classify_pair("USD_JPY") == PairFamily.USD_BASE
        assert classify_pair("USD_CAD") == PairFamily.USD_BASE

    def test_usd_quote(self):
        assert classify_pair("EUR_USD") == PairFamily.USD_QUOTE
        assert classify_pair("AUD_USD") == PairFamily.USD_QUOTE

    def test_jpy_cross(self):
        assert classify_pair("AUD_JPY") == PairFamily.JPY_CROSS
        assert classify_pair("EUR_JPY") == PairFamily.JPY_CROSS

    def test_non_jpy_cross(self):
        assert classify_pair("EUR_GBP") == PairFamily.CROSS
        assert classify_pair("AUD_NZD") == PairFamily.CROSS

    def test_malformed(self):
        assert classify_pair("BTCUSD") == PairFamily.CROSS


class TestRConversions:
    @pytest.mark.parametrize(
        "entry,sl,expected",
        [
            (1.1000, 1.0950, 0.0050),   # 50-pip non-JPY
            (113.651, 113.912, 0.261),  # 26.1-pip AUD/JPY short
            (1.0, 1.0, 0.0),             # no risk edge case
        ],
    )
    def test_initial_risk(self, entry, sl, expected):
        assert initial_risk(entry, sl) == pytest.approx(expected, abs=1e-6)

    def test_r_to_price_distance(self):
        assert r_to_price_distance(1.0, 0.005) == pytest.approx(0.005)
        assert r_to_price_distance(2.5, 0.005) == pytest.approx(0.0125)

    def test_price_distance_to_r(self):
        assert price_distance_to_r(0.010, 0.005) == pytest.approx(2.0)
        assert price_distance_to_r(0.005, 0.0) == 0.0  # safe divide

    def test_r_to_price_long_and_short(self):
        # Long: TP above entry
        assert r_to_price(1.1000, +1, 1.0, 0.005) == pytest.approx(1.1050)
        # Short: TP below entry
        assert r_to_price(1.1000, -1, 1.0, 0.005) == pytest.approx(1.0950)


class TestComputeTp1:
    def test_one_r_long(self):
        tp1 = compute_tp1(1.1000, 1.0950, "long", tp1_r=1.0)
        assert tp1 == pytest.approx(1.1050)

    def test_one_r_short_jpy(self):
        tp1 = compute_tp1(113.651, 113.912, "short", tp1_r=1.0)
        # R=0.261, TP1 = 113.651 - 0.261 = 113.390
        assert tp1 == pytest.approx(113.390, abs=1e-5)

    def test_custom_r_multiple(self):
        tp1 = compute_tp1(1.1000, 1.0950, "long", tp1_r=2.0)
        assert tp1 == pytest.approx(1.1100)

    def test_invalid_returns_zero(self):
        assert compute_tp1(0, 1.0, "long") == 0.0
        assert compute_tp1(1.0, 0, "long") == 0.0
        assert compute_tp1(1.0, 1.0, "long") == 0.0  # no risk
