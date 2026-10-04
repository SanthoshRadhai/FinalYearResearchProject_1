# CAPEC-695: Repo Jacking

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/695.html  

## Description
An adversary takes advantage of the redirect property of directly linked Version Control System (VCS) repositories to trick users into incorporating malicious code into their applications.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- Identification of a popular repository that may be directly referenced in numerous software applications
- A repository owner/maintainer who has recently changed their username or deleted their account

## Skills Required
- [Low] Ability to create an account on a VCS hosting site and recreate an existing directory structure.
- [Low] Ability to create malware that can exploit various software applications.

## Consequences
- Scope: Integrity; Impact: Read Data, Modify Data
- Scope: Access Control, Authorization; Impact: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges

## Mitigations
- Leverage dedicated package managers instead of directly linking to VCS repositories.
- Utilize version pinning and lock files to prevent use of maliciously modified repositories.
- Implement "vendoring" (i.e., including third-party dependencies locally) and leverage automated testing techniques (e.g., static analysis) to determine if the software behaves maliciously.
- Leverage automated tools, such as Checkmarx's "ChainJacking" tool, to determine susceptibility to Repo Jacking attacks.

## Related Weaknesses (CWE)
- CWE-494
- CWE-829
