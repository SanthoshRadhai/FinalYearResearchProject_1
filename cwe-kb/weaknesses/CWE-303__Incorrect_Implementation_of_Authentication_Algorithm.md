# CWE-303: Incorrect Implementation of Authentication Algorithm

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/303.html  

## Description
The requirements for the product dictate the use of an established authentication algorithm, but the implementation of the algorithm is incorrect.

## Extended Description
This incorrect implementation may allow authentication to be bypassed.

## Related Weaknesses
- ChildOf: CWE-1390

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism
