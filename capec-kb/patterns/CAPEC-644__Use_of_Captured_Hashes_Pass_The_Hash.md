# CAPEC-644: Use of Captured Hashes (Pass The Hash)

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/644.html  

## Description
An adversary obtains (i.e. steals or purchases) legitimate Windows domain credential hash values to access systems within the domain that leverage the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.

## Related Attack Patterns
- ChildOf: CAPEC-653
- CanPrecede: CAPEC-151
- CanPrecede: CAPEC-165
- CanPrecede: CAPEC-549
- CanPrecede: CAPEC-545

## Prerequisites
- The system/application is connected to the Windows domain.
- The system/application leverages the Lan Man (LM) and/or NT Lan Man (NTLM) authentication protocols.
- The adversary possesses known Windows credential hash value pairs that exist on the target domain.

## Skills Required
- [Low] Once an adversary obtains a known Windows credential hash value pair, leveraging it is trivial.

## Resources Required
- A list of known Window credential hash value pairs for the targeted domain.

## Consequences
- Scope: Confidentiality, Access Control, Authentication; Impact: Gain Privileges
- Scope: Confidentiality, Authorization; Impact: Read Data
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Prevent the use of Lan Man and NT Lan Man authentication on severs and apply patch KB2871997 to Windows 7 and higher systems.
- Leverage multi-factor authentication for all authentication services and prior to granting an entity access to the domain network.
- Monitor system and domain logs for abnormal credential access.
- Create a strong password policy and ensure that your system enforces this policy.
- Leverage system penetration testing and other defense in depth methods to determine vulnerable systems within a domain.

## Related Weaknesses (CWE)
- CWE-522
- CWE-836
- CWE-308
- CWE-294
- CWE-308
