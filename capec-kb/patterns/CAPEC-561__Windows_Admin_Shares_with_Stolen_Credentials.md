# CAPEC-561: Windows Admin Shares with Stolen Credentials

**Abstraction:** Detailed  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/561.html  

## Description
An adversary guesses or obtains (i.e. steals or purchases) legitimate Windows administrator credentials (e.g. userID/password) to access Windows Admin Shares on a local machine or within a Windows domain.

## Related Attack Patterns
- ChildOf: CAPEC-653
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-165
- CanPrecede: CAPEC-549
- CanPrecede: CAPEC-545

## Prerequisites
- The system/application is connected to the Windows domain.
- The target administrative share allows remote use of local admin credentials to log into domain systems.
- The adversary possesses a list of known Windows administrator credentials that exist on the target domain.

## Skills Required
- [Low] Once an adversary obtains a known Windows credential, leveraging it is trivial.

## Resources Required
- A list of known Windows administrator credentials for the targeted domain.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Do not reuse local administrator account credentials across systems.
- Deny remote use of local admin credentials to log into domain systems.
- Do not allow accounts to be a local administrator on more than one system.

## Related Weaknesses (CWE)
- CWE-522
- CWE-308
- CWE-309
- CWE-294
- CWE-263
- CWE-262
- CWE-521
