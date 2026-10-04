# CWE-1072: Data Resource Access without Use of Connection Pooling

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1072.html  

## Description
The product accesses a data resource through a database without using a connection pooling capability.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Other; Impact: Reduce Performance — This issue can make the product perform more slowly, as connection pools allow connections to be reused without the overhead and time consumption of opening and closing a new connection. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.
