---
type: workflow
status: active
tags: [scrooge, trading, workflow, documentation]
trust:
  score: 90
  confidence: high
  reason: Formalized from existing practice across V1 and V2 development
---

## Summary

Documentation process for Mr. Scrooge V1 and V2 changes. Defines where each type of change gets documented, who is responsible, and the separation of concerns between EC2 NOTES.md (session log), Obsidian vault (structured knowledge), and git commits (code history).

## Documentation Matrix

| What Changed | Where to Document | Who |
|---|---|---|
| Code change (any .py) | EC2 bot NOTES.md (append dated section) | Whoever made the change |
| Bug found or fixed | Vault `mr-scrooge-known-defects.md` | Whoever found/fixed it |
| Scoring calibration | Vault scoring system doc (update points + evidence table) | Requires OANDA data audit |
| Config change | EC2 bot NOTES.md + vault bot doc if significant | Whoever changed it |
| New feature or system | Vault `wiki/systems/` (new file per schema rules) | Whoever built it |
| Incident or failure | Vault `postmortems/` (per schema template) | Whoever investigated |
| Architecture change | Vault `mr-scrooge-architecture.md` | Whoever made the change |

## The Three Layers

### EC2 NOTES.md --- Session Log

- **Purpose:** Append-only timeline of what happened and when
- **Format:** Dated sections with brief descriptions of changes made
- **Location:** Root of each bot directory on EC2
- **Rule:** Append only. Never edit or reorganize previous entries.

### Obsidian Vault --- Structured Knowledge

- **Purpose:** Current truth about how the system works
- **Format:** Per-topic files following vault schema (frontmatter, summary, sections, takeaways, related)
- **Location:** Vault wiki/systems/, wiki/workflows/, postmortems/
- **Rule:** Update to reflect current state. This is not a changelog --- it describes what IS, not what WAS.

### Git Commits --- Code History

- **Purpose:** Atomic record of code changes with descriptive messages
- **Format:** Standard git commits with meaningful messages
- **Location:** GitHub repos (BrockStar3540/mr-scrooge, BrockStar3540/mr-scrooge-v2)
- **Rule:** Each commit should be a logical unit. Do not bundle unrelated changes.

## Rules

1. **Never duplicate the same information across all three layers.** Each has its role. NOTES.md says "what happened today." Vault says "how things work now." Git says "what code changed."

2. **Scoring changes require OANDA data.** The scoring system doc must include an evidence table with trade counts and P/L figures. Do not update scoring point values based on theory alone.

3. **New vault files follow the schema.** Every file needs frontmatter (type, status, tags, trust), Summary, content sections, Key Takeaways (3-5 bullets), and Related (2+ wikilinks).

4. **NOTES.md is append-only.** Previous entries are historical record. Fix errors by adding a correction entry, not by editing the past.

5. **Push to GitHub after every session with code changes.** Also sync to Alien Device. The flow is always EC2 -> GitHub -> Alien Device.

## Key Takeaways

- Three documentation layers serve distinct purposes: session log (NOTES.md), structured knowledge (vault), and code history (git)
- Never duplicate information across layers --- each answers a different question (what happened, how it works, what code changed)
- Scoring documentation requires OANDA trade data evidence, not theoretical reasoning
- NOTES.md is append-only; vault docs reflect current state; git commits are atomic code units
- Always push to GitHub and sync Alien Device after code changes

## Related

- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
