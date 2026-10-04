# CAPEC-646: Peripheral Footprinting

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/646.html  

## Description
Adversaries may attempt to obtain information about attached peripheral devices and components connected to a computer system. Examples may include discovering the presence of iOS devices by searching for backups, analyzing the Windows registry to determine what USB devices have been connected, or infecting a victim system with malware to report when a USB device has been connected. This may allow the adversary to gain additional insight about the system or network environment, which may be useful in constructing further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary needs either physical or remote access to the victim system.

## Skills Required
- [Medium] The adversary needs to be able to infect the victim system in a manner that gives them remote access.
- [Medium] If analyzing the Windows registry, the adversary must understand the registry structure to know where to look for devices.

## Mitigations
- Identify programs that may be used to acquire peripheral information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related Weaknesses (CWE)
- CWE-200
