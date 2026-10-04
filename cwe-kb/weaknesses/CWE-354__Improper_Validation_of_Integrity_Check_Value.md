# CWE-354: Improper Validation of Integrity Check Value

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/354.html  

## Description
The product does not validate or incorrectly validates the integrity check values or "checksums" of a message. This may prevent it from detecting if the data has been modified or corrupted in transmission.

## Extended Description
Improper validation of checksums before use results in an unnecessary risk that can easily be mitigated. The protocol specification describes the algorithm used for calculating the checksum. It is then a simple matter of implementing the calculation and verifying that the calculated checksum and the received checksum match. Improper verification of the calculated checksum and the received checksum can lead to far greater consequences.

## Related Weaknesses
- ChildOf: CWE-345
- ChildOf: CWE-345
- ChildOf: CWE-754
- PeerOf: CWE-353

## Common Consequences
- Scope: Integrity, Other; Impact: Modify Application Data, Other — Integrity checks usually use a secret key that helps authenticate the data origin. Skipping integrity checking generally opens up the possibility that new data from an invalid source can be injected.
- Scope: Integrity, Other; Impact: Other — Data that is parsed and used may be corrupted.
- Scope: Non-Repudiation, Other; Impact: Hide Activities, Other — Without a checksum check, it is impossible to determine if any changes have been made to the data after it was sent.

## Potential Mitigations
- [Implementation] Ensure that the checksums present in messages are properly checked in accordance with the protocol specification before they are parsed and used.

## Demonstrative Examples (summary)
- The following example demonstrates the weakness.
