# CAPEC-520: Counterfeit Hardware Component Inserted During Product Assembly

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/520.html  

## Description
An adversary with either direct access to the product assembly process or to the supply of subcomponents used in the product assembly process introduces counterfeit hardware components into product assembly. The assembly containing the counterfeit components results in a system specifically designed for malicious purposes.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The adversary will need either physical access or be able to supply malicious hardware components to the product development facility.

## Skills Required
- [High] Resources to maliciously construct components used by the manufacturer.
- [High] Resources to physically infiltrate manufacturer or manufacturer's supplier.

## Mitigations
- Hardware attacks are often difficult to detect, as inserted components can be difficult to identify or remain dormant for an extended period of time.
- Acquire hardware and hardware components from trusted vendors. Additionally, determine where vendors purchase components or if any components are created/acquired via subcontractors to determine where supply chain risks may exist.
