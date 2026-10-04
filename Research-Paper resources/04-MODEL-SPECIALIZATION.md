# Model Specialization Methods for Cybersecurity

This document catalogs the actual techniques available for making an LLM better at cybersecurity /
penetration-testing tasks — not just "use a bigger model" — and rates each one for feasibility on our
hardware (one ~30 GB VRAM card + one ~16 GB VRAM card, open-weight models only). It is meant to be
read alongside `02-APPROACHES.md` (which is about *system/architecture* choices) — this document is
about *model-level* choices: what to do to the model itself, or to the data/decoding process around
it, so it performs better at the tool-driven pentesting task described in `01-SCOPE.md`.

The methods are ordered roughly by cost (cheapest/fastest first), because for a resource-constrained
paper the honest answer is usually "do the cheap thing that fixes the specific failure mode you
observed, before reaching for the expensive thing that fixes it more generally." Where a method maps
directly onto the failure taxonomy already documented in `../findings/`, that's called out explicitly
— several of these are not generic advice, they are targeted fixes for the exact bugs we've already
seen (tool-name prefix corruption, schema-echo-instead-of-invoke, fabricated tool names).

---

## 0. The three things "make the model better at cybersecurity" can actually mean

Before picking a method, be precise about which gap is being closed, because the right technique
differs:

| Gap | Symptom (from our own data) | What actually closes it |
|---|---|---|
| **Knowledge gap** — the model doesn't know security facts (CVE details, ATT&CK techniques, tool syntax) | Low CyberMetric/SecEval scores; wrong exploit rationale | RAG, continued pretraining, or SFT on knowledge-style QA |
| **Behavior/format gap** — the model knows the right tool exists but names/calls it wrong | The `ornith` findings: `hexstrike__` → `hexstrips__`, `hexstripe_`, fabricated tool names, JSON-schema-echoed-as-prose instead of invoked | Constrained decoding, tool-use fine-tuning, function-calling-format SFT/DPO |
| **Reasoning/planning gap** — the model calls tools correctly but makes poor strategic decisions (wrong next step, gives up early, loops) | RQ4-style task-tree stalling | RAG over strategy docs (HackTricks, ATT&CK), rejection-sampling fine-tuning (RFT) on your own successful trajectories, DPO on trajectory pairs |

Our own findings so far are almost entirely **behavior/format-gap** symptoms, not knowledge-gap
symptoms — the model named real tool suffixes correctly, it just couldn't reproduce the shared
namespace prefix reliably across a long list. That should weight which methods below get tried
first (see §6, the recommended layering).

---

## 1. Prompt engineering / in-context learning (cost: ~free)

**What it is:** No model changes at all — restructure the system prompt, add few-shot examples of
correct tool calls, tighten the output schema, explicitly enumerate the exact tool names in-context
right before asking the model to use one.

**Reference:** `../data/docs-pentestgpt/codebase-understanding/UNDERSTANDING.md` — the reference
re-implementation's entire `agents.py` is essentially this: `SUPERVISOR_INSTRUCTIONS`/
`EXECUTOR_INSTRUCTIONS` are large, carefully written prompt constants where "every hard validator
rule has a corresponding sentence in one of these prompts telling the model the rule in advance,"
plus strict JSON-Schema-constrained structured output (`additionalProperties: False`, explicit
`required` fields) enforced via the provider's structured-output feature.

**Feasibility:** Trivial — zero GPU cost beyond ordinary inference, works with every model in the
matrix, can be iterated on in minutes.

**Directly applicable fix:** the `ornith` run's prefix-corruption bug happened while asking the model
to *enumerate* all 150 tool names from memory in one long response. A better-engineered prompt would
never ask a model to recall a large structured list from its own generation — it would show the
model the exact list (or the relevant slice of it) in-context immediately before a tool-selection
decision, turning a memory/generation problem into a copy/selection problem, which small models are
categorically better at. **This should be the very first thing tried, before any training-based
method below**, and it costs nothing to test as an ablation (RQ1 extended: hallucination rate with
in-context tool list vs. without).

**Limitations:** Can't fix problems that are structurally about model capability (e.g. multi-step
strategic planning across a long session) — it only helps within what a well-prompted model can
already do in principle.

---

## 2. Constrained / grammar-guided decoding (cost: ~free, highest leverage for our specific bug)

