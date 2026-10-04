# CAPEC-463: Padding Oracle Crypto Attack

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/463.html  

## Description
An adversary is able to efficiently decrypt data without knowing the decryption key if a target system leaks data on whether or not a padding error happened while decrypting the ciphertext. A target system that leaks this type of information becomes the padding oracle and an adversary is able to make use of that oracle to efficiently decrypt data without knowing the decryption key by issuing on average 128*b calls to the padding oracle (where b is the number of bytes in the ciphertext block). In addition to performing decryption, an adversary is also able to produce valid ciphertexts (i.e., perform encryption) by using the padding oracle, all without knowing the encryption key.

## Related Attack Patterns
- ChildOf: CAPEC-97

## Prerequisites
- The decryption routine does not properly authenticate the message / does not verify its integrity prior to performing the decryption operation
- The target system leaks data (in some way) on whether a padding error has occurred when attempting to decrypt the ciphertext.
- The padding oracle remains available for enough time / for as many requests as needed for the adversary to decrypt the ciphertext.

## Resources Required
- Ability to detect instances where a target system is vulnerable to an oracle padding attack Sufficient cryptography knowledge and tools needed to take advantage of the presence of the padding oracle to perform decryption / encryption of data without a key

## Mitigations
- Design: Use a message authentication code (MAC) or another mechanism to perform verification of message authenticity / integrity prior to decryption
- Implementation: Do not leak information back to the user as to any cryptography (e.g., padding) encountered during decryption.

## Related Weaknesses (CWE)
- CWE-209
- CWE-514
- CWE-649
- CWE-347
- CWE-354
- CWE-696
