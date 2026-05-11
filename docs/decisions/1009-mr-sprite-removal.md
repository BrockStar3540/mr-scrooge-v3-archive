# 1009. Mr. Sprite crypto bot removal

**Status:** Reverted (bot existed and was removed)
**Date:** Existed pre-2026-03-06; removed entirely 2026-03-25
**Version scope:** V1 (parallel bot)
**Backfilled:** 2026-05-11

## Context

The Feb 2026 doctrine doc designed Mr. Sprite as a parallel crypto bot — same box theory ported to Kraken across 20 crypto pairs. Distinct from Mr. Scrooge (forex/OANDA, 24 pairs) but sharing strategy DNA.

Live operation surfaced crypto-specific issues:
- `zone_proximity_pct` had to widen from forex's 0.3% to 1.5% (ATOM at $1.942 with PDL at $1.929 = 0.67% gap failed forex default)
- `cl_ord_id` rejection on Kraken
- Position size overflow on low-priced coins (tight stops on $0.50 coins → 1,000-3,000 unit orders on a $785 account)
- Post-only orders never filling at zone entry (Kraken-specific)
- Kraken price precision rejection on slippage-buffered prices

By late March 2026, Mr. Sprite was removed entirely. Per memory: "Mr. Sprite: removed entirely (2026-03-25)."

## Decision

Retire Mr. Sprite. Reasons:
1. **Crypto-specific bugs burdened the codebase** without proportional return on the development effort.
2. **Strategy fidelity was harder** — crypto micro-structure differs from forex (different liquidity providers, different fee tiers, post-only/maker requirements).
3. **Focus** — managing two bots in two asset classes diluted attention from the forex bot's optimization.

## Alternatives considered

- **Keep but freeze (no new development)** — rejected. Even maintenance is non-zero cost; live trading bugs surface even without development.
- **Port forex fixes back to Sprite continuously** — rejected. Cost of maintaining two implementations was higher than the strategy expected value justified.
- **Spin Sprite out as its own repo** — never proposed; the strategy DNA was shared so split made it worse, not better.

## Consequences

**Enabled:**
- Forex bot (Scrooge) and execution-accounting innovations (Shark Audit Transfer, ADR-adjacent) were ported FROM Sprite to Scrooge before removal. The crypto bot's rigor improved the forex bot.
- Single-asset-class focus accelerated V2 / V3 development.

**Closed:**
- Crypto trading via the box-theory line. Future crypto work would be a fresh project.

**Lesson preserved:**
- **Cross-asset bots share strategy DNA but not parameter values.** Defaults that work in forex break in crypto. ADR 1009 is the cautionary tale for any future cross-asset port.

## Cross-references

- `[[scrooge-v1-exec-summary-feb-2026]]` §3.2 (Sprite status), §11.2 (Sprite bugs), §16.4 (universes)
- `[[scrooge-bug-catalog]]` B-016 through B-020 (Sprite-specific bugs)
- Memory: `# OpenClaw System Overview` § Mr. Sprite removed entirely (2026-03-25)
