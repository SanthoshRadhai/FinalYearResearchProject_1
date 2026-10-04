# CAPEC-638: Altered Component Firmware

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Very High  
**Reference:** https://capec.mitre.org/data/definitions/638.html  

## Description
An adversary exploits systems features and/or improperly protected firmware of hardware components, such as Hard Disk Drives (HDD), with the goal of executing malicious code from within the component's Master Boot Record (MBR). Conducting this type of attack entails the adversary infecting the target with firmware altering malware, using known tools, and a payload. Once this malware is executed, the MBR is modified to include instructions to execute the payload at desired intervals and when the system is booted up. A successful attack will obtain persistence within the victim system even if the operating system is reinstalled and/or if the component is formatted or has its data erased.

## Related Attack Patterns
- ChildOf: CAPEC-452

## Prerequisites
- Advanced knowledge about the target component's firmware
- Advanced knowledge about Master Boot Records (MBR)
- Advanced knowledge about tools used to insert firmware altering malware.
- Advanced knowledge about component shipments to the target organization.

## Skills Required
- [High] Ability to access and reverse engineer hardware component firmware.
- [High] Ability to intercept components in transit.
- [Medium] Ability to create malicious payload to be executed from MBR.
- [Low] Ability to leverage known malware tools to infect target system and insert firmware altering malware/payload

## Resources Required
- Manufacturer source code for hardware components.
- Malware tools used to insert malware and payload onto target component.
- Either remote or physical access to the target component.

## Consequences
- Scope: Authentication, Authorization; Impact: Gain Privileges, Execute Unauthorized Commands, Bypass Protection Mechanism, Hide Activities
- Scope: Confidentiality, Access Control; Impact: Read Data, Modify Data

## Mitigations
- Leverage hardware components known to not be susceptible to these types of attacks.
- Implement hardware RAID infrastructure.
