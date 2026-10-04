# CAPEC-234: Hijacking a privileged process

**Abstraction:** Standard  
**Status:** Draft  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/234.html  

## Description
An adversary gains control of a process that is assigned elevated privileges in order to execute arbitrary code with those privileges. Some processes are assigned elevated privileges on an operating system, usually through association with a particular user, group, or role. If an attacker can hijack this process, they will be able to assume its level of privilege in order to execute their own code.

## Related Attack Patterns
- ChildOf: CAPEC-233
- CanFollow: CAPEC-242
- CanFollow: CAPEC-175
- CanFollow: CAPEC-100

## Prerequisites
- The targeted process or operating system must contain a bug that allows attackers to hijack the targeted process.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Related Weaknesses (CWE)
- CWE-732
- CWE-648
