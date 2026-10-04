# CWE-1066: Missing Serialization Control Element

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1066.html  

## Description
The product contains a serializable data element that does not have an associated serialization method.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably, e.g. by triggering an exception. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
