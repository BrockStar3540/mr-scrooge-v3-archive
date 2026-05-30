# 3009. ML observer learns cluster serials, not regime labels

**Status:** Accepted
**Date:** 2026-05-18
**Version scope:** V3
**Author:** Brock (decisions) / Claude (write-up)

## Context

The ML observer was originally framed as "watch the regime classifier, learn which (regime × family × dir) cells are profitable." But once `MatrixRouter` collapsed regime classification into a parquet table of cluster serials (ADR 3008), regime labels became a derived view of cluster membership, not the underlying truth.

Training the observer on regime labels was teaching it a downstream summary instead of the upstream signal.

## Decision

Retrain ML observer to predict realized R conditional on **cluster serial** (the matrix's primary key), not regime label. Each cluster serial has stable membership; regime labels rotate as the regime classifier is retuned.

Cluster serials are version-pinned to the routing table parquet that produced them. Observer model is retrained whenever routing version bumps.

## Alternatives considered

- **Keep training on regime labels, add cluster serial as a feature** — rejected. Forces the model to re-derive cluster membership from the label, which is exactly the indirection we want to remove.
- **Train on the raw 14-bucket signature without clustering** — rejected. Loses the matrix's empirically-validated cluster boundaries, which are the unit of signal.

## Consequences

- Observer is now version-locked to the routing table.
- Cleaner experimental sweeps: when we change the bucket signature (ADR 3010), re-cluster, re-train observer in one cycle.
- Future signal-routing decisions reference cluster serial directly in logs.

## Cross-references

- Task #30
- Routing table parquet schema (cluster_serial column)
