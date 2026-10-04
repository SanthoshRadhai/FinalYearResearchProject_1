# CWE-463: Deletion of Data Structure Sentinel

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/463.html  

## Description
The accidental deletion of a data-structure sentinel can cause serious programming logic problems.

## Extended Description
Often times data-structure sentinels are used to mark structure of the data structure. A common example of this is the null character at the end of strings. Another common example is linked lists which may contain a sentinel to mark the end of the list. It is dangerous to allow this type of control data to be easily accessible. Therefore, it is important to protect from the deletion or modification outside of some wrapper interface which provides safety.

## Related Weaknesses
- ChildOf: CWE-707
- PeerOf: CWE-464

## Common Consequences
- Scope: Availability, Other; Impact: Other — Generally this error will cause the data structure to not work properly.
- Scope: Authorization, Other; Impact: Other — If a control character, such as NULL is removed, one may cause resource access control problems.

## Potential Mitigations
- [Architecture and Design] Use an abstraction library to abstract away risky APIs. Not a complete solution.
- [Build and Compilation] Run or compile the software using features or extensions that automatically provide a protection mechanism that mitigates or eliminates buffer overflows. For example, certain compilers and extensions provide automatic buffer overflow detection mechanisms that are built into the compiled code. Examples include the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice.
- [Operation] Use OS-level preventative functionality. Not a complete solution.

## Demonstrative Examples (summary)
- This example creates a null terminated string and prints it contents.
