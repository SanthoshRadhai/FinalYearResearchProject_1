# CAPEC-473: Signature Spoof

**Abstraction:** Standard  
**Status:** Draft  
**Reference:** https://capec.mitre.org/data/definitions/473.html  

## Description
An attacker generates a message or datablock that causes the recipient to believe that the message or datablock was generated and cryptographically signed by an authoritative or reputable source, misleading a victim or victim operating system into performing malicious actions.

## Related Attack Patterns
- ChildOf: CAPEC-151

## Prerequisites
- The victim or victim system is dependent upon a cryptographic signature-based verification system for validation of one or more security events or actions.
- The validation can be bypassed via an attacker-provided signature that makes it appear that the legitimate authoritative or reputable source provided the signature.

## Skills Required
- [High] Technical understanding of how signature verification algorithms work with data and applications

## Consequences
- Scope: Access Control, Authentication; Impact: Gain Privileges

## Related Weaknesses (CWE)
- CWE-20
- CWE-327
- CWE-290
