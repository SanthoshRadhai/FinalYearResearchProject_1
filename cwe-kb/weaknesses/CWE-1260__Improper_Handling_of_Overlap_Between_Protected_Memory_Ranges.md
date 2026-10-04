# CWE-1260: Improper Handling of Overlap Between Protected Memory Ranges

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1260.html  

## Description
The product allows address regions to overlap, which can result in the bypassing of intended memory protection.

## Extended Description
Isolated memory regions and access control (read/write) policies are used by hardware to protect privileged software. Software components are often allowed to change or remap memory region definitions in order to enable flexible and dynamically changeable memory management by system software. If a software component running at lower privilege can program a memory address region to overlap with other memory regions used by software running at higher privilege, privilege escalation may be available to attackers. The memory protection unit (MPU) logic can incorrectly handle such an address overlap and allow the lower-privilege software to read or write into the protected memory region, resulting in privilege escalation attack. An address overlap weakness can also be used to launch a denial of service attack on the higher-privilege software memory regions.

## Related Weaknesses
- ChildOf: CWE-284
- CanPrecede: CWE-119

## Common Consequences
- Scope: Confidentiality, Integrity, Availability; Impact: Modify Memory, Read Memory, DoS: Instability

## Potential Mitigations
- [Architecture and Design] Ensure that memory regions are isolated as intended and that access control (read/write) policies are used by hardware to protect privileged software.
- [Implementation] For all of the programmable memory protection regions, the memory protection unit (MPU) design can define a priority scheme. For example: if three memory regions can be programmed (Region_0, Region_1, and Region_2), the design can enforce a priority scheme, such that, if a system address is within multiple regions, then the region with the lowest ID takes priority and the access-control policy of that region will be applied. In some MPU designs, the priority scheme can also be programmed by trusted software. Hardware logic or trusted firmware can also check for region definitions and block programming of memory regions with overlapping addresses. The memory-access-control-check filter can also be designed to apply a policy filter to all of the overlapping ranges, i.e., if an address is within Region_0 and Region_1, then access to this address is only granted if both Region_0 and Region_1 policies allow the access.

## Detection Methods
- [Manual Analysis] Create a high privilege memory block of any arbitrary size. Attempt to create a lower privilege memory block with an overlap of the high privilege memory block. If the creation attempt works, fix the hardware. Repeat the test.

## Demonstrative Examples (summary)
- For example, consider a design with a 16-bit address that has two software privilege levels: Privileged_SW and Non_privileged_SW. To isolate the system memory regions accessible by these two privilege levels, the design supports three memory regions: Region_0, Region_1, and Region_2. Each region is defined by two 32 bit registers: its range and its access policy. Address_range[15:0]: specifies the Base address of the region Address_range[31:16]: specifies the size of the region Access_policy[31:0]: specifies what types of software can access a region and which actions are allowed Certain bits of the access policy are defined symbolically as follows: Access_policy.read_np: if set to one, allows reads from Non_privileged_SW Access_policy.write_np: if set to one, allows writes from Non_privileged_SW Access_policy.execute_np: if set to one, allows code execution by Non_privileged_SW Access_policy.read_p: if set to one, allows reads from Privileged_SW Access_policy.write_p: if set to one, allows writes from Privileged_SW Access_policy.execute_p: if set to one, allows code execution by Privileged_SW For any requests from software, an address-protection filter checks the address range and access policies for each of the three regions, and only allows software access if all three filters allow access. Consider the following goals for access control as intended by the designer: Region_0 & Region_1: registers are programmable by Privileged_SW Region_2: registers are programmable by Non_privileged_SW The intention is that Non_privileged_SW cannot modify memory region and policies defined by Privileged_SW in Region_0 and Region_1. Thus, it cannot read or write the memory regions that Privileged_SW is using.
- The example code below is taken from the IOMMU controller module of the HACK@DAC'19 buggy CVA6 SoC [REF-1338]. The static memory map is composed of a set of Memory-Mapped Input/Output (MMIO) regions covering different IP agents within the SoC. Each region is defined by two 64-bit variables representing the base address and size of the memory region (XXXBase and XXXLength).
