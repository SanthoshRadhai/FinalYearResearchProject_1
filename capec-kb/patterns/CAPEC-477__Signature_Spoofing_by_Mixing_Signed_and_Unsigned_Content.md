# CAPEC-477: Signature Spoofing by Mixing Signed and Unsigned Content

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/477.html  

## Description
An attacker exploits the underlying complexity of a data structure that allows for both signed and unsigned content, to cause unsigned data to be processed as though it were signed data.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- Signer and recipient are using complex data storage structures that allow for a mix between signed and unsigned data
- Recipient is using signature verification software that does not maintain separation between signed and unsigned data once the signature has been verified.

## Skills Required
- [High] The attacker may need to continuously monitor a stream of signed data, waiting for an exploitable message to appear.
- [High] Attacker must be able to create malformed data blobs and know how to insert them in a location that the recipient will visit.

## Mitigations
- Ensure the application is fully patched and does not allow the processing of unsigned data as if it is signed data.

## Related Weaknesses (CWE)
- CWE-693
- CWE-311
- CWE-319
