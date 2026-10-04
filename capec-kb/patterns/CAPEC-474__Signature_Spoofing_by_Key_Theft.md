# CAPEC-474: Signature Spoofing by Key Theft

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/474.html  

## Description
An attacker obtains an authoritative or reputable signer's private signature key by theft and then uses this key to forge signatures from the original signer to mislead a victim into performing actions that benefit the attacker.

## Related Attack Patterns
- ChildOf: CAPEC-473

## Prerequisites
- An authoritative or reputable signer is storing their private signature key with insufficient protection.

## Skills Required
- [Low] Knowledge of common location methods and access methods to sensitive data
- [High] Ability to compromise systems containing sensitive data

## Mitigations
- Restrict access to private keys from non-supervisory accounts
- Restrict access to administrative personnel and processes only
- Ensure all remote methods are secured
- Ensure all services are patched and up to date

## Related Weaknesses (CWE)
- CWE-522
