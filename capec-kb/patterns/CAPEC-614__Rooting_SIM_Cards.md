# CAPEC-614: Rooting SIM Cards

**Abstraction:** Detailed  
**Status:** Draft  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/614.html  

## Description
SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credentials, for example in NFC-enabled phones with mobile wallets. This attack leverages over-the-air (OTA) updates deployed via cryptographically-secured SMS messages to deliver executable code to the SIM. By cracking the DES key, an attacker can send properly signed binary SMS messages to a device, which are treated as Java applets and are executed on the SIM. These applets are allowed to send SMS, change voicemail numbers, and query the phone location, among many other predefined functions. These capabilities alone provide plenty of potential for abuse.

## Related Attack Patterns
- ChildOf: CAPEC-186

## Prerequisites
- A SIM card that relies on the DES cipher.

## Skills Required
- [Medium] This is a sophisticated attack, but detailed techniques are published in open literature.

## Consequences
- Scope: Confidentiality, Integrity; Impact: Execute Unauthorized Commands

## Mitigations
- Upgrade the SIM card to use the state-of-the-art AES or the somewhat outdated 3DES algorithm for OTA.

## Related Weaknesses (CWE)
- CWE-327
