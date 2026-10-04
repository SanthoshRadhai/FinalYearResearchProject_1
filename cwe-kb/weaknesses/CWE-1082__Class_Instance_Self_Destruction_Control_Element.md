# CWE-1082: Class Instance Self Destruction Control Element

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1082.html  

## Description
The code contains a class instance that calls the method or function to delete or destroy itself.

## Extended Description
For example, in C++, "delete this" will cause the object to delete itself.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
