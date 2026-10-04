# BFCL (Berkeley Function Calling Leaderboard) — Supplementary Tool-Calling Benchmark

Supplementary, externally-standardized number for **RQ1 (Reliability)** — how
reliably an open-weight LLM in scope invokes tools correctly — reported
alongside this project's own bespoke metrics (tool-call success rate,
hallucination rate, echo-vs-invoke rate; see
`../RedBlue-MultiAgent/RESULTS.md`), not as a replacement for them. BFCL scores
structural correctness (right tool, right arguments) via deterministic
AST/JSON matching against an expected call — no LLM judge, no live external
API execution for the categories run here.

## 1. Setup

- **Model:** `gpt-oss-20b` (MXFP4 MoE quantization), GGUF file
  `gpt-oss-20b-F16.gguf`, served by `llama-server` with `--jinja` (Harmony
  chat template) — the same backend/model this whole project's agents use.
- **Host:** a separate HPC box (`ajaykumarvp.24it@hpc`), **not** the IT-GPU
  server used for the RedBlue-MultiAgent runs elsewhere in this project. Model
  endpoint reachable at `http://localhost:5500/v1` on that host
  (`n_ctx=32768`, `n_ctx_train=131072`, `n_params≈20.9B`).
- **Harness:** `gorilla-llm/berkeley-function-call-leaderboard` (`bfcl` CLI),
  installed in its own `bfcl` conda env (kept separate from this project's
  `hexstrike` env to avoid dependency conflicts).
- **Local-server wiring:** BFCL's `OSSHandler` base class reads
  `REMOTE_OPENAI_BASE_URL` / `REMOTE_OPENAI_API_KEY` (or
  `LOCAL_SERVER_ENDPOINT` / `LOCAL_SERVER_PORT`) env vars and
  `--skip-server-setup`, so it talks directly to the already-running
  `llama-server` instead of spinning up its own vLLM/SGLang server — no BFCL
  source changes were needed, only a new model-registry entry
  (`gpt-oss-20b-local-FC`) pointing at that endpoint with `is_fc_model=True`
  (native OpenAI-style `tools=` calling, matching how every agent in this
  project already talks to the model via `langchain_openai.ChatOpenAI`).

## 2. Command

```bash
bfcl evaluate --model gpt-oss-20b-local-FC \
  --test-category simple_python,multiple,parallel,parallel_multiple,irrelevance
```

Category selection rationale: the non-live, single-turn AST categories
(`simple_python`, `multiple`, `parallel`, `parallel_multiple`) plus
`irrelevance` (does the model correctly *refrain* from calling a tool when
none applies) were chosen as the cheapest, most directly RQ1-relevant subset —
deterministic scoring, no multi-turn stateful backend simulation, and no
programming-language-specific categories (`java`/`javascript`) irrelevant to a
security-tool-calling paper.

## 3. Raw result (BFCL V4 harness)

```
🦍 Model: gpt-oss-20b-local-FC
🔍 Running test: simple_python
✅ Test completed: simple_python. 🎯 Accuracy: 89.00%
🔍 Running test: parallel_multiple
✅ Test completed: parallel_multiple. 🎯 Accuracy: 0.00%
🔍 Running test: multiple
✅ Test completed: multiple. 🎯 Accuracy: 88.00%
🔍 Running test: parallel
✅ Test completed: parallel. 🎯 Accuracy: 0.00%
🔍 Running test: irrelevance
✅ Test completed: irrelevance. 🎯 Accuracy: 85.42%
```

Full detailed CSVs written to (on the HPC host):
`berkeley-function-call-leaderboard/score/data_overall.csv`,
`data_non_live.csv`, `data_live.csv`, `data_multi_turn.csv`, `data_agentic.csv`,
`data_format_sensitivity.csv`.

## 4. Results table

| Category            | Accuracy | Notes |
|----------------------|---------:|-------|
| `simple_python`       | 89.00%  | Single tool call, single argument set — strong |
| `multiple`             | 88.00%  | Correct tool selected among several candidates — strong |
| `irrelevance`           | 85.42%  | Correctly declines to call a tool when none applies — the "not 100%" number expected of a small model, as anticipated |
| `parallel`               |  0.00%  | **Needs investigation before being reported as a capability finding — see §5** |
| `parallel_multiple`       |  0.00%  | **Same caveat as `parallel`** |

## 5. Honest interpretation — the two 0.00% scores are NOT yet a confirmed finding

Per this project's own stated discipline (`../RedBlue-MultiAgent/RESULTS.md`'s
practice of never reporting a number without checking whether it reflects a
real model limitation vs. a measurement artifact — see that file's §8c for a
precedent), the two `0.00%` results on `parallel`/`parallel_multiple` are
flagged, not yet asserted, as a genuine finding. A clean 0% across an entire
category (rather than a partial/degraded score) is at least as consistent
with a harness/handler-side parsing mismatch as with a true model capability
gap. Two hypotheses, not yet distinguished:

1. **Genuine capability gap:** gpt-oss-20b, at this size/quantization, may
   simply not emit multiple simultaneous tool calls in one turn in the exact
   shape BFCL's scorer expects — plausible, and would itself be a legitimate,
   reportable RQ1/RQ2 result (a small-model tool-calling limitation).
2. **Handler/parsing artifact:** `llama-server`'s OpenAI-compatible endpoint
   may return multiple tool calls in a list shape, ordering, or field naming
   that BFCL's AST checker for these two categories doesn't recognize even
   when the underlying call was substantively correct — the same class of
   "measurement artifact, not a real bug" issue documented elsewhere in this
   project.

**Before citing the `parallel`/`parallel_multiple` numbers in the paper**,
inspect the raw per-example logs in
`berkeley-function-call-leaderboard/result/gpt-oss-20b-local-FC/` for at least
a few `parallel`/`parallel_multiple` cases to see the model's actual raw
output next to what the scorer expected, and confirm whether real tool calls
were attempted at all (echo-vs-invoke distinction, mirroring this project's
own metric of the same name) before concluding this is a model limitation
rather than a harness integration issue.

## 6. Status

- ✅ `simple_python`, `multiple`, `irrelevance` — usable as-is for RQ1's
  supplementary community-benchmark number.
- ⏳ `parallel`, `parallel_multiple` — root cause not yet determined; do not
  cite these two numbers in the paper until §5's raw-log check is done.
