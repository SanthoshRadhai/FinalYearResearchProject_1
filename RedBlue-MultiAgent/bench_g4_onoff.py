"""Evaluator on/off comparison on a held-out CVE set (paper gaps G4 and M1).

For every (CVE, condition, repeat) it runs the full StateGraph once and
appends one JSON line to the output file, so a long run can be stopped and
resumed (finished keys are skipped). Conditions:
  on  -- the normal two-tier Evaluator
  off -- accept-all baseline: every finding is promoted to verified unchecked
  all -- Evaluator whose judgment sees every tool result of the run, not just the last one

Scoring is NOT done here; analyze_g4.py scores the saved text against NVD
ground truth. Run via run_agent.sh (it cleans up the browser subprocess):

    G4_REPEATS=3 G4_LIMIT=50 ./run_agent.sh bench_g4_onoff.py

Environment options: G4_CVES (default g4_cves.json), G4_SET (default eval),
G4_REPEATS (3), G4_CONDITIONS (on,off), G4_LIMIT (all), G4_OUT
(g4_onoff.jsonl), G4_TRIAL_TIMEOUT_S (600).
"""

import asyncio
import json
import os
import time
from pathlib import Path

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

import g4_common as g
from graph import build_graph
from langchain_core.messages import ToolMessage
from state import new_state

SERVER_PARAMS = StdioServerParameters(command="npx", args=["-y", "cloakbrowser-mcp@latest"])
RECURSION_LIMIT = 30

CVES_PATH = Path(os.getenv("G4_CVES", "g4_cves.json"))
SET = os.getenv("G4_SET", "eval")
REPEATS = int(os.getenv("G4_REPEATS", "3"))
CONDITIONS = os.getenv("G4_CONDITIONS", "on,off").split(",")
LIMIT = int(os.getenv("G4_LIMIT", "0")) or None
OUT = Path(os.getenv("G4_OUT", "g4_onoff.jsonl"))
TRIAL_TIMEOUT_S = int(os.getenv("G4_TRIAL_TIMEOUT_S", "600"))


def load_done():
    done = set()
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                done.add((r["cve"], r["condition"], r["repeat"]))
    return done


async def run_trial(graph, cve, condition, repeat):
    objective = g.OBJECTIVE_TEMPLATE.format(cve=cve)
    t0 = time.time()
    node_visits, final = [], None
    rec = {"cve": cve, "condition": condition, "repeat": repeat, "objective": objective}
    try:
        async def _go():
            nonlocal final
            async for mode, chunk in graph.astream(
                new_state(objective, mode="red"), config={"recursion_limit": RECURSION_LIMIT},
                stream_mode=["updates", "values"],
            ):
                if mode == "updates":
                    node_visits.extend(chunk.keys())
                elif mode == "values":
                    final = chunk
        await asyncio.wait_for(_go(), timeout=TRIAL_TIMEOUT_S)
        msgs = final.get("messages", [])
        rec.update({
            "ok": True, "latency_s": round(time.time() - t0, 2), "node_visits": node_visits,
            "halted": final.get("halted"),
            "findings": [{"source_agent": f["source_agent"], "claim": f["claim"], "confidence": f["confidence"],
                          "evidence_excerpt": f["evidence_excerpt"]} for f in final.get("findings", [])],
            "verified_claims": [f["claim"] for f in final.get("verified_findings", [])],
            "final_answer": str(msgs[-1].content) if msgs else "",
            "tool_results": [{"name": getattr(m, "name", ""), "content": str(m.content)[:3000]}
                            for m in msgs if isinstance(m, ToolMessage)],
        })
    except Exception as e:  # noqa: BLE001 - record and continue the long run
        rec.update({"ok": False, "latency_s": round(time.time() - t0, 2), "error": f"{type(e).__name__}: {e}"[:500]})
    return rec


async def main():
    doc = json.loads(CVES_PATH.read_text(encoding="utf-8"))
    cves = [c["cve_id"] for c in doc["cves"] if c.get("set") == SET]
    if LIMIT:
        cves = cves[:LIMIT]
    done = load_done()
    total = len(cves) * len(CONDITIONS) * REPEATS
    print(f"{len(cves)} CVEs x {CONDITIONS} x {REPEATS} repeats = {total} runs ({len(done)} already done)")

    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            graphs = {c: build_graph(tools, evaluator_mode=c) for c in CONDITIONS}
            n = 0
            for rep in range(1, REPEATS + 1):
                for cve in cves:
                    for cond in CONDITIONS:
                        n += 1
                        if (cve, cond, rep) in done:
                            continue
                        rec = await run_trial(graphs[cond], cve, cond, rep)
                        with OUT.open("a", encoding="utf-8") as f:
                            f.write(json.dumps(rec) + "\n")
                        state = "ok" if rec["ok"] else "ERR " + rec.get("error", "")[:60]
                        print(f"[{n}/{total}] {cve} {cond} rep{rep}: {state} {rec['latency_s']}s", flush=True)
    print(f"Done. Results in {OUT}")


if __name__ == "__main__":
    asyncio.run(main())
