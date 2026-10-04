# CAPEC-442: Infected Software

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/442.html  

## Description
An adversary adds malicious logic, often in the form of a computer virus, to otherwise benign software. This logic is often hidden from the user of the software and works behind the scenes to achieve negative impacts. Many times, the malicious logic is inserted into empty space between legitimate code, and is then called when the software is executed. This pattern of attack focuses on software already fielded and used in operation as opposed to software that is still under development and part of the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-441

## Prerequisites
- Access to the software currently deployed at a victim location. This access is often obtained by leveraging another attack pattern to gain permissions that the adversary wouldn't normally have.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Mitigations
- Leverage anti-virus products to detect and quarantine software with known virus.

## Related Weaknesses (CWE)
- CWE-506
