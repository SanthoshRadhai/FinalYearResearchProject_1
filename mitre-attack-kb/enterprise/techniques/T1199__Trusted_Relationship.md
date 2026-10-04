# T1199: Trusted Relationship


**ATT&CK ID:** T1199  
**Domain:** Mitre Attack  
**Tactic(s):** Initial Access  
**Platforms:** IaaS, Identity Provider, Linux, macOS, Office Suite, SaaS, Windows  
**Reference:** https://attack.mitre.org/techniques/T1199  

## Description
Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, [Valid Accounts](https://attack.mitre.org/techniques/T1078) used by the other party for access to internal network systems may be compromised and used.(Citation: CISA IT Service Providers)

In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.(Citation: Office 365 Delegated Administration)

## Mitigations
- M1018: User Account Management
- M1030: Network Segmentation
- M1032: Multi-factor Authentication

## Known Threat Groups Using This Technique
- G0007: APT28
- G0016: APT29
- G0115: GOLD SOUTHFIELD
- G0125: HAFNIUM
- G1004: LAPSUS$
- G1005: POLONIUM
- G1039: RedCurl
- G0034: Sandworm Team
- G1041: Sea Turtle
- G0027: Threat Group-3390
- G1055: VOID MANTICORE
- G0045: menuPass
