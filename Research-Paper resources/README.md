# Research-Paper Resources — "LLMs as Penetration Testers"

This folder is the working paper trail for the assigned paper — **PentestGPT: Evaluating and
Harnessing Large Language Models for Automated Penetration Testing** (Deng et al., USENIX Security
2024, `papaers/usenixsecurity24-deng.pdf`) — and for the empirical study we are building around it
given the compute we actually have (a single lab GPU box: one ~30 GB VRAM card + one ~16 GB VRAM
card, open-weight models only, no GPT-4-class API budget).

It exists to answer one question before a single line of the paper is drafted: **given what we
have, what is the honest, defensible, and interesting thing we can actually claim?** The three
documents below answer that in order — scope, then options, then decision.

| Document | Purpose |
|---|---|
| [`01-SCOPE.md`](01-SCOPE.md) | What the paper is and is not about; research questions; hard constraints (compute, ethics, time); what "progress" means for a status update. |
| [`02-APPROACHES.md`](02-APPROACHES.md) | Every architectural and experimental approach we could take, each benchmarked against a real reference implementation, with pros/cons and feasibility on our hardware. |
| [`03-CONCLUSION.md`](03-CONCLUSION.md) | The recommended approach, the reasoning for rejecting the alternatives, the paper outline, the week-by-week roadmap, and known limitations to state up front. |
| [`04-MODEL-SPECIALIZATION.md`](04-MODEL-SPECIALIZATION.md) | A separate axis from the three documents above: not *system architecture* but *model-level* methods — prompting, constrained decoding, RAG, LoRA/QLoRA fine-tuning, DPO/RFT, RLHF/RLAIF, distillation, merging — rated for feasibility on our GPUs and mapped onto which observed failure mode each one actually fixes. |
| [`paper.tex`](paper.tex) | The draft paper itself — IEEE two-column conference format (`IEEEtran`), synthesizing all four documents above into Introduction/Terminology/Related Work/Scope/Approach/Testing/Limitations/Ethics/Conclusion. Fully written except the results table, which is intentionally left as a template pending real experiments. See the compile note at the top of the file — no LaTeX toolchain was detected on this machine, so use Overleaf (fastest) or install MiKTeX/TeX Live locally. |
| [`05-QA-PREP.md`](05-QA-PREP.md) | A plain-language Q&A rehearsal sheet for defending this project to a professor/committee — organized by theme (motivation, comparison to the base paper, method, limitations, ethics, "what if the results are boring") with a one-line cheat-sheet at the end. |

---

## 1. Why this isn't a from-scratch literature review

Two prior sessions of work already exist and this document set is built directly on top of them,
not written in the abstract:

