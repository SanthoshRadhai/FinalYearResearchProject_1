# CAPEC-693: StarJacking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/693.html  

## Description
An adversary spoofs software popularity metadata to deceive users into believing that a maliciously provided package is widely used and originates from a trusted source.

## Related Attack Patterns
- ChildOf: CAPEC-691

## Prerequisites
- Identification of a popular open-source package whose popularity metadata is to be used for the malicious package.

## Skills Required
- [Low] Ability to provide a package to a package manager and associate a popular package's source code repository URL.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Accountability; Impact: Hide Activities
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Before downloading open-source packages, perform precursory metadata checks to determine the author(s), frequency of updates, when the software was last updated, and if the software is widely leveraged.
- Look for conflicting or non-unique repository references to determine if multiple packages share the same repository reference.
- Reference vulnerability databases to determine if the software contains known vulnerabilities.
- Only download open-source packages from reputable package managers.
- After downloading open-source packages, ensure integrity values have not changed.
- Before executing or incorporating the package, leverage automated testing techniques (e.g., static and dynamic analysis) to determine if the software behaves maliciously.

## Related Weaknesses (CWE)
- CWE-494
