# CWE-1098: Data Element containing Pointer Item without Proper Copy Control Element

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1098.html  

## Description
The code contains a data element with a pointer that does not have an associated copy or constructor method.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