1. **A reference corpus in `../data/`** — you (the user) copied in architecture write-ups and, in
   some cases, function-level codebase breakdowns of five prior "LLM does offensive security"
   systems. These are not papers — they are working implementations or documented re-implementations,
   which is more useful for a "how do I build mine" decision than the papers alone:

   | Reference (`../data/...`) | What it actually is | Why it matters here |
   |---|---|---|
   | `docs-pentestgpt/` (`architecture.md`, `codebase-understanding/UNDERSTANDING.md`) | A **modern re-implementation** of the PentestGPT USENIX'24 design: a two-role loop (Supervisor decides one task at a time, Executor performs it), backed by a SQLite `MemoryKernel` as sole canonical state, two pure "compiler" functions (`compile_plan`, `compile_execution`) that reject hallucinated tasks and un-grounded evidence claims, an append-only trace journal for crash recovery, and a read-only `audit.py` that independently re-verifies every claim against raw tool output. | This is the **evidence-grounding pattern** — the single most reusable idea for our paper, because it gives us a mechanical, model-agnostic way to answer "did the LLM actually prove what it claimed, or did it hallucinate it?" — which is exactly the failure mode we've already observed empirically (see §2 below). |
   | `docs-autopentestgpt/ARCHITECTURE.md` | A LangGraph `StateGraph` implementation: `planner → supervisor → (1 of 8 OWASP-Top-10-themed worker agents) → replanner → loop/end`, with per-agent RAG (Pinecone) over OWASP/PortSwigger/HackTricks docs, CVE/CPE lookup tools, persistent/reverse shell tools, and an explicit human-approval gate on command execution. | A **second architectural family** (planner/supervisor/specialist-workers instead of PentestGPT's flat two-role loop) — useful as the comparison point when we frame our own approach, and its documented failure modes (unbounded context growth in `past_steps`, no persistent memory across restarts, single-retry-then-crash orchestration) are exactly the kind of thing our own evaluation should check for. |
   | `docs - HackingBuddyGPT/` | Pointer to `hackingbuddy.ai` docs — a real, published system for **autonomous Linux privilege escalation** using an LLM in a shell loop. | Its authors (Happe, Kaplan, Cito) are the same team behind `papaers/s10664-025-10758-3.pdf` ("LLMs as Hackers: Autonomous Linux Privilege Escalation Attacks"), already in our papers folder — this is our **closest methodologically-comparable, already-published empirical study** (single-machine scope, measurable pass/fail per technique, works with small/local models), and is the best template for our own evaluation design. |
   | `README - Purple LLama.md` | Meta's Purple Llama / CyberSecEval project overview. | The **dual-use safety and evaluation-methodology angle** — CyberSecEval's benchmark design (quantifying an LLM's offensive capability and propensity to comply with attack requests) is directly relevant to how we justify and bound an "LLM does pentesting" evaluation responsibly. |
   | `docs-Langchain-custom-agent/`, `docs-autogen/`, `docs=trajan/` | General-purpose agent-framework reference material (a LangGraph.js HITL email-assistant demo, Microsoft AutoGen's architecture docs, and an unlabelled Trajan flow diagram). | Lower relevance to pentesting specifically, but the **human-in-the-loop interrupt/resume pattern** from the LangGraph HITL docs and AutoGen's general multi-agent orchestration patterns are cited in `02-APPROACHES.md` where relevant (e.g. if we ever want a supervised/HITL mode for safety). |

2. **Our own working infrastructure, already producing data** — this is not hypothetical tooling,
   it is running today in the parent directory:
   - `../CAI-modified/` — a fork of the CAI ("Cybersecurity AI") agentic framework, purpose-built for
     pentesting/CTF workflows, with its own benchmark suite (`benchmarks/cybermetric`,
     `cti_bench`, `seceval`, `cyberPII-bench`).
   - `../hexstrike-ai/` — an MCP server exposing ~127-150 real offensive-security CLI tools
     (`nmap`, `sqlmap`, `nuclei`, `ghidra`, `trivy`, `rustscan`, …) as callable tools.
   - `../MCPHost-modifed/` — `mark3labs/mcphost`, a second, independent MCP orchestrator used as a
     cross-check against CAI.
   - `../caldera/` — MITRE Caldera, for adversary-emulation-style scenario scaffolding if we need a
     controlled, repeatable "range" rather than a one-off VM.
   - `../findings/ornith-1.0-35b-Q4_K_M-latest_2026-09-07_2317.md` — **an actual completed
     experiment**: a 35B-parameter quantized model (via Ollama) driven through three different
     orchestrators (CAI, OpenClaude, mcphost) against the hexstrike-ai MCP server, with a documented,
     specific, reproducible failure taxonomy (tool-name-prefix corruption, fabricated tool names,
     schema-echoing instead of invocation, orchestrator-dependent connection reliability).

The approach documents below are written to convert item 2 (what we already have and have already
observed) into a paper, using item 1 (what others built and how) as the architectural and
methodological reference — not to propose reproducing any of them wholesale.

## 2. The one finding that drives every recommendation in this folder

From `../findings/ornith-1.0-35b-Q4_K_M-latest_2026-09-07_2317.md`: a 35B quantized model, even in
the cleanest-tested environment (mcphost, "clean, immediate" tool loading, no connection flakiness),
still corrupted the shared MCP tool-namespace prefix into at least 6 garbled variants
(`hexstrike__` → `hexstrips__`, `hexstripe_`, …) and fabricated tool names not present in the real
150-tool catalog — while a *different* orchestrator (CAI) against the *same* model and *same* tool
server instead echoed a tool's JSON schema as chat prose without ever invoking it, and a *third*
(OpenClaude) never established a working connection at all and fabricated an entirely fictitious
tool inventory when asked to self-report.

That is three qualitatively different failure modes for one model across three orchestrators against
one real MCP tool server — already collected, already reproducible, and not present (as a systematic,
orchestrator-controlled comparison) in any of the reference papers or reference codebases above. It
is the seed of the paper's actual contribution. See `01-SCOPE.md` for how this becomes a research
question and `03-CONCLUSION.md` for the recommended framing.

## 3. How to use this folder while writing

- Treat `01-SCOPE.md` as the contract: if an experiment or a paragraph doesn't serve one of the
  research questions listed there, it doesn't belong in the paper (or belongs in "future work").
- Treat `02-APPROACHES.md` as the decision log: when someone (an advisor, a reviewer, future-you)
  asks "why didn't you just reproduce PentestGPT/AutoPentest properly," the answer is in there, with
  the specific architectural reason and the specific resource constraint.
- Treat `03-CONCLUSION.md` as the standing plan: it names the recommended approach, the paper
  section outline that follows from it, and the roadmap to get from "three findings files" to a
  submittable draft.

Update all three as evidence changes — these are living documents for the duration of the project,
not a one-time planning exercise.
