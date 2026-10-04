# Scope

## 1. The assigned paper, stated precisely

**PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing**
(Deng, Liu, Mayoral-Vilches, Liu, Li, Xu, et al., USENIX Security 2024).

Its actual contribution, for scoping purposes:
- A three-module architecture — **Reasoning** (maintains a "pentesting task tree," decides the next
  sub-task), **Generation** (produces the concrete command/payload for that sub-task), **Parsing**
  (extracts structured information from raw tool output back into the task tree) — built on top of
  GPT-4.
- Evaluation on real HackTheBox / VulnHub machines with a **human operator in the loop** executing
  the model's suggested commands and feeding results back.
- A benchmark (`PentestGPT-Eval`) of sub-tasks across the pentesting lifecycle, scored by whether the
  model reaches the correct next step, not only by final flag capture.

Why we are not attempting a faithful reproduction (fully justified in `02-APPROACHES.md` §1): it
assumes a GPT-4-class reasoning model, a human operator for every command, and access to live,
authorized HTB-class infrastructure for a multi-week evaluation window. We have none of the first
two by design (open-weight 7B–35B models, fully autonomous tool-calling) and only a constrained
version of the third (local disposable VMs, not HTB).

## 2. Research questions (the actual scope of our paper)

We reframe PentestGPT's core bet — "an LLM can reliably drive a multi-step pentest tool-calling
loop" — as an empirical question about the tier of models we can actually run, instead of assuming
the answer (as PentestGPT can, with GPT-4) and building on top of it.

**RQ1 (reliability).** How reliably do small-to-mid-size open-weight LLMs (7B–35B parameters) invoke
tools correctly — right name, right arguments, actually invoked rather than described — when acting
as the reasoning engine of a PentestGPT-style loop against a real, large (100+ tool) MCP-based
pentesting tool server?

**RQ2 (failure taxonomy).** What are the distinct, reproducible failure modes when this fails, and
are they attributable to the *model* (hallucination, instability on long structured output), the
*orchestrator* (connection handling, prompt/schema translation to the model), or their interaction?

