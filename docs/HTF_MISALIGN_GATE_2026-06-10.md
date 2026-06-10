# Targeted HTF gate (the 7955 class) — 2026-06-10

## Trigger: trade 7955
USD_CAD short, align=0, entered 02:38:02 and lost. Diagnosis: counter-trend
(htf20 bias=long +0.0176, candidate short), cleared pip_eater on a knife-edge
cell (TF2-short align=0/RSI3 = net +1.30p, rsi14=49.77 right at the bucket
boundary -- one min later RSI4 read -4.39p and blocked). htf_trend_filter saw
the misalignment but is in OBSERVE. p_win 0.463. Size was fine (risk-capped $320).

## Why not blanket htf-HARD
htf_trend_filter has neutral_pct=0 (no deadband), so "hard" blocks ANY direction
that opposes the 20d daily bias. Modeled on 8yr corpus: that blocks **46.5% of
volume** -- and it's BLUNT: ~42-50% block rate on EVERY strategy (the 20d sign is
~independent of strategy), not a mean-reversion-specific cut. It would also clip
36% of alpha_extended_fade (the one +EV book).

## The targeted fix (modeled, then shipped)
Block only when htf-misaligned (H20 in d/e) AND align is low:
| rule | vol cut | EV removed | book lift |
|---|---|---|---|
| blanket | 46.5% | -2.20p | +0.382p |
| **align==0** (shipped) | 15.1% | **-2.96p** | +0.214p |
| align<=1 (broaden later) | 31.1% | -2.50p | +0.338p |

align==0 removes only the unambiguous worst (-2.96p) and **spares the fade book**:
alpha_extended_fade align>=2 misaligned = +0.32p (KEPT); only its align<=1
misaligned (-2.31p) is cut -- 12% blocked vs 36% under blanket.

## Shipped
`pip_eater_gate.py`: reuses the already-computed buckets + align_score; blocks when
`htf_misalign_block AND align_score < htf_misalign_floor AND H20 in {H20d,H20e}`.
Behind config `pip_eater.htf_misalign_block=true`, `htf_misalign_floor=1` (== align 0).
Placed upstream of the ADR/EV checks so the rejection reads clean ("counter-trend
no support"). Verified live: blocks USD_CAD short align=0/H20e (the 7955 class).
Broaden to align<=1 later by setting htf_misalign_floor=2. Models: htf_hard_model.py,
htf_targeted.py.
