#!/bin/bash
# Nightly catch-up (02:45Z cron): mirror both Scrooge repos EC2 -> Alien Drive.
# Heals any pushes made while the Mini was offline. EC2 is the truth.
for R in /home/ubuntu/mr-scrooge-v3 /home/ubuntu/mr-scrooge-v4; do
  cd "$R" || continue
  if git push alien --mirror 2>&1; then
    echo "$(date -u +%FT%TZ) $(basename $R) mirrored to alien OK"
  else
    echo "$(date -u +%FT%TZ) $(basename $R) ALIEN MIRROR FAILED (Mini offline?)"
  fi
done
