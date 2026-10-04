# CAPEC-668: Key Negotiation of Bluetooth Attack (KNOB)

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/668.html  

## Description
An adversary can exploit a flaw in Bluetooth key negotiation allowing them to decrypt information sent between two devices communicating via Bluetooth. The adversary uses an Adversary in the Middle setup to modify packets sent between the two devices during the authentication process, specifically the entropy bits. Knowledge of the number of entropy bits will allow the attacker to easily decrypt information passing over the line of communication.

## Related Attack Patterns
- ChildOf: CAPEC-115
- CanPrecede: CAPEC-148

## Prerequisites
- Person in the Middle network setup.

## Skills Required
- [Medium] Ability to modify packets.

## Resources Required
- Bluetooth adapter, packet capturing capabilities.

## Consequences
- Scope: Confidentiality; Impact: Read Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Bypass Protection Mechanism
- Scope: Integrity; Impact: Modify Data

## Mitigations
- Newer Bluetooth firmwares ensure that the KNOB is not negotaited in plaintext. Update your device.

## Related Weaknesses (CWE)
- CWE-425
- CWE-285
- CWE-693
