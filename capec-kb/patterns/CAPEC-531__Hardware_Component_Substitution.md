# CAPEC-531: Hardware Component Substitution

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/531.html  

## Description
An attacker substitutes out a tested and approved hardware component for a maliciously-altered hardware component. This type of attack is carried out directly on the system, enabling the attacker to then cause disruption or additional compromise.

## Related Attack Patterns
- ChildOf: CAPEC-534

## Prerequisites
- Physical access to the system or the integration facility where hardware components are kept.

## Skills Required
- [High] Able to develop and manufacture malicious system components that perform the same functions and processes as their non-malicious counterparts.
