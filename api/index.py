"""
Vercel serverless entrypoint.

Vercel's Python runtime auto-detects an ASGI application exported from
``api/index.py`` and serves it for every route. The application itself lives in
``main.py`` at the project root, so the root is added to ``sys.path`` before the
import to make the app's package layout (``api``, ``routers``, ``utils``,
``models``) resolvable no matter how the runtime sets the working directory.
"""

import sys
from pathlib import Path

_PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from main import app  # noqa: E402  (path setup must run first)

__all__ = ["app"]
