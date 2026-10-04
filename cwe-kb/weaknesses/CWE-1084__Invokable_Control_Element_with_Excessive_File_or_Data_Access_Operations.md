# CWE-1084: Invokable Control Element with Excessive File or Data Access Operations

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1084.html  

## Description
A function or method contains too many operations that utilize a data manager or file resource.

## Extended Description
While the interpretation of "too many operations" may vary for each product or developer, CISQ recommends a default maximum of 7 operations for the same data manager or file.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
