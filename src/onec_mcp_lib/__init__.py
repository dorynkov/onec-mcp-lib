from __future__ import annotations

import importlib.metadata
import os

from .tool_errors import tool_safe
from .logging_setup import setup_logging

__all__ = [
    "tool_safe",
    "setup_logging",
    "build_diagnostics",
    "get_package_version",
]


def get_package_version(package: str) -> str:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "unknown"


def build_diagnostics(
    *,
    package: str,
    service_name: str,
    config: dict,
    checks: dict[str, bool] | None = None,
    stats: dict | None = None,
) -> dict:
    """Build a standard diagnostics payload (matches zvec pattern)."""
    payload: dict = {
        "ok": True,
        "service": service_name,
        "version": get_package_version(package),
        "transport": os.environ.get(f"ONEC_{service_name.upper().replace('-', '_')}_TRANSPORT", "stdio"),
        "log_level": os.environ.get("ONEC_LOG_LEVEL", "INFO"),
        "config": config,
    }
    if checks is not None:
        payload["checks"] = checks
        payload["all_ok"] = all(checks.values())
    if stats is not None:
        payload["stats"] = stats
    return payload
