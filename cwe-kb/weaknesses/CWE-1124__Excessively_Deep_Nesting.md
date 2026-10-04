# CWE-1124: Excessively Deep Nesting

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1124.html  

## Description
The code contains a callable or other code grouping in which the nesting / branching is too deep.

## Related Weaknesses
- ChildOf: CWE-1120

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
