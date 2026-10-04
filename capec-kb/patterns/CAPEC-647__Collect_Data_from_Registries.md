# CAPEC-647: Collect Data from Registries

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/647.html  

## Description
An adversary exploits a weakness in authorization to gather system-specific data and sensitive information within a registry (e.g., Windows Registry, Mac plist). These contain information about the system configuration, software, operating system, and security. The adversary can leverage information gathered in order to carry out further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-150

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).
- The adversary must have capability to navigate the operating system to peruse the registry.

## Skills Required
- [Low] Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line.

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking via using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Related Weaknesses (CWE)
- CWE-285
