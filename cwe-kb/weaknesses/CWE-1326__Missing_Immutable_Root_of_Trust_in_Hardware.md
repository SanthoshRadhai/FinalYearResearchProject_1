# CWE-1326: Missing Immutable Root of Trust in Hardware

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1326.html  

## Description
A missing immutable root of trust in the hardware results in the ability to bypass secure boot or execute untrusted or adversarial boot code.

## Extended Description
A System-on-Chip (SoC) implements secure boot by verifying or authenticating signed boot code. The signing of the code is achieved by an entity that the SoC trusts. Before executing the boot code, the SoC verifies that the code or the public key with which the code has been signed has not been tampered with. The other data upon which the SoC depends are system-hardware settings in fuses such as whether "Secure Boot is enabled". These data play a crucial role in establishing a Root of Trust (RoT) to execute secure-boot flows. One of the many ways RoT is achieved is by storing the code and data in memory or fuses. This memory should be immutable, i.e., once the RoT is programmed/provisioned in memory, that memory should be locked and prevented from further programming or writes. If the memory contents (i.e., RoT) are mutable, then an adversary can modify the RoT to execute their choice of code, resulting in a compromised secure boot. Note that, for components like ROM, secure patching/update features should be supported to allow authenticated and authorized updates in the field.

## Related Weaknesses
- ChildOf: CWE-693

## Common Consequences
- Scope: Authentication, Authorization; Impact: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands, Modify Memory

## Potential Mitigations
- [Architecture and Design] When architecting the system, the RoT should be designated for storage in a memory that does not allow further programming/writes.
- [Implementation] During implementation and test, the RoT memory location should be demonstrated to not allow further programming/writes.

## Detection Methods
- [Automated Dynamic Analysis] Automated testing can verify that RoT components are immutable.
- [Architecture or Design Review] Root of trust elements and memory should be part of architecture and design reviews.

## Demonstrative Examples (summary)
- The RoT is stored in memory. This memory can be modified by an adversary. For example, if an SoC implements "Secure Boot" by storing the boot code in an off-chip/on-chip flash, the contents of the flash can be modified by using a flash programmer. Similarly, if the boot code is stored in ROM (Read-Only Memory) but the public key or the hash of the public key (used to enable "Secure Boot") is stored in Flash or a memory that is susceptible to modifications or writes, the implementation is vulnerable.
- The example code below is a snippet from the bootrom of the HACK@DAC'19 buggy OpenPiton SoC [REF-1348]. The contents of the bootrom are critical in implementing the hardware root of trust.
