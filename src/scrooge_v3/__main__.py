"""Mr. Scrooge V3 — entry point.

Usage:
    python -m scrooge_v3                    # Run with defaults (dry-run)
    python -m scrooge_v3 --live             # Run live trading
    python -m scrooge_v3 --config path.json # Custom config path
    python -m scrooge_v3 --dry-run          # Explicit dry-run
"""

from __future__ import annotations

import argparse
import fcntl
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv


def setup_logging(log_dir: Path, level: str = "INFO") -> None:
    """Configure logging: stdout + rotating file handlers."""
    log_dir.mkdir(parents=True, exist_ok=True)

    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Root logger
    root = logging.getLogger()
    root.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Stdout handler
    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(fmt)
    stdout.setLevel(logging.INFO)
    root.addHandler(stdout)

    # Main log file (10MB, 5 backups)
    main_handler = RotatingFileHandler(
        log_dir / "scrooge_v3.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
    )
    main_handler.setFormatter(fmt)
    main_handler.setLevel(logging.DEBUG)
    root.addHandler(main_handler)

    # Decision log (separate file for trade decisions only)
    decision_logger = logging.getLogger("scrooge_v3.decisions")
    decision_handler = RotatingFileHandler(
        log_dir / "decisions.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
    )
    decision_handler.setFormatter(fmt)
    decision_logger.addHandler(decision_handler)
    decision_logger.propagate = False

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("werkzeug").setLevel(logging.WARNING)


def acquire_lock(lock_path: Path) -> int:
    """Enforce single-instance via file lock. Returns lock fd or exits."""
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(lock_path), os.O_CREAT | os.O_RDWR)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print(f"ERROR: Another instance is running (lock: {lock_path})", file=sys.stderr)
        sys.exit(1)
    os.write(fd, f"{os.getpid()}\n".encode())
    os.fsync(fd)
    return fd


def main() -> None:
    parser = argparse.ArgumentParser(description="Mr. Scrooge V3 Trading Platform")
    parser.add_argument("--config", type=str, default=None, help="Path to config JSON")
    parser.add_argument("--live", action="store_true", help="Enable live trading (default: dry-run)")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode (default)")
    parser.add_argument("--env", type=str, default=".env", help="Path to .env file")
    parser.add_argument("--log-dir", type=str, default="logs", help="Log directory")
    parser.add_argument("--log-level", type=str, default="INFO", help="Log level")
    parser.add_argument("--no-lock", action="store_true", help="Skip singleton lock (for testing)")
    parser.add_argument("--no-dashboard", action="store_true", help="Skip dashboard startup")
    args = parser.parse_args()

    # Load .env
    env_path = Path(args.env)
    if env_path.exists():
        load_dotenv(env_path)

    # Find project root
    project_root = Path(__file__).parent.parent.parent
    log_dir = project_root / args.log_dir

    # Setup logging
    setup_logging(log_dir, args.log_level)
    log = logging.getLogger("scrooge_v3")
    log.info("=" * 60)
    log.info("Mr. Scrooge V3 starting")
    log.info("=" * 60)

    # Singleton lock
    lock_fd = None
    if not args.no_lock:
        lock_path = log_dir / "scrooge_v3.lock"
        lock_fd = acquire_lock(lock_path)
        log.info("Process lock acquired: PID %d", os.getpid())

    # Load config
    from scrooge_v3.core.config import ConfigStore

    config_path = Path(args.config) if args.config else project_root / "config" / "default.json"
    config = ConfigStore(config_path)
    config.load()

    # Override dry_run from CLI
    if args.live:
        config.set("runtime.dry_run", False)
        log.warning("LIVE TRADING MODE — real orders will be placed")
    else:
        config.set("runtime.dry_run", True)
        log.info("Dry-run mode — no real orders")

    # Start dashboard in background thread
    if not args.no_dashboard and config.get("dashboard.enabled", True):
        import threading
        from scrooge_v3.dashboard import WidgetRegistry, run_dashboard
        from scrooge_v3.dashboard.widgets import (
            HealthWidget, SystemWidget, ScoringWidget, GateWidget, ExecutionWidget,
        )
        widget_reg = WidgetRegistry()
        widget_reg.register(HealthWidget())
        widget_reg.register(SystemWidget())
        widget_reg.register(ScoringWidget())
        widget_reg.register(GateWidget())
        widget_reg.register(ExecutionWidget())

        dash_thread = threading.Thread(
            target=run_dashboard,
            args=(widget_reg,),
            kwargs={"config": config.section("dashboard")},
            daemon=True,
            name="dashboard",
        )
        dash_thread.start()
        log.info("Dashboard started on port %d", config.get("dashboard.port", 8084))

    # Start replay recorder
    from scrooge_v3.core.events import EventBus
    from scrooge_v3.telemetry.replay import EventRecorder

    # Boot and run
    from scrooge_v3.core.runtime import Runtime

    runtime = Runtime(config)

    # Wire replay recorder to event bus
    if config.get("telemetry.replay_logs", True):
        from datetime import datetime, timezone
        session_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        replay_path = project_root / "data" / "replay" / f"session_{session_id}.jsonl"
        recorder = EventRecorder(runtime.event_bus, replay_path)
        recorder.start()
        log.info("Replay recorder started → %s", replay_path)

    try:
        runtime.run()
    except KeyboardInterrupt:
        log.info("Keyboard interrupt — shutting down")
        runtime.shutdown()
    finally:
        if lock_fd is not None:
            os.close(lock_fd)
        log.info("Mr. Scrooge V3 stopped")


if __name__ == "__main__":
    main()
