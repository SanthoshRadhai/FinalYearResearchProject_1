# CAPEC-9: Buffer Overflow in Local Command-Line Utilities

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/9.html  

## Description
This attack targets command-line utilities available in a number of shells. An adversary can leverage a vulnerability found in a command-line utility to escalate privilege to root.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The target host exposes a command-line utility to the user.
- The command-line utility exposed by the target host has a buffer overflow vulnerability that can be exploited.

## Skills Required
- [Low] An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as buffer overflow.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Apply the latest patches to your user exposed services. This may not be a complete solution, especially against a zero day attack.
- Do not unnecessarily expose services.

## Related Weaknesses (CWE)
- CWE-120
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-733
- CWE-697
