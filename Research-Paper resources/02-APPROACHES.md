# Approaches

Every option below is anchored to a real reference (either a paper in `../papaers/` or an
architecture/codebase write-up in `../data/`) plus our own existing infrastructure and findings. Each
gets: what it is, the reference it's based on, feasibility on our GPU (one ~30 GB card + one ~16 GB
card, open-weight models), pros, cons, and a verdict. The recommended combination is assembled in
`03-CONCLUSION.md`.

---

## A1 — Faithful PentestGPT reproduction

**What it is:** Re-implement (or reuse) PentestGPT's three-module Reasoning/Generation/Parsing
architecture exactly, run it against HTB/VulnHub machines with a human relaying commands, and
reproduce its benchmark.

**Reference:** `papaers/usenixsecurity24-deng.pdf` directly; `../data/docs-pentestgpt/architecture.md`
confirms even the paper's own follow-on team eventually rebuilt this as `pentestgpt_legacy/` — "the
maintained **human-driven** implementation of the USENIX 2024 workflow" — explicitly kept separate
from their newer autonomous framework.

**Feasibility:** Low. PentestGPT's own architecture was designed and evaluated around GPT-4-class
reasoning; the paper's evaluation window spanned real HTB machines over an extended period with a
human operator present for every command. We have neither the model tier nor the time budget nor
(without paid HTB access) the target infrastructure.

**Pros:** Direct comparability to the original paper's numbers; well-trodden path with an existing
prompt design to borrow from.

**Cons:** Requires a human in the loop for every run (defeats the "autonomous small-model" angle we
actually have data for); requires GPT-4-tier reasoning to get any signal at all — running it with a
7B–35B model would likely just produce a second, less rigorous version of the failure data we
*already have* from `../findings/`; requires live target infra we don't have authorized access to.

**Verdict: Rejected as the primary approach.** Its core idea (task-tree state + evidence-grounded
task completion) is reused — see A6 — but not its module boundaries, its model tier, or its
human-in-the-loop requirement.

---

## A2 — Systematic reliability/failure-taxonomy study on existing infrastructure (empirical)

**What it is:** Formalize what has already been done once (the `ornith` run) into a repeatable
protocol: fix a set of models, a set of orchestrators, and a fixed MCP tool server; run the same
battery of tool-listing and tool-invocation prompts through every combination; record and classify
every failure.

