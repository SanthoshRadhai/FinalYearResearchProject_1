# CWE-599: Missing Validation of OpenSSL Certificate

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/599.html  

## Description
The product uses OpenSSL and trusts or uses a certificate without using the SSL_get_verify_result() function to ensure that the certificate satisfies all necessary security requirements.

## Related Weaknesses
- ChildOf: CWE-295

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data — The data read may not be properly secured - it might be viewed by an attacker.
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — Trust afforded to the system in question may allow for spoofing or redirection attacks.
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — If the certificate is not checked, it may be possible for a redirection or spoofing attack to allow a malicious host with a valid certificate to provide data under the guise of a trusted host. While the attacker in question may have a valid certificate, it may simply be a valid certificate for a different site. This could allow an attacker to use an invalid certificate to claim to be a trusted host, use expired certificates, or conduct other attacks that could be detected if the certificate is properly validated. In order to ensure data integrity, we must check that the certificate is valid, and that it pertains to the site we wish to access.

## Potential Mitigations
- [Architecture and Design] Ensure that proper authentication is included in the system design.
- [Implementation] Understand and properly implement all checks necessary to ensure the identity of entities involved in encrypted communications.

## Demonstrative Examples (summary)
- The following OpenSSL code ensures that the host has a certificate.
