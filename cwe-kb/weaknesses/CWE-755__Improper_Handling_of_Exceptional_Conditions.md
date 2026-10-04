# CWE-755: Improper Handling of Exceptional Conditions

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/755.html  

## Description
The product does not handle or incorrectly handles an exceptional condition.

## Related Weaknesses
- ChildOf: CWE-703

## Common Consequences
- Scope: Other; Impact: Other

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example attempts to resolve a hostname.
- The following example attempts to allocate memory for a character. After the call to malloc, an if statement is used to check whether the malloc function failed.
- The following code mistakenly catches a NullPointerException.
