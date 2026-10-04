# CAPEC-606: Weakening of Cellular Encryption

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/606.html  

## Description
An attacker, with control of a Cellular Rogue Base Station or through cooperation with a Malicious Mobile Network Operator can force the mobile device (e.g., the retransmission device) to use no encryption (A5/0 mode) or to use easily breakable encryption (A5/1 or A5/2 mode).

## Related Attack Patterns
- ChildOf: CAPEC-620

## Prerequisites
- Cellular devices that allow negotiating security modes to facilitate backwards compatibility and roaming on legacy networks.

## Skills Required
- [Medium] Adversaries can purchase and implement rogue BTS stations at a cost effective rate, and can push a mobile device to downgrade to a non-secure cellular protocol like 2G over GSM or CDMA.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Related Weaknesses (CWE)
- CWE-757
