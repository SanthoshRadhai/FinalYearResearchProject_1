# CWE-1068: Inconsistency Between Implementation and Documented Design

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1068.html  

## Description
The implementation of the product is not consistent with the design as described within the relevant documentation.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to maintain the product due to inconsistencies, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
