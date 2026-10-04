# CWE-1261: Improper Handling of Single Event Upsets

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1261.html  

## Description
The hardware logic does not effectively handle when single-event upsets (SEUs) occur.

## Extended Description
Technology trends such as CMOS-transistor down-sizing, use of new materials, and system-on-chip architectures continue to increase the sensitivity of systems to soft errors. These errors are random, and their causes might be internal (e.g., interconnect coupling) or external (e.g., cosmic radiation). These soft errors are not permanent in nature and cause temporary bit flips known as single-event upsets (SEUs). SEUs are induced errors in circuits caused when charged particles lose energy by ionizing the medium through which they pass, leaving behind a wake of electron-hole pairs that cause temporary failures. If these failures occur in security-sensitive modules in a chip, it might compromise the security guarantees of the chip. For instance, these temporary failures could be bit flips that change the privilege of a regular user to root.

## Related Weaknesses
- ChildOf: CWE-1384
- PeerOf: CWE-1254

## Common Consequences
- Scope: Availability, Access Control; Impact: DoS: Crash, Exit, or Restart, DoS: Instability, Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] Implement triple-modular redundancy around security-sensitive modules.
- [Architecture and Design] SEUs mostly affect SRAMs. For SRAMs storing security-critical data, implement Error-Correcting-Codes (ECC) and Address Interleaving.

## Demonstrative Examples (summary)
- This is an example from [REF-1089]. See the reference for full details of this issue.
- In 2016, a security researcher, who was also a patient using a pacemaker, was on an airplane when a bit flip occurred in the pacemaker, likely due to the higher prevalence of cosmic radiation at such heights. The pacemaker was designed to account for bit flips and went into a default safe mode, which still forced the patient to go to a hospital to get it reset. The bit flip also inadvertently enabled the researcher to access the crash file, perform reverse engineering, and detect a hard-coded key. [REF-1101]
