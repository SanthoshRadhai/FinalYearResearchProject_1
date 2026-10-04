# CWE-366: Race Condition within a Thread

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/366.html  

## Description
If two threads of execution use a resource simultaneously, there exists the possibility that resources may be used while invalid, in turn making the state of execution undefined.

## Related Weaknesses
- ChildOf: CWE-362
- ChildOf: CWE-662
- ChildOf: CWE-662

## Common Consequences
- Scope: Integrity, Other; Impact: Alter Execution Logic, Unexpected State — The main problem is that -- if a lock is overcome -- data could be altered in a bad state.

## Potential Mitigations
- [Architecture and Design] Use locking functionality. This is the recommended solution. Implement some form of locking mechanism around code which alters or reads persistent data in a multithreaded environment.
- [Architecture and Design] Create resource-locking validation checks. If no inherent locking mechanisms exist, use flags and signals to enforce your own blocking scheme when resources are being used by other threads of execution.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
