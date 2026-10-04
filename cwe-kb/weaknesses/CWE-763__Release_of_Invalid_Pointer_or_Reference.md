# CWE-763: Release of Invalid Pointer or Reference

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/763.html  

## Description
The product attempts to return a memory resource to the system, but it calls the wrong release function or calls the appropriate release function incorrectly.

## Extended Description
This weakness can take several forms, such as: The memory was allocated, explicitly or implicitly, via one memory management method and deallocated using a different, non-compatible function (CWE-762). The function calls or memory management routines chosen are appropriate, however they are used incorrectly, such as in CWE-761.

## Related Weaknesses
- ChildOf: CWE-404
- ChildOf: CWE-404
- ChildOf: CWE-404

## Common Consequences
- Scope: Integrity, Availability, Confidentiality; Impact: Modify Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands — This weakness may result in the corruption of memory, and perhaps instructions, possibly leading to a crash. If the corrupted memory can be effectively controlled, it may be possible to execute arbitrary code.

## Potential Mitigations
- [Implementation] Only call matching memory management functions. Do not mix and match routines. For example, when you allocate a buffer with malloc(), dispose of the original pointer with free().
- [Implementation] When programming in C++, consider using smart pointers provided by the boost library to help correctly and consistently manage memory.
- [Architecture and Design] Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.
- [Architecture and Design] Use a language that provides abstractions for memory allocation and deallocation.

## Detection Methods
- [Fuzzing] Fuzz testing (fuzzing) is a powerful technique for generating large numbers of diverse inputs - either randomly or algorithmically - and dynamically invoking the code with those inputs. Even with random inputs, it is often capable of generating unexpected results such as crashes, memory corruption, or resource consumption. Fuzzing effectively produces repeatable test cases that clearly indicate bugs, which helps developers to diagnose the issues.
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518] or valgrind [REF-480].

## Demonstrative Examples (summary)
- This code attempts to tokenize a string and place it into an array using the strsep function, which inserts a \0 byte in place of whitespace or a tab character. After finishing the loop, each string in the AP array points to a location within the input string.
- This example allocates a BarObj object using the new operator in C++, however, the programmer then deallocates the object using free(), which may lead to unexpected behavior.
- In this example, the programmer dynamically allocates a buffer to hold a string and then searches for a specific character. After completing the search, the programmer attempts to release the allocated memory and return SUCCESS or FAILURE to the caller. Note: for simplification, this example uses a hard-coded "Search Me!" string and a constant string length of 20.
- Consider the following code in the context of a parsing application to extract commands out of user data. The intent is to parse each command and add it to a queue of commands to be executed, discarding each malformed entry.
