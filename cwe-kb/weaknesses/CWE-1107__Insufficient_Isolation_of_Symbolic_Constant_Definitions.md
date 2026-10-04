# CWE-1107: Insufficient Isolation of Symbolic Constant Definitions

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1107.html  

## Description
The source code uses symbolic constants, but it does not sufficiently place the definitions of these constants into a more centralized or isolated location.

## Related Weaknesses
- ChildOf: CWE-1078

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
