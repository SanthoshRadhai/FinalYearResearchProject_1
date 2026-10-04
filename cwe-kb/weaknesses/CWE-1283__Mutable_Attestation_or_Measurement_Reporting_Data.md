# CWE-1283: Mutable Attestation or Measurement Reporting Data

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1283.html  

## Description
The register contents used for attestation or measurement reporting data to verify boot flow are modifiable by an adversary.

## Extended Description
A System-on-Chip (SoC) implements secure boot or verified boot. During this boot flow, the SoC often measures the code that it authenticates. The measurement is usually done by calculating the one-way hash of the code binary and extending it to the previous hash. The hashing algorithm should be a Secure One-Way hash function. The final hash, i.e., the value obtained after the completion of the boot flow, serves as the measurement data used in reporting or in attestation. The calculated hash is often stored in registers that can later be read by the party of interest to determine tampering of the boot flow. A common weakness is that the contents in these registers are modifiable by an adversary, thus spoofing the measurement.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data

## Potential Mitigations
- [Architecture and Design] Measurement data should be stored in registers that are read-only or otherwise have access controls that prevent modification by an untrusted agent.

## Demonstrative Examples (summary)
- The SoC extends the hash and stores the results in registers. Without protection, an adversary can write their chosen hash values to these registers. Thus, the attacker controls the reported results.
