# CWE-5: J2EE Misconfiguration: Data Transmission Without Encryption

**Abstraction:** Variant  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/5.html  

## Description
Information sent over a network can be compromised while in transit. An attacker may be able to read or modify the contents if the data are sent in plaintext or are weakly encrypted.

## Related Weaknesses
- ChildOf: CWE-319

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data
- Scope: Integrity; Impact: Modify Application Data

## Potential Mitigations
- [System Configuration] The product configuration should ensure that SSL or an encryption mechanism of equivalent strength and vetted reputation is used for all access-controlled pages.
