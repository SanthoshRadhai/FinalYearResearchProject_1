# CAPEC-608: Cryptanalysis of Cellular Encryption

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/608.html  

## Description
The use of cryptanalytic techniques to derive cryptographic keys or otherwise effectively defeat cellular encryption to reveal traffic content. Some cellular encryption algorithms such as A5/1 and A5/2 (specified for GSM use) are known to be vulnerable to such attacks and commercial tools are available to execute these attacks and decrypt mobile phone conversations in real-time. Newer encryption algorithms in use by UMTS and LTE are stronger and currently believed to be less vulnerable to these types of attacks. Note, however, that an attacker with a Cellular Rogue Base Station can force the use of weak cellular encryption even by newer mobile devices.

## Related Attack Patterns
- ChildOf: CAPEC-97

## Prerequisites
- None

## Skills Required
- [Medium] Adversaries can rent commercial supercomputer time globally to conduct cryptanalysis on encrypted data captured from mobile devices. Foreign governments have their own cryptanalysis technology and capabilities. Commercial cellular standards for encryption (GSM and CDMA) are also subject to adversary cryptanalysis.

## Consequences
- Scope: Confidentiality; Impact: Other

## Mitigations
- Use of hardened baseband firmware on retransmission device to detect and prevent the use of weak cellular encryption.
- Monitor cellular RF interface to detect the usage of weaker-than-expected cellular encryption.

## Related Weaknesses (CWE)
- CWE-327
