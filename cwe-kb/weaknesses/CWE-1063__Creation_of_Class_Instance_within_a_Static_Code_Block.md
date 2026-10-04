# CWE-1063: Creation of Class Instance within a Static Code Block

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1063.html  

## Description
A static code block creates an instance of a class.

## Extended Description
This pattern identifies situations where a storable data element or member data element is initialized with a value in a block of code which is declared as static.

## Related Weaknesses
- ChildOf: CWE-1176

## Common Consequences
- Scope: Other; Impact: Reduce Performance — This issue can make the product perform more slowly by performing initialization before it is needed. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.
