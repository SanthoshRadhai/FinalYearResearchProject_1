# CAPEC-511: Infiltration of Software Development Environment

**Abstraction:** Detailed  
**Status:** Draft  
**Likelihood of Attack:** Low  
**Typical Severity:** High  
**Reference:** https://capec.mitre.org/data/definitions/511.html  

## Description
An attacker uses common delivery mechanisms such as email attachments or removable media to infiltrate the IDE (Integrated Development Environment) of a victim manufacturer with the intent of implanting malware allowing for attack control of the victim IDE environment. The attack then uses this access to exfiltrate sensitive data or information, manipulate said data or information, and conceal these actions. This will allow and aid the attack to meet the goal of future compromise of a recipient of the victim's manufactured product further down in the supply chain.

## Related Attack Patterns
- ChildOf: CAPEC-444

## Prerequisites
- The victim must use email or removable media from systems running the IDE (or systems adjacent to the IDE systems).
- The victim must have a system running exploitable applications and/or a vulnerable configuration to allow for initial infiltration.
- The attacker must have working knowledge of some if not all of the components involved in the IDE system as well as the infrastructure.

## Skills Required
- [Medium] Intelligence about the manufacturer's operating environment and infrastructure.
- [High] Ability to develop, deploy, and maintain a stealth malicious backdoor program remotely in what is essentially a hostile environment.
- [High] Development skills to construct malicious attachments that can be used to exploit vulnerabilities in typical desktop applications or system configurations. The malicious attachments should be crafted well enough to bypass typical defensive systems (IDS, anti-virus, etc)

## Mitigations
- Avoid the common delivery mechanisms of adversaries, such as email attachments, which could introduce the malware.
