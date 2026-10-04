# CWE-1051: Initialization with Hard-Coded Network Resource Configuration Data

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1051.html  

## Description
The product initializes data using hard-coded values that act as network resource identifiers.

## Related Weaknesses
- ChildOf: CWE-1419

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably, e.g. if it runs in an environment does not use the hard-coded network resource identifiers. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
