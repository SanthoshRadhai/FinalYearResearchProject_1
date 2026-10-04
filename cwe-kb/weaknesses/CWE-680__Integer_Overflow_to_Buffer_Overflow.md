# CWE-680: Integer Overflow to Buffer Overflow

**Abstraction:** Compound  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/680.html  

## Description
The product performs a calculation to determine how much memory to allocate, but an integer overflow can occur that causes less memory to be allocated than expected, leading to a buffer overflow.

## Related Weaknesses
- StartsWith: CWE-190
- ChildOf: CWE-190

## Common Consequences
- Scope: Integrity, Availability, Confidentiality; Impact: Modify Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- The following image processing code allocates a table for images.
