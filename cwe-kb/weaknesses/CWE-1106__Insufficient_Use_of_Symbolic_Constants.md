# CWE-1106: Insufficient Use of Symbolic Constants

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1106.html  

## Description
The source code uses literal constants that may need to change or evolve over time, instead of using symbolic constants.

## Related Weaknesses
- ChildOf: CWE-1078

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The usage of symbolic names instead of hard-coded constants is preferred.