**What it is:** Instead of letting the model freely generate a tool name as text and hoping it's
correct, constrain the decoder itself so that only a token sequence matching a real tool name (from
a fixed grammar/enum built from the actual MCP tool catalog) can ever be produced — every other path
through the vocabulary is masked out at sampling time.

**Reference:** not present in the `data/` corpus directly, but it is the mechanical generalization of
what the reference PentestGPT re-implementation's `agents.py` already does at the schema level
(`_require_exact_keys`, JSON Schema `additionalProperties: False`) — that enforces *shape*
post-hoc/pre-commit; true constrained decoding enforces it *during generation*, which is strictly
stronger. Standard tools for this: llama.cpp's GBNF grammars, the `outlines` / `guidance` Python
libraries, or vLLM's structured-output backend (all runnable on our own hardware, no cloud
dependency).

**Feasibility:** Very high — no training, no extra GPU memory beyond ordinary inference, works with
every model including the 35B quantized remote model (if the serving stack supports it) and any local
7B–20B model.

**Directly applicable fix:** this is the single most targeted fix for the *exact* observed bug. The
`hexstrike__` namespace-prefix corruption is, by construction, impossible under grammar-constrained
decoding — if the grammar only accepts the 150 real fully-qualified tool names, the model literally
cannot emit `hexstrips__nmap_scan`, because that string has no valid path through the constrained
vocabulary. This turns a *model reliability* question into a *decoding infrastructure* question,
which is a much easier problem to solve completely rather than partially.

**Limitations:** Only fixes the *naming/shape* of a tool call, not whether the *arguments* or the
*decision to call that tool at all* are sensible — a model could still be grammar-guided into calling
the wrong (but real) tool, or the right tool with nonsensical arguments. It also doesn't fix the
"echo instead of invoke" failure mode (the model describing a call in prose rather than emitting an
actual tool-call event) unless the orchestrator itself forces tool-call-only output (which several
orchestrators, including the reference implementation's `toolChoice:"required"` pattern seen in
`../data/docs-Langchain-custom-agent/CODEBASE_UNDERSTANDING.md`, already do).

