#!/bin/bash
# Deploy Mr. Scrooge V3 to EC2
# Run from local Mac: ./deploy/deploy.sh
set -euo pipefail

EC2="ubuntu@[REDACTED-IP]"
KEY="$HOME/.ssh/openclaw-key.pem"
REMOTE_DIR="/home/ubuntu/mr-scrooge-v3"
VENV="/home/ubuntu/mr_burns_env"

echo "=== Deploying Mr. Scrooge V3 to EC2 ==="

# 1. Push to GitHub
echo "→ Pushing to GitHub..."
git push origin main

# 2. Pull on EC2
echo "→ Pulling on EC2..."
ssh -i "$KEY" "$EC2" "cd $REMOTE_DIR && git pull origin main"

# 3. Install dependencies
echo "→ Installing dependencies..."
ssh -i "$KEY" "$EC2" "cd $REMOTE_DIR && $VENV/bin/pip install -e '.' --quiet"

# 4. Run tests
echo "→ Running tests..."
ssh -i "$KEY" "$EC2" "cd $REMOTE_DIR && $VENV/bin/python -m pytest tests/ -q"

# 5. Install systemd service (if not already)
echo "→ Installing systemd service..."
ssh -i "$KEY" "$EC2" "
    mkdir -p ~/.config/systemd/user
    cp $REMOTE_DIR/deploy/mr-scrooge-v3.service ~/.config/systemd/user/
    systemctl --user daemon-reload
    systemctl --user enable mr-scrooge-v3.service
"

# 6. Restart service
echo "→ Restarting service..."
ssh -i "$KEY" "$EC2" "systemctl --user restart mr-scrooge-v3.service"

# 7. Check status
echo "→ Checking status..."
sleep 3
ssh -i "$KEY" "$EC2" "systemctl --user status mr-scrooge-v3.service --no-pager | head -20"

echo "=== Deploy complete ==="
