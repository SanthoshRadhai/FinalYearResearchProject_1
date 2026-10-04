# CWE-325: Missing Cryptographic Step

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/325.html  

## Description
The product does not implement a required step in a cryptographic algorithm, resulting in weaker encryption than advertised by the algorithm.

## Related Weaknesses
- ChildOf: CWE-1240
- ChildOf: CWE-573
- PeerOf: CWE-358

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism
- Scope: Confidentiality, Integrity; Impact: Read Application Data, Modify Application Data
- Scope: Accountability, Non-Repudiation; Impact: Hide Activities

## Detection Methods
- [Automated Static Analysis] Automated static analysis, commonly referred to as Static Application Security Testing (SAST), can find some instances of this weakness by analyzing source code (or binary/compiled code) without having to execute it. Typically, this is done by building a model of data flow and control flow, then searching for potentially-vulnerable patterns that connect "sources" (origins of input) with "sinks" (destinations where the data interacts with external components, a lower layer such as the OS, etc.)

## Demonstrative Examples (summary)
- The example code is taken from the HMAC engine inside the buggy OpenPiton SoC of HACK@DAC'21 [REF-1358]. HAMC is a message authentication code (MAC) that uses both a hash and a secret crypto key. The HMAC engine in HACK@DAC SoC uses the SHA-256 module for the calculation of the HMAC for 512 bits messages.
