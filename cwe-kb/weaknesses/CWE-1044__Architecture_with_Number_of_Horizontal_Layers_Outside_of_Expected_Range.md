# CWE-1044: Architecture with Number of Horizontal Layers Outside of Expected Range

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1044.html  

## Description
The product's architecture contains too many - or too few - horizontal layers.

## Extended Description
While the interpretation of "expected range" may vary for each product or developer, CISQ recommends a default minimum of 4 layers and maximum of 8 layers.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Maintainability — This issue makes it more difficult to maintain the product, which indirectly affects security by making it more difficult or time-consuming to find and/or fix vulnerabilities. It also might make it easier to introduce vulnerabilities.
