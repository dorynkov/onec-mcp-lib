"""@tool_safe decorator — catch exceptions and return JSON error payload."""

from __future__ import annotations

import json
import logging
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., str])


def tool_safe(name: str) -> Callable[[F], F]:
    """Return JSON error payload instead of raising to MCP client."""

    def decorator(fn: F) -> F:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                logger.exception("tool %s failed", name)
                return json.dumps(
                    {"ok": False, "tool": name, "error": str(exc)},
                    ensure_ascii=False,
                    indent=2,
                )

        return wrapper  # type: ignore[return-value]

    return decorator
