# CWE-324: Use of a Key Past its Expiration Date

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/324.html  

## Description
The product uses a cryptographic key or password past its expiration date, which diminishes its safety significantly by increasing the timing window for cracking attacks against that key.

## Extended Description
While the expiration of keys does not necessarily ensure that they are compromised, it is a significant concern that keys which remain in use for prolonged periods of time have a decreasing probability of integrity. For this reason, it is important to replace keys within a period of time proportional to their strength.

## Related Weaknesses
- ChildOf: CWE-672
- PeerOf: CWE-298

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism, Gain Privileges or Assume Identity — The cryptographic key in question may be compromised, providing a malicious user with a method for authenticating as the victim.

## Potential Mitigations
- [Architecture and Design] Adequate consideration should be put in to the user interface in order to notify users previous to the key's expiration, to explain the importance of new key generation and to walk users through the process as painlessly as possible.

## Demonstrative Examples (summary)
- The following code attempts to verify that a certificate is valid.
