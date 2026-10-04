"""Live event bus for the RedBlue Investigate tab (app.py). Ported unchanged
from ../RedBlue-MultiAgent/events.py -- see that file's docstring for the full
rationale. Single-run-at-a-time by design, matching the shared-browser-
subprocess constraint (see browser_tools.py).
"""

import asyncio
import time

_queue: asyncio.Queue | None = None
_run_ready = asyncio.Event()


def start_run():
    global _queue
    _queue = asyncio.Queue()
    _run_ready.set()


async def wait_for_run():
    await _run_ready.wait()
    _run_ready.clear()


def emit(node: str, event: str, message: str, **data) -> dict:
    entry = {"node": node, "event": event, "message": message, "ts": time.time(), **data}
    if _queue is not None:
        try:
            _queue.put_nowait(entry)
        except Exception:
            pass
    return entry


async def subscribe():
    if _queue is None:
        return
    while True:
        entry = await _queue.get()
        yield entry
        if entry.get("event") in ("run_complete", "run_error"):
            return
