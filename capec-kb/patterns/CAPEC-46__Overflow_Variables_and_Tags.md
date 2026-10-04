# CAPEC-46: Overflow Variables and Tags

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/46.html  

## Description
This type of attack leverages the use of tags or variables from a formatted configuration data to cause buffer overflow. The adversary crafts a malicious HTML page or configuration file that includes oversized strings, thus causing an overflow.

## Related Attack Patterns
- ChildOf: CAPEC-100
- PeerOf: CAPEC-8
- PeerOf: CAPEC-10

## Prerequisites
- The target program consumes user-controllable data in the form of tags or variables.
- The target program does not perform sufficient boundary checking.

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
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Do not trust input data from user. Validate all user input.

## Related Weaknesses (CWE)
- CWE-120
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697
