"""End-to-end benchmark: full StateGraph (Safety -> Orchestrator -> {Recon,
Vulnerability Analysis} -> Evaluator -> ...) against real objectives, over the
one shared cloakbrowser-mcp session. Produces the numbers used in
RESULTS.md's "Full graph" table: per-trial latency, node visit count,
verified-finding count, and any circuit-breaker/sanitizer triggers (read off
stdout markers, printed by reliability.py / evaluator.py).

Run via run_bench.sh, not directly, so the browser subprocess is cleaned up
even if a trial hangs.
"""

import asyncio
import json
import time

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

from state import new_state
from graph import build_graph

SERVER_PARAMS = StdioServerParameters(command="npx", args=["-y", "cloakbrowser-mcp@latest"])
RECURSION_LIMIT = 30

# Bumped from n=3 to n=8 for statistical power (RESULTS.md §8a).
OBJECTIVES = [
    "Investigate CVE-2024-3400 and tell me if we should be worried.",
    "Investigate CVE-2026-9862 and tell me if we should be worried.",
    "Look up CVE-2021-44228 (Log4Shell) and assess its severity.",
    "Investigate CVE-2023-4863 (the WebP heap overflow) and tell me if we should be worried.",
    "Look up CVE-2020-1472 (Zerologon) and assess its severity.",
    "Investigate CVE-2017-5638 (the Apache Struts RCE) and tell me if we should be worried.",
    "Look up CVE-2019-0708 (BlueKeep) and assess its severity.",
    "Investigate CVE-2022-30190 (Follina) and tell me if we should be worried.",
]


async def run_trial(graph, objective, idx):
    """Runs the graph EXACTLY ONCE per trial (see RESULTS.md §8c for the bug
    this replaces: the original version called astream() for node-visit
    counting and then a SEPARATE ainvoke() for the final result, doubling
    both latency and LLM cost, and letting two independent, non-identical
    executions of the same objective supply different halves of one
    reported trial). `stream_mode=["updates", "values"]` gets both node names
    (from "updates" chunks) and the fully-reduced final state (the last
    "values" chunk) out of a single execution."""
    state = new_state(objective, mode="red")
    t0 = time.time()
    node_visits = []
    final = None
    try:
        async for mode, chunk in graph.astream(
            state, config={"recursion_limit": RECURSION_LIMIT}, stream_mode=["updates", "values"]
        ):
            if mode == "updates":
                node_visits.extend(chunk.keys())
            elif mode == "values":
                final = chunk  # each "values" chunk is the full state so far; the last one is authoritative

        dt = time.time() - t0
        return {
            "trial": idx,
            "objective": objective,
            "ok": True,
            "latency_s": round(dt, 2),
            "node_visits": node_visits,
            "n_node_visits": len(node_visits),
            "n_findings": len(final.get("findings", [])),
            "n_verified": len(final.get("verified_findings", [])),
            "halted": final.get("halted"),
            "verified_claims": [f["claim"][:200] for f in final.get("verified_findings", [])],
        }
    except Exception as e:
        dt = time.time() - t0
        return {"trial": idx, "objective": objective, "ok": False, "latency_s": round(dt, 2), "error": str(e)[:500]}


async def main():
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            browser_tools = await load_mcp_tools(session)
            print(f"Loaded {len(browser_tools)} browser tools from cloakbrowser-mcp.\n")

            graph = build_graph(browser_tools)
            results = []
            for i, obj in enumerate(OBJECTIVES, 1):
                print(f"=== Trial {i}: {obj} ===")
                r = await run_trial(graph, obj, i)
                print(json.dumps(r, indent=2))
                results.append(r)
                print()

            ok = sum(1 for r in results if r["ok"])
            lat = [r["latency_s"] for r in results if r["ok"]]
            n_verified = [r["n_verified"] for r in results if r["ok"]]
            print("=== SUMMARY ===")
            print(f"trials: {len(results)}, success: {ok}, success_rate: {ok/len(results)*100:.0f}%")
            if lat:
                print(f"avg_latency_s: {sum(lat)/len(lat):.2f}, min: {min(lat):.2f}, max: {max(lat):.2f}")
            if n_verified:
                print(f"avg_verified_findings_per_trial: {sum(n_verified)/len(n_verified):.2f}")

            with open("bench_full_graph_results.json", "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2)
            print("\nWrote bench_full_graph_results.json")


if __name__ == "__main__":
    asyncio.run(main())
