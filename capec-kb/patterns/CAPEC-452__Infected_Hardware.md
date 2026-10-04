# CAPEC-452: Infected Hardware

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/452.html  

## Description
An adversary inserts malicious logic into hardware, typically in the form of a computer virus or rootkit. This logic is often hidden from the user of the hardware and works behind the scenes to achieve negative impacts. This pattern of attack focuses on hardware already fielded and used in operation as opposed to hardware that is still under development and part of the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-441

## Prerequisites
- Access to the hardware currently deployed at a victim location.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands
