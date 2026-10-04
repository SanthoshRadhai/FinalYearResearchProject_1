# CAPEC-97: Cryptanalysis

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/97.html  

## Description
Cryptanalysis is a process of finding weaknesses in cryptographic algorithms and using these weaknesses to decipher the ciphertext without knowing the secret key (instance deduction). Sometimes the weakness is not in the cryptographic algorithm itself, but rather in how it is applied that makes cryptanalysis successful. An attacker may have other goals as well, such as: Total Break (finding the secret key), Global Deduction (finding a functionally equivalent algorithm for encryption and decryption that does not require knowledge of the secret key), Information Deduction (gaining some information about plaintexts or ciphertexts that was not previously known) and Distinguishing Algorithm (the attacker has the ability to distinguish the output of the encryption (ciphertext) from a random permutation of bits).

## Related Attack Patterns
- ChildOf: CAPEC-192
- CanPrecede: CAPEC-20

## Prerequisites
- The target software utilizes some sort of cryptographic algorithm.
- An underlying weaknesses exists either in the cryptographic algorithm used or in the way that it was applied to a particular chunk of plaintext.
- The encryption algorithm is known to the attacker.
- An attacker has access to the ciphertext.

## Skills Required
- [High] Cryptanalysis generally requires a very significant level of understanding of mathematics and computation.

## Resources Required
- Computing resource requirements will vary based on the complexity of a given cryptanalysis technique. Access to the encryption/decryption routines of the algorithm is also required.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Use proven cryptographic algorithms with recommended key sizes.
- Ensure that the algorithms are used properly. That means: 1. Not rolling out your own crypto; Use proven algorithms and implementations. 2. Choosing initialization vectors with sufficiently random numbers 3. Generating key material using good sources of randomness and avoiding known weak keys 4. Using proven protocols and their implementations. 5. Picking the most appropriate cryptographic algorithm for your usage context and data

## Related Weaknesses (CWE)
- CWE-327
- CWE-1204
- CWE-1240
- CWE-1241
- CWE-1279
