# CWE-1176: Inefficient CPU Computation

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1176.html  

## Description
The product performs CPU computations using algorithms that are not as efficient as they could be for the needs of the developer, i.e., the computations can be optimized further.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Availability; Impact: Reduce Performance, DoS: Resource Consumption (CPU) — This issue can make the product perform more slowly, possibly in ways that are noticeable to the users. If an attacker can influence the amount of computation that must be performed, e.g. by triggering worst-case complexity, then this performance problem might introduce a vulnerability.
