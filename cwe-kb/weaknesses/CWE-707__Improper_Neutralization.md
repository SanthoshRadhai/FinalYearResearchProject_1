# CWE-707: Improper Neutralization

**Abstraction:** Pillar  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/707.html  

## Description
The product does not ensure or incorrectly ensures that structured messages or data are well-formed and that certain security properties are met before being read from an upstream component or sent to a downstream component.

## Extended Description
If a message is malformed, it may cause the message to be incorrectly interpreted. Neutralization is an abstract term for any technique that ensures that input (and output) conforms with expectations and is "safe." This can be done by: checking that the input/output is already "safe" (e.g. validation) transformation of the input/output to be "safe" using techniques such as filtering, encoding/decoding, escaping/unescaping, quoting/unquoting, or canonicalization preventing the input/output from being directly provided by an attacker (e.g. "indirect selection" that maps externally-provided values to internally-controlled values) preventing the input/output from being processed at all This weakness typically applies in cases where the product prepares a control message that another process must act on, such as a command or query, and malicious input that was intended as data, can enter the control plane instead. However, this weakness also applies to more general cases where there are not always control implications.

## Common Consequences
- Scope: Other; Impact: Other

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
