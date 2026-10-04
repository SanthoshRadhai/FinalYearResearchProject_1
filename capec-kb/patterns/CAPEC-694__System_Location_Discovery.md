# CAPEC-694: System Location Discovery

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** High  
**Typical Severity:** Very Low  
**Reference:** https://capec.mitre.org/data/definitions/694.html  

## Description
An adversary collects information about the target system in an attempt to identify the system's geographical location. Information gathered could include keyboard layout, system language, and timezone. This information may benefit an adversary in confirming the desired target and/or tailoring further attacks.

## Related Attack Patterns
- ChildOf: CAPEC-169

## Prerequisites
- The adversary must have some level of access to the system and have a basic understanding of the operating system in order to query the appropriate sources for relevant information.

## Skills Required
- [Low] The adversary must know how to query various system sources of information respective of the system's operating system to obtain the relevant information.

## Resources Required
- The adversary requires access to the target's operating system tools to query relevant system information. On windows, registry queries can be conducted with powershell, wmi, or regedit. On Linux or macOS, queries can be performed with through a shell.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- To reduce the amount of information gathered, one could disable various geolocation features of the operating system not required for system operation.

## Related Weaknesses (CWE)
- CWE-497
