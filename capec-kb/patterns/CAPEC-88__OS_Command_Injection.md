# CAPEC-88: OS Command Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/88.html  

## Description
In this type of an attack, an adversary injects operating system commands into existing application functions. An application that uses untrusted input to build command strings is vulnerable. An adversary can leverage OS command injection in an application to elevate privileges, execute arbitrary commands and compromise the underlying operating system.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- User controllable input used as part of commands to the underlying operating system.

## Skills Required
- [High] The attacker needs to have knowledge of not only the application to exploit but also the exact nature of commands that pertain to the target operating system. This may involve, though not always, knowledge of specific assembly commands for the platform.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges, Bypass Protection Mechanism
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Use language APIs rather than relying on passing data to the operating system shell or command line. Doing so ensures that the available protection mechanisms in the language are intact and applicable.
- Filter all incoming data to escape or remove characters or strings that can be potentially misinterpreted as operating system or shell commands
- All application processes should be run with the minimal privileges required. Also, processes must shed privileges as soon as they no longer require them.

## Related Weaknesses (CWE)
- CWE-78
- CWE-88
- CWE-20
- CWE-697
