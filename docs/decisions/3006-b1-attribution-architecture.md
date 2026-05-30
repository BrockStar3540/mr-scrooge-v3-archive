# 3006. B-1 attribution architecture — OrderAttributionWriter + lookup

**Status:** Accepted
**Date:** 2026-05-04
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

`strategy=unknown` was appearing in 30%+ of journal events after 2026-04-28's 48h losing streak diagnosis. Two root causes identified:
1. `AuditEvent` schema was missing a `strategy` field — strategy attribution was being inferred at journal-write time by scanning back through scoring logs.
2. The scan-lookup window was only the last 800 log lines (~60 seconds of activity), so any candidate scored more than ~60s before order fill lost its attribution.

Without attribution, broker-truth audits, ML observer training, and per-strategy WR breakdowns are all unreliable.

## Decision

Two-patch architecture:

**Patch A (commit 492a999):** Add `strategy` field directly to `AuditEvent`. Live-confirm via 1 net-new trade.

**Patch B.right (commit 73f1e41):** New `OrderAttributionWriter` writes a persistent `order_id → strategy / candidate / scoring payload` map at `data/order-attribution.jsonl`. Add `lookup_attribution(order_id)` helper. Wire ML observer + broker-truth audit to resolve attribution via `order_id` lookup, with `attribution_source` field tracking which path succeeded (`field_native` / `order_id_lookup` / `scan_log_fallback`).

## Alternatives considered

- **Patch A only (event field, no lookup map)** — rejected. Solves the live-going-forward case but leaves historical journal events still un-attributable.
- **Reduce scan-lookup window cost by indexing log lines** — rejected. The window cap was a symptom; structural fix is to stop relying on log-scan inference.
- **Force ML observer to skip un-attributed events** — rejected. Loses 30%+ of training signal.

## Consequences

- `attribution_source` field now in every journal event. `order_id_lookup` is the dominant path post-deploy.
- ML observer training set ~30% larger.
- Broker-truth audit can now cross-reference broker fills against live attribution end-to-end.

## Cross-references

- Vault: `wiki/projects/scrooge-v3-attribution-brokertruth-factors.md`
- Commits: `492a999` (Patch A), `73f1e41` (Patch B.right)
- Related: Patch C (2026-05-27) closed the scan-dashboard JSON-stripping side bug — see strategy promotion postmortem.
