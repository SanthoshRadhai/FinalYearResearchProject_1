# CWE-1242: Inclusion of Undocumented Features or Chicken Bits

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1242.html  

## Description
The device includes chicken bits or undocumented features that can create entry points for unauthorized actors.

## Extended Description
A common design practice is to use undocumented bits on a device that can be used to disable certain functional security features. These bits are commonly referred to as "chicken bits". They can facilitate quick identification and isolation of faulty components, features that negatively affect performance, or features that do not provide the required controllability for debug and test. Another way to achieve this is through implementation of undocumented features.

## Related Weaknesses
- ChildOf: CWE-912

## Common Consequences
- Scope: Confidentiality, Integrity, Availability, Access Control; Impact: Modify Memory, Read Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism — An attacker might exploit these interfaces for unauthorized access.

## Potential Mitigations
- [Architecture and Design, Implementation] The implementation of chicken bits in a released product is highly discouraged. If implemented at all, ensure that they are disabled in production devices. All interfaces to a device should be documented.

## Demonstrative Examples (summary)
- Consider a device that comes with various security measures, such as secure boot. The secure-boot process performs firmware-integrity verification at boot time, and this code is stored in a separate SPI-flash device. However, this code contains undocumented "special access features" intended to be used only for performing failure analysis and intended to only be unlocked by the device designer.
