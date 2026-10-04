# CWE-1191: On-Chip Debug and Test Interface With Improper Access Control

**Abstraction:** Base  
**Status:** Stable  
**Reference:** https://cwe.mitre.org/data/definitions/1191.html  

## Description
The chip does not implement or does not correctly perform access control to check whether users are authorized to access internal registers and test modes through the physical debug/test interface.

## Extended Description
A device's internal information may be accessed through a scan chain of interconnected internal registers, usually through a JTAG interface. The JTAG interface provides access to these registers in a serial fashion in the form of a scan chain for the purposes of debugging programs running on a device. Since almost all information contained within a device may be accessed over this interface, device manufacturers typically insert some form of authentication and authorization to prevent unintended use of this sensitive information. This mechanism is implemented in addition to on-chip protections that are already present. If authorization, authentication, or some other form of access control is not implemented or not implemented correctly, a user may be able to bypass on-chip protection mechanisms through the debug interface. Sometimes, designers choose not to expose the debug pins on the motherboard. Instead, they choose to hide these pins in the intermediate layers of the board. This is primarily done to work around the lack of debug authorization inside the chip. In such a scenario (without debug authorization), when the debug interface is exposed, chip internals are accessible to an attacker.

## Related Weaknesses
- ChildOf: CWE-284

## Common Consequences
- Scope: Confidentiality; Impact: Read Application Data
- Scope: Confidentiality; Impact: Read Memory
- Scope: Authorization; Impact: Execute Unauthorized Code or Commands
- Scope: Integrity; Impact: Modify Memory
- Scope: Integrity; Impact: Modify Application Data
- Scope: Access Control; Impact: Bypass Protection Mechanism

## Potential Mitigations
- [Architecture and Design] If feasible, the manufacturer should disable the JTAG interface or implement authentication and authorization for the JTAG interface. If authentication logic is added, it should be resistant to timing attacks. Security-sensitive data stored in registers, such as keys, etc. should be cleared when entering debug mode.

## Detection Methods
- [Dynamic Analysis with Manual Results Interpretation] Authentication and authorization of debug and test interfaces should be part of the architecture and design review process. Withholding of private register documentation from the debug and test interface public specification ("Security by obscurity") should not be considered as sufficient security.
- [Dynamic Analysis with Manual Results Interpretation] Dynamic tests should be done in the pre-silicon and post-silicon stages to verify that the debug and test interfaces are not open by default.
- [Fuzzing] Tests that fuzz Debug and Test Interfaces should ensure that no access without appropriate authentication and authorization is possible.

## Demonstrative Examples (summary)
- A home, WiFi-router device implements a login prompt which prevents an unauthorized user from issuing any commands on the device until appropriate credentials are provided. The credentials are protected on the device and are checked for strength against attack.
- The following example code is a snippet from the JTAG wrapper module in the RISC-V debug module of the HACK@DAC'21 Openpiton SoC [REF-1355]. To make sure that the JTAG is accessed securely, the developers have included a primary authentication mechanism based on a password.
- The example code below is taken from the JTAG access control mechanism of the HACK@DAC'21 buggy OpenPiton SoC [REF-1364]. Access to JTAG allows users to access sensitive information in the system. Hence, access to JTAG is controlled using cryptographic authentication of the users. In this example (see the vulnerable code source), the password checker uses HMAC-SHA256 for authentication. It takes a 512-bit secret message from the user, hashes it using HMAC, and compares its output with the expected output to determine the authenticity of the user.
