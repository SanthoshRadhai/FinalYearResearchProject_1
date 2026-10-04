# CAPEC-14: Client-side Injection-induced Buffer Overflow

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/14.html  

## Description
This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service. This hostile service is created to deliver the correct content to the client software. For example, if the client-side application is a browser, the service will host a webpage that the browser loads.

## Related Attack Patterns
- ChildOf: CAPEC-100

## Prerequisites
- The targeted client software communicates with an external server.
- The targeted client software has a buffer overflow vulnerability.

## Skills Required
- [Low] To achieve a denial of service, an attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector.
- [High] Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap requires a more in-depth knowledge and higher skill level.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Availability; Impact: Resource Consumption
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- The client software should not install untrusted code from a non-authenticated server.
- The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers.
- Perform input validation for length of buffer inputs.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Ensure all buffer uses are consistently bounds-checked.
- Use OS-level preventative functionality. Not a complete solution.

## Related Weaknesses (CWE)
- CWE-120
- CWE-353
- CWE-118
- CWE-119
- CWE-74
- CWE-20
- CWE-680
- CWE-697
