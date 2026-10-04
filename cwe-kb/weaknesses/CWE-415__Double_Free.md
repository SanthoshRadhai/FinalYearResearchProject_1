# CWE-415: Double Free

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/415.html  

## Description
The product calls free() twice on the same memory address.

## Related Weaknesses
- ChildOf: CWE-825
- ChildOf: CWE-1341
- ChildOf: CWE-672
- ChildOf: CWE-672
- ChildOf: CWE-672
- ChildOf: CWE-666
- PeerOf: CWE-416
- PeerOf: CWE-123

## Common Consequences
- Scope: Integrity, Confidentiality, Availability; Impact: Modify Memory, Execute Unauthorized Code or Commands — When a program calls free() twice with the same argument, the program's memory management data structures may become corrupted, potentially leading to the reading or modification of unexpected memory addresses. This corruption can cause the program to crash or, in some circumstances, cause two later calls to malloc() to return the same pointer. If malloc() returns the same value twice and the program later gives the attacker control over the data that is written into this doubly-allocated memory, the program becomes vulnerable to a buffer overflow attack. Doubly freeing memory may result in a write-what-where condition, allowing an attacker to execute arbitrary code.

## Potential Mitigations
- [Architecture and Design] Choose a language that provides automatic memory management.
- [Implementation] Ensure that each allocation is freed only once. After freeing a chunk, set the pointer to NULL to ensure the pointer cannot be freed again. In complicated error conditions, be sure that clean-up routines respect the state of allocation properly. If the language is object oriented, ensure that object destructors delete each chunk of memory only once.
- [Implementation] Use a static analysis tool to find double free instances.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518].

## Demonstrative Examples (summary)
- The following code shows a simple example of a double free vulnerability.
- While contrived, this code should be exploitable on Linux distributions that do not ship with heap-chunk check summing turned on.
