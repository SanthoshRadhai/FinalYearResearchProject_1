# CWE-1086: Class with Excessive Number of Child Classes

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1086.html  

## Description
A class contains an unnecessarily large number of children.

## Extended Description
While the interpretation of "large number of children" may vary for each product or developer, CISQ recommends a default maximum of 10 child classes.

## Related Weaknesses
- ChildOf: CWE-1093

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to understand and maintain the software, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
