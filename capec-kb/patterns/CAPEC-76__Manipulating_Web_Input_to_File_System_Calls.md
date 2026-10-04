# CAPEC-76: Manipulating Web Input to File System Calls

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/76.html  

## Description
An attacker manipulates inputs to the target software which the target software passes to file system calls in the OS. The goal is to gain access to, and perhaps modify, areas of the file system that the target software did not intend to be accessible.

## Related Attack Patterns
- ChildOf: CAPEC-126

## Prerequisites
- Program must allow for user controlled variables to be applied directly to the filesystem

## Skills Required
- [Low] To identify file system entry point and execute against an over-privileged system interface

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Design: Enforce principle of least privilege.
- Design: Ensure all input is validated, and does not contain file system commands
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Design: For interactive user applications, consider if direct file system interface is necessary, instead consider having the application proxy communication.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Related Weaknesses (CWE)
- CWE-23
- CWE-22
- CWE-73
- CWE-77
- CWE-346
- CWE-348
- CWE-285
- CWE-272
- CWE-59
- CWE-74
- CWE-15
