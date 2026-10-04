# Conclusion & Roadmap

## 1. Recommended approach

Combine **A2** (systematic reliability/failure-taxonomy study across models × orchestrators, on our
already-working CAI/mcphost/hexstrike-ai stack) as the empirical backbone with **A6** (a minimal
evidence-grounding wrapper, ported down from the reference PentestGPT re-implementation's
`compile_execution`) as the paper's methodological contribution. A5 (cheap benchmark control
variable), A7 (HITL discussion-section analysis), and A8 (ATT&CK-technique vocabulary for progression
scoring) are folded in as supporting evidence, not separate workstreams. A1 (faithful reproduction),
A3 (specialist-worker architecture), and A4 (narrow privesc replication) are explicitly not the
paper's core, for the reasons already logged in `02-APPROACHES.md`.

In one sentence: **we are not asking "can a small LLM be PentestGPT" — we are asking "how does a
small LLM actually fail when forced into PentestGPT's job, and does PentestGPT's own
evidence-grounding trick help," and we already have the infrastructure and the first data point to
answer both.**

## 2. Paper outline (maps directly onto the research questions in `01-SCOPE.md`)

1. **Introduction** — motivate with PentestGPT as SOTA; state explicitly that all prior evaluation of
   this architecture assumes GPT-4-class reasoning; state the gap (nothing evaluates what happens
   when the same architectural bet is placed on the 7B–35B open-weight tier most practitioners can
   actually afford to self-host); state the three contributions (a controlled model×orchestrator
   reliability study; a reproducible failure taxonomy; a lightweight evidence-grounding mitigation
   with a measured effect size).
2. **Related work** — `usenixsecurity24-deng.pdf` (PentestGPT, the architecture we're stress-testing
   at smaller scale); `s10664-025-10758-3.pdf` (Happe et al., closest methodologically — single-scope,
   statistically-powered pass/fail study — cite for evaluation-design rigor); `s10207-024-00835-x.pdf`
   (Hilario et al., "the good, the bad, the ugly" — cite for the risk/limitations framing); the
   `s11227-026-08439-z.pdf` Autosecagent paper (RAG/recursive-memory angle — cite as a mitigation
   direction we did *not* pursue, for contrast with our lighter-weight evidence-grounding approach);
   Purple Llama / CyberSecEval (cite for the responsible-evaluation framing, `data/README - Purple
   LLama.md`).
3. **System / Method**
   - 3.1 Tool surface: hexstrike-ai MCP server (~150 tools).
   - 3.2 Orchestrators under test: CAI, mcphost (+ OpenClaude as a third if its connection reliability
     is fixed in time — currently non-functional per existing findings).
   - 3.3 Model matrix (below).
   - 3.4 The evidence-grounding wrapper (A6) — describe the minimal ported predicate, explicitly
     citing which parts of the reference `compile_execution` design were kept (exact-substring
     matching with newline normalization; multi-line ordered matching; the DONE→PROGRESS downgrade
     rule) and which were deliberately dropped (SQLite MemoryKernel, crash recovery, multi-attempt
     leasing) with a one-line justification each (not needed at our run scale/duration).
   - 3.5 Targets and the ATT&CK-technique progression vocabulary borrowed from CALDERA (A8).
4. **Evaluation**
   - 4.1 RQ1/RQ2 results — the model × orchestrator × metric table (below), with the failure taxonomy
     illustrated by concrete transcript excerpts (we already have 6+ distinct prefix-corruption
     variants and a list of specific fabricated tool names from the `ornith` run — this kind of
     concrete example is what makes the section persuasive, not the aggregate numbers alone).
   - 4.2 RQ3 results — false-positive completion rate with vs. without the evidence-grounding wrapper,
     for at least the weakest model in the matrix (where the effect should be largest and easiest to
     demonstrate).
   - 4.3 RQ4 (if time allows) — task-tree progression per model, reported against the ATT&CK
     vocabulary.
   - 4.4 Supplementary: cybermetric/seceval knowledge-benchmark scores per model (A5), as a control
     variable correlated (or not) against the live tool-use reliability numbers.
5. **Discussion** — orchestrator choice matters as much as, or more than, model choice (already
   suggested by the existing 3-orchestrator comparison); implications for anyone deploying an
   LLM-driven pentest agent without frontier-model access; the HITL analysis (A7) — how many observed
   failures a human-approval gate would have caught, and at what cost to autonomy.
6. **Limitations** — see §5 below; state plainly.
7. **Conclusion**.

## 3. The experiment matrix (Table 1 in the paper)

**Models** (chosen to fit the stated hardware — one ~30 GB card, one ~16 GB card):

