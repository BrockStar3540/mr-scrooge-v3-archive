# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — V3_SCORER log-line parser.

The V3 scorer logs the FULL per-candidate breakdown to stdout/journald:

    [V3_SCORER] base=5 final=12 tier=REJECT fam=direct session=asia_london_open
        (floor=30 b=44 a=54 cap=16) pairs_raw=+7 capped=+7
        | hr=+10 age=+9 stp=-2 vol=-1 mom=-4 dc=+4 z=-7 bb=-2 e50=+0 e20=-3
          otr=+0 adr=+2 dur=+5 wal=+1 bdy=-4 bbs=+2 rsi=-5
          p_hr_norm=+8 p_age_norm=+5 n_z_norm=-6
        || px=93.399 ema20=93.445 ema50=93.592 box=0.646 age=5.2h

The V3 REST API exposes the bulk of the signal (features, classifications,
scorer.breakdown), but several fields live ONLY in this log line:
  - fam, session, floor, b, a, cap, pairs_raw, capped
  - All p_*/n_* pair-specific adjustments (variable per candidate)
  - px, ema20, ema50, box, age (at the exact scoring moment)

We parse defensively: the head is positional-ish, the factor block is
dict-style (key=value space-separated), and the p_/n_ adjustments are
arbitrary keys. Anything unrecognized is preserved in the `raw_extra` dict
so downstream training never silently loses a new feature.
"""

from __future__ import annotations

import re
from typing import Optional

# Matches:  [V3_SCORER] base=5 final=12 tier=REJECT fam=direct session=asia_london_open
#           (floor=30 b=44 a=54 cap=16) pairs_raw=+7 capped=+7 | <factors> || <ctx>
_MARKER = "[V3_SCORER]"

# Factor block keys — the 17 core scorer components.
_CORE_FACTORS = {
    "hr", "age", "stp", "vol", "mom", "dc", "z", "bb", "e50", "e20",
    "otr", "adr", "dur", "wal", "bdy", "bbs", "rsi",
}

_HEAD_RX = re.compile(
    r"base=(?P<base>-?\d+)\s+"
    r"final=(?P<final>-?\d+)\s+"
    r"tier=(?P<tier>\S+)\s+"
    r"fam=(?P<fam>\S+)\s+"
    r"session=(?P<session>\S+)\s+"
    r"\(floor=(?P<floor>-?\d+)\s+b=(?P<b>-?\d+)\s+a=(?P<a>-?\d+)\s+cap=(?P<cap>-?\d+)\)\s+"
    r"pairs_raw=(?P<pairs_raw>[+-]?\d+)\s+"
    r"capped=(?P<capped>[+-]?\d+)"
)

# key=value pairs anywhere in factor block (signed int)
_KV_INT_RX = re.compile(r"(?P<k>[A-Za-z_][A-Za-z0-9_]*)=(?P<v>[+-]?\d+)\b")
# key=value pairs for context (float, may end with unit letter we strip)
_KV_FLOAT_RX = re.compile(
    r"(?P<k>[A-Za-z_][A-Za-z0-9_]*)="
    r"(?P<v>[+-]?\d+(?:\.\d+)?)(?P<unit>[A-Za-z]*)"
)


def parse_v3_scorer_line(line: str) -> Optional[dict]:
    """
    Parse a single [V3_SCORER] log line. Returns a dict on success, or None
    if the marker is absent or the head is unparseable.

    Shape:
        {
            "base": int, "final": int, "tier": str, "fam": str, "session": str,
            "floor": int, "b": int, "a": int, "cap": int,
            "pairs_raw": int, "capped": int,
            "factors": {17 core factors ... },
            "pair_adjustments": {p_*: int, n_*: int, ...},  # variable
            "context": {"px": float, "ema20": float, "ema50": float,
                        "box": float, "age": float},   # "age" hours stripped of 'h'
            "raw_extra": {any unrecognized key}         # future-proof
        }
    """
    if _MARKER not in line:
        return None
    # Extract the payload after the marker
    _, _, body = line.partition(_MARKER)
    body = body.strip()
    m = _HEAD_RX.search(body)
    if not m:
        return None
    head = m.groupdict()

    # Split into sections using the '|' and '||' separators.
    # Structure: "<head> | <factors and pair-adj> || <context>"
    # The head match ends right before the first '|'.
    tail = body[m.end():].strip()
    factors_raw, _, context_raw = tail.partition("||")
    factors_raw = factors_raw.lstrip("|").strip()

    factors: dict = {}
    pair_adjustments: dict = {}
    raw_extra: dict = {}
    for km in _KV_INT_RX.finditer(factors_raw):
        k, v = km.group("k"), int(km.group("v"))
        if k in _CORE_FACTORS:
            factors[k] = v
        elif k.startswith("p_") or k.startswith("n_"):
            pair_adjustments[k] = v
        else:
            raw_extra[k] = v

    context: dict = {}
    for km in _KV_FLOAT_RX.finditer(context_raw):
        k = km.group("k")
        try:
            v = float(km.group("v"))
        except ValueError:
            continue
        context[k] = v

    return {
        "base": int(head["base"]),
        "final": int(head["final"]),
        "tier": head["tier"],
        "fam": head["fam"],
        "session": head["session"],
        "floor": int(head["floor"]),
        "b": int(head["b"]),
        "a": int(head["a"]),
        "cap": int(head["cap"]),
        "pairs_raw": int(head["pairs_raw"]),
        "capped": int(head["capped"]),
        "factors": factors,
        "pair_adjustments": pair_adjustments,
        "context": context,
        "raw_extra": raw_extra,
    }


__all__ = ["parse_v3_scorer_line"]
