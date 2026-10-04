# CWE-1062: Parent Class with References to Child Class

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1062.html  

## Description
The code has a parent class that contains references to a child class, its methods, or its members.

## Related Weaknesses
- ChildOf: CWE-1061

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
