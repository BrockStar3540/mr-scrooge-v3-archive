"""Unit tests for position sizing — verifies USD-base / USD-quote / cross pairs."""

import pytest

from scrooge_v3.execution.sizing import (
    SizingCalculator,
    classify_pair,
    compute_notional_and_pip,
)


def test_classify_pair():
    assert classify_pair("USD_JPY") == "usd_base"
    assert classify_pair("EUR_USD") == "usd_quote"
    assert classify_pair("EUR_JPY") == "cross"
    assert classify_pair("AUD_NZD") == "cross"


def test_notional_usd_base_jpy():
    # USD_JPY @ 159.18: pip 0.01, 1 unit = 1 USD
    n, p, fam = compute_notional_and_pip("USD_JPY", 159.18, 0.01)
    assert fam == "usd_base"
    assert n == pytest.approx(1.0)
    # pip value per unit in USD: 0.01 / 159.18 ≈ 0.0000628
    assert p == pytest.approx(0.01 / 159.18, rel=1e-4)


def test_notional_usd_quote_eurusd():
    n, p, fam = compute_notional_and_pip("EUR_USD", 1.08, 0.0001)
    assert fam == "usd_quote"
    assert n == pytest.approx(1.08)
    assert p == pytest.approx(0.0001)


def test_notional_cross_eurjpy_with_conversion():
    # EUR_JPY @ 170, EUR->USD = 1.08
    lookup = lambda ccy: 1.08 if ccy == "EUR" else None
    n, p, fam = compute_notional_and_pip("EUR_JPY", 170.0, 0.01, lookup)
    assert fam == "cross"
    assert n == pytest.approx(1.08)
    # pip in USD: 0.01 * 1.08 / 170 ≈ 0.0000635
    assert p == pytest.approx(0.01 * 1.08 / 170.0, rel=1e-4)


def test_notional_cross_approx_when_no_lookup():
    n, p, fam = compute_notional_and_pip("AUD_NZD", 1.216, 0.0001, None)
    assert fam == "cross_approx"
    assert n == pytest.approx(1.0)


def test_usd_jpy_sizing_util_0_4():
    """USD_JPY @ 159.18, equity $82,301, margin_util 0.4, margin_rate 0.05.
    target_margin = 32920.4 ; notional = 1 USD ; units = 32920.4 / (1 * 0.05) = 658,408."""
    sizer = SizingCalculator(config={"margin_utilization": 0.4})
    inst_info = {"pipLocation": -2, "marginRate": 0.05}
    units = sizer.calculate("USD_JPY", 159.18, 82301.0, inst_info, free_margin=1_000_000.0)
    assert units == pytest.approx(658_408, rel=0.002)


def test_usd_jpy_sizing_util_0_8():
    sizer = SizingCalculator(config={"margin_utilization": 0.8})
    inst_info = {"pipLocation": -2, "marginRate": 0.05}
    units = sizer.calculate("USD_JPY", 159.18, 82301.0, inst_info, free_margin=1_000_000.0)
    assert units == pytest.approx(1_316_816, rel=0.002)


def test_eur_usd_sizing_util_0_4():
    """EUR_USD @ 1.08, equity $82,301, margin_util 0.4, margin_rate 0.03.
    notional/unit = 1.08 USD ; target = 32920.4 ; units = 32920.4 / (1.08 * 0.03) ≈ 1,016,062."""
    sizer = SizingCalculator(config={"margin_utilization": 0.4})
    inst_info = {"pipLocation": -4, "marginRate": 0.03}
    units = sizer.calculate("EUR_USD", 1.08, 82301.0, inst_info, free_margin=1_000_000.0)
    # spec says ~1,097,000 but math: 32920.4 / 0.0324 = 1,016,062
    # (spec was approximate — test the actual correct math)
    assert units == pytest.approx(1_016_062, rel=0.005)


def test_eur_usd_pip_value_in_log(caplog):
    """For EUR_USD @ $109/pip target: units * 0.0001 should be ~$109."""
    import logging
    sizer = SizingCalculator(config={"margin_utilization": 0.4})
    inst_info = {"pipLocation": -4, "marginRate": 0.03}
    with caplog.at_level(logging.INFO, logger="scrooge_v3.execution.sizing"):
        units = sizer.calculate("EUR_USD", 1.08, 82301.0, inst_info, free_margin=1_000_000.0)
    pip_dollar = units * 0.0001
    assert pip_dollar == pytest.approx(101.6, rel=0.02)


def test_aud_nzd_cross_approx_logs_warning(caplog):
    import logging
    sizer = SizingCalculator(config={"margin_utilization": 0.4})
    inst_info = {"pipLocation": -4, "marginRate": 0.03}
    with caplog.at_level(logging.WARNING, logger="scrooge_v3.execution.sizing"):
        units = sizer.calculate(
            "AUD_NZD", 1.216, 82301.0, inst_info, free_margin=1_000_000.0,
            usd_conversion_lookup=lambda c: None,
        )
    assert units is not None
    assert any("no USD conversion" in r.message for r in caplog.records)


def test_aud_nzd_cross_with_conversion():
    """AUD->USD = 0.66, AUD_NZD @ 1.216. notional = 0.66 USD/unit.
    target = 32920.4 ; units = 32920.4 / (0.66 * 0.03) ≈ 1,662,645."""
    sizer = SizingCalculator(config={"margin_utilization": 0.4})
    inst_info = {"pipLocation": -4, "marginRate": 0.03}
    units = sizer.calculate(
        "AUD_NZD", 1.216, 82301.0, inst_info, free_margin=1_000_000.0,
        usd_conversion_lookup=lambda c: 0.66 if c == "AUD" else None,
    )
    assert units == pytest.approx(1_662_645, rel=0.005)


def test_gbp_jpy_cross():
    """GBP_JPY @ 214.46, GBP->USD = 1.27. notional = 1.27 USD/unit.
    target (util 0.4) = 32920.4; margin_rate 0.05;
    units = 32920.4 / (1.27 * 0.05) ≈ 518,431."""
    sizer = SizingCalculator(config={"margin_utilization": 0.4})
    inst_info = {"pipLocation": -2, "marginRate": 0.05}
    units = sizer.calculate(
        "GBP_JPY", 214.46, 82301.0, inst_info, free_margin=1_000_000.0,
        usd_conversion_lookup=lambda c: 1.27 if c == "GBP" else None,
    )
    assert units == pytest.approx(518_431, rel=0.005)
