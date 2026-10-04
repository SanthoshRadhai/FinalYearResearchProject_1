# CWE-1312: Missing Protection for Mirrored Regions in On-Chip Fabric Firewall

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1312.html  

## Description
The firewall in an on-chip fabric protects the main addressed region, but it does not protect any mirrored memory or memory-mapped-IO (MMIO) regions.

## Extended Description
Few fabrics mirror memory and address ranges, where mirrored regions contain copies of the original data. This redundancy is used to achieve fault tolerance. Whatever protections the fabric firewall implements for the original region should also apply to the mirrored regions. If not, an attacker could bypass existing read/write protections by reading from/writing to the mirrored regions to leak or corrupt the original data.

## Related Weaknesses
- ChildOf: CWE-284
- PeerOf: CWE-1251

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control; Impact: Modify Memory, Read Memory, Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] The fabric firewall should apply the same protections as the original region to the mirrored regions.
- [Implementation] The fabric firewall should apply the same protections as the original region to the mirrored regions.

## Detection Methods
- [Manual Dynamic Analysis] Using an external debugger, send write transactions to mirrored regions to test if original, write-protected regions are modified. Similarly, send read transactions to mirrored regions to test if the original, read-protected signals can be read.

## Demonstrative Examples (summary)
- A memory-controller IP block is connected to the on-chip fabric in a System on Chip (SoC). The memory controller is configured to divide the memory into four parts: one original and three mirrored regions inside the memory. The upper two bits of the address indicate which region is being addressed. 00 indicates the original region and 01, 10, and 11 are used to address the mirrored regions. All four regions operate in a lock-step manner and are always synchronized. The firewall in the on-chip fabric is programmed to protect the assets in the memory.
