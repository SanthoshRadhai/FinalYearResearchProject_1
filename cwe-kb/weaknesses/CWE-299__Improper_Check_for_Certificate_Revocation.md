# CWE-299: Improper Check for Certificate Revocation

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/299.html  

## Description
The product does not check or incorrectly checks the revocation status of a certificate, which may cause it to use a certificate that has been compromised.

## Extended Description
An improper check for certificate revocation is a far more serious flaw than related certificate failures. This is because the use of any revoked certificate is almost certainly malicious. The most common reason for certificate revocation is compromise of the system in question, with the result that no legitimate servers will be using a revoked certificate, unless they are sorely out of sync.

## Related Weaknesses
- ChildOf: CWE-295
- ChildOf: CWE-404

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — Trust may be assigned to an entity who is not who it claims to be.
- Scope: Integrity, Other; Impact: Other — Data from an untrusted (and possibly malicious) source may be integrated.
- Scope: Confidentiality; Impact: Read Application Data — Data may be disclosed to an entity impersonating a trusted entity, resulting in information disclosure.

## Potential Mitigations
- [Architecture and Design] Ensure that certificates are checked for revoked status.
- [Implementation] If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the revoked status.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The following OpenSSL code ensures that there is a certificate before continuing execution.
