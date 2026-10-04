# CAPEC-532: Altered Installed BIOS

**Abstraction:** Detailed  
**Status:** Stable  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/532.html  

## Description
An attacker with access to download and update system software sends a maliciously altered BIOS to the victim or victim supplier/integrator, which when installed allows for future exploitation.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- Advanced knowledge about the installed target system design.
- Advanced knowledge about the download and update installation processes.
- Access to the download and update system(s) used to deliver BIOS images.

## Skills Required
- [High] Able to develop a malicious BIOS image with the original functionality as a normal BIOS image, but with added functionality that allows for later compromise and/or disruption.

## Mitigations
- Deploy strong code integrity policies to allow only authorized apps to run.
- Use endpoint detection and response solutions that can automaticalkly detect and remediate suspicious activities.
- Maintain a highly secure build and update infrastructure by immediately applying security patches for OS and software, implementing mandatory integrity controls to ensure only trusted tools run, and requiring multi-factor authentication for admins.
- Require SSL for update channels and implement certificate transparency based verification.
- Sign update packages and BIOS patches.
- Use hardware security modules/trusted platform modules to verify authenticity using hardware-based cryptography.
