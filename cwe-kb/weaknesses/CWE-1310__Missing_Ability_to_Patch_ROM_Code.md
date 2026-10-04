# CWE-1310: Missing Ability to Patch ROM Code

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1310.html  

## Description
Missing an ability to patch ROM code may leave a System or System-on-Chip (SoC) in a vulnerable state.

## Extended Description
A System or System-on-Chip (SoC) that implements a boot process utilizing security mechanisms such as Root-of-Trust (RoT) typically starts by executing code from a Read-only-Memory (ROM) component. The code in ROM is immutable, hence any security vulnerabilities discovered in the ROM code can never be fixed for the systems that are already in use. A common weakness is that the ROM does not have the ability to patch if security vulnerabilities are uncovered after the system gets shipped. This leaves the system in a vulnerable state where an adversary can compromise the SoC.

## Related Weaknesses
- ChildOf: CWE-1329

## Common Consequences
- Scope: Other; Impact: Varies by Context, Reduce Maintainability — When the system is unable to be patched, it can be left in a vulnerable state.

## Potential Mitigations
- [Architecture and Design, Implementation] Secure patch support to allow ROM code to be patched on the next boot.
- [Architecture and Design, Implementation] Support patches that can be programmed in-field or during manufacturing through hardware fuses. This feature can be used for limited patching of devices after shipping, or for the next batch of silicon devices manufactured, without changing the full device ROM.

## Demonstrative Examples (summary)
- A System-on-Chip (SOC) implements a Root-of-Trust (RoT) in ROM to boot secure code. However, at times this ROM code might have security vulnerabilities and need to be patched. Since ROM is immutable, it can be impossible to patch.
- The example code is taken from the SoC peripheral wrapper inside the buggy OpenPiton SoC of HACK@DAC'21. The wrapper is used for connecting the communications between SoC peripherals, such as crypto-engines, direct memory access (DMA), reset controllers, JTAG, etc. The secure implementation of the SoC wrapper should allow users to boot from a ROM for Linux (i_bootrom_linux) or from a patchable ROM (i_bootrom_patch) if the Linux bootrom has security or functional issues.The example code is taken from the SoC peripheral wrapper inside the buggy OpenPiton SoC of HACK@DAC'21. The wrapper is used for connecting the communications between SoC peripherals, such as crypto-engines, direct memory access (DMA), reset controllers, JTAG, etc. The secure implementation of the SoC wrapper should allow users to boot from a ROM for Linux (i_bootrom_linux) or from a patchable ROM (i_bootrom_patch) if the Linux bootrom has security or functional issues.