**Recommendation for the paper:** run this as an ablation arm in the RQ1/RQ2 matrix — same
model/orchestrator/target, with and without grammar-constrained tool-name decoding — this is cheap
enough to run for every model in the matrix and would produce one of the paper's cleanest, most
convincing results (a near-total elimination of the hallucination-rate metric specifically, isolating
that the *format* failure was fixable independent of the model's underlying capability).

---

## 3. Retrieval-Augmented Generation (RAG) (cost: low — CPU/embedding cost only, no GPU training)

**What it is:** Retrieve relevant reference text (tool documentation, CVE details, technique guides)
at inference time and inject it into the prompt, instead of relying on the model's parametric memory.

**Reference:** `../data/docs-autopentestgpt/ARCHITECTURE.md` §6.5/`text_embeddings.py` — a full worked
example: per-agent Pinecone namespaces, documents chunked at 500 characters, ingested from a fixed
set of URLs (OWASP Top 10, MITRE CWE pages, PortSwigger/HackTricks guides), retrieved via a
condense-question sub-chain before every worker-agent turn. Its documented bugs are worth reading
before copying it verbatim: a latent bug where the Pinecone index is always created with 1536-dim
(ada-002) vectors regardless of which embedding model is actually configured, silently breaking
retrieval for any other embedding dimensionality; and RAG ingestion being a separate manual step
whose completion status is pure operational state, easy to forget.

**Feasibility:** High — embeddings and vector search are cheap (run on CPU or a small fraction of
either GPU); no cloud dependency needed (avoid Pinecone specifically to keep this local and
reproducible — use Chroma, Qdrant, or FAISS running locally instead, especially since we have no
budget assumption for a hosted vector DB service).

**What corpus to build for this paper specifically:**
- The **hexstrike-ai tool catalog itself** (all ~150 tool names + argument schemas + descriptions) —
  retrieving the exact, correct tool spec immediately before a tool-selection decision is really RAG
  applied to method §1's in-context fix, and directly targets the observed hallucination bug.
- **MITRE ATT&CK/CWE/CAPEC** technique descriptions — supports RQ4's task-tree-progression reasoning.
- **HackTricks** and **PortSwigger Web Security Academy** technique pages — the same sources the
  AutoPentest reference already uses; genuinely high-quality, freely available pentesting methodology
  text.
- **NIST NVD CVE data** — for any target where a specific CVE is relevant (matches the reference
  `nist_nvd.py` tool pattern, §7.1 of the AutoPentest breakdown).

**Limitations:** RAG improves what the model *knows to reference*, but does not fix format-level tool
hallucination on its own (a model can retrieve the correct tool doc and still botch reproducing the
namespace prefix in its own output) — best combined with §1/§2, not used as a substitute.

---

## 4. Full-parameter fine-tuning (cost: infeasible at our scale for anything beyond ~1–3B)

**What it is:** Update every weight in the model via gradient descent on a task-specific dataset.

**Feasibility:** **Not feasible** for any model in our realistic matrix (7B and above) on a ~30 GB +
~16 GB two-card setup. Adam-family optimizers need roughly 4 bytes/parameter for the optimizer state
alone (momentum + variance, in fp32) on top of the model weights and gradients — for a 7B model
that's on the order of 100+ GB of memory even before activations, far beyond what either card offers
individually and impractical to shard across only two consumer-class cards for a resource-constrained
project. This is true industry-wide, which is exactly why the next two methods (LoRA-family PEFT,
and RAG/prompting) dominate practical small-lab LLM specialization.

**Verdict: Rule out explicitly and say so in the paper's Method section** — this is a legitimate,
citable resource-constraint statement, not a gap in effort.

---

## 5. Parameter-efficient fine-tuning — LoRA / QLoRA / DoRA (cost: medium, feasible on our hardware)

**What it is:** Freeze the base model's weights; train only small low-rank adapter matrices injected
into attention/MLP layers (LoRA), optionally with the base model held in 4-bit quantized form during
training to shrink memory further (QLoRA), or with an additional weight-decomposition trick for
slightly better quality at the same adapter size (DoRA).

**Feasibility:** **High, and the most realistic training-based method available to us.** QLoRA on a
4-bit-quantized 7B model is comfortably trainable on a single ~16 GB card; a 13B–14B model is feasible
on the ~30 GB card; the same setup can push into the low-30B range with careful batch-size/sequence-
length tuning. Standard tooling (`peft` + `bitsandbytes`/`transformers`, or `Unsloth` for a
faster/lower-memory implementation of the same idea) runs entirely locally, no cloud training service
required — consistent with running everything in a local, reproducible, offline-capable setup.

**What to fine-tune it on for this paper specifically:**
- **Function-calling/tool-use format data** — the most direct fix for the observed failure mode.
  Public tool-use SFT datasets (e.g. Gorilla-style API-call datasets, ToolBench-style traces) adapted
  to include hexstrike-ai's actual tool schemas, *plus* our own collected traces: every clean,
  correctly-invoked tool call in our existing/future run logs is itself a positive training example;
  every hallucinated one is a negative example useful for contrastive framing (see §7, DPO).
- **Cybersecurity instruction-tuning data** — CTF write-up Q&A pairs, ATT&CK-technique explanation
  pairs, or the same style of data underlying the CAI-vendored `cybermetric`/`seceval` benchmarks
  already in `../CAI-modified/benchmarks/`.

**Limitations:** Still requires a curated dataset (garbage in, garbage out); a LoRA adapter trained on
too narrow a distribution can overfit to the specific tool server/prompt format used to generate the
data and generalize poorly to a different MCP server or orchestrator — worth explicitly testing
cross-orchestrator generalization if this path is pursued, since our own paper's premise is that
orchestrator matters.

---

## 6. Continued / domain-adaptive pretraining (DAPT) (cost: high relative to benefit here — generally not recommended)

**What it is:** Keep training the base model with the original next-token-prediction objective, but
on a large corpus of raw domain text (e.g. security blogs, CVE descriptions, tool manuals) rather than
task-specific instruction pairs, before any instruction-tuning/RLHF stage.

**Feasibility:** Technically possible with LoRA at a small scale, but it is the least data-efficient
method on this list per unit of GPU time, and for the *specific* gap we've observed (tool-calling
format reliability, not raw domain knowledge) it is the wrong tool — RAG (§3) delivers the same
knowledge-grounding benefit far more cheaply and with easier attribution/updatability (swap the
retrieval corpus instead of re-training).

**Verdict:** Not recommended for this paper's scope; mentioned for completeness and to justify, in
the paper's Method section, *why* RAG was chosen over DAPT for the knowledge-gap dimension.

