# CWE-1328: Security Version Number Mutable to Older Versions

**Abstraction:** Base  
**Status:** Draft  
**Reference:** https://cwe.mitre.org/data/definitions/1328.html  

## Description
Security-version number in hardware is mutable, resulting in the ability to downgrade (roll-back) the boot firmware to vulnerable code versions.

## Extended Description
A System-on-Chip (SoC) implements secure boot or verified boot. It might support a security version number, which prevents downgrading the current firmware to a vulnerable version. Once downgraded to a previous version, an adversary can launch exploits on the SoC and thus compromise the security of the SoC. These downgrade attacks are also referred to as roll-back attacks. The security version number must be stored securely and persistently across power-on resets. A common weakness is that the security version number is modifiable by an adversary, allowing roll-back or downgrade attacks or, under certain circumstances, preventing upgrades (i.e. Denial-of-Service on upgrades). In both cases, the SoC is in a vulnerable state.

## Related Weaknesses
- ChildOf: CWE-285
- PeerOf: CWE-757

## Common Consequences
- Scope: Confidentiality, Integrity, Authentication, Authorization; Impact: Other — Impact includes roll-back or downgrade to a vulnerable version of the firmware or DoS (prevent upgrades).

## Potential Mitigations
- [Architecture and Design] When architecting the system, security version data should be designated for storage in registers that are either read-only or have access controls that prevent modification by an untrusted agent.
- [Implementation] During implementation and test, security version data should be demonstrated to be read-only and access controls should be validated.

## Detection Methods
- [Automated Dynamic Analysis] Mutability of stored security version numbers and programming with older firmware images should be part of automated testing.
- [Architecture or Design Review] Anti-roll-back features should be reviewed as part of Architecture or Design review.

## Demonstrative Examples (summary)
- A new version of firmware is signed with a security version number higher than the previous version. During the firmware update process the SoC checks for the security version number and upgrades the SoC firmware with the latest version. This security version number is stored in persistent memory upon successful upgrade for use across power-on resets.
