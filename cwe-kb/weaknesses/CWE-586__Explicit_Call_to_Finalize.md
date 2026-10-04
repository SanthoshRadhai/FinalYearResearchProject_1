# CWE-586: Explicit Call to Finalize()

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/586.html  

## Description
The product makes an explicit call to the finalize() method from outside the finalizer.

## Extended Description
While the Java Language Specification allows an object's finalize() method to be called from outside the finalizer, doing so is usually a bad idea. For example, calling finalize() explicitly means that finalize() will be called more than once: the first time will be the explicit call and the last time will be the call that is made after the object is garbage collected.

## Related Weaknesses
- ChildOf: CWE-1076

## Common Consequences
- Scope: Integrity, Other; Impact: Unexpected State, Quality Degradation

## Potential Mitigations
- [Implementation] Do not make explicit calls to finalize().

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following code fragment calls finalize() explicitly:
