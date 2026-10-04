# CWE-1067: Excessive Execution of Sequential Searches of Data Resource

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1067.html  

## Description
The product contains a data query against an SQL table or view that is configured in a way that does not utilize an index and may cause sequential searches to be performed.

## Related Weaknesses
- ChildOf: CWE-1176

## Common Consequences
- Scope: Availability; Impact: Reduce Performance — This issue can make the product perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.
