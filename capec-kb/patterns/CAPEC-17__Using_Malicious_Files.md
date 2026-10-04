# CAPEC-17: Using Malicious Files

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/17.html  

## Description
An attack of this type exploits a system's configuration that allows an adversary to either directly access an executable file, for example through shell access; or in a possible worst case allows an adversary to upload a file and then execute it. Web servers, ftp servers, and message oriented middleware systems which have many integration points are particularly vulnerable, because both the programmers and the administrators must be in synch regarding the interfaces and the correct privileges for each interface.

## Related Attack Patterns
- ChildOf: CAPEC-122
- CanPrecede: CAPEC-233

## Prerequisites
- System's configuration must allow an attacker to directly access executable files or upload files to execute. This means that any access control system that is supposed to mediate communications between the subject and the object is set incorrectly or assumes a benign environment.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Resources Required
- Ability to communicate synchronously or asynchronously with server that publishes an over-privileged directory, program, or interface. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.

## Related Weaknesses (CWE)
- CWE-732
- CWE-285
- CWE-272
- CWE-59
- CWE-282
- CWE-270
- CWE-693
