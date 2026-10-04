# Multi-Agent Architecture — Red/Blue Team LLM Agent Graph

## 0. What this document is

`06-GPT-OSS-LLAMACPP-TOOLCALLING-FINDINGS.md` established that a single small open-weight model
(gpt-oss-20b), on the right serving stack (llama.cpp + `--jinja`), can drive a single ReAct
tool-calling loop reliably enough to do real work (live CVE lookups, MITRE ATT&CK lookups, cross-
verified against ground truth). This document is the next step: turning that one proven agent into
one node of a larger **multi-agent graph**, with dedicated red-team (offensive) and blue-team
(defensive) roles, plus cross-cutting agents that keep the whole system honest.

This is a **design document**, written before implementation, in the same spirit as
`02-APPROACHES.md` — it exists so the architecture is decided deliberately, on paper, before code is
written, and so it can be handed to an advisor/reviewer as-is. It assumes the reader has read
`01-SCOPE.md` (research questions), `03-CONCLUSION.md` (recommended approach), and
`06-GPT-OSS-LLAMACPP-TOOLCALLING-FINDINGS.md` (what already works).

It answers, per agent: **what is it responsible for, what must it never do, what tools/MCP servers
does it need, what does it read from and write to shared state, and how does it fit the paper's
research questions.**

---

## 1. Why a graph instead of one bigger agent

