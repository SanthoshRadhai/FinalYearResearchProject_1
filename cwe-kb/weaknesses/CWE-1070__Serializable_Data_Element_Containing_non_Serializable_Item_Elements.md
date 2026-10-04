# CWE-1070: Serializable Data Element Containing non-Serializable Item Elements

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1070.html  

## Description
The product contains a serializable, storable data element such as a field or member, but the data element contains member elements that are not serializable.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
