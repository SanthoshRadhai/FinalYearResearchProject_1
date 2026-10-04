# MCP Implementation Options — Sourcing Prebuilt Servers for the Multi-Agent Architecture

## 0. What this document is

`07-MULTI-AGENT-ARCHITECTURE.md` §8 listed a consolidated MCP-server inventory and marked most rows
"Not yet built." Before building anything from scratch, this document surveys what already exists
in the open-source/MCP-registry ecosystem for each row, so the implementation plan reuses vetted
prebuilt tools wherever a reasonable one exists, and only custom-builds the gaps.

**Method note (read before trusting this document's "community opinion" claims):** web search
surfaced abundant blog/directory content (LobeHub, PulseMCP, mcpservers.org, Glama.ai, awesome-lists)
but did **not** surface any specific, findable Reddit threads directly comparing these tools —
searches for `reddit.com` + MCP security/browser topics returned MCP directory pages, not actual
Reddit discussion threads. Where this document says "well-regarded" or "widely listed," that is based
on GitHub star counts, curated awesome-lists, and repeated independent listing across multiple
directories — not verified firsthand user sentiment from Reddit or other social platforms. This
caveat should be stated in the paper too if this survey is cited: **absence of evidence of poor
reception is not the same as positive community consensus**, especially for single-maintainer
security-tool repos with no visible download/star-count signal in the search results.

**Standing risk, independent of which specific tool is picked:** every third-party MCP server here
is unaudited code from an unknown maintainer, running with your credentials/network access. General
MCP-security writeups surfaced this repeatedly (tool poisoning via malicious tool metadata, "rug
pulls" where a tool's behavior silently changes after install, server spoofing). Before wiring any
of these into the actual experiment, each candidate should at minimum be read end-to-end (not just
`pip install`ed) and ideally run through a scanner like Ramparts, per the general guidance surfaced
in search. This is a hard requirement for the paper's own credibility — "we ran unaudited third-party
code with live network access as part of a security research pipeline" is a finding that needs to be
disclosed and mitigated, not glossed over.

---

## 1. Candidates per capability

### 1.1 Browser automation (Recon/OSINT, Exploit/PoC Discovery, Threat Intel Correlation)

| Option | What it is | Pros | Cons |
|---|---|---|---|
| **`cloakbrowser-mcp`** (already in use, script 6) | Wraps upstream `@playwright/mcp` unchanged, pointed at CloakBrowser Chromium (anti-detection fork) | **Already working** — cleanest transcript in the project so far (`Langchain/Output/heretic_output_gpt_oss_20b_cve_mitreAttack_.txt`); standard Playwright MCP tool surface is well-documented and widely used, so the model has presumably seen more of this API shape in training data than a bespoke tool surface | Anti-detection claims are the vendor's own, not independently verified in this project |
| `stealth-browser-mcp` (already in use, scripts 4-5) | Custom 97-tool server, `spawn_browser`/`instance_id` model | Already integrated; very deep tool surface (CDP execution, network capture, element cloning) if a future agent needs it | Documented in `06-...FINDINGS.md` as noisier; 97 simultaneously-visible tools is itself likely a contributor to tool-selection error per the `ornith` findings' namespace-corruption pattern |
| Upstream `microsoft/playwright-mcp` directly (no CloakBrowser layer) | The official Playwright MCP server | Official, actively maintained by Microsoft, the "reference" implementation other stealth forks build on top of | No anti-detection layer — recon against sites with basic bot-detection may get blocked, which is exactly the scenario your earlier plan for script 5 called for a stealth fallback |
| `browser-use` | A separate, popular Python browser-agent framework (not MCP-native by default, but has MCP wrappers) | Frequently cited alongside Playwright MCP in 2026 "best browser automation" roundups as a leading alternative approach (agent decides actions from page state directly rather than via a fixed snapshot/ref tool contract) | Different integration model than what scripts 4-6 already use; would be a bigger rework than staying on the Playwright MCP tool contract |
| `BrowserMCP` (browsermcp.com) | Cloud-hosted browser with built-in proxies/stealth/fingerprint evasion, exposed as MCP | Offloads anti-detection engineering entirely to a managed service | Cloud dependency — a paper explicitly building a *local*, open-weight, reproducible pipeline (per `01-SCOPE.md`'s hardware/reproducibility constraints) should be cautious about a hosted dependency; also unclear pricing/availability for a student project |

**Recommendation:** keep `cloakbrowser-mcp` as the default for all browsing-capable agents (§8 of
`07-...ARCHITECTURE.md` already reached this conclusion independently of this search; the search
reinforces it rather than overturning it). Note upstream `playwright-mcp` as the fallback if
CloakBrowser's extra layer ever becomes the variable under test (e.g. an ablation: "does the
anti-detection layer change tool-call reliability, independent of anti-bot effectiveness?").

### 1.2 NVD / CVE lookup (Recon/OSINT fast path, Vulnerability Analysis)

Numerous single-purpose wrappers around the NVD REST API exist: `SOCTeam-ai/nvd-cve-mcp-server`,
`HaroldFinchIFT/vuln-nist-mcp-server`, `Cyreslab-AI/nist-nvd-mcp-server`, `millsks/nvd-cve-mcp-server`,
`marcoeg/mcp-nvd`, `sockcymbal/nvd-mcp-server`, and a Go implementation (`ayitas/mcp-nvd-go`). All of
these do essentially the same thing you're already doing by hand (script 4 calls the NVD REST API
directly, without an MCP wrapper).

**Recommendation:** given script 4 already has a working, understood, direct integration with the
NVD REST API (`services.nvd.nist.gov/rest/json/cves/2.0?cveId=<ID>`), there is limited value in
swapping to a third-party wrapper for this specific capability alone — it adds a dependency and an
unaudited-code surface for no new functionality. Revisit only if you adopt one of the **consolidated
multi-source servers** below, which bundle NVD lookup together with several other capabilities you'd
otherwise build separately.

### 1.3 CISA KEV feed (Threat Intel Correlation)

Multiple small, focused options: `52-devops/cisa-kev-catalog`, `yeger00/kev-mcp`,
`lambdamechanic/kev-mcp`, `WCoppedge/CISA-Threat-Intelligence-MCP-Server` (adds SSVC-style
prioritization on top of the raw KEV list), and `cyanheads/cisa-cybersecurity-mcp-server` (adds BOD
26-04 federal remediation deadlines and the full CSAF ICS-advisory corpus — considerably more scope
than plain KEV lookup).

**Recommendation:** `cyanheads/cisa-cybersecurity-mcp-server` if the extra ICS/CSAF scope is wanted
later; otherwise one of the smaller single-purpose ones (`52-devops/cisa-kev-catalog` or
`yeger00/kev-mcp`) matches the narrow "is this CVE in KEV" need from §6.1 of the architecture doc
most directly and is easier to audit end-to-end given its smaller surface.

### 1.4 MITRE ATT&CK lookup (Exploit/PoC Discovery, Attack Planning, Log/Alert Triage)

This is the most mature category found. `Montimage/mitre-mcp` (also on PyPI as `mitre-mcp`) is built
on the official `mitreattack-python` library and the official MCP Python SDK, with a PR referencing
explicit **MCP 2026-07-28 spec conformance** — a concrete, checkable maintenance signal most of the
smaller single-maintainer repos don't show. `imouiche/complete-mitre-attack-mcp-server` claims 80+
tools across Enterprise/Mobile/ICS domains — broader than needed for this project's scope, which
raises the same "too many visible tools" concern §1 of the architecture doc is designed to avoid.
`stoyky/mitre-attack-mcp` and `mthorley/mcp-mitre-attack-server` are smaller independent
implementations.

**Recommendation:** `Montimage/mitre-mcp` — built on the official `mitreattack-python` library
(reduces the risk of a hand-rolled STIX parser getting technique data subtly wrong), demonstrated
active maintenance against the current MCP spec, and its tool count is scoped to ATT&CK only rather
than a much larger multi-framework surface. This satisfies the "local ATT&CK dataset + lookup tool"
row exactly as specified in §8 of the architecture doc (it caches STIX bundles locally rather than
re-scraping `attack.mitre.org` per lookup).

### 1.5 MITRE D3FEND lookup (Detection & Mitigation)

This is a **real gap**, not an artifact of imperfect searching: unlike ATT&CK, there is no mature,
independent D3FEND-specific MCP server. D3FEND coverage exists only as a sub-feature of larger
consolidated servers (see §1.7) — e.g. one listing claims "200+ D3FEND defenses" as part of a
broader security-intelligence bundle, and MITRE's own D3FEND resources page lists no MCP integration
directly.

**Recommendation:** do not build a bespoke D3FEND MCP server for this alone. Either (a) adopt one of
the consolidated servers in §1.7 that already bundles D3FEND alongside ATT&CK/CVE data (lower
engineering cost, one more third-party dependency to audit), or (b) for a first pass, have the
Detection & Mitigation Agent work from MITRE's published D3FEND JSON/TTL ontology file downloaded
once and queried with a small local script (no MCP wrapper needed at all — this is a case where
"deterministic local tool" from `07-...ARCHITECTURE.md` §7.1's Evaluator philosophy applies equally
well to a specialist agent's own tool). Given this is a real ecosystem gap, it is also a legitimate,
citable observation for the paper itself: *"the MCP ecosystem's security-tool coverage is uneven —
offensive-framework coverage (ATT&CK, CVE, KEV) is mature; defensive-countermeasure coverage
(D3FEND) lags behind,"* which is itself a small but real finding about the maturity of "LLM
security tooling" as a category, relevant to a paper about small LLMs doing both red- and blue-team
work.

### 1.6 CWE lookup (Vulnerability Analysis, optional)

`pipeworx-io/mcp-mitre-cwe` and `Bilel-Eljaamii/cwe-search_mcp` both wrap the official MITRE CWE API
directly. Both are small, single-purpose, easy to audit.

**Recommendation:** either is fine; `pipeworx-io/mcp-mitre-cwe` is listed independently across
multiple directories (PulseMCP, mcpservers.org), a mild positive maintenance/visibility signal.
Low priority either way — §8 already marks this "optional."

### 1.7 CVSS vector parsing (Vulnerability Analysis)

A dedicated, no-AI, pure-code Apify-hosted MCP tool exists specifically for this
("CVSS 3.1 Calculator - Vector String to Base Score & Severity"), matching exactly the
"deterministic, not LLM-based" requirement from §5.2 of the architecture doc. Independently, the
`RedHatProductSecurity/cvss` Python library (CVSS2/3/4, with an interactive calculator) is a
well-established, non-MCP option if you'd rather wrap it yourself in three lines of code than take a
dependency on a third-party-hosted MCP tool.

**Recommendation:** wrap `RedHatProductSecurity/cvss` (a Red Hat Product Security team library —
notably more institutionally credible provenance than an anonymous single-maintainer repo) in a
five-tool-line local MCP server yourself. This is the cheapest, most auditable option in this entire
document — CVSS vector parsing is pure arithmetic on a well-specified string format, not something
worth taking on a third-party hosted-service dependency for.

### 1.8 Consolidated multi-source security-intelligence servers

Several projects bundle many of the above into one server:

| Server | Claimed scope |
|---|---|
| `mukul975/cve-mcp-server` | 27 tools across 21 APIs: CVE, EPSS, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal |
| `badchars/cve-mcp` | 23 tools: NVD, EPSS, CISA KEV, GitHub Advisory, OSV, risk scoring, bulk triage, exploit search |
| `K4PXD/cve-mcp-server` | NVD, CISA KEV, EPSS, GitHub advisories, PoC discovery, Metasploit/Nuclei exploit tooling |
| `UPinar/contrastapi` | 55 tools: CVE/KEV/CWE, EPSS, MITRE ATLAS+D3FEND, Sigma detection rules, SPF/DMARC, domain/web intel |
| (unnamed, referenced in search) | "331,000+ CVE records, 700+ ATT&CK techniques, 200+ D3FEND defenses, 200+ ATLAS techniques, 550+ CAPEC patterns, 960+ CWE weaknesses, 140+ threat actors" |

**This directly conflicts with the architecture document's own design principle** (§1 and §8's
closing note: keep each agent's visible tool surface small and role-scoped, because tool-count
inflation is the exact failure mode this whole project is measuring). Adopting a 27-55-tool
all-in-one server and handing the *entire* thing to, say, the Vulnerability Analysis Agent would
reintroduce the `ornith` findings' namespace-corruption risk at the single-agent level, even though
it looks like "less engineering work."

**Recommendation:** if a consolidated server is adopted (reasonable, since it closes the D3FEND gap
in one dependency — see §1.5), **do not hand the whole tool list to one agent**. Use the MCP
client-side tool filter (LangChain's `load_mcp_tools` already used in scripts 4-6 returns a list you
can subset before passing to `create_react_agent`) to expose only the 3-5 tools each specialist
actually needs from that server, exactly as if it were several small servers. This preserves the
architecture's per-agent tool-scoping principle while getting the D3FEND/Sigma/CWE coverage a
patchwork of single-purpose servers doesn't fully provide. `UPinar/contrastapi` is the most relevant
single candidate for this role given it's the only one found that explicitly includes both D3FEND
and Sigma coverage alongside CVE/KEV/CWE.

### 1.9 Log parsing / Sigma detection rules (Log/Alert Triage, Detection & Mitigation)

No mature MCP server exists purely for "parse arbitrary logs and flag anomalies" — this remains a
genuine build-it-yourself gap, consistent with §8's original "Not yet built" status and the framing
in `01-SCOPE.md` that this must work against synthetic/local logs anyway. For the **detection-rule**
half specifically (not the parsing/triage half), `SigmaHQ/sigma` is the canonical, extremely
well-established open-source rule repository (this is the reference implementation the entire
"Sigma" detection-format ecosystem is built around, not a niche fork) and pairs naturally with the
Detection & Mitigation Agent: rather than generating a Sigma rule from scratch via LLM, the agent can
be given a **local, offline-searchable copy of `SigmaHQ/sigma`'s rule corpus** as a lookup tool
("does an existing, vetted Sigma rule already cover this technique/CVE"), falling back to LLM-drafted
rule sketches only when no existing rule matches — this is a stronger evidence-grounding pattern than
free-generation and fits the Evaluator-agent philosophy from `07-...ARCHITECTURE.md` §7.1.

**Recommendation:** build a small local tool (regex/field extraction for the log-triage half, as
already specified in §8; a local clone + simple keyword/technique-ID search over `SigmaHQ/sigma`'s
rule YAML files for the detection-rule half) rather than searching further for a prebuilt MCP
wrapper — none of the search results turned up one, and this is a small enough scope to build
directly and keep fully auditable.

### 1.10 Reference: OSINT MCP server catalog

`soxoj/awesome-osint-mcp-servers` is a maintained, curated list (soxoj is a known, established OSINT
tooling author) covering username/email OSINT (Sherlock, Blackbird, Maigret, Holehe, GHunt),
domain/company intel, and Shodan/CVEDB integration. Not needed for the current agent roster, but
worth keeping as the reference list if the Recon/OSINT Agent's scope ever grows beyond
CVE/vendor-advisory lookup into broader target reconnaissance (username/email enumeration, etc.) —
at that point, check this list first rather than re-searching from scratch.

### 1.11 `hexstrike-ai` — additional context found

Confirms what §8 of the architecture doc already treats cautiously: this is a real, actively-used
(11,800+ GitHub stars), 150+-tool offensive-security MCP server — but search also surfaced a
Check Point Research writeup documenting **real-world malicious reuse** (threat actors discussing
weaponizing it against Citrix NetScaler zero-days within days of release) and a Register article on
the same incident. This is directly useful, citable evidence for the paper's ethics/scope section
justifying **why** `07-...ARCHITECTURE.md` §8 deliberately leaves it unwired pending an explicit
Safety/Guardrail gate: it is not a hypothetical dual-use concern, it is a documented one for this
exact tool.

---

## 2. Three implementation plans

### Plan A — "Minimal build, maximum reuse" (recommended starting point)

Adopt the smallest, most auditable single-purpose server per capability, building only the two real
gaps (log/Sigma triage, CVSS wrapper) yourself:

| Capability | Choice |
|---|---|
| Browser automation | `cloakbrowser-mcp` (already in use) |
| CVE/NVD | Keep direct REST call (already in use, script 4) — no new server |
| CISA KEV | `52-devops/cisa-kev-catalog` or `yeger00/kev-mcp` |
| MITRE ATT&CK | `Montimage/mitre-mcp` |
| MITRE D3FEND | Local D3FEND ontology file + small custom script (no MCP server) |
| CWE | `pipeworx-io/mcp-mitre-cwe` (optional, low priority) |
| CVSS | Custom 5-line wrapper around `RedHatProductSecurity/cvss` |
| Sigma / log triage | Custom local tools + local `SigmaHQ/sigma` clone |
| hexstrike-ai | Not wired in (unchanged from §8) |

Pros: smallest total attack surface, easiest to audit every dependency end-to-end, closest to what's
already running. Cons: more separate MCP server processes to manage/launch than a consolidated
option; D3FEND coverage is thinner (one local file, not a maintained upstream feed).

### Plan B — "Consolidated adopt"

Replace CISA KEV / MITRE ATT&CK / CWE / D3FEND / CVSS rows with a single consolidated server
(`UPinar/contrastapi`, the only one found with explicit D3FEND + Sigma coverage), tool-filtered
per-agent as described in §1.8.

Pros: closes the D3FEND gap properly, fewer server processes to manage, one dependency to audit
instead of five. Cons: one unaudited single-maintainer repo now sits in the critical path for most
of the blue-team agents' data; if it has a bug, security issue, or gets abandoned, it affects five
capabilities at once instead of one.

### Plan C — "Hybrid" (recommended overall)

Use Plan A's choices for anything with a mature, independently-maintained, narrowly-scoped option
(browser automation, ATT&CK via `Montimage/mitre-mcp`, CVE via direct REST call, CVSS via your own
tiny wrapper) — these are the capabilities where a small, focused, easily-audited dependency clearly
beats a bundle. Use a consolidated server **only** to close the D3FEND gap specifically (§1.5's
option (a)), since that is the one row with no good narrow alternative. Keep Sigma/log-triage
custom-built per §1.9 regardless of plan, since no prebuilt option exists either way.

This keeps the architecture document's per-agent tool-scoping principle intact everywhere it's
achievable, accepts one consolidated dependency only where the ecosystem genuinely offers nothing
narrower, and keeps the total number of *new* third-party dependencies to audit as low as it can be
without leaving a real capability gap (D3FEND) unfilled.

---

## 3. Updated §8 inventory (supersedes the "Not yet built" placeholders)

| Row from `07-...ARCHITECTURE.md` §8 | Recommended source (Plan C) | Audit priority before use |
|---|---|---|
| CISA KEV JSON feed | `52-devops/cisa-kev-catalog` or `yeger00/kev-mcp` | Medium — small surface, quick to read fully |
| Local MITRE ATT&CK dataset + lookup | `Montimage/mitre-mcp` | Medium — built on official `mitreattack-python`, lowest-risk of the new dependencies |
| Local MITRE D3FEND dataset + lookup | `UPinar/contrastapi` (filtered to D3FEND tools only) **or** local ontology file + custom script if you want zero new server dependency | **High** — this is the one place Plan C accepts a broader consolidated dependency; read it fully before use |
| CVSS vector parser | Custom wrapper around `RedHatProductSecurity/cvss` | Low — you're writing the wrapper yourself; audit the upstream library once |
| Local CWE dataset lookup (optional) | `pipeworx-io/mcp-mitre-cwe` | Low priority, medium audit effort if adopted |
| Log parsing tool | Custom-built, plus local `SigmaHQ/sigma` clone for the rule-lookup half | N/A — self-written |
| `hexstrike-ai` | Unchanged: reserved, not wired in, pending explicit Safety/Guardrail gate | **High**, and already flagged — see §1.11's documented real-world misuse |

---

## 4. Sources

- [Montimage/mitre-mcp](https://github.com/Montimage/mitre-mcp) — MITRE ATT&CK MCP server, built on `mitreattack-python`
- [mitre-mcp PR #163 — MCP 2026-07-28 conformance](https://github.com/Montimage/mitre-mcp/pull/163)
- [imouiche/complete-mitre-attack-mcp-server](https://github.com/imouiche/complete-mitre-attack-mcp-server)
- [stoyky/mitre-attack-mcp](https://github.com/stoyky/mitre-attack-mcp)
- [mthorley/mcp-mitre-attack-server](https://github.com/mthorley/mcp-mitre-attack-server)
- [SOCTeam-ai/nvd-cve-mcp-server](https://github.com/SOCTeam-ai/nvd-cve-mcp-server)
- [HaroldFinchIFT/vuln-nist-mcp-server](https://github.com/HaroldFinchIFT/vuln-nist-mcp-server)
- [Cyreslab-AI/nist-nvd-mcp-server](https://github.com/Cyreslab-AI/nist-nvd-mcp-server)
- [marcoeg/mcp-nvd](https://github.com/marcoeg/mcp-nvd)
- [52-devops/cisa-kev-catalog](https://github.com/52-devops/cisa-kev-catalog)
- [WCoppedge/CISA-Threat-Intelligence-MCP-Server](https://github.com/wcoppedge/cisa-threat-intelligence-mcp-server)
- [yeger00/kev-mcp](https://github.com/yeger00/kev-mcp)
- [cyanheads/cisa-cybersecurity-mcp-server](https://github.com/cyanheads/cisa-cybersecurity-mcp-server)
- [pipeworx-io/mcp-mitre-cwe](https://github.com/pipeworx-io/mcp-mitre-cwe)
- [Bilel-Eljaamii/cwe-search_mcp](https://github.com/Bilel-Eljaamii/cwe-search_mcp)
- [RedHatProductSecurity/cvss](https://github.com/RedHatProductSecurity/cvss)
- [CVSS 3.1 Calculator MCP (Apify)](https://apify.com/timely_quarterstaff/cvss-scorer/api/mcp)
- [mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server)
- [badchars/cve-mcp](https://github.com/badchars/cve-mcp)
- [K4PXD/cve-mcp-server](https://github.com/K4PXD/cve-mcp-server)
- [UPinar/contrastapi](https://github.com/UPinar/contrastapi)
- [firetix/vulnerability-intelligence-mcp-server](https://github.com/firetix/vulnerability-intelligence-mcp-server)
- [SigmaHQ/sigma](https://github.com/sigmahq/sigma)
- [MITRE D3FEND resources](https://d3fend.mitre.org/resources/)
- [soxoj/awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers)
- [TensorBlock/awesome-mcp-servers — security.md](https://github.com/TensorBlock/awesome-mcp-servers/blob/main/docs/security.md)
- [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)
- [Check Point Research — HexStrike AI: LLM Orchestration Driving Real-World Zero-Day Exploits](https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/)
- [The Register — Crims claim HexStrike AI penetration tool makes quick work of Citrix bugs](https://www.theregister.com/2025/09/03/hexstrike_ai_citrix_exploits/)
- [Evaluating MCP Servers for Security Risks](https://glama.ai/mcp/servers/@MCP-Manager/MCP-Checklists/blob/8981c060283424635dd6d3fd84f30490f9a18aee/infrastructure/docs/security-screening-mcp-servers.md)
- [Ramparts security scanner for MCP servers](https://hub.docker.com/mcp/server/ramparts/overview)
- [6 Best MCP Servers for Browser Automation in 2026](https://www.webfuse.com/blog/the-top-5-best-mcp-servers-for-ai-agent-browser-automation)
- [Build an MCP Server with Playwright Stealth for AI Agents](https://alterlab.io/blog/build-an-mcp-server-with-playwright-stealth-for-ai-browsing)
