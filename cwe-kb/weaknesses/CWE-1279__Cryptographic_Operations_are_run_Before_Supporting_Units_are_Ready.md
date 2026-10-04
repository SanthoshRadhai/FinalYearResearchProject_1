# CWE-1279: Cryptographic Operations are run Before Supporting Units are Ready

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1279.html  

## Description
Performing cryptographic operations without ensuring that the supporting inputs are ready to supply valid data may compromise the cryptographic result.

## Extended Description
Many cryptographic hardware units depend upon other hardware units to supply information to them to produce a securely encrypted result. For example, a cryptographic unit that depends on an external random-number-generator (RNG) unit for entropy must wait until the RNG unit is producing random numbers. If a cryptographic unit retrieves a private encryption key from a fuse unit, the fuse unit must be up and running before a key may be supplied.

## Related Weaknesses
- ChildOf: CWE-696
- ChildOf: CWE-665

## Common Consequences
- Scope: Access Control, Confidentiality, Integrity, Availability, Accountability, Authentication, Authorization, Non-Repudiation; Impact: Varies by Context

## Potential Mitigations
- [Architecture and Design] Best practices should be used to design cryptographic systems.
- [Implementation] Continuously ensuring that cryptographic inputs are supplying valid information is necessary to ensure that the encrypted output is secure.

## Demonstrative Examples (summary)
- The following pseudocode illustrates the weak encryption resulting from the use of a pseudo-random-number generator output.
