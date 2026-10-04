# CWE-1282: Assumed-Immutable Data is Stored in Writable Memory

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1282.html  

## Description
Immutable data, such as a first-stage bootloader, device identifiers, and "write-once" configuration settings are stored in writable memory that can be re-programmed or updated in the field.

## Extended Description
Security services such as secure boot, authentication of code and data, and device attestation all require assets such as the first stage bootloader, public keys, golden hash digests, etc. which are implicitly trusted. Storing these assets in read-only memory (ROM), fuses, or one-time programmable (OTP) memory provides strong integrity guarantees and provides a root of trust for securing the rest of the system. Security is lost if assets assumed to be immutable can be modified.

## Related Weaknesses
- ChildOf: CWE-668
- CanPrecede: CWE-471

## Common Consequences
- Scope: Integrity; Impact: Varies by Context

## Potential Mitigations
- [Implementation] All immutable code or data should be programmed into ROM or write-once memory.

## Demonstrative Examples (summary)
- Cryptographic hash functions are commonly used to create unique fixed-length digests used to ensure the integrity of code and keys. A golden digest is stored on the device and compared to the digest computed from the data to be verified. If the digests match, the data has not been maliciously modified. If an attacker can modify the golden digest they then have the ability to store arbitrary data that passes the verification check. Hash digests used to verify public keys and early stage boot code should be immutable, with the strongest protection offered by hardware immutability.