---

## 7. Preference-based / RL-style methods

This is a family, not one method — ordered from heaviest/most-general to lightest/most-targeted.

### 7a. RLHF via PPO (cost: infeasible)

**What it is:** The classical pipeline — train a reward model on human preference comparisons, then
optimize the policy model against it with PPO, which requires holding the policy, a reference copy of
the policy, the reward model, and (often) a value model simultaneously in memory during training.

**Feasibility:** **Not feasible** on our hardware for any model above a couple billion parameters —
even before counting optimizer state, PPO's requirement of multiple full model copies resident at
once multiplies the already-prohibitive full-fine-tuning memory cost from §4. Also requires a
human-preference-labeling pipeline we have no budget or team for.

**Verdict:** Explicitly ruled out, same as §4.

### 7b. RLAIF (cost: same training cost as 7a, cheaper labeling)

**What it is:** Replace human preference labels with AI-generated ones (e.g. a stronger model judges
which of two candidate outputs is better), keeping the same PPO-style training loop otherwise.

**Feasibility:** The labeling cost is solved, but the training-time memory problem from 7a is not —
still infeasible on our hardware at a useful model size.

**Verdict:** Ruled out for the same reason as 7a; the *labeling* idea (use a stronger judge model to
score outputs) is still useful and gets reused below in a lighter-weight training method (7d) and in
the evaluation methodology (a judge model to score task-tree progression quality, if used carefully
and reported as such).

### 7c. Direct Preference Optimization family — DPO / ORPO / KTO (cost: medium, feasible on our hardware)

**What it is:** Skip the separate reward model and the PPO rollout loop entirely; train directly on
`(prompt, chosen response, rejected response)` triples with a closed-form loss that increases the
policy's relative preference for the chosen response — no reward model, no value model, no rollout
sampling loop, memory cost comparable to ordinary SFT/LoRA training (§5).

**Feasibility:** **High** — this is the practical, single-GPU-friendly way to get most of RLHF's
benefit without its memory cost. Runs with the same `peft`/LoRA infrastructure as §5.

**The elegant part for this specific paper:** we do not need to construct preference pairs from
scratch or pay for human/AI labeling — **the evidence-grounding wrapper from `02-APPROACHES.md` §A6
is itself a preference-pair generator.** For any given task, a trajectory whose completion claim
passes the evidence-grounding check (a real, verified, exact-substring-matched tool result) is a
natural "chosen" example; a trajectory that made the same kind of claim but failed the check
(hallucinated, unverifiable, or downgraded to `PROGRESS`) is a natural "rejected" example — generated
automatically, for free, as a byproduct of experiments we are already running for RQ1–RQ3. This
directly connects the model-specialization work in this document to the paper's main empirical
contribution, rather than being a separate, disconnected training exercise.

**Recommendation:** if time allows past the roadmap in `03-CONCLUSION.md`, this is the highest-value
next step after the RQ1–RQ3 measurement work — it turns "we measured that small models hallucinate
tool calls" into "we measured it, and we show a cheap, reproducible training recipe (sourced entirely
from our own evaluation infrastructure) that reduces it," which is a substantially stronger paper.

### 7d. Rejection-sampling fine-tuning / RFT / STaR-style self-improvement (cost: medium, feasible, and the most natural fit)

**What it is:** Sample many candidate trajectories from the model for a range of tasks, keep only the
ones that pass a correctness/verification check, and fine-tune (ordinary SFT, not preference-pair
based) on the surviving "self-generated but verified-correct" trajectories — no external labels
needed at all beyond the verifier.

