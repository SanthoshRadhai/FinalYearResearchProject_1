# CWE-1126: Declaration of Variable with Unnecessarily Wide Scope

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1126.html  

## Description
The source code declares a variable in one scope, but the variable is only used within a narrower scope.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to understand and/or maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
