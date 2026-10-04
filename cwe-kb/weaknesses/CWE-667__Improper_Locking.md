# CWE-667: Improper Locking

**Abstraction:** Class  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/667.html  

## Description
The product does not properly acquire or release a lock on a resource, leading to unexpected resource state changes and behaviors.

## Extended Description
Locking is a type of synchronization behavior that ensures that multiple independently-operating processes or threads do not interfere with each other when accessing the same resource. All processes/threads are expected to follow the same steps for locking. If these steps are not followed precisely - or if no locking is done at all - then another process/thread could modify the shared resource in a way that is not visible or predictable to the original process. This can lead to data or memory corruption, denial of service, etc.

## Related Weaknesses
- ChildOf: CWE-662
- ChildOf: CWE-662
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Availability; Impact: DoS: Resource Consumption (CPU) — Inconsistent locking discipline can lead to deadlock.

## Potential Mitigations
- [Implementation] Use industry standard APIs to implement locking mechanism.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following Java snippet, methods are defined to get and set a long field in an instance of a class that is shared across multiple threads. Because operations on double and long are nonatomic in Java, concurrent access may cause unexpected behavior. Thus, all operations on long and double fields should be synchronized.
- This code tries to obtain a lock for a file, then writes to it.
- The following function attempts to acquire a lock in order to perform operations on a shared resource.
- It may seem that the following bit of code achieves thread safety while avoiding unnecessary synchronization...
