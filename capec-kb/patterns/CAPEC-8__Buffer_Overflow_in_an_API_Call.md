# CAPEC-8: Buffer Overflow in an API Call

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/8.html  

## Description
This attack targets libraries or shared code modules which are vulnerable to buffer overflow attacks. An adversary who has knowledge of known vulnerable libraries or shared code can easily target software that makes use of these libraries. All clients that make use of the code library thus become vulnerable by association. This has a very broad effect on security across a system, usually affecting more than one software process.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The target host exposes an API to the user.
- One or more API functions exposed by the target host has a buffer overflow vulnerability.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-118
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697
