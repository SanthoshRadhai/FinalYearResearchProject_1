# CAPEC-253: Remote Code Inclusion

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/253.html  

## Description
The attacker forces an application to load arbitrary code files from a remote location. The attacker could use this to try to load old versions of library files that have known vulnerabilities, to load malicious files that the attacker placed on the remote machine, or to otherwise change the functionality of the targeted application in unexpected ways.

## Related Attack Patterns
- ChildOf: CAPEC-175
- CanPrecede: CAPEC-664

## Prerequisites
- Target application server must allow remote files to be included.The malicious file must be placed on the remote machine previously.

## Mitigations
- Minimize attacks by input validation and sanitization of any user data that will be used by the target application to locate a remote file to be included.

## Related Weaknesses (CWE)
- CWE-829
