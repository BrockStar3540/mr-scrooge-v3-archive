"""Extract three expansion-target CSVs from live seed-telemetry.jsonl.

Brock 2026-05-18: live block telemetry is the search-target generator for
offline expansion. Each BLOCKED candidate identifies a real-world
(regime, pair, session, family, direction) tuple the routing surface
should cover. Three offline queues consume this:

  live_gap_expansion_targets.csv     no cell anywhere -- mine a new one
  boundary_thin_targets.csv          cell exists but shave_rule misses by <10%
  session_sibling_targets.csv        cell exists but for the wrong session

Each row carries enough context to drive a targeted expansion run without
re-scanning the corpus from scratch.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import pandas as pd

# match `<feat> <op> <val> (got <observed>)` from EntryFilterGate's
# `shave_rule_violated: ...` reason format
SHAVE_VIOLATION_RE = re.compile(
    r"^shave_rule_violated:\s*(?P<feat>[\w_]+)\s*(?P<op>==|!=|<=|>=|<|>)\s*(?P<thr>[\w\.\-]+)\s*\(got\s*(?P<got>[^)]+)\)\s*$"
)


def parse_violation(reason: str) -> dict | None:
    """Parse a shave_rule_violated reason into structured fields."""
    if not reason or not reason.startswith("shave_rule_violated"):
        return None
    m = SHAVE_VIOLATION_RE.match(reason)
    if not m:
        return None
    feat = m.group("feat")
    op = m.group("op")
    thr_str = m.group("thr").strip()
    got_str = m.group("got").strip()
    out = {"feat": feat, "op": op, "thr_str": thr_str, "got_str": got_str}
    # If threshold and observed are numeric, compute proximity %.
    try:
        thr = float(thr_str)
        got = float(got_str)
        denom = max(abs(thr), 1e-9)
        out["thr"] = thr
        out["got"] = got
        out["delta"] = got - thr
        out["delta_pct_of_thr"] = abs(got - thr) / denom
    except ValueError:
        out["thr"] = None
        out["got"] = None
        out["delta"] = None
        out["delta_pct_of_thr"] = None
    return out


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def pair_live_shadow(rows: list[dict]) -> list[tuple[dict, dict | None]]:
    """Pair (live, shadow) rows by (symbol, ts) bucket of ~1s.

    The two gates evaluate the same candidate within milliseconds; matching
    on ts-truncated-to-second + symbol + direction + candidate_strategy
    catches the pair cleanly.
    """
    # Index shadow rows
    shadow_idx: dict[tuple, dict] = {}
    for r in rows:
        if r.get("gate") == "entry_filter_shadow":
            key = (
                r.get("symbol"),
                r.get("ts", "")[:19],  # second precision
                r.get("direction"),
                r.get("candidate_strategy"),
            )
            shadow_idx[key] = r

    paired = []
    for r in rows:
        if r.get("gate") != "entry_filter":
            continue
        key = (
            r.get("symbol"),
            r.get("ts", "")[:19],
            r.get("direction"),
            r.get("candidate_strategy"),
        )
        paired.append((r, shadow_idx.get(key)))
    return paired


def build_targets(
    paired: list[tuple[dict, dict | None]],
    boundary_thin_pct: float = 0.10,
) -> dict[str, pd.DataFrame]:
    no_match: list[dict] = []
    boundary_thin: list[dict] = []
    session_sibling: list[dict] = []

    for live, shadow in paired:
        reason = live.get("block_reason") or ""
        base = {
            "ts": live.get("ts"),
            "symbol": live.get("symbol"),
            "regime53": live.get("regime53"),
            "session_bucket": live.get("session_bucket"),
            "direction": live.get("direction"),
            "candidate_family": live.get("candidate_strategy"),
            "live_block_reason": reason,
        }

        # Case 1: no cell at all for this tuple
        if reason.startswith("no_routing_match"):
            no_match.append({**base, "shadow_reason": (shadow or {}).get("block_reason")})
            continue

        # If shadow row is missing we can't classify further; skip
        if not shadow:
            continue

        sreason = shadow.get("block_reason") or ""
        srule = shadow.get("shave_rule")
        scell = shadow.get("cell_label")
        sfactors = shadow.get("factors") or {}

        # Case 2: shave_rule_violated -- classify by which clause failed
        v = parse_violation(sreason)
        if v:
            row = {
                **base,
                "shadow_reason": sreason,
                "shadow_cell": scell,
                "shadow_cell_strategy": shadow.get("cell_strategy"),
                "shadow_cell_family": shadow.get("cell_family"),
                "shadow_shave_rule": srule,
                "shadow_factors": json.dumps(sfactors),
                "violated_feature": v["feat"],
                "violated_op": v["op"],
                "violated_threshold": v.get("thr"),
                "violated_observed": v.get("got"),
                "delta_pct_of_thr": v.get("delta_pct_of_thr"),
            }
            # session clause is a string equality -- always goes to session-sibling queue
            if v["feat"] == "session_bucket":
                session_sibling.append({
                    **row,
                    "cell_session": v.get("thr_str"),
                    "candidate_session": v.get("got_str"),
                })
            else:
                # boundary thin if numeric and proximity <= threshold pct
                pct = v.get("delta_pct_of_thr")
                if pct is not None and pct <= boundary_thin_pct:
                    boundary_thin.append(row)
                # else: distant miss, not actionable as boundary thin

    df_no_match = pd.DataFrame(no_match).drop_duplicates(
        subset=["regime53", "symbol", "session_bucket", "direction", "candidate_family"],
        keep="last",
    ) if no_match else pd.DataFrame()
    df_boundary = pd.DataFrame(boundary_thin).drop_duplicates(
        subset=["regime53", "symbol", "session_bucket", "direction",
                "candidate_family", "shadow_shave_rule"],
        keep="last",
    ) if boundary_thin else pd.DataFrame()
    df_session = pd.DataFrame(session_sibling).drop_duplicates(
        subset=["regime53", "symbol", "direction", "candidate_family",
                "shadow_shave_rule", "candidate_session"],
        keep="last",
    ) if session_sibling else pd.DataFrame()
    return {
        "live_gap_expansion_targets": df_no_match,
        "boundary_thin_targets": df_boundary,
        "session_sibling_targets": df_session,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--boundary-thin-pct", type=float, default=0.10)
    args = p.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    print(f"Loading {args.ledger} ...")
    rows = load_jsonl(Path(args.ledger))
    print(f"  rows: {len(rows):,}")
    print(f"  live  : {sum(1 for r in rows if r.get('gate') == 'entry_filter')}")
    print(f"  shadow: {sum(1 for r in rows if r.get('gate') == 'entry_filter_shadow')}")

    paired = pair_live_shadow(rows)
    print(f"  paired live+shadow: {len(paired):,}")

    targets = build_targets(paired, boundary_thin_pct=args.boundary_thin_pct)
    for name, df in targets.items():
        path = out / f"{name}.csv"
        df.to_csv(path, index=False)
        print(f"  {name:40s} {len(df):>5d} rows -> {path}")


if __name__ == "__main__":
    main()
