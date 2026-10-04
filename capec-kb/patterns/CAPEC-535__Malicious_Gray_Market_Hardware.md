# CAPEC-535: Malicious Gray Market Hardware

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/535.html  

## Description
An attacker maliciously alters hardware components that will be sold on the gray market, allowing for victim disruption and compromise when the victim needs replacement hardware components for systems where the parts are no longer in regular supply from original suppliers, or where the hardware components from the attacker seems to be a great benefit from a cost perspective.

## Related Attack Patterns
- ChildOf: CAPEC-531

## Prerequisites
- Physical access to a gray market reseller's hardware components supply, or the ability to appear as a gray market reseller to the victim's buyer.

## Skills Required
- [High] Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.

## Mitigations
- Purchase only from authorized resellers.
- Validate serial numbers from multiple sources
