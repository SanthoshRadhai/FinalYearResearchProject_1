# CWE-228: Improper Handling of Syntactically Invalid Structure

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/228.html  

## Description
The product does not handle or incorrectly handles input that is not syntactically well-formed with respect to the associated specification.

## Related Weaknesses
- ChildOf: CWE-703
- ChildOf: CWE-707

## Common Consequences
- Scope: Integrity, Availability; Impact: Unexpected State, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU) — If an input is syntactically invalid, then processing the input could place the system in an unexpected state that could lead to a crash, consume available system resources or other unintended behaviors.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This Android application has registered to handle a URL when sent an intent:
