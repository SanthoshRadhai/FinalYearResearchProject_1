# CWE-1257: Improper Access Control Applied to Mirrored or Aliased Memory Regions

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1257.html  

## Description
Aliased or mirrored memory regions in hardware designs may have inconsistent read/write permissions enforced by the hardware. A possible result is that an untrusted agent is blocked from accessing a memory region but is not blocked from accessing the corresponding aliased memory region.

## Extended Description
Hardware product designs often need to implement memory protection features that enable privileged software to define isolated memory regions and access control (read/write) policies. Isolated memory regions can be defined on different memory spaces in a design (e.g. system physical address, virtual address, memory mapped IO). Each memory cell should be mapped and assigned a system address that the core software can use to read/write to that memory. It is possible to map the same memory cell to multiple system addresses such that read/write to any of the aliased system addresses would be decoded to the same memory cell. This is commonly done in hardware designs for redundancy and simplifying address decoding logic. If one of the memory regions is corrupted or faulty, then that hardware can switch to using the data in the mirrored memory region. Memory aliases can also be created in the system address map if the address decoder unit ignores higher order address bits when mapping a smaller address region into the full system address. A common security weakness that can exist in such memory mapping is that aliased memory regions could have different read/write access protections enforced by the hardware such that an untrusted agent is blocked from accessing a memory address but is not blocked from accessing the corresponding aliased memory address. Such inconsistency can then be used to bypass the access protection of the primary memory block and read or modify the protected memory. An untrusted agent could also possibly create memory aliases in the system address map for malicious purposes if it is able to change the mapping of an address region or modify memory region sizes.

## Related Weaknesses
- ChildOf: CWE-284
- CanPrecede: CWE-119

## Common Consequences
- Scope: Confidentiality; Impact: Read Memory
- Scope: Integrity; Impact: Modify Memory
- Scope: Availability; Impact: DoS: Instability

## Potential Mitigations
- [Architecture and Design, Implementation] The checks should be applied for consistency access rights between primary memory regions and any mirrored or aliased memory regions. If different memory protection units (MPU) are protecting the aliased regions, their protected range definitions and policies should be synchronized.
- [Architecture and Design, Implementation] The controls that allow enabling memory aliases or changing the size of mapped memory regions should only be programmable by trusted software components.

## Demonstrative Examples (summary)
- In a System-on-a-Chip (SoC) design the system fabric uses 16 bit addresses. An IP unit (Unit_A) has 4 kilobyte of internal memory which is mapped into a 16 kilobyte address range in the system fabric address map. System Address Mapped to 0x0000 - 0x3FFF Unit_A registers : 0x0000 - 0x0FFF 0x4000 - 0xFFFF Other IPs & Memory To protect the register controls in Unit_A unprivileged software is blocked from accessing addresses between 0x0000 - 0x0FFF. The address decoder of Unit_A masks off the higher order address bits and decodes only the lower 12 bits for computing the offset into the 4 kilobyte internal memory space.