**RQ3 (mitigation via evidence-grounding).** Does adopting a PentestGPT-style evidence-grounding
discipline — a deterministic layer that only accepts a task as "done" if the claimed result is a
verifiable, exact substring of real tool output (as implemented in the reference
`docs-pentestgpt/codebase-understanding/UNDERSTANDING.md` re-implementation's `compile_execution`) —
measurably reduce false-positive "task complete" claims from a small/unreliable model, compared to
trusting the model's own self-report?

**RQ4 (task-tree progression, secondary/stretch).** How far through a PentestGPT-style task
lifecycle (recon → service enumeration → vulnerability identification → exploitation attempt) does a
7B–35B model get autonomously on a disposable local vulnerable target, and where does it stall?

RQ1–RQ2 are already partially answered by existing data (`../findings/`) and are the paper's floor —
achievable even in the worst case. RQ3 is the paper's main methodological contribution if time
allows. RQ4 is a stretch goal that turns the paper from "reliability study" into "reliability study
+ a working (if limited) end-to-end demonstration."

## 3. In scope

- Open-weight models in the 7B–35B range, run either locally (16 GB / ~30 GB VRAM cards) or via the
  already-working remote-Ollama-over-ngrok path used for the 35B run.
- At least two independent orchestrators/hosts (CAI, mcphost; OpenClaude optionally as a third) so
  that model-attributable vs. orchestrator-attributable failures can be told apart — this is the one
  methodological non-negotiable, since the existing finding shows the two are conflated if only one
  host is tested.
- The hexstrike-ai MCP server as the tool surface (real, large, already integrated, already produced
  one documented failure taxonomy).
- Local, legally unambiguous, disposable targets: Metasploitable2, DVWA, and/or a small number of
  intentionally-vulnerable CTF-style VMs run on hardware we own/control. No third-party infrastructure,
  no HTB/live-internet targets.
- Quantitative metrics collected systematically across the model × orchestrator matrix (defined in
  `03-CONCLUSION.md` §3): tool-call success rate, hallucination rate, echo-vs-invoke rate, and (if
  RQ3 is attempted) false-positive completion rate with vs. without evidence-grounding.
- A written failure taxonomy with concrete examples (we already have one instance of this from the
  `ornith` run; the paper needs several more, systematically collected, not anecdotal).

## 4. Explicitly out of scope

- **Reproducing PentestGPT's Reasoning/Generation/Parsing architecture faithfully**, or its full
  benchmark suite. We reuse its *evidence-grounding idea*, not its module boundaries or its GPT-4
  dependency.
- **Any live, third-party, or unauthorized target.** Every experiment runs against infrastructure we
  own or a disposable local VM. This is a hosting/legal precaution, not a research-quality
  concession — it also makes the paper fully reproducible by anyone reading it.
- **Fine-tuning a model.** No compute budget for it, and it is a different (and much larger) research
  question than "how does an off-the-shelf small model behave in this loop."
- **Full CyberSecEval- or PentestGPT-Eval-scale benchmarking.** We may borrow individual task
  categories or scoring ideas from these, but standing up either benchmark suite in full is a
  multi-week effort on its own that would crowd out the actual novel contribution.
- **Claiming general "LLMs can/cannot pentest" conclusions.** Every claim in the paper is scoped to
  "models in the 7B–35B range, under these specific orchestrators, against this specific tool
  surface" — the paper's value is precision at this scale, not a sweeping verdict.
- **Novel jailbreak/dual-use capability elicitation.** We are measuring *reliability and grounding of
  tool use*, not attempting to elicit or publish new offensive capability. Anything resembling that
  is flagged out of scope per the CyberSecEval framing referenced in `../data/README - Purple LLama.md`.

## 5. Hard constraints

| Constraint | Detail | Implication |
|---|---|---|
| Compute | One GPU box: ~30 GB VRAM card + ~16 GB VRAM card. No frontier-model API budget assumed as the primary subject (may use one frontier model briefly as an upper-bound reference point only). | Model matrix capped at ~35B, mostly quantized; the 16 GB card is the practical ceiling for a fast local iteration loop (7B–20B), the 30 GB card unlocks heavier local models (up to ~34B in 4-bit) or the remote 35B path already validated. |
| Time | This is a "show progress now" checkpoint, not a finished submission. | The scope above is deliberately front-loaded with what's already partially done (RQ1/RQ2) so a credible progress report exists even if RQ3/RQ4 slip. |
| Ethics/authorization | No paid CTF ranges, no live/third-party hosts. | All targets local and disposable; this must be stated explicitly in the paper's Methodology, mirroring how the reference `docs-pentestgpt` re-implementation confines HTB execution to "the authorized remote attack box described in the parent project guide, never directly from the development [machine]." |
| Reproducibility | Every orchestrator/model/target combination must be re-runnable from the existing configs (`../MCPHost-modifed/mcp.json`, `../CAI-modified/agents.yml.example`, `../hexstrike-ai/hexstrike-ai-mcp.json`). | Findings files (`../findings/*.md`) are the paper's raw-data appendix; keep writing one per run, in the existing format, rather than only aggregate summaries. |

## 6. What "progress" means for this checkpoint

Given the above, a credible progress deliverable this week is:
1. This resource folder (scope, approaches, conclusion — done by this document set).
2. 2–4 more structured findings files answering RQ1/RQ2 more systematically (same model/orchestrator
   pairing that's already been run, plus at least one new model — see `03-CONCLUSION.md` §4 for the
   specific next runs).
3. A draft results table (model × orchestrator × metric) that can become Table 1 in the paper, even
   partially filled.

That is a legitimate, presentable unit of progress on a hard paper, without pretending the full
PentestGPT reproduction happened.
