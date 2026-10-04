# CWE-1049: Excessive Data Query Operations in a Large Data Table

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1049.html  

## Description
The product performs a data query with a large number of joins and sub-queries on a large data table.

## Extended Description
While the interpretation of "large data table" and "large number of joins or sub-queries" may vary for each product or developer, CISQ recommends a default of 1 million rows for a "large" data table, a default minimum of 5 joins, and a default minimum of 3 sub-queries.

## Related Weaknesses
- ChildOf: CWE-1176

## Common Consequences
- Scope: Other; Impact: Reduce Performance — This issue can make the product perform more slowly. If the relevant code is reachable by an attacker, then this performance problem might introduce a vulnerability.
