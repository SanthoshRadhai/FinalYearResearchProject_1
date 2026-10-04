# CWE-1329: Reliance on Component That is Not Updateable

**Abstraction:** Base  
**Status:** Incomplete  
**Reference:** https://cwe.mitre.org/data/definitions/1329.html  

## Description
The product contains a component that cannot be updated or patched in order to remove vulnerabilities or significant bugs.

## Extended Description
If the component is discovered to contain a vulnerability or critical bug, but the issue cannot be fixed using an update or patch, then the product's owner will not be able to protect against the issue. The only option might be replacement of the product, which could be too financially or operationally expensive for the product owner. As a result, the inability to patch or update can leave the product open to attacker exploitation or critical operation failures. This weakness can be especially difficult to manage when using ROM, firmware, or similar components that traditionally have had limited or no update capabilities. In industries such as healthcare, "legacy" devices can be operated for decades. As a US task force report [REF-1197] notes, "the inability to update or replace equipment has both large and small health care delivery organizations struggle with numerous unsupported legacy systems that cannot easily be replaced (hardware, software, and operating systems) with large numbers of vulnerabilities and few modern countermeasures." While hardware can be prone to this weakness, software systems can also be affected, such as when a third-party driver or library is no longer actively maintained or supported but is still critical for the required functionality.

## Related Weaknesses
- ChildOf: CWE-1357
- ChildOf: CWE-1357
- ChildOf: CWE-664

## Common Consequences
- Scope: Confidentiality, Integrity, Access Control, Authentication, Authorization, Other; Impact: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart, Quality Degradation, Reduce Maintainability — If an attacker can identify an exploitable vulnerability in one product that has no means of patching, the attack may be used against all affected versions of that product.

## Potential Mitigations
- [Requirements] Specify requirements that each component should be updateable, including ROM, firmware, etc.
- [Architecture and Design] Design the product to allow for updating of its components. Include the external infrastructure that might be necessary to support updates, such as distribution servers.
- [Architecture and Design, Implementation] With hardware, support patches that can be programmed in-field or during manufacturing through hardware fuses. This feature can be used for limited patching of devices after shipping, or for the next batch of silicon devices manufactured, without changing the full device ROM.
- [Implementation] Implement the necessary functionality to allow each component to be updated.

## Detection Methods
- [Architecture or Design Review] Check the consumer or maintainer documentation, the architecture/design documentation, or the original requirements to ensure that the documentation includes details for how to update the firmware.

## Demonstrative Examples (summary)
- A refrigerator has an Internet interface for the official purpose of alerting the manufacturer when that refrigerator detects a fault. Because the device is attached to the Internet, the refrigerator is a target for hackers who may wish to use the device other potentially more nefarious purposes.
- A System-on-Chip (SOC) implements a Root-of-Trust (RoT) in ROM to boot secure code. However, at times this ROM code might have security vulnerabilities and need to be patched. Since ROM is immutable, it can be impossible to patch.
- The example code is taken from the JTAG module of the buggy OpenPiton SoC of HACK@DAC'21. JTAG is protected with a password checker. Access to JTAG operations will be denied unless the correct password is provided by the user. This user-provided password is first sent to the HMAC module where it is hashed with a secret crypto key. This user password hash (pass_hash) is then compared with the hash of the correct password (exp_hash). If they match, JTAG will then be unlocked.
