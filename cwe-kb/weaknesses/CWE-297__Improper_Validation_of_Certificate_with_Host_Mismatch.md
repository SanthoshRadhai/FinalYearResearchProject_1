# CWE-297: Improper Validation of Certificate with Host Mismatch

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/297.html  

## Description
The product communicates with a host that provides a certificate, but the product does not properly ensure that the certificate is actually associated with that host.

## Extended Description
Even if a certificate is well-formed, signed, and follows the chain of trust, it may simply be a valid certificate for a different site than the site that the product is interacting with. In order to ensure data integrity, the certificate must be valid, and it must pertain to the site that is being accessed. Even if the product attempts to check the hostname, it is still possible to incorrectly check the hostname. For example, attackers could create a certificate with a name that begins with a trusted name followed by a NUL byte, which could cause some string-based comparisons to only examine the portion that contains the trusted name.

## Related Weaknesses
- ChildOf: CWE-923
- ChildOf: CWE-295

## Common Consequences
- Scope: Access Control; Impact: Gain Privileges or Assume Identity — The data read from the system vouched for by the certificate may not be from the expected system.
- Scope: Authentication, Other; Impact: Other — Trust afforded to the system in question - based on the malicious certificate - may allow for spoofing or redirection attacks.
- Scope: Access Control, Other; Impact: Gain Privileges or Assume Identity, Other — If the certificate's host-specific data is not properly checked - such as the Common Name (CN) in the Subject or the Subject Alternative Name (SAN) extension of an X.509 certificate - it may be possible for a redirection or spoofing attack to allow a malicious host with a valid certificate to provide data, impersonating a trusted host.

## Potential Mitigations
- [Architecture and Design] Fully check the hostname of the certificate and provide the user with adequate information about the nature of the problem and how to proceed.
- [Implementation] If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)
- [Dynamic Analysis with Manual Results Interpretation] Set up an untrusted endpoint (e.g. a server) with which the product will connect. Create a test certificate that uses an invalid hostname but is signed by a trusted CA and provide this certificate from the untrusted endpoint. If the product performs any operations instead of disconnecting and reporting an error, then this indicates that the hostname is not being checked and the test certificate has been accepted.
- [Black Box] When Certificate Pinning is being used in a mobile application, consider using a tool such as Spinner [REF-955]. This methodology might be extensible to other technologies.

## Demonstrative Examples (summary)
- The following OpenSSL code obtains a certificate and verifies it.
