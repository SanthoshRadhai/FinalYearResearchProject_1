# CWE-1301: Insufficient or Incomplete Data Removal within Hardware Component

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1301.html  

## Description
The product's data removal process does not completely delete all data and potentially sensitive information within hardware components.

## Extended Description
Physical properties of hardware devices, such as remanence of magnetic media, residual charge of ROMs/RAMs, or screen burn-in may still retain sensitive data after a data removal process has taken place and power is removed. Recovering data after erasure or overwriting is possible due to a phenomenon called data remanence. For example, if the same value is written repeatedly to a memory location, the corresponding memory cells can become physically altered to a degree such that even after the original data is erased that data can still be recovered through physical characterization of the memory cells.

## Related Weaknesses
- ChildOf: CWE-226

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory, Read Application Data

## Potential Mitigations
- [Architecture and Design] Apply blinding or masking techniques to implementations of cryptographic algorithms.
- [Implementation] Alter the method of erasure, add protection of media, or destroy the media to protect the data.
