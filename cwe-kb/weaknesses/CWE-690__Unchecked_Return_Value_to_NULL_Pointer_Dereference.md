# CWE-690: Unchecked Return Value to NULL Pointer Dereference

**Abstraction:** Compound  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/690.html  

## Description
The product does not check for an error after calling a function that can return with a NULL pointer if the function fails, which leads to a resultant NULL pointer dereference.

## Extended Description
While unchecked return value weaknesses are not limited to returns of NULL pointers (see the examples in CWE-252), functions often return NULL to indicate an error status. When this error condition is not checked, a NULL pointer dereference can occur.

## Related Weaknesses
- StartsWith: CWE-252
- ChildOf: CWE-252

## Common Consequences
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands, Read Memory, Modify Memory — In rare circumstances, when NULL is equivalent to the 0x0 memory address and privileged code can access it, then writing or reading memory is possible, which may lead to code execution.

## Detection Methods
- [Black Box] This typically occurs in rarely-triggered error conditions, reducing the chances of detection during black box testing.
- [White Box] Code analysis can require knowledge of API behaviors for library functions that might return NULL, reducing the chances of detection when unknown libraries are used.
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- The code below makes a call to the getUserName() function but doesn't check the return value before dereferencing (which may cause a NullPointerException).
- This example takes an IP address from a user, verifies that it is well formed and then looks up the hostname and copies it into a buffer.
