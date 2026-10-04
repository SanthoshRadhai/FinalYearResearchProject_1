# CWE-1091: Use of Object without Invoking Destructor Method

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1091.html  

## Description
The product contains a method that accesses an object but does not later invoke the element's associated finalize/destructor method.

## Related Weaknesses
- ChildOf: CWE-772
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Reduce Performance — This issue can make the product perform more slowly by retaining memory and/or other resources longer than necessary. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
