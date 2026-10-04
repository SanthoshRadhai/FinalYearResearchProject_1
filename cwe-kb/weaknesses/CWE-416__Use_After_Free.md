# CWE-416: Use After Free

**Abstraction:** Variant  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/416.html  

## Description
The product reuses or references memory after it has been freed. At some point afterward, the memory may be allocated again and saved in another pointer, while the original pointer references a location somewhere within the new allocation. Any operations using the original pointer are no longer valid because the memory "belongs" to the code that operates on the new pointer.

## Related Weaknesses
- ChildOf: CWE-825
- ChildOf: CWE-672
- ChildOf: CWE-672
- ChildOf: CWE-672
- CanPrecede: CWE-120
- CanPrecede: CWE-123

## Common Consequences
- Scope: Integrity; Impact: Modify Memory — The use of previously freed memory may corrupt valid data, if the memory area in question has been allocated and used properly elsewhere.
- Scope: Availability; Impact: DoS: Crash, Exit, or Restart — If chunk consolidation occurs after the use of previously freed data, the process may crash when invalid data is used as chunk information.
- Scope: Confidentiality; Impact: Read Memory — Read operations on freed memory can sometimes leak sensitive information instead of causing a crash
- Scope: Integrity, Confidentiality, Availability; Impact: Execute Unauthorized Code or Commands — If malicious data is entered before chunk consolidation can take place, it may be possible to take advantage of a write-what-where primitive to execute arbitrary code. If the newly allocated data happens to hold a class, in C++ for example, various function pointers may be scattered within the heap data. If one of these function pointers is overwritten with an address to valid shellcode, execution of arbitrary code can be achieved.

## Potential Mitigations
- [Architecture and Design] Choose a language that provides automatic memory management.
- [Implementation] When freeing pointers, be sure to set them to NULL once they are freed. However, the utilization of multiple or complex data structures may lower the usefulness of this strategy.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
- The following code illustrates a use after free error:
