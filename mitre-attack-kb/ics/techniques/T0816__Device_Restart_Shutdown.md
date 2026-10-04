# T0816: Device Restart/Shutdown


**ATT&CK ID:** T0816  
**Domain:** Mitre Ics Attack  
**Tactic(s):** Inhibit Response Function  
**Platforms:** None  
**Reference:** https://attack.mitre.org/techniques/T0816  

## Description
Adversaries may forcibly restart or shutdown a device in an ICS environment to disrupt and potentially negatively impact physical processes. Methods of device restart and shutdown exist in some devices as built-in, standard functionalities. These functionalities can be executed using interactive device web interfaces, CLIs, and network protocol commands.

Unexpected restart or shutdown of control system devices may prevent expected response functions happening during critical states.

A device restart can also be a sign of malicious device modifications, as many updates require a shutdown in order to take effect.

## Mitigations
- M0800: Authorization Enforcement
- M0801: Access Management
- M0802: Communication Authenticity
- M0804: Human User Authentication
- M0807: Network Allowlists
- M0813: Software Process and Device Authentication
- M0930: Network Segmentation
- M0937: Filter Network Traffic
- M0942: Disable or Remove Feature or Program

## Known Software Using This Technique
- S0604: Industroyer
