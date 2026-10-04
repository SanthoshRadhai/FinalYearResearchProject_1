# CWE-1102: Reliance on Machine-Dependent Data Representation

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1102.html  

## Description
The code uses a data representation that relies on low-level data representation or constructs that may vary across different processors, physical machines, OSes, or other physical components.

## Related Weaknesses
- ChildOf: CWE-758
- PeerOf: CWE-1105

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain and/or port the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
