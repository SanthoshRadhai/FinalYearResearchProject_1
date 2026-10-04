# CAPEC-100: Overflow Buffers

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/100.html  

## Description
Buffer Overflow attacks target improper or missing bounds checking on buffer operations, typically triggered by input injected by an adversary. As a consequence, an adversary is able to write past the boundaries of allocated buffer regions in memory, causing a program crash or potentially redirection of execution as per the adversaries' choice.

## Related Attack Patterns
- ChildOf: CAPEC-123

## Prerequisites
- Targeted software performs buffer operations.
- Targeted software inadequately performs bounds-checking on buffer operations.
- Adversary has the capability to influence the input to buffer operations.

## Skills Required
- [Low] In most cases, overflowing a buffer does not require advanced skills beyond the ability to notice an overflow and stuff an input variable with content.
- [High] In cases of directed overflows, where the motive is to divert the flow of the program or application as per the adversaries' bidding, high level skills are required. This may involve detailed knowledge of the target system architecture and kernel.

## Resources Required
- None: No specialized resources are required to execute this type of attack. Detecting and exploiting a buffer overflow does not require any resources beyond knowledge of and access to the target system.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Utilize static source code analysis tools to identify potential buffer overflow weaknesses in the software.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-131
- CWE-129
- CWE-805
- CWE-680
