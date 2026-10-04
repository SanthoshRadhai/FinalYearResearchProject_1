# CAPEC-534: Malicious Hardware Update

**Abstraction:** Standard  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/534.html  

## Description
An adversary introduces malicious hardware during an update or replacement procedure, allowing for additional compromise or site disruption at the victim location. After deployment, it is not uncommon for upgrades and replacements to occur involving hardware and various replaceable parts. These upgrades and replacements are intended to correct defects, provide additional features, and to replace broken or worn-out parts. However, by forcing or tricking the replacement of a good component with a defective or corrupted component, an adversary can leverage known defects to obtain a desired malicious impact.

## Related Attack Patterns
- ChildOf: CAPEC-440

## Skills Required
- [High] Able to develop and manufacture malicious hardware components that perform the same functions and processes as their non-malicious counterparts.
