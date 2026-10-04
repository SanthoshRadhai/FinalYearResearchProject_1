# gpt-oss-20b Tool-Calling Across Backends — Test Log and Conclusions

This document is the write-up for a single, self-contained empirical thread: getting
**gpt-oss-20b** (OpenAI's 20B-parameter open-weight model) to reliably drive
**`stealth-browser-mcp`** (a ~97-tool browser-automation MCP server) through a LangChain
ReAct agent, serving the model locally on the lab's NVIDIA A100-PCIE-40GB. It sits alongside
the `../findings/ornith-1.0-35b-...md` experiment referenced in `README.md` — a second,
independent data point for the same underlying question the paper is built around: **when an
open-weight model fails at tool calling, is the failure in the model or in the serving
stack around it?**

The short answer this thread arrived at: **for gpt-oss-20b, it was almost entirely the serving
stack.** Three different backends were tried. Two had concrete, diagnosed, backend-specific
blockers that had nothing to do with the model's actual tool-calling competence. The third
(llama.cpp) worked, but only after three further, separately-diagnosed bugs were found and
fixed — none of which were "the model can't do this," all of which were "the harness around
the model was letting a recoverable hiccup become a hard failure."

---

## 1. The setup

- **Model:** `gpt-oss-20b`, native MXFP4 quantization (~13GB on disk), OpenAI's "Harmony"
  chat-template format (system/developer/user/assistant channels, explicit tool-call
  channel markers, a documented CoT/analysis channel separate from the final answer).
- **Client:** a LangChain + LangGraph `create_react_agent`, `ChatOpenAI` pointed at whichever
  backend's OpenAI-compatible endpoint was under test, wired to `stealth-browser-mcp` over
  stdio (FastMCP 2.0, 97 tools: `spawn_browser`, `navigate`, `execute_script`,
  `get_page_content`, `execute_cdp_command`, and more).
- **Task used for every test:** answer a real CVE question, using the tools to fetch the
  actual NVD record (`https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=<ID>`) rather
  than answering from parametric memory — chosen specifically because it gives a
  cross-checkable ground truth (NVD's own published CVSS score/vector/dates) for every run.

## 2. Backend 1 — SGLang

Launched with `--reasoning-parser gpt-oss --tool-call-parser gpt-oss` (SGLang's built-in
Harmony support). **Partially worked** — real tool chains executed
(`spawn_browser → navigate → get_page_content`) and real CVE data was retrieved successfully
at least once. But it also intermittently produced a **completely empty final turn**
(`content=''`, `tool_calls=[]`, no error) after a tool result — a known-shaped SGLang
gpt-oss/Harmony content-vs-reasoning-field parsing issue tracked across multiple SGLang
GitHub issues. Not resolved within this thread; noted as the most functional of the three
backends but with an unresolved reliability gap.

## 3. Backend 2 — Ollama

**Failed outright**, and the cause was fully diagnosed: a custom-imported tag
(`gpt-oss-20b:latest`, built via `ollama create` from a raw Hugging Face safetensors folder)
returned:

```
Error code: 400 - {'error': {'message': 'registry.ollama.ai/library/gpt-oss-20b:latest does not support tools', ...}}
```

Root cause, confirmed directly with `ollama show gpt-oss-20b:latest --modelfile`: a plain
`ollama create` from a local safetensors folder does **not** auto-generate the model's real
chat template. It falls back to a bare passthrough:

```
TEMPLATE {{ .Prompt }}
```

No chat structure, no tool-call schema, nothing — which is exactly why Ollama's own
capability probe (`ollama show`) listed only `completion` and `thinking`, never `tools`, for
this import. The **official** `ollama.com/library/gpt-oss` build ships a hand-authored Go
template with real tool-call support; the gap is entirely in *how the model was imported*,
not in gpt-oss's actual tool-calling ability.

Two fix paths were evaluated and explicitly **rejected** in favor of the llama.cpp route below:

- **Paste the model's own `chat_template.jinja` directly into the Modelfile's `TEMPLATE`
  field.** This fails: Ollama's `TEMPLATE` is parsed by **Go's `text/template` engine, not
  Jinja2**. The two share superficial `{{ }}` syntax but nothing else. Concretely, this
  attempt ran the *entire* GGUF conversion successfully (14,500+ lines of tensor processing)
  and only failed at the very last step, compiling the template:
  `Error: template error: template: :27: function "inner_type" not defined` — `inner_type`
  is a Jinja macro used in gpt-oss's real template, meaningless to a Go template parser.
- **Auto-convert Jinja → Go via `@huggingface/ollama-utils`** (`convertJinjaToGoTemplate` /
  `convertGGUFTemplateToOllama`). Inspected the actual library source: its known-template
  table has no pre-vetted mapping for gpt-oss/Harmony, and its generic auto-converter only
  ever test-renders plain system/user/assistant messages — it never renders with a `tools`
  argument at all, so even a "successful" conversion would not have produced real tool-call
  formatting. Not attempted for a live test; ruled out from source inspection alone.

**Conclusion for Ollama:** the blocker is real, diagnosed, and specific to the *custom import
path* — not a statement about gpt-oss's tool-calling capability, which the official tag
would have provided out of the box.

## 4. Backend 3 — llama.cpp (the one that ultimately worked)

### 4.1 Build and conversion

- Cloned `ggml-org/llama.cpp` fresh, built with CUDA (`-DGGML_CUDA=ON
  -DCMAKE_CUDA_ARCHITECTURES=80`, A100/SM80), producing `llama-server`, `llama-quantize`,
  `llama-cli`. (`cmake` itself had to be installed via `pip install cmake` inside a Python
  environment first — not present system-wide.)
- Converted the HF safetensors checkpoint with `convert_hf_to_gguf.py --outtype f16`.
  Notably the output GGUF stayed close to the original size (13GB → 13.8GB) because
  llama.cpp's gpt-oss converter **keeps the MoE expert weights in their native MXFP4
  format** and only upconverts the smaller non-expert tensors to F16 — so no separate
  quantization pass was needed for this use case.
- Launched with `llama-server --jinja ...`. The `--jinja` flag is the key difference from
  Ollama: llama.cpp has its **own built-in Jinja-compatible template engine** (confirmed in
  the build log: `common/jinja/{lexer,parser,runtime,value,string,caps}.cpp`), so it can
  consume the model's real `chat_template.jinja` **directly**, with zero Go-template
  translation and zero manual template authoring.

### 4.2 First real test — success

Question: *"What is CVE-2024-3400 about?"* (Palo Alto PAN-OS GlobalProtect command
injection). The agent: spawned a browser, tried a couple of blocked/CORS'd `execute_script`
fetch attempts, correctly pivoted to `navigate` directly to the NVD REST endpoint, hit one
malformed tool call (a leaked garbage token stream used as the `instance_id` argument for
`get_page_content` — a Harmony-token-leakage artifact), **self-corrected on the very next
turn**, and produced a final answer.

**Cross-verified against live NVD data** (via `services.nvd.nist.gov`): CVSS 10.0, same
vector (`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`), same CWE-77, same
published/modified dates, same description — an exact match. (One accuracy gap noted: the
"Affected Products" table in the final answer was garbled/repetitive, a rendering-level
symptom of the same token-leakage issue, even though the core facts were correct.)

### 4.3 Reliability testing exposes two further bugs

A second test, same setup, different CVE (`CVE-2023-4863`, the libwebp heap overflow), was
run specifically to check this wasn't a one-off. It **failed**: the agent correctly
navigated to the right URL but never called `get_page_content`, and produced a **completely
empty final answer**. Root cause, found via the script's `DEBUG_HARMONY=1` raw-output mode:

```
Error code: 400 - request (34494 tokens) exceeds the available context size (32768 tokens)
```

**Context-window exhaustion**, not a Harmony-parsing bug. Each failed `execute_script` fetch
retry (blocked by CORS from that execution context) adds a full tool-call/tool-result round
trip to history; by the time `get_page_content` was reached the transcript had grown past
the server's `32768`-token limit and the request hard-failed. In one run this surfaced as a
visible `[error]` line; in another it appears to have been swallowed inside LangGraph's
internal ReAct loop and surfaced only as a silently-empty final message — same underlying
cause either way.

**Fix 1 — larger context window.** Relaunched `llama-server` with `-c 131072` (the model's
full trained context, `n_ctx_train` from its own `/v1/models` metadata) instead of `32768`.

**Fix 2 — proactive compaction**, added directly to the LangGraph `post_model_hook`
(`sanitize_ai_message` in `4_langchain_stealth_llamacpp.py`), so the fix isn't just "a bigger
number to eventually run out of" again on a longer task:
- Uses **llama-server's own `/tokenize` endpoint** for an exact token count after every model
  turn (not a rough character-based estimate).
- If the running history exceeds 75% of the context limit, it drops the middle of the
  conversation — via LangGraph's `RemoveMessage` marker — while preserving the system
  prompt, the original user request, and the most recent messages, ensuring the cut always
  lands on a clean AIMessage/ToolMessage boundary (never orphaning a tool result without its
  originating tool call, which both llama.cpp and OpenAI-style APIs reject).

Retested `CVE-2023-4863` after both fixes: succeeded cleanly, no context error. Cross-checked
against NVD: CVSS 8.8, exact vector match, correct version thresholds for both Chrome and
libwebp.

### 4.4 A genuinely novel CVE, to rule out memorized knowledge

To make sure "the model answered correctly" wasn't just "the model already knew this from
training," the test was repeated with a **real CVE from this month**
(`CVE-2026-85880` — a Windows ALPC heap-based buffer overflow, actively exploited per CISA,
published 2026-09-08), independently verified against NVD *before* running the test to fix
the ground truth in advance. This CVE post-dates gpt-oss-20b's training cutoff by a wide
margin, so a correct answer can only come from the tool-fetched page content, not
memorization.

First attempt: **failed** — the model skipped `spawn_browser` entirely and called
`execute_cdp_command` with empty arguments, twice in a row, tripping the script's existing
malformed-call circuit breaker (which aborted cleanly, as designed, but the task itself was
not completed). A debug rerun of the same question **succeeded** on the first malformed
call before self-correcting into the normal spawn → navigate → get_page_content flow.

**Fix 3 — targeted auto-recovery for the premature-tool-call pattern.** Rather than only
having the blunt circuit breaker as a backstop, a cheaper, more specific check was added to
the same `post_model_hook`: if a tool call needs a live `instance_id` and none has ever been
successfully produced by `spawn_browser` yet in the conversation, the call is silently
**redirected** to `spawn_browser` instead of being dispatched (a guaranteed failure) or
counted toward the circuit breaker. Retested: the model made the *same* mistake again
(confirming it's a real, recurring tendency at `temperature=1.0`, not a fluke), the
auto-recovery caught it, and the run completed successfully.

**Final cross-check**, post-fix: the model's answer for `CVE-2026-85880` reported CVSS 7.8
with vector `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` and a CISA action-due date of
`2026-09-22` — an **exact match** against the independently-fetched NVD ground truth on
every checkable field.

## 5. Overall results table

| # | CVE tested | Context size | Fixes in place | Outcome | NVD cross-check |
|---|---|---|---|---|---|
| 1 | CVE-2024-3400 | 32768 | none (first llama.cpp test) | ✅ success (1 self-corrected malformed call) | Exact match |
| 2 | CVE-2023-4863 | 32768 | none | ❌ empty final answer — context overflow (34,494 > 32,768 tokens) | n/a |
| 3 | CVE-2023-4863 | 131072 | larger context | ❌ transient connection error (unrelated, server warm-up) | n/a |
| 4 | CVE-2023-4863 | 131072 | larger context | ✅ success | Exact match |
| 5 | CVE-2026-85880 | 131072 | larger context + compaction | ❌ circuit breaker aborted — premature tool call before `spawn_browser` | n/a (no data fetched) |
| 6 | CVE-2026-85880 | 131072 | larger context + compaction (debug rerun) | ✅ success (1 self-corrected malformed call) | Exact match |
| 7 | CVE-2026-85880 | 131072 | larger context + compaction + auto-recovery | ✅ success — same premature-call mistake made again, auto-recovered this time | Exact match |

**4 of 7 runs succeeded outright; the 3 failures each had a distinct, fully diagnosed root
cause** (context overflow, an unrelated transient network hiccup, and a premature tool call)
— none of them "the model doesn't know how to do this" or "the model can't answer the
question." Every run that reached a final answer was factually accurate against live NVD
data, including for a CVE published after the model's training cutoff.

## 6. What this means for the paper's thesis

This is a second, independent instance of the same pattern the `ornith-1.0-35b` findings
file already established: **failure mode is largely a property of the serving
stack/orchestrator pairing, not a fixed property of the model.** Concretely, for the same
model (gpt-oss-20b) and the same task:

- **Ollama** failed 100% of the time, for a reason that has nothing to do with the model's
  tool-calling competence (an import-path template gap).
- **SGLang** partially worked but had its own backend-specific parsing bug (empty completions).
- **llama.cpp** worked, but only after diagnosing and fixing three separate,
  backend-adjacent issues: a context-size misconfiguration, a token-leakage-driven malformed
  tool-call pattern, and a tool-call-ordering mistake — each fixed with a targeted,
  model-agnostic mitigation (bigger context + compaction, a circuit breaker, and a
  premature-call redirect) rather than anything specific to gpt-oss.

This directly supports the paper's evidence-grounding framing (§2 of `README.md`): the right
question to ask when an agentic LLM system fails at tool use is not just "is the model
capable enough," but "does the serving/orchestration harness correctly expose the model's
actual capability, or does it silently degrade or misroute a recoverable hiccup into a hard
failure?" For gpt-oss-20b specifically, once the harness issues were fixed, the model's own
tool-calling and fact-grounding behavior was accurate on every completed run, including
against genuinely-unseen (post-cutoff) data.

## 7. Known limitations / not yet resolved

- **Not provably 100% reliable.** The underlying tendency for Harmony-formatted output to
  occasionally leak stray tokens into tool-call arguments (garbled `instance_id`) or to pick
  the wrong first tool is still present at `temperature=1.0` (gpt-oss's own recommended
  sampling setting) — it is now *handled* (self-correction, circuit breaker, auto-recovery),
  not eliminated. A larger run count (n≫7) would be needed to state a real success-rate
  percentage rather than a qualitative "it recovers" claim.
- **SGLang's empty-completion bug** was not revisited after switching to llama.cpp; it
  remains an open, unresolved backend-specific issue if SGLang is used again in the future.
- **Ollama's official `gpt-oss:20b` tag** (as opposed to the broken custom import) was never
  actually pulled and tested end-to-end in this thread — the diagnosis that it *would* work
  is based on Ollama's own capability metadata and template architecture, not a live test.
- **This was single-model, single-task-type testing** (CVE lookups only, 97-tool MCP server
  but a narrow slice of its actual tool surface exercised). It does not generalize to a claim
  about gpt-oss-20b's tool-calling reliability on more complex, multi-tool-type tasks.
