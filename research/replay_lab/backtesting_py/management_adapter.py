"""TP1 / BE / ratchet management replay using backtesting.py trade API."""
from __future__ import annotations


def compute_signal_anchored_levels(
    signal_entry: float, direction: str,
    sl_pips: float = 10.0, tp_pips: float = 12.0, pip_size: float = 0.0001,
) -> tuple[float, float]:
    """Scalper-clamp: signal-anchored SL/TP, direction-aware."""
    if direction == "long":
        sl = signal_entry - sl_pips * pip_size
        tp = signal_entry + tp_pips * pip_size
    else:
        sl = signal_entry + sl_pips * pip_size
        tp = signal_entry - tp_pips * pip_size
    return sl, tp


def compute_entry_price(
    signal_entry: float, direction: str, pip_size: float, mode: str,
) -> float:
    """signal | pullback_2 | pullback_4 | old_stop_zone"""
    if mode == "signal":
        return signal_entry
    if mode == "pullback_2":
        return signal_entry - 2 * pip_size if direction == "long" else signal_entry + 2 * pip_size
    if mode == "pullback_4":
        return signal_entry - 4 * pip_size if direction == "long" else signal_entry + 4 * pip_size
    if mode == "old_stop_zone":
        return signal_entry - 10 * pip_size if direction == "long" else signal_entry + 10 * pip_size
    raise ValueError(f"unknown entry_mode: {mode}")


def apply_management(
    trade,
    current_price: float,
    pip_size: float,
    direction: str,
    entry_fill: float,
    management_mode: str = "tp1_be",
    *,
    tp1_pips: float = 6.0,       # half-TP target
    be_trigger_pips: float = 7.0,
    be_offset_pips: float = 6.0,
    ratchet_steps: tuple = ((6.0, -6.0), (8.0, -3.0), (10.0, 0.0)),
) -> dict:
    """Apply TP1/BE/ratchet to a backtesting.Trade in place.

    Returns audit dict of actions taken this tick.
    """
    actions = {}
    if management_mode == "none":
        return actions

    if direction == "long":
        favor_pips = (current_price - entry_fill) / pip_size
    else:
        favor_pips = (entry_fill - current_price) / pip_size

    # TP1 partial harvest at tp1_pips of favor
    if management_mode in ("tp1_only", "tp1_be", "tp1_be_ratchet"):
        if favor_pips >= tp1_pips and trade.size != 0 and not getattr(trade, "_tp1_taken", False):
            try:
                # backtesting.py: trade.close(portion=fraction)
                trade.close(0.5)
                trade._tp1_taken = True
                actions["tp1_taken"] = favor_pips
            except Exception as e:
                actions["tp1_error"] = str(e)

    # BE move
    if management_mode in ("tp1_be", "tp1_be_ratchet"):
        if favor_pips >= be_trigger_pips:
            new_sl = entry_fill + be_offset_pips * pip_size if direction == "long" else entry_fill - be_offset_pips * pip_size
            try:
                # backtesting.py: trade.sl assignable
                if direction == "long" and (trade.sl is None or new_sl > trade.sl):
                    trade.sl = new_sl
                    actions["be_lifted"] = new_sl
                elif direction == "short" and (trade.sl is None or new_sl < trade.sl):
                    trade.sl = new_sl
                    actions["be_lifted"] = new_sl
            except Exception as e:
                actions["be_error"] = str(e)

    # Ratchet steps
    if management_mode == "tp1_be_ratchet":
        for trigger, offset in ratchet_steps:
            if favor_pips >= trigger:
                new_sl = entry_fill + offset * pip_size if direction == "long" else entry_fill - offset * pip_size
                try:
                    if direction == "long" and (trade.sl is None or new_sl > trade.sl):
                        trade.sl = new_sl
                        actions[f"ratchet_{trigger:g}"] = new_sl
                    elif direction == "short" and (trade.sl is None or new_sl < trade.sl):
                        trade.sl = new_sl
                        actions[f"ratchet_{trigger:g}"] = new_sl
                except Exception as e:
                    actions[f"ratchet_{trigger:g}_error"] = str(e)
    return actions
