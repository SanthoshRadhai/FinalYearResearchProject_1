"""LangGraph checkpoint storage -- one sqlite file, one shared connection for
the whole app's lifetime.

Must be AsyncSqliteSaver (not the sync SqliteSaver) because app.py drives the
graph with `graph.astream(...)`/`graph.aget_state(...)` for token streaming;
the sync saver raises NotImplementedError as soon as an async method is
called on it. The connection is created lazily, inside a coroutine that runs
on Gradio's own event loop (see app.py's `get_graph()`), because aiosqlite
binds a connection to the event loop that opened it -- opening it eagerly at
import time under a throwaway `asyncio.run()` loop would break as soon as
Gradio's real (different) event loop tried to use it.
"""

from pathlib import Path

import aiosqlite
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

DB_PATH = Path(__file__).resolve().parent / "chat_sessions.db"


async def get_checkpointer() -> AsyncSqliteSaver:
    conn = await aiosqlite.connect(str(DB_PATH))
    await conn.execute("PRAGMA journal_mode=WAL")
    saver = AsyncSqliteSaver(conn)
    await saver.setup()
    return saver
