# CAPEC-530: Provide Counterfeit Component

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/530.html  

## Description
An attacker provides a counterfeit component during the procurement process of a lower-tier component supplier to a sub-system developer or integrator, which is then built into the system being upgraded or repaired by the victim, allowing the attacker to cause disruption or additional compromise.

## Related Attack Patterns
- ChildOf: CAPEC-531

## Prerequisites
- Advanced knowledge about the target system and sub-components.

## Skills Required
- [High] Able to develop and manufacture malicious system components that resemble legitimate name-brand components.

## Mitigations
- There are various methods to detect if the component is a counterfeit. See section II of [REF-703] for many techniques.
