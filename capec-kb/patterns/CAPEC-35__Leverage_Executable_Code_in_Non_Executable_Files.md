# CAPEC-35: Leverage Executable Code in Non-Executable Files

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/35.html  

## Description
An attack of this type exploits a system's trust in configuration and resource files. When the executable loads the resource (such as an image file or configuration file) the attacker has modified the file to either execute malicious code directly or manipulate the target process (e.g. application server) to execute based on the malicious configuration parameters. Since systems are increasingly interrelated mashing up resources from local and remote sources the possibility of this attack occurring is high.

## Related Attack Patterns
- ChildOf: CAPEC-636
- PeerOf: CAPEC-23
- PeerOf: CAPEC-75

## Prerequisites
- The attacker must have the ability to modify non-executable files consumed by the target software.

## Skills Required
- [Low] To identify and execute against an over-privileged system interface

## Resources Required
- Ability to communicate synchronously or asynchronously with server that publishes an over-privileged directory, program, or interface. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Run server interfaces with a non-root account and/or utilize chroot jails or other configuration techniques to constrain privileges even if attacker gains some limited access to commands.
- Implementation: Perform testing such as pen-testing and vulnerability scanning to identify directories, programs, and interfaces that grant direct access to executables.
- Implementation: Implement host integrity monitoring to detect any unwanted altering of configuration files.
- Implementation: Ensure that files that are not required to execute, such as configuration files, are not over-privileged, i.e. not allowed to execute.

## Related Weaknesses (CWE)
- CWE-94
- CWE-96
- CWE-95
- CWE-97
- CWE-272
- CWE-59
- CWE-282
- CWE-270
