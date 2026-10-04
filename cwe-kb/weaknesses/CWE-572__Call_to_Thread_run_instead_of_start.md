# CWE-572: Call to Thread run() instead of start()

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/572.html  

## Description
The product calls a thread's run() method instead of calling start(), which causes the code to run in the thread of the caller instead of the callee.

## Extended Description
In most cases a direct call to a Thread object's run() method is a bug. The programmer intended to begin a new thread of control, but accidentally called run() instead of start(), so the run() method will execute in the caller's thread of control.

## Related Weaknesses
- ChildOf: CWE-821

## Common Consequences
- Scope: Other; Impact: Quality Degradation, Varies by Context

## Potential Mitigations
- [Implementation] Use the start() method instead of the run() method.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following excerpt from a Java program mistakenly calls run() instead of start().
