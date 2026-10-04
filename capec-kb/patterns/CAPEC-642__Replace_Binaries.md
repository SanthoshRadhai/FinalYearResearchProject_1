# CAPEC-642: Replace Binaries

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/642.html  

## Description
Adversaries know that certain binaries will be regularly executed as part of normal processing. If these binaries are not protected with the appropriate file system permissions, it could be possible to replace them with malware. This malware might be executed at higher system permission levels. A variation of this pattern is to discover self-extracting installation packages that unpack binaries to directories with weak file permissions which it does not clean up appropriately. These binaries can be replaced by malware, which can then be executed.

## Related Attack Patterns
- ChildOf: CAPEC-17

## Prerequisites
- The attacker must be able to place the malicious binary on the target machine.

## Mitigations
- Insure that binaries commonly used by the system have the correct file permissions. Set operating system policies that restrict privilege elevation of non-Administrators. Use auditing tools to observe changes to system services.

## Related Weaknesses (CWE)
- CWE-732
