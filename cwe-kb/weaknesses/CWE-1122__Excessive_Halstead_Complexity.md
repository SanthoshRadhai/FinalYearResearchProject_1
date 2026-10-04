# CWE-1122: Excessive Halstead Complexity

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1122.html  

## Description
The code is structured in a way that a Halstead complexity measure exceeds a desirable maximum.

## Extended Description
A variety of Halstead complexity measures exist, such as program vocabulary size or volume.

## Related Weaknesses
- ChildOf: CWE-1120

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to understand and/or maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
