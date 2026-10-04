# CWE-1323: Improper Management of Sensitive Trace Data

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1323.html  

## Description
Trace data collected from several sources on the System-on-Chip (SoC) is stored in unprotected locations or transported to untrusted agents.

## Extended Description
To facilitate verification of complex System-on-Chip (SoC) designs, SoC integrators add specific IP blocks that trace the SoC's internal signals in real-time. This infrastructure enables observability of the SoC's internal behavior, validation of its functional design, and detection of hardware and software bugs. Such tracing IP blocks collect traces from several sources on the SoC including the CPU, crypto coprocessors, and on-chip fabrics. Traces collected from these sources are then aggregated inside trace IP block and forwarded to trace sinks, such as debug-trace ports that facilitate debugging by external hardware and software debuggers. Since these traces are collected from several security-sensitive sources, they must be protected against untrusted debuggers. If they are stored in unprotected memory, an untrusted software debugger can access these traces and extract secret information. Additionally, if security-sensitive traces are not tagged as secure, an untrusted hardware debugger might access them to extract confidential information.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory — An adversary can read secret values if they are captured in debug traces and stored unsafely.

## Potential Mitigations
- [Implementation] Tag traces to indicate owner and debugging privilege level (designer, OEM, or end user) needed to access that trace.

## Demonstrative Examples (summary)
- In a SoC, traces generated from sources include security-sensitive IP blocks such as CPU (with tracing information such as instructions executed and memory operands), on-chip fabric (e.g., memory-transfer signals, transaction type and destination, and on-chip-firewall-error signals), power-management IP blocks (e.g., clock- and power-gating signals), and cryptographic coprocessors (e.g., cryptographic keys and intermediate values of crypto operations), among other non-security-sensitive IP blocks including timers and other functional blocks. The collected traces are then forwarded to the debug and trace interface used by the external hardware debugger.
