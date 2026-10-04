# CAPEC-667: Bluetooth Impersonation AttackS (BIAS)

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/667.html  

## Description
An adversary disguises the MAC address of their Bluetooth enabled device to one for which there exists an active and trusted connection and authenticates successfully. The adversary can then perform malicious actions on the target Bluetooth device depending on the target’s capabilities.

## Related Attack Patterns
- ChildOf: CAPEC-616

## Prerequisites
- Knowledge of a target device's list of trusted connections.

## Skills Required
- [Low] Adversaries must be capable of using command line Linux tools.
- [Low] Adversaries must be in close proximity to Bluetooth devices.

## Consequences
- Scope: Integrity; Impact: (unspecified)
- Scope: Confidentiality; Impact: (unspecified)

## Mitigations
- Disable Bluetooth in public places.
- Verify incoming Bluetooth connections; do not automatically trust.
- Change default PIN passwords and always use one when connecting.

## Related Weaknesses (CWE)
- CWE-290
