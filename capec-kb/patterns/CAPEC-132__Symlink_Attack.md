# CAPEC-132: Symlink Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/132.html  

## Description
An adversary positions a symbolic link in such a manner that the targeted user or application accesses the link's endpoint, assuming that it is accessing a file with the link's name.

## Related Attack Patterns
- ChildOf: CAPEC-159

## Prerequisites
- The targeted application must perform the desired activities on a file without checking whether the file is a symbolic link or not. The adversary must be able to predict the name of the file the target application is modifying and be able to create a new symbolic link where that file would appear.

## Skills Required
- [Low] To create symlinks
- [High] To identify the files and create the symlinks during the file operation time window

## Resources Required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to create the necessary symbolic link.

## Consequences
- Scope: Confidentiality; Impact: Other
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality; Impact: Read Data
- Scope: Integrity; Impact: Modify Data
- Scope: Authorization; Impact: Execute Unauthorized Commands
- Scope: Accountability, Authentication, Authorization, Non-Repudiation; Impact: Gain Privileges
- Scope: Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Availability; Impact: Unreliable Execution

## Mitigations
- Design: Check for the existence of files to be created, if in existence verify they are neither symlinks nor hard links before opening them.
- Implementation: Use randomly generated file names for temporary files. Give the files restrictive permissions.

## Related Weaknesses (CWE)
- CWE-59
