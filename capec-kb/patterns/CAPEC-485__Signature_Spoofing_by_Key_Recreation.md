# CAPEC-485: Signature Spoofing by Key Recreation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/485.html  

## Description
An attacker obtains an authoritative or reputable signer's private signature key by exploiting a cryptographic weakness in the signature algorithm or pseudorandom number generation and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- An authoritative signer is using a weak method of random number generation or weak signing software that causes key leakage or permits key inference.
- An authoritative signer is using a signature algorithm with a direct weakness or with poorly chosen parameters that enable the key to be recovered using signatures from that signer.

## Skills Required
- [High] Cryptanalysis of signature generation algorithm
- [High] Reverse engineering and cryptanalysis of signature generation algorithm implementation and random number generation
- [High] Ability to create malformed data blobs and know how to present them directly or indirectly to a victim.

## Mitigations
- Ensure cryptographic elements have been sufficiently tested for weaknesses.

## Related Weaknesses (CWE)
- CWE-330
