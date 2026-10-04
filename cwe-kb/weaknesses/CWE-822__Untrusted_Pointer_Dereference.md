# CWE-822: Untrusted Pointer Dereference

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/822.html  

## Description
The product obtains a value from an untrusted source, converts this value to a pointer, and dereferences the resulting pointer.

## Extended Description
An attacker can supply a pointer for memory locations that the product is not expecting. If the pointer is dereferenced for a write operation, the attack might allow modification of critical state variables, cause a crash, or execute code. If the dereferencing operation is for a read, then the attack might allow reading of sensitive data, cause a crash, or set a variable to an unexpected value (since the value will be read from an unexpected memory location). There are several variants of this weakness, including but not necessarily limited to: The untrusted value is directly invoked as a function call. In OS kernels or drivers where there is a boundary between "userland" and privileged memory spaces, an untrusted pointer might enter through an API or system call (see CWE-781 for one such example). Inadvertently accepting the value from an untrusted control sphere when it did not have to be accepted as input at all. This might occur when the code was originally developed to be run by a single user in a non-networked environment, and the code is then ported to or otherwise exposed to a networked environment.

## Related Weaknesses
- ChildOf: CWE-119
- ChildOf: CWE-119
- ChildOf: CWE-119
- CanPrecede: CWE-125
- CanPrecede: CWE-787

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory — If the untrusted pointer is used in a read operation, an attacker might be able to read sensitive portions of memory.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — If the untrusted pointer references a memory location that is not accessible to the product, or points to a location that is "malformed" or larger than expected by a read or write operation, the application may terminate unexpectedly.
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands, Modify Memory — If the untrusted pointer is used in a function call, or points to unexpected data in a write operation, then code execution may be possible.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].