**Reference:** Our own `../findings/ornith-1.0-35b-Q4_K_M-latest_2026-09-07_2317.md`; methodologically
closest published work is `papaers/s10664-025-10758-3.pdf` (Happe, Kaplan, Cito, "LLMs as Hackers:
Autonomous Linux Privilege Escalation Attacks") — a single-machine-scope, pass/fail-per-technique
empirical study explicitly designed around what's practically measurable, not around a specific
model tier.

**Feasibility:** High — this is a continuation of work already running (`../CAI-modified/`,
`../MCPHost-modifed/`, `../hexstrike-ai/` are already wired together and have already produced one
findings file). Requires only more systematic repetition plus 1–2 additional models pulled locally
(e.g. gpt-oss-20b on the 16 GB card).

**Pros:** Lowest risk, fastest path to a results table; directly extends work that already exists;
produces genuinely novel data (no reference system already does a controlled orchestrator × model ×
tool-server comparison at this scale — AutoPentest, PentestGPT's re-implementation, and
HackingBuddyGPT each fix their own single orchestrator/model stack rather than comparing across
them).

**Cons:** By itself it's a measurement study with no working end-to-end demonstration — reviewers may
ask "so what should someone do instead," which A6 (below) answers.

**Verdict: Adopted as the paper's empirical backbone (answers RQ1/RQ2).**

---

## A3 — LangGraph planner/supervisor/specialist-worker architecture (AutoPentest-style)

**What it is:** Build our own version of the planner → supervisor → N domain-specialist-worker loop
(one worker per OWASP Top-10 category or similar), each with its own tool subset and optionally RAG
over reference docs.

**Reference:** `../data/docs-autopentestgpt/ARCHITECTURE.md` in full detail — LangGraph `StateGraph`
with `plan_step`/`supervise`/8 task-specific-agent nodes/`replan_step`, Pinecone RAG per agent, CVE
lookup tools, shell tools gated by an environment-variable human-approval switch.

**Feasibility:** Medium. The architecture itself is buildable on our stack (LangGraph or a
hand-rolled equivalent over CAI), but its documented weaknesses are exactly the kind of thing a
smaller/weaker model would make worse, not better: `past_steps` grows unbounded and is resent in
full to every worker (context-length pressure that a 7B model's smaller context window would hit
much sooner than GPT-4); the planner/supervisor/replanner path is fragile (one retry, then a hard
crash on any LLM/API error) — this is a real risk with less-reliable small models producing more
malformed structured output, not less.

**Pros:** A genuinely different architectural family from PentestGPT's flat two-role loop — useful if
we want to test whether the *specialist-worker decomposition* itself changes reliability (a smaller
model doing one narrow OWASP-category task might be more reliable than the same model doing an
undifferentiated "just pentest this" task).

**Cons:** Meaningfully more engineering effort than A2 for a currently-secondary research question;
its documented single-retry-then-crash orchestration would need hardening before it could survive a
multi-hour run with a less reliable model, which is itself extra unplanned work.

**Verdict: Deferred to future work**, but worth **1 exploratory run** if time allows after RQ1–RQ3 are
covered, specifically to test whether task decomposition (many narrow specialist calls) changes the
tool-hallucination rate compared to A2's single generalist loop — this would be a nice discussion-
section data point even as an n=1 anecdote.

---

## A4 — HackingBuddyGPT-style narrow-scope single-technique study

**What it is:** Instead of a broad "pentest this box" mission, narrow to one well-defined technique
class (e.g. Linux local privilege escalation, matching HackingBuddyGPT/Happe et al. exactly) with a
clean pass/fail signal per attempt, across many runs, for statistical power.

**Reference:** `../data/docs - HackingBuddyGPT/index.md` (pointer to the public docs) and directly
`papaers/s10664-025-10758-3.pdf`.

**Feasibility:** High technically, but this paper already exists and covers exactly this scope with
(presumably, pending our own read of the full paper) a broader model sweep than we can match. Doing
the same experiment on the same technique class would be a replication, not a novel contribution.

**Pros:** Cleanest possible evaluation methodology (binary success signal, easy statistics); directly
citable/comparable numbers.

**Cons:** Narrower than our actual assets (hexstrike-ai's ~150 tools cover far more than privesc);
duplicates rather than extends existing published work; doesn't use our most interesting existing
data (the multi-orchestrator MCP comparison, which privesc-only scope wouldn't naturally surface).

**Verdict: Reused only as a methodology template** (their pass/fail-per-attempt rigor is worth
copying for RQ4's task-tree-progression metric), **not as the paper's scope**.

---

## A5 — Full CyberSecEval / PentestGPT-Eval-style benchmark suite

**What it is:** Stand up an established benchmark (Meta's CyberSecEval or PentestGPT's own eval set)
in full and report our models' scores against its published leaderboard baselines.

**Reference:** `../data/README - Purple LLama.md` (CyberSecEval v1–v3); PentestGPT's own benchmark as
described in `papaers/usenixsecurity24-deng.pdf`. Also directly relevant: `../CAI-modified/benchmarks/`
already contains `cybermetric/`, `cti_bench/`, `seceval/`, `cyberPII-bench` harnesses ready to run.

**Feasibility:** Medium-high for the *already-vendored* CAI benchmarks (`cybermetric`, `seceval`,
`cti_bench`) since the harness exists in our own tree already; low for standing up CyberSecEval or
PentestGPT-Eval from scratch, which is its own multi-week integration effort.

**Pros:** Instant comparability to published leaderboard numbers for cybersecurity *knowledge*
(cybermetric/seceval are largely knowledge-QA-style, not live tool-use); zero new infrastructure
needed for the CAI-vendored suites.

**Cons:** Knowledge-benchmark scores (can the model answer security questions correctly) are a
different construct from what our paper is actually about (can the model *drive tools* correctly in
a live loop) — a high cybermetric score doesn't predict a low tool-hallucination rate, and conflating
the two would weaken the paper's central claim rather than strengthen it.

**Verdict: Adopted only as a lightweight, cheap supplementary result** — running each candidate model
through the already-integrated `cybermetric`/`seceval` harnesses (a few hours, no new code) gives a
useful "does this model even have baseline security knowledge" control variable to report alongside
the live tool-use numbers, contextualizing e.g. whether a model's poor tool-calling is compounded by
also lacking domain knowledge. **Not** a substitute for the live-tool-use study (A2).

---

## A6 — Evidence-grounding wrapper layer (PentestGPT re-implementation's core idea, ported down)

**What it is:** Add a deterministic verification layer between "the model claims a task is done /
found something" and "the system records that as true" — modeled directly on the reference
re-implementation's `compile_execution`: a claimed result is only accepted as `DONE` if it is an
exact, verifiable substring of real tool/command output; anything softer (paraphrase, no receipt, a
fallback/truncated match) is recorded as mere `PROGRESS`, never `DONE`.

**Reference:** `../data/docs-pentestgpt/codebase-understanding/UNDERSTANDING.md`, the entire
`execution.py`/`memory.py` breakdown — specifically the cascade of exact/widened/unique-line/
cross-receipt matching strategies, the "outcome downgrade rule" (a claimed DONE with only fallback
evidence is silently downgraded to PROGRESS), and the independent read-only `audit.py` re-verifier
that never trusts the same code path that produced the state.

**Feasibility:** High for a *minimal* version. We do not need the full `MemoryKernel`/SQLite/
crash-recovery machinery (that solves a production-reliability problem we don't have at our scale) —
we need only the core predicate: "is the model's claimed finding/completion a literal substring of
an actual tool-output receipt captured in this run's log?" This is a small, self-contained checker we
can run as a post-hoc pass over our own trace logs (we already capture raw logs — see
`../mcphost_raw1.log`, `../pty_session*.log` etc. in the parent directory), or inline as a lightweight
gate in CAI's own hook/tool layer.

**Pros:** Turns RQ1/RQ2's raw failure-rate numbers into a paper's actual methodological contribution
(RQ3): "here is a cheap, model-agnostic technique that catches X% of a small model's false
completion claims without needing a bigger model." This is the single highest-leverage piece of
engineering in this whole document — small effort, directly reuses a well-designed reference
mechanism, and produces the paper's most citable result.

**Cons:** Requires care to port correctly — the reference implementation's matching cascade
(newline-normalization, ordered multi-line matching, unique-line envelopes, cross-receipt
projection) exists specifically to avoid two failure modes of a naive "does the string appear
anywhere" check: false negatives (rejecting a real quote just because of trivial reformatting) and
false positives (accepting a coincidental substring match). A naive implementation could quietly
introduce either.

**Verdict: Adopted — this is RQ3, and it is the paper's main methodological contribution.**

---

## A7 — Human-in-the-loop supervised mode as a safety/ablation variant

**What it is:** Add an approval gate before any tool invocation with side effects (matching the
`HUMAN_INPUT_FOR_COMMAND_EXECUTION` pattern in AutoPentest, or the `interrupt()`/resume pattern in the
LangGraph HITL email-assistant reference), and compare autonomous vs. human-gated runs.

**Reference:** `../data/docs-autopentestgpt/ARCHITECTURE.md` §8 ("Human-in-the-loop gating");
`../data/docs-Langchain-custom-agent/CODEBASE_UNDERSTANDING.md` §2 (the `interrupt()`/`Command(resume=...)`
pattern, with its own documented caveat that the framework's checkpoint/resume internals aren't fully
verifiable by reading the repo alone).

**Feasibility:** High as a small toggle, since our targets are local/disposable and low-stakes
either way.

**Pros:** Directly useful for the paper's ethics/safety framing (Purple Llama's CyberSecEval angle,
`../data/README - Purple LLama.md`) — "would a human-approval gate have caught this specific
hallucinated/dangerous tool call" is an easy, concrete question to answer post-hoc against logs we
already have.

**Cons:** Not a core research question (RQ1–RQ4 don't require it); adds a second axis to the
experiment matrix that could dilute focus if over-invested in.

**Verdict: Adopted only as a short discussion-section analysis** — reviewing existing/new trace logs
and reporting how many of the observed hallucinated tool calls *would* have been caught by a human
approval gate, without building a full interactive HITL system.

---

## A8 — CALDERA-based adversary-emulation scoring instead of a bespoke task tree

**What it is:** Use MITRE CALDERA's existing ability/adversary-profile structure as the ground-truth
"task tree" / ATT&CK-technique checklist that a model's autonomous run is scored against, instead of
inventing our own task taxonomy.

**Reference:** `../caldera/` (already present, MITRE's own adversary emulation platform).

**Feasibility:** Medium — CALDERA is designed for orchestrating its own agents (implants) executing
predefined abilities, not for scoring an external LLM-driven tool-calling loop; adapting it to that
role is extra integration work, though its ATT&CK-technique taxonomy is directly reusable as a
*scoring rubric* even without running CALDERA's own agents.

**Pros:** Gives RQ4 (task-tree progression) a standardized, ATT&CK-mapped vocabulary instead of an
ad-hoc one — "the model reached T1046 (Network Service Discovery) and T1210 (Exploitation of Remote
Services) but never T1068 (Privilege Escalation)" is more legible to a security-research audience
than a bespoke stage list.

**Cons:** Full CALDERA integration (running it as the actual orchestration engine) is more machinery
than RQ4 needs; the taxonomy alone is easy to borrow, running the platform itself is not necessary.

**Verdict: Adopted partially** — borrow CALDERA's ATT&CK-technique labels as the vocabulary for
RQ4's task-tree-progression metric; do not attempt to make CALDERA the orchestration engine.

---

## Summary comparison

| # | Approach | Reference basis | Feasibility (our GPU/time) | Verdict |
|---|---|---|---|---|
| A1 | Faithful PentestGPT reproduction | `usenixsecurity24-deng.pdf`, `docs-pentestgpt/architecture.md` | Low | Rejected as primary; idea reused via A6 |
| A2 | Systematic reliability/failure-taxonomy study | Our own `findings/`, `s10664-025-10758-3.pdf` | High | **Adopted — RQ1/RQ2 backbone** |
| A3 | LangGraph planner/supervisor/specialist-workers | `docs-autopentestgpt/ARCHITECTURE.md` | Medium | Deferred; 1 exploratory run if time allows |
| A4 | Narrow single-technique study (privesc-only) | `docs - HackingBuddyGPT/`, `s10664-025-10758-3.pdf` | High | Methodology reused, scope not adopted (replication risk) |
| A5 | Full benchmark suite (CyberSecEval/PentestGPT-Eval) | `README - Purple LLama.md`, `CAI-modified/benchmarks/` | Medium-high (vendored subset) | Adopted as cheap supplementary control variable only |
| A6 | Evidence-grounding wrapper layer | `docs-pentestgpt/codebase-understanding/UNDERSTANDING.md` (`execution.py`/`memory.py`) | High (minimal port) | **Adopted — RQ3, the paper's methodological contribution** |
| A7 | Human-in-the-loop ablation | `docs-autopentestgpt` §8, `docs-Langchain-custom-agent` §2 | High | Adopted as a short discussion-section analysis only |
| A8 | CALDERA/ATT&CK-based scoring vocabulary | `../caldera/` | Medium | Adopted partially — taxonomy only, not the engine |

`03-CONCLUSION.md` assembles A2 + A6 (+ A5, A7, A8 as supporting pieces) into the final recommended
paper structure and roadmap.