**Feasibility:** High, same training cost as §5 (it's just SFT on a filtered dataset).

**Why this is arguably the single best-fit method for our exact situation:** the verifier this method
needs is, again, exactly the evidence-grounding wrapper we are already building for RQ3. Concretely:
run the model many times against our local disposable targets, keep only the trajectories whose task
completions are evidence-grounded (real, verified tool output, not hallucinated), and fine-tune the
same (or a smaller) model on those verified-correct trajectories. This requires no external dataset,
no human labeling, and no preference-pair construction — only compute (many sampled rollouts) and the
verifier we are building anyway.

**Limitations of 7c/7d together:** both depend entirely on the *quality and precision* of the
verifier — an unreliable verifier (either too permissive, admitting bad trajectories as "chosen"/
"verified," or too strict, discarding rare but genuinely correct trajectories) directly corrupts the
resulting fine-tune. This is exactly why the reference implementation's matching cascade
(`compile_execution`'s exact/widened/unique-line/cross-receipt strategies, see `02-APPROACHES.md`
§A6) is worth porting carefully rather than approximating with a naive substring check — the training
signal is only as good as this check.

### 7e. RL from execution feedback (RLEF) (cost: high — mentioned for completeness, not recommended here)

**What it is:** A more general framing where the reward signal comes from actually executing the
model's output (e.g. did the exploit succeed, did the command run without error) rather than from a
learned reward model or a fixed verifier check — closer to classical RL with an environment.

**Feasibility:** Conceptually appealing (it's the "real" reward for a pentesting agent — did the
attack actually work), but building a stable RL training loop around live tool execution (with all
the safety, reproducibility, and reward-shaping challenges that implies) is a substantially larger
engineering effort than 7c/7d for comparable benefit at our scale, and risks non-reproducible or
unsafe training-time side effects against real tools/targets.

**Verdict:** Noted as the natural "next step after this paper" in `03-CONCLUSION.md`'s future work,
not attempted here — 7c/7d already capture most of the practical benefit (a verified-outcome-based
training signal) without live-RL's engineering and safety overhead.

---

## 8. Knowledge distillation from a stronger model (cost: medium — mostly inference cost on the teacher, then ordinary SFT)

**What it is:** Use a stronger (e.g. frontier) model to generate high-quality reasoning traces or
tool-use trajectories for a range of pentesting tasks, then fine-tune (ordinary SFT, §5's LoRA
infrastructure) the small target model on those traces — transferring some of the teacher's
capability without needing the teacher at inference time.

**Feasibility:** High, and it composes directly with something already planned: `03-CONCLUSION.md`'s
experiment matrix already includes "one frontier API model used sparingly... as a calibration
reference point." Those same calibration runs, if logged as full trajectories, are simultaneously the
distillation dataset for this method — no extra data-collection cost beyond what's already budgeted.

**Limitations:** Quality is capped by the teacher's own performance on this exact tool surface (if the
frontier model itself struggles against hexstrike-ai's specific 150-tool catalog, distillation
inherits that ceiling); still requires the same LoRA/SFT infrastructure and a modest number of teacher
rollouts across enough task diversity to generalize.

---

## 9. Model merging / adapter composition (cost: very low — no additional training)

**What it is:** Combine multiple already-trained models or LoRA adapters into one set of weights via
arithmetic in weight-space (e.g. `mergekit`-style task-vector merging, or simply loading multiple LoRA
adapters and combining them), instead of training a single model to do everything at once.

**Feasibility:** Very high, essentially free once the component adapters exist — e.g. merge a
tool-calling-format LoRA adapter (from §5/§7d) with a security-knowledge LoRA adapter trained
separately, testing whether the merge retains both improvements better/worse than training on a mixed
dataset directly.

**Verdict:** Worth a small exploratory experiment if multiple LoRA adapters end up being trained
anyway (§5, §7c/7d) — cheap enough that there's little reason not to try it once the components exist,
but not worth building a dedicated pipeline for on its own.

---

## 10. Quantization level as an experimental variable, not just a deployment choice

**What it is:** The precision a model is served at (fp16, 8-bit, 4-bit/Q4_K_M, etc.) is normally
treated as a pure inference-cost/deployment decision — but it directly affects output stability, and
we already have anecdotal reason to suspect it matters here.

**Reference:** the existing `ornith` findings explicitly flag quantization as a suspect: "likely
repetition/instability on long structured lists with a repeated prefix token, **possibly exacerbated
by quantization**" — currently an untested hypothesis, not a confirmed finding.

**Feasibility:** High to test cheaply — the same model at two quantization levels (e.g. Q4_K_M vs.
Q8_0, or 4-bit vs. fp16 if VRAM allows for the smaller models) is just two more rows in the existing
experiment matrix from `03-CONCLUSION.md`, not a new method requiring new infrastructure.

**Recommendation:** add quantization level as a controlled variable for at least one model in the
matrix (likely one of the local 7B–20B models, where both a higher- and lower-precision run fit in
16–30 GB) — this would let the paper either confirm or rule out quantization as a contributing factor
to the hallucination rate, directly resolving a hypothesis the existing findings file already raised
but left open.

---

