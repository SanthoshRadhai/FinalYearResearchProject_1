# CWE-1232: Improper Lock Behavior After Power State Transition

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1232.html  

## Description
Register lock bit protection disables changes to system configuration once the bit is set. Some of the protected registers or lock bits become programmable after power state transitions (e.g., Entry and wake from low power sleep modes) causing the system configuration to be changeable.

## Extended Description
Devices may allow device configuration controls which need to be programmed after device power reset via a trusted firmware or software module (commonly set by BIOS/bootloader) and then locked from any further modification. This action is commonly implemented using a programmable lock bit, which, when set, disables writes to a protected set of registers or address regions. After a power state transition, the lock bit is set to unlocked. Some common weaknesses that can exist in such a protection scheme are that the lock gets cleared, the values of the protected registers get reset, or the lock become programmable.

## Related Weaknesses
- ChildOf: CWE-667

## Common Consequences
- Scope: Access Control; Impact: Modify Memory

## Potential Mitigations
- [Architecture and Design, Implementation, Testing] Security Lock bit protections should be reviewed for behavior across supported power state transitions. Security lock programming flow and lock properties should be tested in pre-silicon and post-silicon testing including testing across power transitions.

## Demonstrative Examples (summary)
- Consider the memory configuration settings of a system that uses DDR3 DRAM memory. Protecting the DRAM memory configuration from modification by software is required to ensure that system memory access control protections cannot be bypassed. This can be done by using lock bit protection that locks all of the memory configuration registers. The memory configuration lock can be set by the BIOS during the boot process. If such a system also supports a rapid power on mode like hibernate, the DRAM data must be saved to a disk before power is removed and restored back to the DRAM once the system powers back up and before the OS resumes operation after returning from hibernate.
- The example code below is taken from the register lock module (reglk_wrapper) of the Hack@DAC'21 buggy OpenPiton System-on-Chip (SoC). Upon powering on, most of the silicon registers are initially unlocked. However, critical resources must be configured and locked by setting the lock bit in a register. In this module, a set of six memory-mapped I/O registers (reglk_mem) is defined and maintained to control the access control of registers inside different peripherals in the SoC [REF-1432]. Each bit represents a register's read/write ability or sets of registers inside a peripheral. Setting improper lock values after system power transition or system rest would make a temporary window for the attackers to read unauthorized data, e.g., secret keys from the crypto engine, and write illegitimate data to critical registers, e.g., framework data. Furthermore, improper register lock values can also result in DoS attacks. In this faulty implementation, the locks are disabled, i.e., initialized to zero, at reset instead of setting them to their appropriate values [REF-1433]. Improperly initialized locks might allow unauthorized access to sensitive registers, compromising the system's security.
