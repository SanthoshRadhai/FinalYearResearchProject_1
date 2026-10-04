"""Entry point: spawns the ONE shared cloakbrowser-mcp subprocess, builds the
Phase-1 graph, and runs an interactive REPL.

Run via run_agent.sh (not `python main.py` directly) so the cloakbrowser-mcp /
Chromium subtree is guaranteed torn down on exit — see run_agent.sh's header
comment for why that matters (same orphaned-process problem documented in
Langchain/run_cloak_agent.sh).
"""

import asyncio

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools

from state import new_state
from graph import build_graph

# Same server this project already validated in Langchain/6_langchain_cloakbrowser_lama_cpp.py.
SERVER_PARAMS = StdioServerParameters(
    command="npx",
    args=["-y", "cloakbrowser-mcp@latest"],
)

RECURSION_LIMIT = 30


def _print_verified_findings(state: dict):
    verified = state.get("verified_findings", [])
    if not verified:
        print("\n[no verified findings yet]\n")
        return
    print("\n=== Verified findings ===")
    for f in verified:
        print(f"- [{f['source_agent']}] {f['claim']}")
    print()


async def main():
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            browser_tools = await load_mcp_tools(session)
            print(f"Loaded {len(browser_tools)} tools from cloakbrowser-mcp.")

            graph = build_graph(browser_tools)
            print("Red/Blue multi-agent system ready. Type 'exit' or 'quit' to stop.\n")

            while True:
                objective = input("Objective: ").strip()
                if objective.lower() in ("exit", "quit"):
                    break
                if not objective:
                    continue

                state = new_state(objective, mode="red")
                try:
                    result = await graph.ainvoke(state, config={"recursion_limit": RECURSION_LIMIT})
                except Exception as e:
                    print(f"[error] graph run failed: {e}\n")
                    continue

                if result.get("halted"):
                    print(f"\n[halted] {result.get('halt_reason')}\n")
                    continue

                _print_verified_findings(result)


if __name__ == "__main__":
    asyncio.run(main())
