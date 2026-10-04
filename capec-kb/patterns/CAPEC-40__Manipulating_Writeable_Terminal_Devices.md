# CAPEC-40: Manipulating Writeable Terminal Devices

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/40.html  

## Description
This attack exploits terminal devices that allow themselves to be written to by other users. The attacker sends command strings to the target terminal device hoping that the target user will hit enter and thereby execute the malicious command with their privileges. The attacker can send the results (such as copying /etc/passwd) to a known directory and collect once the attack has succeeded.

## Related Attack Patterns
- ChildOf: CAPEC-248

## Prerequisites
- User terminals must have a permissive access control such as world writeable that allows normal users to control data on other user's terminals.

## Skills Required
- [Low] Ability to discover permissions on terminal devices. Of course, brute force can also be used.

## Resources Required
- Access to a terminal on the target network

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Integrity, Availability; Impact: Execute Unauthorized Commands

## Mitigations
- Design: Ensure that terminals are only writeable by named owner user and/or administrator
- Design: Enforce principle of least privilege

## Related Weaknesses (CWE)
- CWE-77
