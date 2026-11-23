"""Central logging configuration — configurable level, stderr + optional file."""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

_CONFIGURED = False


def setup_logging(
    *,
    name: str = "1c-mcp",
    level_env: str = "ONEC_LOG_LEVEL",
    default_level: str = "INFO",
    log_file_env: str = "ONEC_LOG_FILE",
) -> None:
    """Configure root logging once (stderr + optional file from env).

    Args:
        name: Service name for log prefix (e.g. "1c-bsl-mcp").
        level_env: Env var name for log level.
        default_level: Fallback log level.
        log_file_env: Env var name for optional log file path.
    """
    global _CONFIGURED
    if _CONFIGURED:
        return

    level_name = os.environ.get(level_env, default_level).upper()
    level = getattr(logging, level_name, logging.INFO)

    formatter = logging.Formatter(
        f"%(asctime)s [{name}] %(levelname)s %(name)s: %(message)s"
    )

    handlers: list[logging.Handler] = []
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    handlers.append(stderr_handler)

    log_file = os.environ.get(log_file_env, "").strip()
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)

    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(level)
    for handler in handlers:
        root.addHandler(handler)

    _CONFIGURED = True
