# CWE-1050: Excessive Platform Resource Consumption within a Loop

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1050.html  

## Description
The product has a loop body or loop condition that contains a control element that directly or indirectly consumes platform resources, e.g. messaging, sessions, locks, or file descriptors.

## Related Weaknesses
- ChildOf: CWE-405

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other), Reduce Performance — This issue can make the product perform more slowly. If an attacker can influence the number of iterations in the loop, then this performance problem might allow a denial of service by consuming more platform resources than intended.