| Tier | Model | Where it runs | Why included |
|---|---|---|---|
| Baseline / already run | `ornith-1.0-35b` (Q4_K_M) | Remote Ollama via ngrok (existing setup) | Already produced one findings file; re-run with actual invocation attempts, not just listing, to close the gap the existing file flags as "not yet tested." |
| Local, strong tool-calling | `gpt-oss-20b` | 16 GB card (MXFP4) | Native tool-calling format, good contrast point against the 35B quantized model; fastest local iteration loop. |
| Local, 7–8B class | Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, or Hermes-2-Pro-7B (pick 1–2 based on which has the most reliable function-calling template for the orchestrators in use) | 16 GB or 30 GB card | Represents the tier most people can actually self-host; expected to show the highest failure rate — an important anchor point. |
| Optional upper-bound reference | One frontier API model (used sparingly, not the paper's subject) | API | A single calibration run only, to confirm our metrics correctly show "near-zero hallucination" on a model known to be reliable — a sanity check on the measurement methodology itself, not a comparison target. |

**Orchestrators:** CAI (`../CAI-modified/`), mcphost (`../MCPHost-modifed/`), optionally OpenClaude if
its MCP connection issue (currently failing 100% per the existing findings file) gets resolved.

**Targets:** Metasploitable2 and/or DVWA, run locally; optionally one additional intentionally-
vulnerable CTF-style VM for RQ4's progression measurement.

**Metrics** (defined precisely, so results are comparable across runs):

| Metric | Definition |
|---|---|
| Tool-call success rate | Of all attempted tool invocations, the fraction where the tool name exactly matches a real registered tool and required arguments are well-formed (first attempt, no retries counted as success). |
| Hallucination rate | Fraction of referenced/attempted tool names that do not exist in the real MCP tool catalog (cross-checked against the tool list captured independently, as already done for hexstrike-ai's 150-tool catalog in the existing findings file). |
| Echo-vs-invoke rate | Fraction of model turns where a tool call is described in prose/JSON-shaped text but no actual invocation event occurs in the orchestrator's trace log. |
| False-positive completion rate (RQ3) | Fraction of model-claimed "task complete" / "vulnerability confirmed" statements that do **not** survive the evidence-grounding check (A6) — i.e. are not a verifiable exact substring of real tool output — measured with and without the wrapper active. |
| Task-tree progression (RQ4) | Highest ATT&CK-technique stage (per the CALDERA-borrowed vocabulary) reached autonomously before stalling, timing out, or looping. |

## 4. Roadmap

**This week (the checkpoint this folder exists for):**
1. This resource folder (done).
2. Re-run the `ornith` scenario end-to-end with actual tool *invocation* attempts (not just listing)
   through both CAI and mcphost — this directly closes the gap flagged in the existing findings file
   and gives the first real echo-vs-invoke and hallucination numbers.
3. Pull and wire in `gpt-oss-20b` locally on the 16 GB card; run the same battery.
4. Start the results table (even partially filled) as the literal artifact to show as "progress."

**Next 1–2 weeks:**
5. Add one 7–8B model; complete the model × orchestrator matrix for RQ1/RQ2.
6. Implement the minimal evidence-grounding wrapper (A6) as a post-hoc log checker; run it over every
   trace already collected plus new runs; produce the RQ3 with/without comparison.
7. Run the cybermetric/seceval benchmarks (A5) on each model in the matrix for the supplementary
   control-variable numbers — cheap, no new infrastructure.

**If time remains:**
8. Stand up one local vulnerable target and attempt RQ4's task-tree-progression measurement for at
   least the two strongest models in the matrix.
9. One exploratory LangGraph specialist-worker run (A3) for the discussion section.
10. The HITL retrospective analysis (A7) over existing trace logs.

**Writing, in parallel throughout:** draft Introduction/Related Work/Method early (they don't depend
on final numbers); leave Evaluation/Discussion/Conclusion for last.

## 5. Known limitations to state explicitly in the paper

- **Model coverage is necessarily small** (3–5 models) given single-GPU-box constraints; we are
  explicit throughout that claims are scoped to the tested models, not "small LLMs in general."
- **Target coverage is local/disposable**, not real HTB-class infrastructure — this trades some
  ecological validity against reproducibility and legality; stated as a deliberate choice, not an
  oversight.
- **The evidence-grounding wrapper (A6) is a minimal port**, not the reference implementation's full
  machinery (no crash recovery, no multi-attempt leasing, no SQLite canonical state) — sufficient for
  single-session experimental runs, explicitly not claimed as production-ready.
- **Orchestrator versions are a moving target** (CAI, mcphost, and the hexstrike-ai server are all
  actively developed) — pin and record exact versions/commits for every run (already partially done
  in the existing findings file's format; keep doing this).
- **OpenClaude is currently non-functional** against hexstrike-ai per existing findings — if this
  isn't fixed in time, it is dropped from the matrix and reported as a known negative result rather
  than silently omitted.
- **The false-positive/oracle check in the evidence-grounding wrapper is a substring match**, per the
  reference implementation's own stated limitation ("proves the exact expected string appears in some
  canonical, evidence-grounded observation... does not prove arbitrary semantic goal entailment") —
  inherited knowingly, not accidentally.

## 6. Future work (explicitly deferred, not forgotten)

- Full LangGraph specialist-worker architecture (A3) at the same model tier, properly hardened against
  its documented single-retry-then-crash fragility.
- Full CyberSecEval or PentestGPT-Eval benchmark integration (A5), beyond the cheap vendored subset
  used here.
- A real interactive HITL mode (A7) rather than a retrospective log analysis.
- Extending the model matrix upward (larger local models, more frontier-model calibration points) as
  hardware allows.
- A full CALDERA-engine integration (A8) rather than borrowing only its technique vocabulary.
