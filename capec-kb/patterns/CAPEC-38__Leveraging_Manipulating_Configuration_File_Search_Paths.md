# CAPEC-38: Leveraging/Manipulating Configuration File Search Paths

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/38.html  

## Description
This pattern of attack sees an adversary load a malicious resource into a program's standard path so that when a known command is executed then the system instead executes the malicious component. The adversary can either modify the search path a program uses, like a PATH variable or classpath, or they can manipulate resources on the path to point to their malicious components. J2EE applications and other component based applications that are built from multiple binaries can have very long list of dependencies to execute. If one of these libraries and/or references is controllable by the attacker then application controls can be circumvented by the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- The attacker must be able to write to redirect search paths on the victim host.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Ensure that the program's compound parts, including all system dependencies, classpath, path, and so on, are secured to the same or higher level assurance as the program
- Implementation: Host integrity monitoring

## Related Weaknesses (CWE)
- CWE-426
- CWE-427
