# CWE-825: Expired Pointer Dereference

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/825.html  

## Description
The product dereferences a pointer that contains a location for memory that was previously valid, but is no longer valid.

## Extended Description
When a product releases memory, but it maintains a pointer to that memory, then the memory might be re-allocated at a later time. If the original pointer is accessed to read or write data, then this could cause the product to read or modify data that is in use by a different function or process. Depending on how the newly-allocated memory is used, this could lead to a denial of service, information exposure, or code execution.

## Related Weaknesses
- ChildOf: CWE-119
- ChildOf: CWE-119
- ChildOf: CWE-119
- ChildOf: CWE-672
- CanPrecede: CWE-125
- CanPrecede: CWE-787

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory — If the expired pointer is used in a read operation, an attacker might be able to control data read in by the application.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — If the expired pointer references a memory location that is not accessible to the product, or points to a location that is "malformed" (such as NULL) or larger than expected by a read or write operation, then a crash may occur.
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — If the expired pointer is used in a function call, or points to unexpected data in a write operation, then code execution may be possible.

## Potential Mitigations
- [Architecture and Design] Choose a language that provides automatic memory management.
- [Implementation] When freeing pointers, be sure to set them to NULL once they are freed. However, the utilization of multiple or complex data structures may lower the usefulness of this strategy.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- The following code shows a simple example of a use after free error:
- The following code shows a simple example of a double free error:
