"""Live event bus for the web UI (webui/server.py).

Deliberately NOT part of GraphState -- GraphState's `trace` field (see
state.py) is the durable, post-hoc record attached to the final result;
this module is the real-time push channel a WebSocket client consumes while
a run is still in progress. The two overlap in content but serve different
purposes: `trace` survives in the returned state for any caller (bench
scripts, `main.py`'s REPL, tests) without needing a live listener; this bus
exists only for the moment something is actually watching.

Single-run-at-a-time by design, matching the rest of this project's
single-shared-browser-subprocess constraint (see README.md) -- one process,
one asyncio.Queue, reset at the start of each run.
"""

import asyncio
import time

_queue: asyncio.Queue | None = None
_run_ready = asyncio.Event()


def start_run():
    """Call once at the start of a graph run -- (re)creates the queue so a
    new WebSocket subscriber only sees this run's events, not a stale one,
    and signals any waiter in wait_for_run() that a run has begun."""
    global _queue
    _queue = asyncio.Queue()
    _run_ready.set()


async def wait_for_run():
    """Blocks until start_run() is called, then clears the flag so the next
    call blocks again until the NEXT run starts. Used by the WebSocket
    handler to sit idle between runs instead of busy-looping subscribe()
    against a None queue."""
    await _run_ready.wait()
    _run_ready.clear()


def emit(node: str, event: str, message: str, **data) -> dict:
    """Build a trace entry, push it to the live queue if one exists (a run
    is in progress and something may be listening), and return the entry so
    callers can also append it to their own local trace list to include in
    the GraphState update they return."""
    entry = {"node": node, "event": event, "message": message, "ts": time.time(), **data}
    if _queue is not None:
        try:
            _queue.put_nowait(entry)
        except Exception:
            pass  # never let a full/broken queue break the actual agent run
    return entry


async def subscribe():
    """Async generator yielding events as they're emitted. Ends when a
    {"event": "run_complete"} or {"event": "run_error"} entry is seen."""
    if _queue is None:
        return
    while True:
        entry = await _queue.get()
        yield entry
        if entry.get("event") in ("run_complete", "run_error"):
            return
