# CWE-1316: Fabric-Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1316.html  

## Description
The address map of the on-chip fabric has protected and unprotected regions overlapping, allowing an attacker to bypass access control to the overlapping portion of the protected region.

## Extended Description
Various ranges can be defined in the system-address map, either in the memory or in Memory-Mapped-IO (MMIO) space. These ranges are usually defined using special range registers that contain information, such as base address and size. Address decoding is the process of determining for which range the incoming transaction is destined. To ensure isolation, ranges containing secret data are access-control protected. Occasionally, these ranges could overlap. The overlap could either be intentional (e.g. due to a limited number of range registers or limited choice in choosing size of the range) or unintentional (e.g. introduced by errors). Some hardware designs allow dynamic remapping of address ranges assigned to peripheral MMIO ranges. In such designs, intentional address overlaps can be created through misconfiguration by malicious software. When protected and unprotected ranges overlap, an attacker could send a transaction and potentially compromise the protections in place, violating the principle of least privilege.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control, Authorization; Impact: Bypass Protection Mechanism, Read Memory, Modify Memory

## Potential Mitigations
- [Architecture and Design] When architecting the address map of the chip, ensure that protected and unprotected ranges are isolated and do not overlap. When designing, ensure that ranges hardcoded in Register-Transfer Level (RTL) do not overlap.
- [Implementation] Ranges configured by firmware should not overlap. If overlaps are mandatory because of constraints such as a limited number of registers, then ensure that no assets are present in the overlapped portion.
- [Testing] Validate mitigation actions with robust testing.

## Detection Methods
- [Automated Dynamic Analysis] Review address map in specification to see if there are any overlapping ranges.
- [Manual Static Analysis] Negative testing of access control on overlapped ranges.

## Demonstrative Examples (summary)
- An on-chip fabric supports a 64KB address space that is memory-mapped. The fabric has two range registers that support creation of two protected ranges with specific size constraints--4KB, 8KB, 16KB or 32KB. Assets that belong to user A require 4KB, and those of user B require 20KB. Registers and other assets that are not security-sensitive require 40KB. One range register is configured to program 4KB to protect user A's assets. Since a 20KB range cannot be created with the given size constraints, the range register for user B's assets is configured as 32KB. The rest of the address space is left as open. As a result, some part of untrusted and open-address space overlaps with user B range.
