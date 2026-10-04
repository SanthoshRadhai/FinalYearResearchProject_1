# CAPEC-475: Signature Spoofing by Improper Validation

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/475.html  

## Description
An adversary exploits a cryptographic weakness in the signature verification algorithm implementation to generate a valid signature without knowing the key.

## Related Attack Patterns
- ChildOf: CAPEC-473
- CanPrecede: CAPEC-542

## Prerequisites
- Recipient is using a weak cryptographic signature verification algorithm or a weak implementation of a cryptographic signature verification algorithm, or the configuration of the recipient's application accepts the use of keys generated using cryptographically weak signature verification algorithms.

## Skills Required
- [High] Cryptanalysis of signature verification algorithm
- [High] Reverse engineering and cryptanalysis of signature verification algorithm implementation

## Mitigations
- Use programs and products that contain cryptographic elements that have been thoroughly tested for flaws in the signature verification routines.

## Related Weaknesses (CWE)
- CWE-347
- CWE-327
- CWE-295
