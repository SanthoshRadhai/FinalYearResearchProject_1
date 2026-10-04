# T0881: Service Stop


**ATT&CK ID:** T0881  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0881  

## Description
Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment. (Citation: Enterprise ATT&CK)  Services may not allow for modification of their data stores while running. Adversaries may stop services in order to conduct Data Destruction. (Citation: Enterprise ATT&CK)

## Mitigations
- M0918: User Account Management
- M0922: Restrict File and Directory Permissions
- M0924: Restrict Registry Permissions
- M0930: Network Segmentation

## Known Software Using This Technique
- S0605: EKANS
- S0604: Industroyer
- S1072: Industroyer2
- S0607: KillDisk
- S0496: REvil
