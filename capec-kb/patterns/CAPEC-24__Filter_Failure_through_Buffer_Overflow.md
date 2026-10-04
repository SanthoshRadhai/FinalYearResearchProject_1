# CAPEC-24: Filter Failure through Buffer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/24.html  

## Description
In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail securely (i.e. the user input is let into the system unfiltered).

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- Ability to control the length of data passed to an active filter.

## Skills Required
- [Low] An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.
- Pre-design: Use a language or compiler that performs automatic bounds checking.
- Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-119
- CWE-118
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697
