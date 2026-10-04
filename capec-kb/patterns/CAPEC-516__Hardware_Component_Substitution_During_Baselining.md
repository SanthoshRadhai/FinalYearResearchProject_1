# CAPEC-516: Hardware Component Substitution During Baselining

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/516.html  

## Description
An adversary with access to system components during allocated baseline development can substitute a maliciously altered hardware component for a baseline component during the product development and research phases. This can lead to adjustments and calibrations being made in the product so that when the final product, now containing the modified component, is deployed it will not perform as designed and be advantageous to the adversary.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills Required
- [Medium] Intelligence data on victim's purchasing habits.
- [High] Resources to maliciously construct/alter hardware components used for testing by the supplier.
- [High] Resources to physically infiltrate supplier.

## Mitigations
- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.
