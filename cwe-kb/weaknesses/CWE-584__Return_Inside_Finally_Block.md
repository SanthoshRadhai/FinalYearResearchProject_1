# CWE-584: Return Inside Finally Block

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/584.html  

## Description
The code has a return statement inside a finally block, which will cause any thrown exception in the try block to be discarded.

## Related Weaknesses
- ChildOf: CWE-705

## Common Consequences
- Scope: Other; Impact: Alter Execution Logic

## Potential Mitigations
- [Implementation] Do not use a return statement inside the finally block. The finally block should have "cleanup" code.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- In the following code excerpt, the IllegalArgumentException will never be delivered to the caller. The finally block will cause the exception to be discarded.
