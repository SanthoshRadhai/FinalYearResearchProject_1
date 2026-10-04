# CWE-1065: Runtime Resource Management Control Element in a Component Built to Run on Application Servers

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1065.html  

## Description
The product uses deployed components from application servers, but it also uses low-level functions/methods for management of resources, instead of the API provided by the application server.

## Related Weaknesses
- ChildOf: CWE-710

## Common Consequences
- Scope: Other; Impact: Reduce Reliability — This issue can prevent the product from running reliably. If the relevant code is reachable by an attacker, then this reliability problem might introduce a vulnerability.
