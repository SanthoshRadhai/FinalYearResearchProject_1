# CWE-370: Missing Check for Certificate Revocation after Initial Check

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/370.html  

## Description
The product does not check the revocation status of a certificate after its initial revocation check, which can cause the product to perform privileged actions even after the certificate is revoked at a later time.

## Extended Description
If the revocation status of a certificate is not checked before each action that requires privileges, the system may be subject to a race condition. If a certificate is revoked after the initial check, all subsequent actions taken with the owner of the revoked certificate will lose all benefits guaranteed by the certificate. In fact, it is almost certain that the use of a revoked certificate indicates malicious activity.

## Related Weaknesses
- ChildOf: CWE-299
- PeerOf: CWE-296
- PeerOf: CWE-297
- PeerOf: CWE-298

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — Trust may be assigned to an entity who is not who it claims to be.
- Scope: Integrity; Impact: Modify Application Data — Data from an untrusted (and possibly malicious) source may be integrated.
- Scope: Confidentiality; Impact: Read Application Data — Data may be disclosed to an entity impersonating a trusted entity, resulting in information disclosure.

## Potential Mitigations
- [Architecture and Design] Ensure that certificates are checked for revoked status before each use of a protected resource. If the certificate is checked before each access of a protected resource, the delay subject to a possible race condition becomes almost negligible and significantly reduces the risk associated with this issue.

## Demonstrative Examples (summary)
- The following code checks a certificate before performing an action.
