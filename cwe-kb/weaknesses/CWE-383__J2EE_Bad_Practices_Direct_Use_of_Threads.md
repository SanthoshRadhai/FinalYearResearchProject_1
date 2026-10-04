# CWE-383: J2EE Bad Practices: Direct Use of Threads

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/383.html  

## Description
Thread management in a Web application is forbidden in some circumstances and is always highly error prone.

## Extended Description
Thread management in a web application is forbidden by the J2EE standard in some circumstances and is always highly error prone. Managing threads is difficult and is likely to interfere in unpredictable ways with the behavior of the application container. Even without interfering with the container, thread management usually leads to bugs that are hard to detect and diagnose like deadlock, race conditions, and other synchronization errors.

## Related Weaknesses
- ChildOf: CWE-695

## Common Consequences
- Scope: Other; Impact: Quality Degradation

## Potential Mitigations
- [Architecture and Design] For EJB, use framework approaches for parallel execution, instead of using threads.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following example, a new Thread object is created and invoked directly from within the body of a doGet() method in a Java servlet.
