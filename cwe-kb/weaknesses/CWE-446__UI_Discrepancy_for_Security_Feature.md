# CWE-446: UI Discrepancy for Security Feature

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/446.html  

## Description
The user interface does not correctly enable or configure a security feature, but the interface provides feedback that causes the user to believe that the feature is in a secure state.

## Extended Description
When the user interface does not properly reflect what the user asks of it, then it can lead the user into a false sense of security. For example, the user might check a box to enable a security option to enable encrypted communications, but the product does not actually enable the encryption. Alternately, the user might provide a "restrict ALL" access control rule, but the product only implements "restrict SOME".

## Related Weaknesses
- ChildOf: CWE-684

## Common Consequences
- Scope: Other; Impact: Varies by Context
