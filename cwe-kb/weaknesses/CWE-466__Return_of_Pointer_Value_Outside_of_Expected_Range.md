# CWE-466: Return of Pointer Value Outside of Expected Range

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/466.html  

## Description
A function can return a pointer to memory that is outside of the buffer that the pointer is expected to reference.

## Related Weaknesses
- ChildOf: CWE-119
- ChildOf: CWE-20

## Common Consequences
- Scope: Confidentiality, Integrity; Impact: Read Memory, Modify Memory

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].
