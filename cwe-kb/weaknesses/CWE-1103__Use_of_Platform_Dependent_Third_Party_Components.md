# CWE-1103: Use of Platform-Dependent Third Party Components

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1103.html  

## Description
The product relies on third-party components that do not provide equivalent functionality across all desirable platforms.

## Related Weaknesses
- ChildOf: CWE-758

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
