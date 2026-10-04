# CWE-408: Incorrect Behavior Order: Early Amplification

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/408.html  

## Description
The product allows an entity to perform a legitimate but expensive operation before authentication or authorization has taken place.

## Related Weaknesses
- ChildOf: CWE-405
- ChildOf: CWE-696

## Common Consequences
- Scope: Availability; Impact: DoS: Amplification, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory) — System resources, CPU and memory, can be quickly consumed. This can lead to poor system performance or system crash.

## Demonstrative Examples (summary)
- This function prints the contents of a specified file requested by a user.
