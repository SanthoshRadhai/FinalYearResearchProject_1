"""Lazy singleton loader for the ONE shared cloakbrowser-mcp subprocess used by
the Recon agent. Ported pattern from ../RedBlue-MultiAgent/webui/server.py's
FastAPI `lifespan`, adapted for Gradio: Gradio has no equivalent startup/
shutdown hook wired into app.py by default, so instead of opening this at
import time (which would bind it to whatever throwaway event loop exists
before Gradio's own loop starts running -- the same problem checkpointer.py
solves for the sqlite connection), it opens lazily on first use, from inside
a request handler that is already running on Gradio's real event loop.

Only ever call get_browser_tools() -- never spawn a second cloakbrowser-mcp
subprocess. Run the app via run_app.sh, not `python app.py` directly, so the
subprocess is guaranteed torn down on exit (see that script's header).
"""

import asyncio
from contextlib import AsyncExitStack

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

SERVER_PARAMS = StdioServerParameters(command="npx", args=["-y", "cloakbrowser-mcp@latest"])

_tools: list | None = None
_lock = asyncio.Lock()

# Must be a MODULE-LEVEL reference, not a local variable inside
# get_browser_tools(). anyio's cancel scopes (which stdio_client uses
# internally) are tied to the exact asyncio Task that entered them; if
# nothing keeps `exit_stack` alive, Python's GC eventually finalizes the
# still-open async generator via a callback that runs in a DIFFERENT task
# than the one that opened it, which anyio rejects with "Attempted to exit
# cancel scope in a different task than it was entered in" -- exactly the
# crash this caused the first time Recon (or anything using the browser
# tools) ran. Keeping this reference alive for the app's whole lifetime, and
# never calling .aclose() on it, avoids that finalization entirely -- the
# subprocess is torn down by run_app.sh's cleanup trap on exit instead.
_exit_stack: AsyncExitStack | None = None


async def get_browser_tools() -> list:
    global _tools, _exit_stack
    async with _lock:
        if _tools is None:
            _exit_stack = AsyncExitStack()
            read, write = await _exit_stack.enter_async_context(stdio_client(SERVER_PARAMS))
            session = await _exit_stack.enter_async_context(ClientSession(read, write))
            await session.initialize()
            _tools = await load_mcp_tools(session)
            print(f"[browser_tools] loaded {len(_tools)} browser tools from cloakbrowser-mcp")
        return _tools
