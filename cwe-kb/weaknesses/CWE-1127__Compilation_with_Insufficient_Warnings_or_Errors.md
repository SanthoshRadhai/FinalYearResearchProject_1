# CWE-1127: Compilation with Insufficient Warnings or Errors

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1127.html  

## Description
The code is compiled without sufficient warnings enabled, which may prevent the detection of subtle bugs or quality issues.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.

## Detection Methods
- [Manual Analysis] Inspect scripts and tools that invoke the compiler. Ensure that the appropriate command line switches and/or configuration are specified to report warnings and errors.
