# CWE-1234: Hardware Internal or Debug Modes Allow Override of Locks

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1234.html  

## Description
System configuration protection may be bypassed during debug mode.

## Extended Description
Device configuration controls are commonly programmed after a device power reset by a trusted firmware or software module (e.g., BIOS/bootloader) and then locked from any further modification. This is commonly implemented using a trusted lock bit, which when set, disables writes to a protected set of registers or address regions. The lock protection is intended to prevent modification of certain system configuration (e.g., memory/memory protection unit configuration). If debug features supported by hardware or internal modes/system states are supported in the hardware design, modification of the lock protection may be allowed allowing access and modification of configuration information.

## Related Weaknesses
- ChildOf: CWE-667

## Common Consequences
- Scope: Access Control; Impact: Bypass Protection Mechanism — Bypass of lock bit allows access and modification of system configuration even when the lock bit is set.

## Potential Mitigations
- [Architecture and Design, Implementation, Testing] Security Lock bit protections should be reviewed for any bypass/override modes supported. Any supported override modes either should be removed or protected using authenticated debug modes. Security lock programming flow and lock properties should be tested in pre-silicon and post-silicon testing.

## Demonstrative Examples (summary)
- For example, consider the example Locked_override_register example. This register module supports a lock mode that blocks any writes after lock is set to 1. However, it also allows override of the lock protection when scan_mode or debug_unlocked modes are active.
- The following example code [REF-1375] is taken from the register lock security peripheral of the HACK@DAC'21 buggy OpenPiton SoC. It demonstrates how to lock read or write access to security-critical hardware registers (e.g., crypto keys, system integrity code, etc.). The configuration to lock all the sensitive registers in the SoC is managed through the reglk_mem registers. These reglk_mem registers are reset when the hardware powers up and configured during boot up. Malicious users, even with kernel-level software privilege, do not get access to the sensitive contents that are locked down. Hence, the security of the entire system can potentially be compromised if the register lock configurations are corrupted or if the register locks are disabled.
