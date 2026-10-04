# CAPEC-45: Buffer Overflow via Symbolic Links

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/45.html  

## Description
This type of attack leverages the use of symbolic links to cause buffer overflows. An adversary can try to create or manipulate a symbolic link file such that its contents result in out of bounds data. When the target software processes the symbolic link file, it could potentially overflow internal buffers with insufficient bounds checking.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The adversary can create symbolic link on the target host.
- The target host does not perform correct boundary checking while consuming data from a resources.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Pay attention to the fact that the resource you read from can be a replaced by a Symbolic link. You can do a Symlink check before reading the file and decide that this is not a legitimate way of accessing the resource.
- Because Symlink can be modified by an adversary, make sure that the ones you read are located in protected directories.
- Pay attention to the resource pointed to by your symlink links (See attack pattern named "Forced Symlink race"), they can be replaced by malicious resources.
- Always check the size of the input data before copying to a buffer.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-285
- CWE-302
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-697
