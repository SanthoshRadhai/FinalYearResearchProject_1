# CWE-543: Use of Singleton Pattern Without Synchronization in a Multithreaded Context

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/543.html  

## Description
The product uses the singleton pattern when creating a resource within a multithreaded environment.

## Extended Description
The use of a singleton pattern may not be thread-safe.

## Related Weaknesses
- ChildOf: CWE-820
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Other, Integrity; Impact: Other, Modify Application Data

## Potential Mitigations
- [Architecture and Design] Use the Thread-Specific Storage Pattern. See References.
- [Implementation] Do not use member fields to store information in the Servlet. In multithreading environments, storing user data in Servlet member fields introduces a data access race condition.
- [Implementation] Avoid using the double-checked locking pattern in language versions that cannot guarantee thread safety. This pattern may be used to avoid the overhead of a synchronized call, but in certain versions of Java (for example), this has been shown to be unsafe because it still introduces a race condition (CWE-209).

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This method is part of a singleton pattern, yet the following singleton() pattern is not thread-safe. It is possible that the method will create two objects instead of only one.
