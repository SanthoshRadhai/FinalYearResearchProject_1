# CWE-1431: Driving Intermediate Cryptographic State/Results to Hardware Module Outputs

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1431.html  

## Description
The product uses a hardware module implementing a cryptographic algorithm that writes sensitive information about the intermediate state or results of its cryptographic operations via one of its output wires (typically the output port containing the final result).

## Related Weaknesses
- ChildOf: CWE-200
- PeerOf: CWE-497

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data — Mathematically sound cryptographic algorithms rely on their correct implementation for security. These assumptions might break when a hardware crypto module leaks intermediate encryption states or results such that they can be observed by an adversary. If intermediate state is observed, it might be possible for an attacker to identify the secrets used in the cryptographic operation.

## Potential Mitigations
- [Architecture and Design] Designers/developers should add or modify existing control flow logic along any data flow paths that connect "sources" (signals with intermediate cryptographic state/results) with "sinks" (hardware module outputs and other signals outside of trusted cryptographic zone). The control flow logic should only allow cryptographic results to be driven to "sinks" when appropriate conditions are satisfied (typically when the final result for a cryptographic operation has been generated). When the appropriate conditions are not satisfied (i.e., before or during a cryptographic operation), the control flow logic should drive a safe default value to "sinks".
- [Implementation] Designers/developers should add or modify existing control flow logic along any data flow paths that connect "sources" (signals with intermediate cryptographic state/results) with "sinks" (hardware module outputs and other signals outside of trusted cryptographic zone). The control flow logic should only allow cryptographic results to be driven to "sinks" when appropriate conditions are satisfied (typically when the final result for a cryptographic operation has been generated). When the appropriate conditions are not satisfied (i.e., before or during a cryptographic operation), the control flow logic should drive a safe default value to "sinks".

## Detection Methods
- [Automated Static Analysis - Source Code] Automated static analysis can find some instances of this weakness by analyzing source register-transfer level (RTL) code without having to simulate it or analyze it with a formal verification engine. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (signals with intermediate cryptographic state/results) with "sinks" (hardware module outputs and other signals outside of trusted cryptographic zone) without any control flow.
- [Simulation / Emulation] Simulation/emulation based analysis can find some instances of this weakness by simulating source register-transfer level (RTL) code along with a set of assertions that incorporate the simulated values of relevant design signals. Typically, these assertions will capture desired or undesired behavior. Analysis can be improved by using simulation-based information flow tracking (IFT) to more precisely detect unexpected results.
- [Formal Verification] Formal verification can find some instances of this weakness by exhaustively analyzing whether a given assertion holds true for a given hardware design specified in register-transfer level (RTL) code. Typically, these assertions will capture desired or undesired behavior. For this weakness, an assertion should check for undesired behavior in which one output is a signal that captures when a cryptographic algorithm has completely finished; another output is a signal with intermediate cryptographic state/results; and there is an assignment to a hardware module output or other signal outside of a trusted cryptographic zone. Alternatively, when using a formal IFT verification, the same undesired behavior can be detected by checking if computation results can ever leak to an output when the cryptographic result is not copmlete.
- [Manual Analysis] Manual analysis can find some instances of this weakness by manually reviewing relevant lines of source register-transfer level (RTL) code to detect potentially-vulnerable patterns. Typically, the reviewer will trace the sequence of assignments that connect "sources" (signals with intermediate cryptographic state/results) with "sinks" (hardware module outputs and other signals outside of trusted cryptographic zone). If this sequence of assignments is missing adequate control flow, then the weakness is likely to exist.

## Demonstrative Examples (summary)
- The following SystemVerilog code is a crypto module that takes input data and encrypts it by processing the data through multiple encryption rounds. Note: this example is derived from [REF-1469].
