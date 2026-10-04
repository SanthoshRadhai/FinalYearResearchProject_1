"""Phase-1 web UI backend. Owns the one shared cloakbrowser-mcp session and
the compiled graph for the lifetime of the process (same lifecycle as
main.py's REPL), and exposes:

    POST /api/run   {"objective": "..."}   -> starts a run (409 if one is
                                              already in progress -- see
                                              README.md's single-run
                                              constraint, same reason
                                              main.py only ever runs one
                                              turn at a time: there is only
                                              one shared browser subprocess)
    WS   /ws                                -> streams every events.py
                                              entry live, then a final
                                              consolidated payload when the
                                              run ends; loops to wait for
                                              the next run afterwards.
    GET  /                                  -> the static frontend (index.html)

Run via ../run_webui.sh, never directly -- same cloakbrowser-mcp cleanup
requirement as run_agent.sh.
"""
import asyncio
import sys
import time
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Make the parent (RedBlue-MultiAgent/) importable -- server.py lives one
# level down in webui/, but state.py/graph.py/events.py/etc. all assume
# they're imported with RedBlue-MultiAgent/ as the working root, exactly as
# main.py already does when launched via run_agent.sh from that directory.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

import events
from state import new_state
from graph import build_graph

SERVER_PARAMS = StdioServerParameters(command="npx", args=["-y", "cloakbrowser-mcp@latest"])
RECURSION_LIMIT = 30

app_state = {
    "graph": None,
    "busy": False,
    "last_result": None,
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            browser_tools = await load_mcp_tools(session)
            print(f"[webui] loaded {len(browser_tools)} browser tools")
            app_state["graph"] = build_graph(browser_tools)
            print("[webui] graph built, ready")
            yield
    print("[webui] shutting down")


app = FastAPI(lifespan=lifespan)


class RunRequest(BaseModel):
    objective: str


@app.post("/api/run")
async def run_objective(req: RunRequest):
    if app_state["busy"]:
        return JSONResponse(status_code=409, content={"error": "A run is already in progress."})
    if not req.objective.strip():
        return JSONResponse(status_code=400, content={"error": "Objective must not be empty."})

    app_state["busy"] = True
    events.start_run()

    async def _run():
        t0 = time.time()
        try:
            state = new_state(req.objective, mode="red")
            result = await app_state["graph"].ainvoke(state, config={"recursion_limit": RECURSION_LIMIT})
            app_state["last_result"] = {
                "ok": True,
                "objective": req.objective,
                "latency_s": round(time.time() - t0, 2),
                "halted": result.get("halted"),
                "halt_reason": result.get("halt_reason"),
                "verified_findings": [
                    {"source_agent": f["source_agent"], "claim": f["claim"]}
                    for f in result.get("verified_findings", [])
                ],
                "rejected_findings": [
                    {"source_agent": f["source_agent"], "claim": f["claim"]}
                    for f in result.get("findings", []) if f["confidence"] == "rejected"
                ],
                "answer": result["messages"][-1].content if result.get("messages") else "",
            }
            events.emit("graph", "run_complete", "run finished")
        except Exception as e:
            app_state["last_result"] = {"ok": False, "objective": req.objective, "error": str(e)}
            events.emit("graph", "run_error", str(e))
        finally:
            app_state["busy"] = False

    asyncio.create_task(_run())
    return {"status": "started"}


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await events.wait_for_run()
            async for entry in events.subscribe():
                await websocket.send_json(entry)
            await websocket.send_json({"type": "final", **(app_state["last_result"] or {})})
    except WebSocketDisconnect:
        pass


STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")
