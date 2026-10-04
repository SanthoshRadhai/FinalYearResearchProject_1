# CWE-1073: Non-SQL Invokable Control Element with Excessive Number of Data Resource Accesses

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1073.html  

## Description
The product contains a client with a function or method that contains a large number of data accesses/queries that are sent through a data manager, i.e., does not use efficient database capabilities.

## Extended Description
While the interpretation of "large number of data accesses/queries" may vary for each product or developer, CISQ recommends a default maximum of 2 data accesses per function/method.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Other; Impact: Reduce Performance — This issue can make the product perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.
