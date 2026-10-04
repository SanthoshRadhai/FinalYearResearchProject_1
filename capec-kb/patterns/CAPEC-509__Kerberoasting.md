# CAPEC-509: Kerberoasting

**Abstraction:** Detailed  
**Status:** Stable  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/509.html  

## Description
Through the exploitation of how service accounts leverage Kerberos authentication with Service Principal Names (SPNs), the adversary obtains and subsequently cracks the hashed credentials of a service account target to exploit its privileges. The Kerberos authentication protocol centers around a ticketing system which is used to request/grant access to services and to then access the requested services. As an authenticated user, the adversary may request Active Directory and obtain a service ticket with portions encrypted via RC4 with the private key of the authenticated account. By extracting the local ticket and saving it disk, the adversary can brute force the hashed value to reveal the target account credentials.

## Related Attack Patterns
- ChildOf: CAPEC-652
- CanPrecede: CAPEC-151

## Prerequisites
- The adversary requires access as an authenticated user on the system. This attack pattern relates to elevating privileges.
- The adversary requires use of a third-party credential harvesting tool (e.g., Mimikatz).
- The adversary requires a brute force tool.

## Consequences
- Scope: Confidentiality; Impact: Gain Privileges

## Mitigations
- Monitor system and domain logs for abnormal access.
- Employ a robust password policy for service accounts. Passwords should be of adequate length and complexity, and they should expire after a period of time.
- Employ the principle of least privilege: limit service accounts privileges to what is required for functionality and no more.
- Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible.

## Related Weaknesses (CWE)
- CWE-522
- CWE-308
- CWE-309
- CWE-294
- CWE-263
- CWE-262
- CWE-521
