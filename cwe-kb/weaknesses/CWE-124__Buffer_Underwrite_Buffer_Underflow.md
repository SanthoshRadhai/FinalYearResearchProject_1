# CWE-124: Buffer Underwrite ('Buffer Underflow')

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/124.html  

## Description
The product writes to a buffer using an index or pointer that references a memory location prior to the beginning of the buffer.

## Related Weaknesses
- ChildOf: CWE-786
- ChildOf: CWE-787

## Common Consequences
- Scope: Integrity, Availability; Impact: Modify Memory, DoS: Crash, Exit, or Restart — Out of bounds memory access will very likely result in the corruption of relevant memory, and perhaps instructions, possibly leading to a crash.
- Scope: Integrity, Confidentiality, Availability, Access Control, Other; Impact: Execute Unauthorized Code or Commands, Modify Memory, Bypass Protection Mechanism, Other — If the corrupted memory can be effectively controlled, it may be possible to execute arbitrary code. If the corrupted memory is data rather than instructions, the system will continue to function with improper changes, possibly in violation of an implicit or explicit policy. The consequences would only be limited by how the affected data is used, such as an adjacent memory location that is used to specify whether the user has special privileges.
- Scope: Access Control, Other; Impact: Bypass Protection Mechanism, Other — When the consequence is arbitrary code execution, this can often be used to subvert any other security service.

## Potential Mitigations
- [Requirements] Choose a language that is not susceptible to these issues.
- [Implementation] All calculated values that are used as index or for pointer arithmetic should be validated to ensure that they are within an expected range.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- In the following C/C++ example, a utility function is used to trim trailing whitespace from a character string. The function copies the input string to a local character string and uses a while statement to remove the trailing whitespace by moving backward through the string and overwriting whitespace with a NUL character.
- The following is an example of code that may result in a buffer underwrite. This code is attempting to replace the substring "Replace Me" in destBuf with the string stored in srcBuf. It does so by using the function strstr(), which returns a pointer to the found substring in destBuf. Using pointer arithmetic, the starting index of the substring is found.
