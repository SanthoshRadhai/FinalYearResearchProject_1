# T0859: Valid Accounts


**ATT&CK ID:** T0859  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Persistence, Lateral Movement  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0859  

## Description
Adversaries may steal the credentials of a specific user or service account using credential access techniques. In some cases, default credentials for control system devices may be publicly available. Compromised credentials may be used to bypass access controls placed on various resources on hosts and within the network, and may even be used for persistent access to remote systems. Compromised and default credentials may also grant an adversary increased privilege to specific systems and devices or access to restricted areas of the network. Adversaries may choose not to use malware or tools, in conjunction with the legitimate access those credentials provide, to make it harder to detect their presence or to control devices and send legitimate commands in an unintended way. 

Adversaries may also create accounts, sometimes using predefined account names and passwords, to provide a means of backup access for persistence. (Citation: Booz Allen Hamilton) 

The overlap of credentials and permissions across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator)  and possibly between the enterprise and operational technology environments. Adversaries may be able to leverage valid credentials from one system to gain access to another system.

## Mitigations
- M0801: Access Management
- M0913: Application Developer Guidance
- M0915: Active Directory Configuration
- M0918: User Account Management
- M0926: Privileged Account Management
- M0927: Password Policies
- M0932: Multi-factor Authentication
- M0936: Account Use Policies
- M0937: Filter Network Traffic
- M0947: Audit

## Known Threat Groups Using This Technique
- G1000: ALLANITE
- G0049: OilRig

## Known Software Using This Technique
- S0089: BlackEnergy
- S1045: INCONTROLLER
