# CWE-1233: Security-Sensitive Hardware Controls with Missing Lock Bit Protection

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1233.html  

## Description
The product uses a register lock bit protection mechanism, but it does not ensure that the lock bit prevents modification of system registers or controls that perform changes to important hardware system configuration.

## Extended Description
Integrated circuits and hardware intellectual properties (IPs) might provide device configuration controls that need to be programmed after device power reset by a trusted firmware or software module, commonly set by BIOS/bootloader. After reset, there can be an expectation that the controls cannot be used to perform any further modification. This behavior is commonly implemented using a trusted lock bit, which can be set to disable writes to a protected set of registers or address regions. The lock protection is intended to prevent modification of certain system configuration (e.g., memory/memory protection unit configuration). However, if the lock bit does not effectively write-protect all system registers or controls that could modify the protected system configuration, then an adversary may be able to use software to access the registers/controls and modify the protected hardware configuration.

## Related Weaknesses
- ChildOf: CWE-284
- ChildOf: CWE-667

## Common Consequences
- Scope: Access Control; Impact: Modify Memory — System Configuration protected by the lock bit can be modified even when the lock is set.

## Potential Mitigations
- [Architecture and Design, Implementation, Testing] Security lock bit protections must be reviewed for design inconsistency and common weaknesses. Security lock programming flow and lock properties must be tested in pre-silicon and post-silicon testing.

## Detection Methods
- [Manual Analysis] Set the lock bit. Attempt to modify the information protected by the lock bit. If the information is changed, implement a design fix. Retest. Also, attempt to indirectly clear the lock bit or bypass it.

## Demonstrative Examples (summary)
- Consider the example design below for a digital thermal sensor that detects overheating of the silicon and triggers system shutdown. The system critical temperature limit (CRITICAL_TEMP_LIMIT) and thermal sensor calibration (TEMP_SENSOR_CALIB) data have to be programmed by the firmware.
