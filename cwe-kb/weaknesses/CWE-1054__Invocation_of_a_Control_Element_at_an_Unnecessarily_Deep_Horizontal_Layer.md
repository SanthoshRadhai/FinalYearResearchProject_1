# CWE-1054: Invocation of a Control Element at an Unnecessarily Deep Horizontal Layer

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1054.html  

## Description
The code at one architectural layer invokes code that resides at a deeper layer than the adjacent layer, i.e., the invocation skips at least one layer, and the invoked code is not part of a vertical utility layer that can be referenced from any horizontal layer.

## Related Weaknesses
- ChildOf: CWE-1061

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to understand and maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
