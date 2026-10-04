# RedBlue-MultiAgent

Phase-1 implementation of the multi-agent red/blue LangGraph architecture
designed in [`../Research-Paper resources/07-MULTI-AGENT-ARCHITECTURE.md`](../Research-Paper%20resources/07-MULTI-AGENT-ARCHITECTURE.md),
sourced per [`../Research-Paper resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md`](../Research-Paper%20resources/08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md),
diagrammed in [`../Research-Paper resources/09-multi-agent-stategraph.drawio`](../Research-Paper%20resources/09-multi-agent-stategraph.drawio).

## Why this looks the way it does (read before adding an MCP server)

Building this hit the same problem `Langchain/run_cloak_agent.sh` already
solved: an MCP server launched over stdio (`npx`) can orphan its
node/Chromium subtree if the parent process is killed, silently blocking the
next run. Given the deadline, the fix applied everywhere in this project is:

**Only one subprocess exists in this entire system — `cloakbrowser-mcp`,
shared by every browser-needing agent.** Every other capability (CVE lookup,
CVSS parsing, MITRE ATT&CK lookup) is a **plain in-process Python function**
wrapped as a LangChain `@tool` (see `tools/`) — no subprocess, no MCP server,
nothing to orphan, nothing that needs its own cleanup script. This was a
deliberate trade-off, not an oversight — see the "Plan C — Hybrid" section of
`08-MCP-TOOL-IMPLEMENTATION-OPTIONS.md`.

**Always launch this project via `run_agent.sh`, never `python main.py`
directly** — the wrapper guarantees the one subprocess it does own gets torn
down on exit/crash.

## Layout

```
RedBlue-MultiAgent/
  state.py           GraphState / Finding TypedDicts (shared across all nodes)
  llm.py             One shared llama.cpp ChatOpenAI client (IT-GPU, --jinja)
  reliability.py      Harmony-token sanitizer + malformed-call circuit breaker,
                       ported from Langchain/6_langchain_cloakbrowser_lama_cpp.py
  tools/
    cvss_tool.py       Deterministic CVSS vector parser (no LLM, no network)
    attack_kb_tool.py  Local offline MITRE ATT&CK lookup (../../mitre-attack-kb)
    nvd_tool.py        Direct NVD REST API call (no browser)
    rag_tool.py        BM25 search over ../../rag/ (6 KBs + 4 papers + project docs)
  agents/
    safety.py          Deterministic scope allow/deny check (no LLM)
    orchestrator.py     Router (LLM, structured output, no tools)
    recon.py            Browser + NVD tool agent (the only MCP-touching node)
    vuln_analysis.py    CVSS/ATT&CK tool agent (no browser)
    evaluator.py         Substring check + LLM judgment -> verified_findings
    common.py            Shared run/Finding-extraction helper
  graph.py            Wires the StateGraph (see the drawio diagram)
  main.py             REPL entry point
  run_agent.sh        ALWAYS use this to launch, not `python main.py`
  events.py           Live event bus for the web UI (see webui/ below)
  webui/
    server.py          FastAPI backend: owns the graph + browser session,
                        exposes POST /api/run and a streaming WS /ws
    static/             Plain HTML/CSS/vanilla-JS frontend, no build step
  run_webui.sh        ALWAYS use this to launch the web UI, not uvicorn directly
```

## Phase-1 scope (what's actually wired up)

Only **Safety -> Orchestrator -> {Recon, Vulnerability Analysis} ->
Evaluator -> back to Orchestrator -> END** is implemented and runnable. The
Orchestrator's routing schema already lists the full Phase-2/3 specialist
roster (Exploit/PoC Discovery, Attack Planning, Threat Intel Correlation,
Log/Alert Triage, Detection & Mitigation, Incident Response); picking one of
those currently routes to a `not_implemented` stub that ends the turn instead
of crashing. See `07-MULTI-AGENT-ARCHITECTURE.md` §11 for the phased build
order — add each remaining specialist by copying `vuln_analysis.py`'s shape
(system prompt + a short tool list + `run_tool_agent`), then wire one
`add_node` + one routing-map entry in `graph.py`.

## Prerequisites

- `llama-server` running on IT-GPU with `--jinja`, gpt-oss-20b, port 5500
  (same as `Langchain/6_langchain_cloakbrowser_lama_cpp.py` — see
  `../Research-Paper resources/06-GPT-OSS-LLAMACPP-TOOLCALLING-FINDINGS.md`
  for how that's launched).
- `../mitre-attack-kb/` present (already built — see its own README.md).
- Node.js 22.13+/24+ on PATH (for `npx cloakbrowser-mcp`).
- Python deps: `pip install -r requirements.txt` inside the `hexstrike` conda
  env (per the project's standing "use conda" preference).
- `../rag/rag_corpus.jsonl` present (already built — run `python ingest.py`
  inside `../rag/` if missing; see its own README.md).

## Run

**REPL (terminal):**
```bash
./run_agent.sh
```

**Web UI** — plain, single-page, no build step, shows every agent's live
"thinking" (routing reasons, tool calls, Evaluator verdicts) as it happens:
```bash
./run_webui.sh          # http://127.0.0.1:8000 (or ./run_webui.sh 8001 for a different port)
```
Single-run-at-a-time by design — same shared-browser-subprocess constraint
as the REPL. If the default port is already taken by something unrelated on
your machine, pass a different port as shown above rather than killing
whatever else owns it.

## Test results

See [`RESULTS.md`](RESULTS.md) for the Phase-1 benchmark numbers/tables
(tool-calling reliability, Evaluator evidence-grounding checks, and a
documented infra failure in the browser-based Recon path) — written for
direct use in the research paper.

Then type an objective at the `Objective:` prompt, e.g.:

```
Investigate CVE-2026-9862 and tell me if we should be worried.
```
