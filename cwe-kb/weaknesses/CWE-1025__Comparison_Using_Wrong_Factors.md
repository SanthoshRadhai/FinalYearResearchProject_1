# CWE-1025: Comparison Using Wrong Factors

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1025.html  

## Description
The code performs a comparison between two entities, but the comparison examines the wrong factors or characteristics of the entities, which can lead to incorrect results and resultant weaknesses.

## Related Weaknesses
- ChildOf: CWE-697

## Common Consequences
- Scope: Other; Impact: Varies by Context — This can lead to incorrect results and resultant weaknesses. For example, the code might inadvertently compare references to objects, instead of the relevant contents of those objects, causing two "equal" objects to be considered unequal.

## Detection Methods
- [Manual Static Analysis] Thoroughly test the comparison scheme before deploying code into production. Perform positive testing as well as negative testing.

## Demonstrative Examples (summary)
- In the example below, two Java String objects are declared and initialized with the same string values. An if statement is used to determine if the strings are equivalent.
