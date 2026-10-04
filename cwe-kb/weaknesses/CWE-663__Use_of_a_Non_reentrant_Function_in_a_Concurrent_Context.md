# CWE-663: Use of a Non-reentrant Function in a Concurrent Context

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/663.html  

## Description
The product calls a non-reentrant function in a concurrent context in which a competing code sequence (e.g. thread or signal handler) may have an opportunity to call the same function or otherwise influence its state.

## Related Weaknesses
- ChildOf: CWE-662

## Common Consequences
- Scope: Integrity, Confidentiality, Other; Impact: Modify Memory, Read Memory, Modify Application Data, Read Application Data, Alter Execution Logic

## Potential Mitigations
- [Implementation] Use reentrant functions if available.
- [Implementation] Add synchronization to your non-reentrant function.
- [Implementation] In Java, use the ReentrantLock Class.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In this example, a signal handler uses syslog() to log a message:
- The following code relies on getlogin() to determine whether or not a user is trusted. It is easily subverted.
