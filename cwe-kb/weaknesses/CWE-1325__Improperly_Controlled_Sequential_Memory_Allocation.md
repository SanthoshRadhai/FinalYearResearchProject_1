# CWE-1325: Improperly Controlled Sequential Memory Allocation

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1325.html  

## Description
The product manages a group of objects or resources and performs a separate memory allocation for each object, but it does not properly limit the total amount of memory that is consumed by all of the combined objects.

## Extended Description
While the product might limit the amount of memory that is allocated in a single operation for a single object (such as a malloc of an array), if an attacker can cause multiple objects to be allocated in separate operations, then this might cause higher total memory consumption than the developer intended, leading to a denial of service.

## Related Weaknesses
- ChildOf: CWE-770
- PeerOf: CWE-789
- CanPrecede: CWE-476

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (Memory) — Not controlling memory allocation can result in a request for too much system memory, possibly leading to a crash of the application due to out-of-memory conditions, or the consumption of a large amount of memory on the system.

## Potential Mitigations
- [Implementation] Ensure multiple allocations of the same kind of object are properly tracked - possibly across multiple sessions, requests, or messages. Define an appropriate strategy for handling requests that exceed the limit, and consider supporting a configuration option so that the administrator can extend the amount of memory to be used if necessary.
- [Operation] Run the program using system-provided resource limits for memory. This might still cause the program to crash or exit, but the impact to the rest of the system will be minimized.

## Demonstrative Examples (summary)
- This example contains a small allocation of stack memory. When the program was first constructed, the number of times this memory was allocated was probably inconsequential and presented no problem. Over time, as the number of objects in the database grow, the number of allocations will grow - eventually consuming the available stack, i.e. "stack exhaustion." An attacker who is able to add elements to the database could cause stack exhaustion more rapidly than assumed by the developer.