## 11. Feasibility summary (our hardware: one ~30 GB card + one ~16 GB card)

| Method | GPU cost | Data/labeling needed | Fixes which gap (§0) | Verdict for this paper |
|---|---|---|---|---|
| Prompt engineering / in-context tool list | ~free | None | Behavior/format | **Do first — cheapest possible ablation** |
| Constrained/grammar-guided decoding | ~free | Tool schema (already have it) | Behavior/format | **Do first — highest leverage for the observed bug** |
| RAG (local vector DB, not Pinecone) | Low (embeddings only) | Curated corpus (ATT&CK/HackTricks/tool docs — sourceable now) | Knowledge, partially reasoning | Adopted per `02-APPROACHES.md` A6/A8 framing |
| Full fine-tuning | Infeasible (>7B) | Large labeled dataset | All | Ruled out, stated explicitly |
| LoRA / QLoRA / DoRA | Medium, feasible (7B on 16GB, up to ~30B on the 30GB card) | Moderate — tool-use + security instruction data | Behavior/format, knowledge | Recommended next step after core measurement work |
| Continued pretraining (DAPT) | High relative to benefit | Large raw corpus | Knowledge | Not recommended — RAG dominates it here |
| RLHF / PPO | Infeasible | Human preference labels | All | Ruled out |
| RLAIF | Infeasible (same as PPO) | AI preference labels | All | Ruled out |
| DPO / ORPO / KTO | Medium, feasible (same cost as LoRA SFT) | Preference pairs — **generatable for free from the evidence-grounding wrapper (A6)** | Behavior/format, reasoning | **Strong recommendation, directly reuses paper infrastructure** |
| Rejection-sampling fine-tuning (RFT/STaR) | Medium, feasible (same cost as LoRA SFT) | None beyond the verifier (A6) + rollout compute | Behavior/format, reasoning | **Strong recommendation, arguably the best fit overall** |
| RL from execution feedback (RLEF) | High, nontrivial engineering | Live execution environment | All | Future work, not attempted now |
| Distillation from a frontier model | Medium (teacher inference + LoRA SFT) | Teacher rollouts (already budgeted as the calibration run) | All | Opportunistic — reuse the planned calibration run's logs |
| Model merging | ~free | Pre-existing trained adapters | Composability of the above | Small exploratory experiment if adapters exist |
| Quantization level as a variable | ~free (reuses existing runs) | None | Behavior/format (tests a specific hypothesis) | **Add to the experiment matrix — resolves an open question from existing findings** |

---

## 12. Recommended layering for this paper

Given the feasibility ratings above and the paper's actual scope (`01-SCOPE.md`), the sensible order
of investment — each layer assuming the previous one is at least attempted — is:

1. **Layer 0 (already exists):** agentic orchestration + tool-server integration (CAI/mcphost +
   hexstrike-ai) — the current baseline that produced the observed failures.
2. **Layer 1 (do immediately, ~free):** prompt engineering (§1) + grammar-constrained decoding (§2) as
   ablation arms added to the existing RQ1/RQ2 experiment matrix. This alone may explain and fix a
   large fraction of the observed hallucination rate, and costs essentially nothing to test.
3. **Layer 2 (cheap, do next):** local RAG (§3) over the hexstrike-ai tool catalog and a small
   HackTricks/ATT&CK corpus, feeding into the RQ4 task-tree-progression measurement.
4. **Layer 3 (medium cost, do if Layer 1–2 results justify it):** LoRA/QLoRA fine-tuning (§5) on
   tool-use format data, evaluated against the same metrics as the baseline runs.
5. **Layer 4 (medium cost, highest research payoff per effort, do if time allows):** DPO (§7c) or
   rejection-sampling fine-tuning (§7d), using preference pairs / verified trajectories generated as a
   *byproduct* of the evidence-grounding wrapper already being built for RQ3 — this is where the
   model-specialization work and the paper's main empirical contribution become the same piece of
   work rather than two separate efforts.
6. **Layer 5 (explicitly out of scope, stated as future work):** full fine-tuning, PPO-based RLHF/
   RLAIF, RL from live execution feedback, continued pretraining.

This layering means every method actually attempted either costs nothing extra (Layers 0–2) or
directly reuses infrastructure already being built for the paper's core contribution (Layers 3–4) —
nothing on this list requires a separate, disconnected research effort to justify its inclusion.
