# CWE-761: Free of Pointer not at Start of Buffer

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/761.html  

## Description
The product calls free() on a pointer to a memory resource that was allocated on the heap, but the pointer is not at the start of the buffer.

## Extended Description
This can cause the product to crash, or in some cases, modify critical program variables or execute code. This weakness often occurs when the memory is allocated explicitly on the heap with one of the malloc() family functions and free() is called, but pointer arithmetic has caused the pointer to be in the interior or end of the buffer.

## Related Weaknesses
- ChildOf: CWE-763
- ChildOf: CWE-404

## Common Consequences
- Scope: Integrity, Availability, Confidentiality; Impact: Modify Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands

## Potential Mitigations
- [Implementation] When utilizing pointer arithmetic to traverse a buffer, use a separate variable to track progress through memory and preserve the originally allocated address for later freeing.
- [Implementation] When programming in C++, consider using smart pointers provided by the boost library to help correctly and consistently manage memory.
- [Architecture and Design] Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, glibc in Linux provides protection against free of invalid pointers.
- [Architecture and Design] Use a language that provides abstractions for memory allocation and deallocation.

## Detection Methods
- [Automated Dynamic Analysis] Use tools that are integrated during compilation to insert runtime error-checking mechanisms related to memory safety errors, such as AddressSanitizer (ASan) for C/C++ [REF-1518] or valgrind [REF-480].

## Demonstrative Examples (summary)
- In this example, the programmer dynamically allocates a buffer to hold a string and then searches for a specific character. After completing the search, the programmer attempts to release the allocated memory and return SUCCESS or FAILURE to the caller. Note: for simplification, this example uses a hard-coded "Search Me!" string and a constant string length of 20.
- This code attempts to tokenize a string and place it into an array using the strsep function, which inserts a \0 byte in place of whitespace or a tab character. After finishing the loop, each string in the AP array points to a location within the input string.
- Consider the following code in the context of a parsing application to extract commands out of user data. The intent is to parse each command and add it to a queue of commands to be executed, discarding each malformed entry.
