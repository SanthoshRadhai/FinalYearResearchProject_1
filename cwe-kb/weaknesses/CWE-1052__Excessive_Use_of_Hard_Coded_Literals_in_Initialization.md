# CWE-1052: Excessive Use of Hard-Coded Literals in Initialization

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1052.html  

## Description
The product initializes a data element using a hard-coded literal that is not a simple integer or static constant element.

## Related Weaknesses
- ChildOf: CWE-1419

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to modify or maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
