# CAPEC-643: Identify Shared Files/Directories on System

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/643.html  

## Description
An adversary discovers connections between systems by exploiting the target system's standard practice of revealing them in searchable, common areas. Through the identification of shared folders/drives between systems, the adversary may further their goals of locating and collecting sensitive information/files, or map potential routes for lateral movement within the network.

## Related Attack Patterns
- ChildOf: CAPEC-309
- CanPrecede: CAPEC-561
- CanPrecede: CAPEC-545
- CanPrecede: CAPEC-165

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).

## Skills Required
- [Low] Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line. The adversary, or their malware, can simply employ a set of commands that search for shared drives on the system (e.g., net view \\remote system or net share).

## Resources Required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- Scope: Confidentiality; Impact: Read Data

## Mitigations
- Identify unnecessary system utilities or potentially malicious software that may contain functionality to identify network share information, and audit and/or block them by using allowlist tools.

## Related Weaknesses (CWE)
- CWE-267
- CWE-200
