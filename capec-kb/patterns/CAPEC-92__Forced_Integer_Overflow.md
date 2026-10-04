# CAPEC-92: Forced Integer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/92.html  

## Description
This attack forces an integer variable to go out of range. The integer variable is often used as an offset such as size of memory allocation or similarly. The attacker would typically control the value of such variable and try to get it out of range. For instance the integer in question is incremented past the maximum possible value, it may wrap to become a very small, or negative number, therefore providing a very incorrect value which can lead to unexpected behavior. At worst the attacker can execute arbitrary code.

## Related Attack Patterns
- ChildOf: CAPEC-128

## Prerequisites
- The attacker can manipulate the value of an integer variable utilized by the target host.
- The target host does not do proper range checking on the variable before utilizing it.
- When the integer variable is incremented or decremented to an out of range value, it gets a very different value (e.g. very small or negative number)

## Skills Required
- [Low] An attacker can simply overflow an integer by inserting an out of range value.
- [High] Exploiting a buffer overflow by injecting malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as integer overflow.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Always do bound checking before consuming user input data.

## Related Weaknesses (CWE)
- CWE-190
- CWE-128
- CWE-120
- CWE-122
- CWE-196
- CWE-680
- CWE-697
