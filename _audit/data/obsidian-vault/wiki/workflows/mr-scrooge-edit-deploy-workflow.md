# Mr. Scrooge Edit and Deploy Workflow

type: method
status: active
tags: [scrooge, trading, workflow, deployment, safety]

trust:
  score: 95
  confidence: high
  evidence:
    - source: established workflow, used in production 2026-04-07/09
      type: reproducible

## Summary
Step-by-step procedure for editing Mr. Scrooge bot code, deploying changes, and syncing backups. This is the #1 safety document — follow it exactly. Skipping steps has caused production incidents.

## Prerequisites
- SSH access to EC2: `ssh -i ~/.ssh/openclaw-key.pem ubuntu@[REDACTED-IP]`
- Bot workspace: `~/.openclaw/workspace/agents/mr-scrooge/` (V1) or `mr-scrooge-v2/` (V2)

## Procedure

### Step 0: Read the Pre-Change Checklist
Before editing anything, read the relevant pre-change checklist for the bot you're modifying:
- V1: [[Mr. Scrooge V1 Pre-Edit Briefing]]
- V2: [[Mr. Scrooge V2 Pre-Change Checklist]]

### Step 1: Edit on EC2
SSH to EC2 and edit the file directly. The live bot runs from EC2 — this is where changes must originate.

```bash
ssh -i ~/.ssh/openclaw-key.pem ubuntu@[REDACTED-IP]
cd ~/.openclaw/workspace/agents/mr-scrooge/   # or mr-scrooge-v2/
nano main.py   # or vim, or use sed -i for targeted fixes
```

### Step 2: Restart the Service
```bash
# V1
systemctl --user restart mr-scrooge.service

# V2
systemctl --user restart mr-scrooge-v2.service

# If you edited the harvester:
systemctl --user restart mr-scrooge-harvester.service      # V1
systemctl --user restart mr-scrooge-v2-harvester.service   # V2

# If you edited the dashboard:
systemctl --user restart mr-scrooge-dashboard.service      # Affects BOTH V1 and V2
```

### Step 2.5: Clear Pycache
Remove stale bytecode before restarting to avoid loading cached versions of changed modules:
```bash
find . -name '*.pyc' -delete && find . -name '__pycache__' -type d -exec rm -rf {} +
```

### Step 3: Check Logs (DO NOT SKIP)
Wait 10 seconds, then verify the bot started cleanly:
```bash
# V1
tail -20 ~/.openclaw/workspace/agents/mr-scrooge/logs/mrscrooge.log

# V2
tail -20 ~/.openclaw/workspace/agents/mr-scrooge-v2/logs/mrscroogev2.log

# Check for errors
grep -i 'error\|traceback\|exception' ~/.openclaw/workspace/agents/mr-scrooge/logs/mrscrooge.log | tail -5
```

Look for: "Cycle XX:XX" lines appearing at 5-min intervals, correct instrument count, no tracebacks.

### Step 4: Commit and Push to GitHub
V1 and V2 have separate .git repos and separate GitHub remotes.

**V1:**
```bash
cd ~/.openclaw/workspace/agents/mr-scrooge/
git add <changed_files>
git commit -m "description of change"
git push origin main

**Important:** V1 and V2 have separate isolated git repos:
- V1: `.git` inside `~/.openclaw/workspace/agents/mr-scrooge/` (GitHub: `BrockStar3540/mr-scrooge`)
- V2: `.git` inside `~/.openclaw/workspace/agents/mr-scrooge-v2/` (GitHub: `BrockStar3540/mr-scrooge-v2`)
The workspace root (`~/.openclaw/workspace/`) is NOT a git repo. Never run git commands from there.
```

**V2:**
```bash
cd ~/.openclaw/workspace/agents/mr-scrooge-v2/
git add <changed_files>
git commit -m "description of change"
git push origin main
```

### Step 5: Push to Alien Device
Both bots have alien remotes configured:
```bash
# V1
cd ~/.openclaw/workspace/agents/mr-scrooge/
git push alien main

# V2
cd ~/.openclaw/workspace/agents/mr-scrooge-v2/
git push alien main
```

This pushes via Tailscale SSH to the Mac Mini's Alien Device backup. The remote is configured with `receive.denyCurrentBranch=updateInstead` so the working tree auto-updates.

### Step 6: Update Notes
If the change was significant (new feature, bug fix, defect):
- Update `project_future_experiments.md` in Claude memory if defects changed
- Update `MEMORY.md` if architecture or config changed
- Update [[Mr. Scrooge Known Defects]] if a defect was fixed or found
- Update vault docs if scoring, architecture, or defects changed. See [[Mr. Scrooge Changelog Process]].

## NEVER DO
- **Never edit on Mac then copy to EC2** — EC2 is the source of truth
- **Never use nohup to start bots** — systemd owns the processes; nohup creates duplicate instances
- **Never skip the log check** — a silent crash means no trades and no alerts
- **Never amend a commit after a pre-commit hook failure** — amend modifies the previous commit; create a new one
- **Never restart the dashboard without knowing it serves BOTH V1 and V2**
- **Never edit Alien Device files directly** — they get overwritten by `git push alien main`

## If Something Goes Wrong
1. Check service status: `systemctl --user status mr-scrooge.service`
2. Check logs for traceback: `grep -i traceback .../mrscrooge.log | tail -5`
3. If the bot crashed on restart, the native OANDA SL/TP protects open positions
4. Roll back: `git revert HEAD && systemctl --user restart mr-scrooge.service`
5. See [[Mr. Scrooge Debugging Workflow]] for detailed troubleshooting

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V1 Pre-Edit Briefing]]
- [[Mr. Scrooge V2 Pre-Change Checklist]]
- [[Mr. Scrooge Changelog Process]]
- [[Mr. Scrooge Debugging Workflow]]
- [[Mr. Scrooge Known Defects]]
