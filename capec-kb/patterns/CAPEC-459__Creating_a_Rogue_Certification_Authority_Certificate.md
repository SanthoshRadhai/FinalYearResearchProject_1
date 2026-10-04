# CAPEC-459: Creating a Rogue Certification Authority Certificate

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/459.html  

## Description
An adversary exploits a weakness resulting from using a hashing algorithm with weak collision resistance to generate certificate signing requests (CSR) that contain collision blocks in their "to be signed" parts. The adversary submits one CSR to be signed by a trusted certificate authority then uses the signed blob to make a second certificate appear signed by said certificate authority. Due to the hash collision, both certificates, though different, hash to the same value and so the signed blob works just as well in the second certificate. The net effect is that the adversary's second X.509 certificate, which the Certification Authority has never seen, is now signed and validated by that Certification Authority.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- Certification Authority is using a hash function with insufficient collision resistance to generate the certificate hash to be signed

## Skills Required
- [High] Understanding of how to force a hash collision in X.509 certificates
- [High] An attacker must be able to craft two X.509 certificates that produce the same hash value
- [Medium] Knowledge needed to set up a certification authority

## Resources Required
- Knowledge of a certificate authority that uses hashing algorithms with poor collision resistance
- A valid certificate request and a malicious certificate request with identical hash values

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Mitigations
- Certification Authorities need to stop using deprecated or cryptographically insecure hashing algorithms to hash the certificates that they are about to sign. Instead they should be using stronger hashing functions such as SHA-256 or SHA-512.

## Related Weaknesses (CWE)
- CWE-327
- CWE-295
- CWE-290
