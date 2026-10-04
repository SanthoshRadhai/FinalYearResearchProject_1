# CWE-475: Undefined Behavior for Input to API

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/475.html  

## Description
The behavior of this function is undefined unless its control parameter is set to a specific value.

## Related Weaknesses
- ChildOf: CWE-573

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
