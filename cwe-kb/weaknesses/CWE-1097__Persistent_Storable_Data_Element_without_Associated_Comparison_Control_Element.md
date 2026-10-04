# CWE-1097: Persistent Storable Data Element without Associated Comparison Control Element

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1097.html  

## Description
The product uses a storable data element that does not have all of the associated functions or methods that are necessary to support comparison.

## Related Weaknesses
- ChildOf: CWE-1076
- ChildOf: CWE-595

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably, due to incorrect or unexpected comparison results. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
