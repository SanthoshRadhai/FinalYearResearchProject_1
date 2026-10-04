# CWE-1074: Class with Excessively Deep Inheritance

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1074.html  

## Description
A class has an inheritance level that is too high, i.e., it has a large number of parent classes.

## Extended Description
While the interpretation of "large number of parent classes" may vary for each product or developer, CISQ recommends a default maximum of 7 parent classes.

## Related Weaknesses
- ChildOf: CWE-1093

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability, Increase Analytical Complexity — This issue makes it more difficult to understand and maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
