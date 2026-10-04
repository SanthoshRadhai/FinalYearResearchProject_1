# Finding: ornith-1.0-35b-Q4_K_M (via mcphost) + HexStrike AI MCP

- **Model**: `ornith-1.0-35b-Q4_K_M:latest`
- **Model backend**: remote Ollama, `https://uncomforted-agnatical-orion.ngrok-free.dev`
- **Date/time**: 2026-09-07, ~23:17 (host clock)
- **Host/orchestrator**: mcphost v0.34.0 (`mark3labs/mcphost`, `go install` build "dev")
- **Environment**: Kali WSL2 (distro `kali-linux`), config at `S:\CALDERA\MCPHost-modifed\mcp.json`
- **MCP server under test**: HexStrike AI v6.0 (`hexstrike_server.py` + `hexstrike_mcp.py`, conda env `hexstrike`, Python 3.11)
- **Prompt used**: "List the exact names of every tool you currently have access to, especially any tools from an MCP server called hexstrike (e.g. nmap_scan). Just list names, do not call anything."

## Debug values
- HexStrike server health at test time: `status: healthy`, `all_essential_tools_available: false` (only 4-5 of 127 CLI tools actually installed in this WSL instance: nmap, curl, file, xxd)
- mcphost connection: **clean, immediate** — log line `Loaded 150 tools from MCP servers`, no retries, no failures (contrast with CAI and OpenClaude, both of which showed flaky/failing connections to the same HexStrike instance)
- Raw debug log: `S:\CALDERA\mcphost_raw1.log` (93,950 lines pre-clean) / cleaned: `S:\CALDERA\mcphost_clean1.txt` (7.6M chars, ANSI-stripped)
- Tool-name prefix corruption observed: model rendered the `hexstrike__` namespace prefix as at least 6 distinct garbled variants across the same response: `hexstrike__`, `hexstrip__`, `hexstrips__`, `hexstripe__`, `hexstripe_`, `hexstrike.`
- Real tool suffixes correctly referenced (sample): `nmap_scan`, `nmap_advanced_scan`, `sqlmap_scan`, `ghidra_analysis`, `trivy_scan`, `nuclei_scan`, `rustscan_fast_scan`, `wafw00f_scan`
- Fabricated tools NOT present in HexStrike's real 150-tool catalog (confirmed against the tool tree captured earlier via CAI): `bind_127.0.0.1`, `ssh_connect`, `ssh_relay_scan`, `smtp_enum_scan`, `patchwork_exploit`, `shutdown`, `chromedriver_start`, `dbus_scan`, `review`, `mfburp_scan`, `lacbe_bench_cis`
- Model self-flagged its own instability mid-response: *"Note from above that many names have slight variations which were probably transcription errors... Please note: I've listed them as they appear... some may have minor transcription variations."*

## Verdict
mcphost is the cleanest/most reliable MCP host tested so far (no connection flakiness, correct 150-tool load confirmed independent of the model). Despite this clean environment, **ornith still produces unstable, partially-hallucinated output** when asked to enumerate HexStrike's 150 tools — correct real tool suffixes mixed with corrupted namespace prefixes and outright fabricated tool names. This is the cleanest evidence yet that the failure is a **model-level limitation** (likely repetition/instability on long structured lists with a repeated prefix token, possibly exacerbated by quantization), not a bug in CAI, OpenClaude, or mcphost specifically.

**Not yet tested**: an actual tool-*invocation* attempt through mcphost (this run only tested tool *listing*). Given the prefix corruption seen here, a real invocation attempt would likely reference a garbled name (e.g. `hexstrips__nmap_scan`) that doesn't match the real registered tool (`hexstrike__nmap_scan`), and would be expected to fail on a name-mismatch basis.

## Comparison to prior findings (same model, different hosts)
| Host | Connection to HexStrike | Tool-call behavior |
|---|---|---|
| CAI v1.1.5 | Eventually succeeds after ~30-40s (misleading "failed after 3 attempts" message resolves later) | Echoes a tool's JSON schema as chat text instead of invoking; later run named the right tool (`nmap_scan`) in JSON-shaped prose but still never actually invoked it |
| OpenClaude v0.30.0 | Consistently fails (`✗ Failed to connect`) even after 45s+ warm-up | N/A — never got a working connection; separately fabricated an entire fictitious tool inventory resembling Claude Code's own tools when asked to self-report capabilities |
| mcphost v0.34.0 | Clean, immediate, reliable | Correctly lists most real tool suffixes but corrupts the shared namespace prefix and fabricates some tool names entirely |
