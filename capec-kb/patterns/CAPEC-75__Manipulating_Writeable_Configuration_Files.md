# CAPEC-75: Manipulating Writeable Configuration Files

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/75.html  

## Description
Generally these are manually edited files that are not in the preview of the system administrators, any ability on the attackers' behalf to modify these files, for example in a CVS repository, gives unauthorized access directly to the application, the same as authorized users.

## Related Attack Patterns
- ChildOf: CAPEC-176

## Prerequisites
- Configuration files must be modifiable by the attacker

## Skills Required
- [Medium] To identify vulnerable configuration files, and understand how to manipulate servers and erase forensic evidence

## Consequences
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- Design: Enforce principle of least privilege
- Design: Backup copies of all configuration files
- Implementation: Integrity monitoring for configuration files
- Implementation: Enforce audit logging on code and configuration promotion procedures.
- Implementation: Load configuration from separate process and memory space, for example a separate physical device like a CD

## Related Weaknesses (CWE)
- CWE-349
- CWE-99
- CWE-77
- CWE-346
- CWE-353
- CWE-354
