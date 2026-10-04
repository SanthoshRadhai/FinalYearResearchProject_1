# CWE-1115: Source Code Element without Standard Prologue

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1115.html  

## Description
The source code contains elements such as source files that do not consistently provide a prologue or header that has been standardized for the project.

## Extended Description
Standard prologues or headers may contain information such as module name, version number, author, date, purpose, function, assumptions, limitations, accuracy considerations, etc.

## Related Weaknesses
- ChildOf: CWE-1078

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product due to insufficient analyzability, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
- Scope: Other; Impact: Increase Analytical Complexity — The lack of a prologue can make it more difficult to accurately and quickly understand the associated code.
