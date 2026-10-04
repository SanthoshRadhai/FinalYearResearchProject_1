# CAPEC-39: Manipulating Opaque Client-based Data Tokens

**Abstraction:** Standard  
**Status:** Draft  
**Likelihood of Attack:** High  
**Typical Severity:** Medium  
**Reference:** https://capec.mitre.org/data/definitions/39.html  

## Description
In circumstances where an application holds important data client-side in tokens (cookies, URLs, data files, and so forth) that data can be manipulated. If client or server-side application components reinterpret that data as authentication tokens or data (such as store item pricing or wallet information) then even opaquely manipulating that data may bear fruit for an Attacker. In this pattern an attacker undermines the assumption that client side tokens have been adequately protected from tampering through use of encryption or obfuscation.

## Related Attack Patterns
- ChildOf: CAPEC-22

## Prerequisites
- An attacker already has some access to the system or can steal the client based data tokens from another user who has access to the system.
- For an Attacker to viably execute this attack, some data (later interpreted by the application) must be held client-side in a way that can be manipulated without detection. This means that the data or tokens are not CRCd as part of their value or through a separate meta-data store elsewhere.

## Skills Required
- [Medium] If the client site token is obfuscated.
- [High] If the client site token is encrypted.

## Resources Required
- The Attacker needs no special hardware-based resources in order to conduct this attack. Software plugins, such as Tamper Data for Firefox, may help in manipulating URL- or cookie-based data.

## Consequences
- Scope: Integrity; Impact: Modify Data
- Scope: Confidentiality, Access Control, Authorization; Impact: Gain Privileges

## Mitigations
- One solution to this problem is to protect encrypted data with a CRC of some sort. If knowing who last manipulated the data is important, then using a cryptographic "message authentication code" (or hMAC) is prescribed. However, this guidance is not a panacea. In particular, any value created by (and therefore encrypted by) the client, which itself is a "malicious" value, all the protective cryptography in the world can't make the value 'correct' again. Put simply, if the client has control over the whole process of generating and encoding the value, then simply protecting its integrity doesn't help.
- Make sure to protect client side authentication tokens for confidentiality (encryption) and integrity (signed hash)
- Make sure that all session tokens use a good source of randomness
- Perform validation on the server side to make sure that client side data tokens are consistent with what is expected.

## Related Weaknesses (CWE)
- CWE-353
- CWE-285
- CWE-302
- CWE-472
- CWE-565
- CWE-315
- CWE-539
- CWE-384
- CWE-233
