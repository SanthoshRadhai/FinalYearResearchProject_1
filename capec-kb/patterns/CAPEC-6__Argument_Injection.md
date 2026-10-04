# CAPEC-6: Argument Injection

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/6.html  

## Description
An attacker changes the behavior or state of a targeted application through injecting data or command syntax through the targets use of non-validated and non-filtered arguments of exposed services or methods.

## Related Attack Patterns
- ChildOf: CAPEC-137

## Prerequisites
- Target software fails to strip all user-supplied input of any content that could cause the shell to perform unexpected actions.
- Software must allow for unvalidated or unfiltered input to be executed on operating system shell, and, optionally, the system configuration must allow for output to be sent back to client.

## Skills Required
- [Medium] The attacker has to identify injection vector, identify the operating system-specific commands, and optionally collect the output.

## Resources Required
- Ability to communicate synchronously or asynchronously with server. Optionally, ability to capture output directly through synchronous communication or other method such as FTP.

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Design: Do not program input values directly on command shell, instead treat user input as guilty until proven innocent. Build a function that takes user input and converts it to applications specific types and values, stripping or filtering out all unauthorized commands and characters in the process.
- Design: Limit program privileges, so if metacharacters or other methods circumvent program input validation routines and shell access is attained then it is not running under a privileged account. chroot jails create a sandbox for the application to execute in, making it more difficult for an attacker to elevate privilege even in the case that a compromise has occurred.
- Implementation: Implement an audit log that is written to a separate host, in the event of a compromise the audit log may be able to provide evidence and details of the compromise.

## Related Weaknesses (CWE)
- CWE-74
- CWE-146
- CWE-184
- CWE-78
- CWE-185
- CWE-697
