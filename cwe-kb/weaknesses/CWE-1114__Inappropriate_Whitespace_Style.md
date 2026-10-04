# CWE-1114: Inappropriate Whitespace Style

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1114.html  

## Description
The source code contains whitespace that is inconsistent across the code or does not follow expected standards for the product.

## Related Weaknesses
- ChildOf: CWE-1078

## Common Consequences
- Scope: Other; Impact: Increase Analytical Complexity — A human auditor might indirectly trust that whitespace (especially indentation) reflects the actual control flow of the code, which could make it more difficult to find vulnerabilities.
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to understand and maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities.
