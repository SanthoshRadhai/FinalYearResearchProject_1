# CWE-407: Inefficient Algorithmic Complexity

**Abstraction:** Class  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/407.html  

## Description
An algorithm in a product has an inefficient worst-case computational complexity that may be detrimental to system performance and can be triggered by an attacker, typically using crafted manipulations that ensure that the worst case is being reached.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other) — The typical consequence is CPU consumption, but memory consumption and consumption of other resources can also occur.

## Demonstrative Examples (summary)
- This example attempts to check if an input string is a "sentence" [REF-1164].
