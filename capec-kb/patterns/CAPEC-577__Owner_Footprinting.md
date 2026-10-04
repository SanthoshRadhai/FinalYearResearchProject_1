# CAPEC-577: Owner Footprinting

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Low  
**Reference:** https://capec.mitre.org/data/definitions/577.html  

## Description
An adversary exploits functionality meant to identify information about the primary users on the target system to an authorized user. They may do this, for example, by reviewing logins or file modification times. By knowing what owners use the target system, the adversary can inform further and more targeted malicious behavior. An example Windows command that may accomplish this is "dir /A ntuser.dat". Which will display the last modified time of a user's ntuser.dat file when run within the root folder of a user. This time is synonymous with the last time that user was logged in.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.
- Administrator permissions are required to view the home folder of other users.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism, Hide Activities

## Mitigations
- Ensure that proper permissions on files and folders are enacted to limit accessibility.

## Related Weaknesses (CWE)
- CWE-200
