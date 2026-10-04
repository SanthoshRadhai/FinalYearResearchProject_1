# CAPEC-10: Buffer Overflow via Environment Variables

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/10.html  

## Description
This attack pattern involves causing a buffer overflow through manipulation of environment variables. Once the adversary finds that they can modify an environment variable, they may try to overflow associated buffers. This attack leverages implicit trust often placed in environment variables.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The application uses environment variables.
- An environment variable exposed to the user is vulnerable to a buffer overflow.
- The vulnerable environment variable uses untrusted data.
- Tainted data used in the environment variables is not properly validated. For instance boundary checking is not done before copying the input data to a buffer.

## Skills Required
- [Low] An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.

## Consequences
- Scope: Availability; Impact: Unreliable Execution
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Do not expose environment variable to the user.
- Do not use untrusted data in your environment variables.
- Use a language or compiler that performs automatic bounds checking
- There are tools such as Sharefuzz [REF-2] which is an environment variable fuzzer for Unix that support loading a shared library. You can use Sharefuzz to determine if you are exposing an environment variable vulnerable to buffer overflow.

## Related Weaknesses (CWE)
- CWE-120
- CWE-302
- CWE-118
- CWE-119
- CWE-74
- CWE-99
- CWE-20
- CWE-680
- CWE-733
- CWE-697