A single ReAct agent with all ~97-150 tools loaded at once (stealth-browser-mcp's 97 browser tools
plus hexstrike-ai's ~127-150 offensive-security CLI tools plus anything blue-team-specific) is exactly
the failure mode `../findings/ornith-1.0-35b-Q4_K_M-latest_2026-09-07_2317.md` already documented:
tool-namespace corruption, fabricated tool names, schema-echoing instead of invocation — and that was
with *one* tool server, not several combined. A 7B–35B model's tool-selection reliability degrades as
the number of simultaneously-visible tool schemas grows; splitting responsibility across specialist
agents, each with a small, focused tool surface, is a mitigation for the same root problem RQ1/RQ2
are studying, not just a software-engineering convenience.

This also maps directly onto **RQ3 (evidence-grounding)**: a dedicated Evaluator agent that
independently re-checks claims against raw tool output is the multi-agent-graph equivalent of the
`docs-pentestgpt` reference implementation's `compile_execution`/`audit.py` pattern — instead of one
function embedded in the loop, it is a first-class graph node other agents must pass through.

---

## 2. High-level graph

```
                              ┌────────────────────┐
                              │   Orchestrator      │◄────────────────────┐
                              │   (router)          │                     │
                              └─────────┬───────────┘                     │
                 ┌────────────┬─────────┼─────────┬────────────┐         │
                 ▼            ▼         ▼          ▼            ▼         │
        ┌────────────┐ ┌───────────┐ ┌────────┐ ┌──────────┐ ┌────────┐  │
        │  Recon /    │ │  Vuln     │ │Exploit/│ │  Attack  │ │  ...   │  │
        │  OSINT      │ │  Analysis │ │  PoC   │ │ Planning │ │ (blue) │  │
        │  (red)      │ │  (red)    │ │(red)   │ │  (red)   │ │        │  │
        └──────┬──────┘ └─────┬─────┘ └───┬────┘ └────┬─────┘ └───┬────┘  │
               │              │           │           │           │      │
               └──────────────┴─────┬─────┴───────────┴───────────┘      │
                                     ▼                                    │
                            ┌─────────────────┐                          │
                            │  Evaluator /     │                         │
                            │  Judge Agent     │─── verified? ───────────┘
                            └────────┬─────────┘
                                     │ rejected / needs redo
                                     ▼
                              back to Orchestrator
```

Blue-team agents (Threat Intel Correlation, Log/Alert Triage, Detection & Mitigation, Incident
Response) sit in the same position as the red-team box on the diagram above — the Orchestrator routes
to whichever specialist the current task needs, red or blue, and every specialist's output passes
through the same Evaluator before it is accepted into shared state. This symmetry is intentional: it
lets the paper report reliability metrics (RQ1/RQ2) for red-team and blue-team roles on an identical
harness, which is itself a paper-worthy comparison ("is a small LLM more reliable at defensive
triage than offensive planning, or vice versa?").

The **Safety/Guardrail Agent** is not on the main path — it is a side-channel check the Orchestrator
consults before dispatching any red-team specialist (see §6).

---

## 3. Shared state (the `StateGraph` state object)

All agents read/write a single shared `TypedDict` state, threaded through the graph the same way
`messages` is threaded through the existing single-agent scripts (4-6). Proposed shape:

```python
class GraphState(TypedDict):
    objective: str                    # the user's original request, verbatim
    mode: Literal["red", "blue", "auto"]  # which team's workflow this run is in
    messages: list[BaseMessage]       # full transcript, same role this plays in scripts 4-6
    target_scope: dict                # target identifiers (CVE ID, hostname, IOC, log excerpt, etc.)
    findings: list[Finding]           # accumulating structured findings, each tagged with source agent
    verified_findings: list[Finding]  # subset that passed the Evaluator
    attack_plan: AttackPlan | None    # populated by Attack Planning Agent
    mitigation_plan: MitigationPlan | None  # populated by Detection & Mitigation Agent
    next_agent: str | None            # set by Orchestrator's routing decision
    halted: bool                      # set by Safety/Guardrail Agent or circuit breaker
    halt_reason: str | None
```

`Finding` is a small structured record (not free text) so the Evaluator has something mechanical to
check, echoing the "structured task tree" idea from PentestGPT and the reference `MemoryKernel`
pattern in `docs-pentestgpt/codebase-understanding/UNDERSTANDING.md`:

```python
class Finding(TypedDict):
    source_agent: str
    claim: str                # e.g. "CVE-2026-9862 is CVSS 9.8 critical OS command injection"
    evidence_ref: str         # exact tool-call id / message id the claim must be traceable to
    evidence_excerpt: str     # verbatim substring of raw tool output supporting the claim
    confidence: Literal["verified", "unverified", "rejected"]
```

This is the mechanism that makes RQ3 measurable: **a claim only becomes `verified` after the
Evaluator agent confirms `evidence_excerpt` is an actual substring of the tool output referenced by
`evidence_ref`** — a deterministic check, not another LLM call, wherever possible (mirrors
`compile_execution`'s "verifiable, exact substring" rule from `01-SCOPE.md` RQ3).

---

## 4. Orchestrator / Coordinator Agent

**Responsibility.** Single entry point for a task. Reads `objective` and current `findings`, decides
which specialist agent runs next (`next_agent`), and decides when the overall task is complete
(routes to `END`). Also owns the top-level circuit breaker: if the same specialist is invoked more
than N times without new verified findings, it halts the run rather than looping forever (the
multi-agent analogue of the `MALFORMED_CALL_LIMIT` circuit breaker already in scripts 4-6).

**What it must never do.** Never calls external tools itself, never fabricates findings, never
bypasses the Evaluator by writing directly into `verified_findings`.

**Model.** Can be the *same* small model as the specialists (gpt-oss-20b) doing structured routing
via a constrained-output schema (`next_agent: Literal[...]`), which is itself a useful RQ1 data
point — routing is a simpler tool-call-shaped task than full tool-use, so it's a good "does the
model at least get the easy part right" baseline.

**MCP/tools needed.** None. Pure reasoning over `GraphState`. This keeps its own tool surface at
zero, minimizing exactly the failure class this whole design is trying to reduce.

**Implementation note.** In LangGraph terms this is the conditional-edge router function (comparable
to the `should_continue` routing already used inside the single-agent ReAct loops in scripts 4-6),
promoted to its own LLM-backed node because the routing decision here is open-ended (which of ~9
specialists) rather than binary (continue/stop).

---

## 5. Red team (offensive) agents

### 5.1 Recon / OSINT Web-Search Agent

**Responsibility.** Given a target scope (a vendor name, product, CVE ID, or domain), gather public
information: CVE records, vendor advisories, exposed-service fingerprints, related MITRE ATT&CK
techniques. This is the agent you already have working — scripts 4 (CVE-focused) and 5/6 (general
multi-site, Google-dorking, cited-sources) are direct implementations of this role.

**What it must never do.** Never treats search-result *snippets* as ground truth without opening the
source page (same discipline already built into scripts 4-6: cite only actually-navigated sites).
Never attempts authenticated access, login bypass, or any interaction beyond passive reading — recon
here is OSINT, not active exploitation (see Exploit/PoC agent for that boundary).

**MCP/tools needed.**
- A browser-automation MCP server: either `stealth-browser-mcp` (script 4/5's server, ~97 tools,
  `spawn_browser`/`instance_id`-based) or `cloakbrowser-mcp` (script 6's server, standard
  `@playwright/mcp` surface, `navigate`/`snapshot`/`ref`-based). Per `06-...FINDINGS.md`, script 6's
  transcript in `Langchain/Output/heretic_output_gpt_oss_20b_cve_mitreAttack_.txt` is currently the
  cleanest end-to-end run, so **cloakbrowser-mcp is the recommended default** for this agent, with
  stealth-browser-mcp kept as a documented alternative (its 97-tool surface — CDP execution, network
  capture, element cloning — is overkill for pure recon and is more likely to be the *source* of
  tool-selection noise, per the ornith findings' namespace-corruption pattern).
- Optionally the NVD REST API directly (`https://services.nvd.nist.gov/rest/json/cves/2.0`) as a
  plain HTTP tool for CVE ID lookups, bypassing the browser entirely when the ID is already known —
  script 4's `SYSTEM_PROMPT` already instructs preferring this route.

**Reads/writes to state.** Reads `target_scope`. Writes `Finding` records into `findings` (not yet
`verified_findings` — that requires the Evaluator).

### 5.2 Vulnerability Analysis Agent

**Responsibility.** Consumes recon `findings`, maps them onto CVE/CWE identifiers, and scores/ranks
them (CVSS base score, exploit maturity, whether a public PoC is known to exist) to decide what's
worth escalating to the Exploit/PoC and Attack Planning agents. This is a **reasoning-over-structured-
data** role, not a browsing role.

**What it must never do.** Never re-derives a CVSS score itself from prose description (models are
unreliable at this per general LLM-scoring literature) — it must extract the vendor/NVD-published
score verbatim from a recon `Finding`'s `evidence_excerpt`, and only flag "no published score found"
rather than inventing one.

**MCP/tools needed.** No browsing tools. A narrow toolset: a CVSS-vector parser/calculator tool
(deterministic, not LLM-based — parses a CVSS vector string into human-readable severity, so the
agent never has to compute severity itself), and optionally a CWE lookup tool (static local dataset,
no network needed — MITRE publishes CWE as downloadable XML/JSON).

**Reads/writes to state.** Reads `findings` (recon output). Writes new `Finding`s of its own
(`claim` = severity/priority assessment, `evidence_ref` = the recon finding it's based on).

### 5.3 Exploit/PoC Discovery Agent

**Responsibility.** For a vulnerability the Vulnerability Analysis Agent has prioritized, search for
publicly documented exploitation details: PoC code (Exploit-DB, GitHub advisories, vendor security
bulletins), and map the technique to MITRE ATT&CK (as already demonstrated for T1595.001 in script
6's transcript).

**What it must never do.** Never executes discovered PoC code — this agent is discovery/mapping
only, strictly read-only browsing, same as Recon. Actual execution (if ever in scope, which
`01-SCOPE.md` §4 currently rules out against anything but disposable local VMs) would be a
*different*, explicitly-gated agent, not this one.

**MCP/tools needed.** Same browser MCP server as Recon (cloakbrowser-mcp recommended) — this agent
is architecturally a specialized Recon agent with a narrower prompt/objective, and could in practice
share the Recon agent's tool wiring, differing only in system prompt and the schema of `Finding` it
emits (`claim` describes an exploit technique, not just a vulnerability description).

**Reads/writes to state.** Reads prioritized `findings` from Vulnerability Analysis. Writes
`Finding`s tagged with ATT&CK technique IDs where identifiable.

### 5.4 Attack Planning Agent

**Responsibility.** Chains recon + vulnerability + exploit findings into an ordered plan —
effectively a kill-chain — referencing MITRE ATT&CK tactics/techniques at each step. Populates
`attack_plan` in state. This is the closest analogue to PentestGPT's "Reasoning module" (task-tree
construction) from `01-SCOPE.md` §1, but scoped to *planning only*, not live command generation
against a target (that would require the out-of-scope live-target execution loop from RQ4).

**What it must never do.** Never claims a step "worked" — this agent produces a *plan*, and every
step must cite which `verified_findings` it's grounded in; steps with no supporting finding must be
explicitly labeled `(unverified / hypothetical)`.

**MCP/tools needed.** None required for the planning step itself, but should have a read-only ATT&CK
technique lookup tool (local MITRE ATT&CK STIX/JSON dataset — no network dependency, faster and more
reliable than repeated live `attack.mitre.org` browsing for something as structured as tactic/technique
metadata) to avoid re-scraping the same reference site the Recon agent may have already visited.

**Reads/writes to state.** Reads `verified_findings`. Writes `attack_plan`.

---

## 6. Blue team (defensive) agents

### 6.1 Threat Intel Correlation Agent

**Responsibility.** The defensive mirror of Recon: given an indicator (IOC, CVE ID, ATT&CK technique,
or something surfaced by Log/Alert Triage), pulls in "is this being actively exploited" context —
CISA KEV (Known Exploited Vulnerabilities) list, vendor advisories, threat-intel blog coverage.

**MCP/tools needed.** Same browser MCP server as Recon (cloakbrowser-mcp), plus a dedicated CISA KEV
feed tool (`https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` —
a stable, structured, machine-readable feed, so this specific lookup should be a plain HTTP tool
rather than a browse-and-scrape task, for the same reliability reasons the NVD REST API is preferred
over browsing NVD's HTML pages in §5.1).

**Reads/writes to state.** Symmetric to Recon: writes `Finding`s, tagged `source_agent:
"threat_intel"`.

### 6.2 Log/Alert Triage Agent

**Responsibility.** Ingests a batch of log lines or alert records (provided by the user, or in a
later experiment, generated by a controlled local test harness — never live production logs), flags
anomalous entries, and correlates them against known ATT&CK techniques where a pattern matches (e.g.
a spike of failed logins → credential-access technique).

**What it must never do.** Never claims a log entry represents a specific technique without quoting
the exact log line(s) it's basing that on in `evidence_excerpt` — this is the blue-team analogue of
"never claim a page said something a tool result doesn't show," already a hard rule in scripts 4-6's
`SYSTEM_PROMPT`s.

**MCP/tools needed.** No browsing needed for the core triage step. A local log-parsing tool
(regex/structured-field extraction — deterministic, not LLM-based, for the actual parsing; the LLM's
job is judgment about what's anomalous, not string extraction) and optionally the same ATT&CK lookup
tool as the Attack Planning Agent, for technique correlation.

**Reads/writes to state.** Reads `target_scope` (the log excerpt supplied for this run). Writes
`Finding`s describing detected anomalies.

### 6.3 Detection & Mitigation Agent

**Responsibility.** Given a `verified_finding` (a vulnerability, technique, or triaged anomaly),
proposes concrete detections (e.g. a Sigma rule sketch, a log field/pattern to alert on) and
mitigations (patch version, config change, compensating control), ideally referencing MITRE D3FEND
countermeasure categories the way the Attack Planning Agent references ATT&CK tactics.

**MCP/tools needed.** A local D3FEND dataset lookup tool (same rationale as the local ATT&CK dataset
— structured reference data, no need to re-browse it live). No browser tool required unless the
mitigation requires confirming a specific vendor patch version, in which case it can call the same
Recon/browser tool the red-team side uses (this is a legitimate case for tool-sharing across the
red/blue boundary, since "find the vendor's official patch advisory" is the same *kind* of task
regardless of which team asked for it).

**Reads/writes to state.** Reads `verified_findings`. Writes `mitigation_plan`.

### 6.4 Incident Response Agent

**Responsibility.** Once a finding is flagged as active/exploited (e.g. corroborated by Threat Intel
Correlation against CISA KEV), drafts a response/remediation runbook — ordered containment,
eradication, recovery steps — grounded in the `mitigation_plan` and `verified_findings`.

**MCP/tools needed.** None required — this is a synthesis/writing role over already-verified state,
comparable to the Attack Planning Agent's role on the red-team side. No new external tool surface.

**Reads/writes to state.** Reads `verified_findings` and `mitigation_plan`. Writes the final runbook
into `messages` as the terminal output of a blue-team run.

---

## 7. Cross-cutting agents

### 7.1 Evaluator / Judge Agent

**Responsibility.** The mechanism that makes RQ3 real. Every `Finding` any specialist produces passes
through this agent before it is promoted from `findings` to `verified_findings`. Two-tier check:

1. **Deterministic check first** (no LLM call): does `evidence_excerpt` appear as a literal substring
   of the actual tool-output message referenced by `evidence_ref` in `messages`? If not, immediately
   `confidence: "rejected"` — this is pure string matching, exactly mirroring
   `docs-pentestgpt/codebase-understanding/UNDERSTANDING.md`'s `compile_execution` pattern, and it is
   the cheapest, most reliable anti-hallucination check available (no model call needed to catch
   fabricated evidence).
2. **LLM judgment second**, only for excerpts that pass step 1: does the `claim` actually follow from
   the `evidence_excerpt` (not just quote real text, but draw a correct conclusion from it)? This step
   uses the LLM because "is this a fair reading of this text" is not mechanically checkable, but it
   only ever runs on already-substring-verified evidence, narrowing the LLM's job to judgment rather
   than fact-retrieval.

**What it must never do.** Never approves a `Finding` whose `evidence_ref` doesn't resolve to a real
message in `messages`. Never modifies `claim` or `evidence_excerpt` itself — it only accepts or
rejects, so there's no path for the Evaluator itself to introduce a hallucination into the record.

**MCP/tools needed.** None beyond read access to `messages` (already in shared state, no separate
tool call required). This is deliberately the "no tools" agent in the graph, alongside the
Orchestrator — the two nodes whose entire job is judging/routing rather than acting.

**Metrics this directly produces for the paper.** False-positive completion rate (RQ3): fraction of
specialist-emitted `Finding`s that get `rejected` at step 1 vs. step 2, broken down by which
specialist and which model produced them — this is a table-ready number, comparable across the
model/orchestrator matrix already defined in `03-CONCLUSION.md` §3.

### 7.2 Safety / Guardrail Agent

**Responsibility.** A pre-dispatch check the Orchestrator consults before routing to any red-team
specialist: is the current `objective`/`target_scope` within the stated scope from `01-SCOPE.md` §3-4
(local/disposable targets only, no live third-party infrastructure, no PoC execution)? If not, sets
`halted: True` with a `halt_reason` instead of letting the Orchestrator dispatch.

**Why this matters for the paper specifically.** This agent is the natural place to run the
comparison the Heretic/abliteration work (`Langchain/Output/heretic_output_gpt_oss_20b_cve_mitreAttack_.txt`
being the un-abliterated baseline transcript) is building toward: run the *same* red-team workflow
with (a) the stock gpt-oss-20b and (b) an abliterated variant produced via Heretic on the HPC H200
node, and measure whether the Safety/Guardrail Agent's refusal/flag rate changes — a directly
measurable, paper-worthy data point about how guardrail removal affects a multi-agent pipeline's
own internal safety layer, as distinct from the underlying model's chat-level refusals.

**What it must never do.** It is not itself a content filter on model *output* prose (that's a much
harder, separate problem) — its job is scoped and mechanical: checking `target_scope` against an
allow-list of local/disposable hosts and a deny-list of action types (exploit execution, credential
use, live external targets), not judging arbitrary text.

**MCP/tools needed.** None — a rules/allow-list check against `target_scope`, implementable without
any LLM call at all for the common case (pure Python validation), with an LLM fallback only for
ambiguous natural-language objectives that don't cleanly parse into a structured `target_scope` yet.

**Reads/writes to state.** Reads `objective`, `target_scope`. Writes `halted`, `halt_reason`.

---

## 8. MCP servers — consolidated inventory

| MCP server / tool source | Used by | Status |
|---|---|---|
| `cloakbrowser-mcp` (`@playwright/mcp` surface, `navigate`/`snapshot`/`ref`) | Recon/OSINT, Exploit/PoC Discovery, Threat Intel Correlation, (optionally) Detection & Mitigation | **Working** — script 6, cleanest transcript so far. |
| `stealth-browser-mcp` (97 tools, `spawn_browser`/`instance_id`) | Same roles as above, documented alternative | **Working but noisier** — scripts 4-5; kept as a comparison point for RQ1/RQ2, not the default going forward. |
| NVD REST API (`services.nvd.nist.gov/rest/json/cves/2.0`) | Recon/OSINT (CVE-ID-known fast path), Vulnerability Analysis | **Working** — already used/validated in script 4. |
| CISA KEV JSON feed | Threat Intel Correlation | **Not yet built** — plain HTTP GET + JSON filter, no LLM/browser needed. |
| Local MITRE ATT&CK STIX/JSON dataset + lookup tool | Exploit/PoC Discovery, Attack Planning, Log/Alert Triage | **Not yet built** — download once, query locally; avoids re-scraping `attack.mitre.org` for structured data already proven reachable in script 6. |
| Local MITRE D3FEND dataset + lookup tool | Detection & Mitigation | **Not yet built.** |
| CVSS vector parser (deterministic) | Vulnerability Analysis | **Not yet built** — trivial, existing open-source parsers available. |
| Local CWE dataset lookup | Vulnerability Analysis | **Not yet built**, optional. |
| Log parsing tool (regex/field extraction, deterministic) | Log/Alert Triage | **Not yet built** — scope depends on what log format the eventual experiment uses (must be synthetic/local per `01-SCOPE.md` §4). |
| `hexstrike-ai` MCP server (~127-150 offensive CLI tools: nmap, sqlmap, nuclei, ghidra, trivy, rustscan, …) | **Not assigned to any agent above yet** | Reserved for a future, explicitly-gated "Active Testing Agent" if/when RQ4 (live disposable-target execution) is attempted — deliberately **not** wired into Recon/Exploit-Discovery/Attack-Planning, since those three are scoped to passive OSINT/planning only per §5. Introducing hexstrike-ai's live-execution tools is a scope escalation that must go through the Safety/Guardrail Agent's allow-list and `01-SCOPE.md`'s local-disposable-target constraint explicitly, not be bundled into agents designed for read-only work. |

The Evaluator, Orchestrator, and Incident Response agents intentionally have **no MCP tool surface at
all** — this is a design choice, not an oversight: keeping the "judgment" and "synthesis" roles
tool-free is itself part of the reliability story, since every prior finding in this project traces
tool-selection noise back to having *too many* tools visible to one reasoning step.

---

## 9. Data flow walkthrough (worked example)

To make §3–§7 concrete, here is one full run through the graph for a plausible research-paper
experiment prompt: *"Investigate CVE-2026-9862 and tell me if we should be worried."*

1. **Orchestrator** parses the objective, sets `mode: "red"` (this is fundamentally an offensive-
   intel-gathering request), sets `target_scope = {"cve_id": "CVE-2026-9862"}`, routes to
   **Safety/Guardrail**.
2. **Safety/Guardrail** checks `target_scope` — a CVE lookup against public NVD data is unambiguously
   in-scope (no live target, no execution). Clears it; `halted` stays `False`.
3. **Orchestrator** routes to **Recon/OSINT**. It calls the NVD REST API fast path (CVE ID already
   known), gets the CVSS 9.8 / OS-command-injection record (same data already captured live in
   script 6's transcript), and writes a `Finding` with `evidence_ref` pointing at that tool result.
4. **Evaluator** checks the `Finding`: `evidence_excerpt` is a literal substring of the NVD JSON
   response → passes step 1. LLM judgment step confirms the claim ("CVSS 9.8 critical") matches what
   the excerpt says → `confidence: "verified"`. Promoted to `verified_findings`.
5. **Orchestrator** routes to **Vulnerability Analysis**. It reads the verified CVSS vector, parses
   severity deterministically (no re-scoring), and writes a priority `Finding` ("critical, remotely
   exploitable, no auth required — high priority").
6. **Evaluator** verifies this second finding the same way, promotes it.
7. **Orchestrator** decides the objective ("should we be worried") is answerable from
   `verified_findings` already in hand and does **not** need Exploit/PoC Discovery or Attack Planning
   for this particular question — routes straight to `END` with a synthesized answer built only from
   `verified_findings`.
8. Final answer to the user cites both verified findings by their `evidence_ref`, exactly like
   script 4/6's existing "only cite actually-navigated/verified sources" discipline, now enforced
   structurally by the graph rather than only by system-prompt instruction.

A blue-team-flavored variant of the same objective ("we're seeing failed BoKS autoregistration
attempts in our logs, should we be worried") would instead route: Orchestrator → Safety/Guardrail →
**Log/Alert Triage** (flags the anomaly, correlates to CVE-2026-9862 if the log pattern matches) →
**Threat Intel Correlation** (checks CISA KEV — is this CVE known to be actively exploited in the
wild right now) → Evaluator (verifies both) → **Detection & Mitigation** (proposes a detection rule
+ patch recommendation) → **Incident Response** (drafts the runbook) → END.

---

## 10. Mapping back to the research questions

| RQ (from `01-SCOPE.md`) | How this architecture addresses it |
|---|---|
| RQ1 (reliability) | Each specialist's tool-call success rate can now be measured *per role*, not just per model/orchestrator pair — a finer-grained version of the existing metric, and it directly tests whether narrowing an agent's tool surface (per §1's motivation) measurably improves reliability versus the flatter single-agent scripts 4-6. |
| RQ2 (failure taxonomy) | The Evaluator's rejection reasons (step 1 substring failure vs. step 2 judgment failure) give a structured, automatic failure taxonomy for free, instead of hand-curated findings files. |
| RQ3 (evidence-grounding) | This is what §7.1 is *for* — the false-positive completion rate the Evaluator produces is a direct, quantitative answer to RQ3, generalized from a single-loop mechanism to a graph-wide one. |
| RQ4 (task-tree progression, stretch) | The Attack Planning Agent's `attack_plan` gives an observable stopping point ("planning got to step N of the kill chain before running out of verified findings to build on") even without ever executing against a live target — a safer, in-scope proxy for RQ4 that doesn't require the disposable-VM execution loop `01-SCOPE.md` currently treats as a stretch goal. |
| New: Heretic/abliteration comparison | §7.2's Safety/Guardrail Agent gives a clean, measurable hook for comparing stock vs. abliterated model behavior *inside* a controlled multi-agent pipeline, rather than only at the raw chat-completion level — this is a natural extension of the paper's scope that the single-agent scripts couldn't cleanly measure. |

---

## 11. Open questions / not yet decided

- **One model for all agents, or role-specialized models?** The simplest starting point is the same
  gpt-oss-20b instance behind every agent (different system prompts, same weights) — this isolates
  *architecture* effects from *model* effects, which is the cleaner experiment for a first pass. A
  follow-up experiment could swap in a smaller/cheaper model for the "judgment-only" agents
  (Orchestrator, Evaluator) to test whether routing/verification needs less capacity than
  specialist tool-use — that's a `04-MODEL-SPECIALIZATION.md`-flavored question, not answered here.
- **Shared vs. per-agent MCP server processes.** Running one long-lived `cloakbrowser-mcp` process
  shared across Recon/Exploit-Discovery/Threat-Intel (sequential access, one browser context) avoids
  the orphaned-Chromium-process problem `run_cloak_agent.sh` already had to work around, but means
  those three agents cannot literally run concurrently without a second browser instance/profile.
  For a first implementation, sequential (Orchestrator dispatches one specialist at a time) is
  simpler and matches how `create_react_agent`-based scripts 4-6 already operate.
- **Where does hexstrike-ai's active-tooling surface plug in, if RQ4 is attempted for real?** Per §8,
  deliberately left unassigned in this version of the architecture — needs its own design pass
  (probably a gated "Active Testing Agent," reachable only via an explicit Safety/Guardrail approval
  step) once/if RQ4 moves from stretch goal to active work.
- **Persistence across runs.** This document specifies in-memory `GraphState` for a single run/
  session, matching current scripts. The reference `docs-pentestgpt` implementation's SQLite
  `MemoryKernel` (durable, crash-recoverable state) is the natural next step if experiments need to
  span multiple sessions or survive a server crash — not required for the first working version of
  this graph.
