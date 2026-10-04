# CWE-1222: Insufficient Granularity of Address Regions Protected by Register Locks

**Abstraction:** Variant  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1222.html  

## Description
The product defines a large address region protected from modification by the same register lock control bit. This results in a conflict between the functional requirement that some addresses need to be writable by software during operation and the security requirement that the system configuration lock bit must be set during the boot process.

## Extended Description
Integrated circuits and hardware IPs can expose the device configuration controls that need to be programmed after device power reset by a trusted firmware or software module (commonly set by BIOS/bootloader) and then locked from any further modification. In hardware design, this is commonly implemented using a programmable lock bit which enables/disables writing to a protected set of registers or address regions. When the programmable lock bit is set, the relevant address region can be implemented as a hardcoded value in hardware logic that cannot be changed later. A problem can arise wherein the protected region definition is not granular enough. After the programmable lock bit has been set, then this new functionality cannot be implemented without change to the hardware design.

## Related Weaknesses
- ChildOf: CWE-1220

## Common Consequences
- Scope: Access Control; Impact: Other — System security configuration cannot be defined in a way that does not conflict with functional requirements of device.

## Potential Mitigations
- [Architecture and Design] The defining of protected locked registers should be reviewed or tested early in the design phase with software teams to ensure software flows are not blocked by the security locks. As an alternative to using register lock control bits and fixed access control regions, the hardware design could use programmable security access control configuration so that device trusted firmware can configure and change the protected regions based on software usage and security models.

## Demonstrative Examples (summary)
- For example, consider a hardware unit with a 32 kilobyte configuration address space where the first 8 kilobyte address contains security sensitive controls that must only be writable by device bootloader. One way to protect the security configuration could be to define a 32 bit system configuration locking register (SYS_LOCK) where each bit lock locks the corresponding 1 kilobyte region.
