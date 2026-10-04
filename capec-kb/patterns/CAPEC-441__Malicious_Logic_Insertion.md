# CAPEC-441: Malicious Logic Insertion

**Abstraction:** Meta  
**Status:** Stable  
**Likelihood of Attack:** Medium  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/441.html  

## Description
An adversary installs or adds malicious logic (also known as malware) into a seemingly benign component of a fielded system. This logic is often hidden from the user of the system and works behind the scenes to achieve negative impacts. With the proliferation of mass digital storage and inexpensive multimedia devices, Bluetooth and 802.11 support, new attack vectors for spreading malware are emerging for things we once thought of as innocuous greeting cards, picture frames, or digital projectors. This pattern of attack focuses on systems already fielded and used in operation as opposed to systems and their components that are still under development and part of the supply chain.

## Prerequisites
- Access to the component currently deployed at a victim location.

## Consequences
- Scope: Authorization; Impact: Execute Unauthorized Commands

## Related Weaknesses (CWE)
- CWE-284
