# CWE-1100: Insufficient Isolation of System-Dependent Functions

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1100.html  

## Description
The product or code does not isolate system-dependent functionality into separate standalone modules.

## Related Weaknesses
- ChildOf: CWE-1061

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain and/or port the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
