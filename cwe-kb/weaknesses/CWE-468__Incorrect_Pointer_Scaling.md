# CWE-468: Incorrect Pointer Scaling

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/468.html  

## Description
In C and C++, one may often accidentally refer to the wrong memory due to the semantics of when math operations are implicitly scaled.

## Related Weaknesses
- ChildOf: CWE-682

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Memory, Modify Memory — Incorrect pointer scaling will often result in buffer overflow conditions. Confidentiality can be compromised if the weakness is in the context of a buffer over-read or under-read.

## Potential Mitigations
- [Architecture and Design] Use a platform with high-level memory abstractions.
- [Implementation] Always use array indexing instead of direct pointer manipulation.
- [Architecture and Design] Use technologies for preventing buffer overflows.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- This example attempts to calculate the position of the second byte of a pointer.
